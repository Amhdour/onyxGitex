from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock

import pytest

from onyx.auth.permissions import require_permission
from onyx.auth.users import current_user
from onyx.auth.users import double_check_user
from onyx.db.document_access import apply_document_access_filter
from onyx.db.enums import AccountType
from onyx.db.enums import Permission
from onyx.db.models import Document
from onyx.error_handling.exceptions import OnyxError
from onyx.server.utils import BasicAuthenticationError
from sqlalchemy import select


@pytest.mark.asyncio
async def test_unauthorized_user_access_denied() -> None:
    with pytest.raises(BasicAuthenticationError, match="not authenticated"):
        await double_check_user(None)


@pytest.mark.asyncio
async def test_missing_session_denied() -> None:
    with pytest.raises(BasicAuthenticationError, match="not authenticated"):
        await current_user(None)


@pytest.mark.asyncio
async def test_expired_identity_denied() -> None:
    user = MagicMock()
    user.is_verified = True
    user.oidc_expiry = datetime.now(timezone.utc) - timedelta(minutes=5)

    with pytest.raises(BasicAuthenticationError, match="OIDC token has expired"):
        await double_check_user(user)


@pytest.mark.asyncio
async def test_admin_only_operation_denied_for_non_admin_permission() -> None:
    user = MagicMock()
    user.effective_permissions = [Permission.BASIC_ACCESS.value]

    dependency = require_permission(Permission.MANAGE_CONNECTORS)
    with pytest.raises(OnyxError, match="required permissions"):
        await dependency(user)


@pytest.mark.asyncio
async def test_admin_only_operation_allowed_for_admin_permission() -> None:
    user = MagicMock()
    user.effective_permissions = [Permission.FULL_ADMIN_PANEL_ACCESS.value]

    dependency = require_permission(Permission.MANAGE_CONNECTORS)
    resolved_user = await dependency(user)
    assert resolved_user is user


@pytest.mark.asyncio
async def test_service_account_misuse_denied_when_limited() -> None:
    user = MagicMock()
    user.is_verified = True
    user.oidc_expiry = None
    user.account_type = AccountType.SERVICE_ACCOUNT
    user.effective_permissions = []

    with pytest.raises(BasicAuthenticationError, match="limited permissions"):
        await current_user(user)


def test_wrong_department_group_scope_isolated_in_filter() -> None:
    stmt = select(Document)
    filtered = apply_document_access_filter(
        stmt=stmt,
        user_email="user@example.com",
        external_group_ids=["department-engineering"],
    )

    rendered = str(filtered)
    assert "external_user_group_ids" in rendered
    assert "department-engineering" in rendered
