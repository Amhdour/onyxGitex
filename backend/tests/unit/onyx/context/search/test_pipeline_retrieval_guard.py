from types import SimpleNamespace

import pytest

from onyx.context.search.models import BaseFilters
from onyx.context.search.pipeline import _build_index_filters
from onyx.error_handling.error_codes import OnyxErrorCode
from onyx.error_handling.exceptions import OnyxError


def _user(user_id: str | None) -> SimpleNamespace:
    return SimpleNamespace(id=user_id)


def test_build_index_filters_allows_authorized_document_sets(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "onyx.context.search.pipeline.filter_document_set_names_by_user_access",
        lambda db_session, document_set_names, user: document_set_names,
    )

    filters = _build_index_filters(
        user_provided_filters=BaseFilters(document_set=["finance"]),
        user=_user("u-1"),
        project_id_filter=None,
        persona_id_filter=None,
        persona_document_sets=None,
        persona_time_cutoff=None,
        db_session=object(),
    )

    assert filters.document_set == ["finance"]


def test_build_index_filters_denies_unauthorized_document_set(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "onyx.context.search.pipeline.filter_document_set_names_by_user_access",
        lambda db_session, document_set_names, user: [],
    )

    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["restricted"]),
            user=_user("u-1"),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=object(),
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS


def test_build_index_filters_fails_closed_without_identity() -> None:
    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["restricted"]),
            user=_user(None),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=object(),
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS


def test_build_index_filters_fails_closed_without_document_permission_context() -> None:
    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["restricted"]),
            user=_user("u-1"),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=None,
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
