from __future__ import annotations

import pytest

from onyx.error_handling.error_codes import OnyxErrorCode
from onyx.error_handling.exceptions import OnyxError
from onyx.security_readiness.retrieval_guard_adapter import enforce_bypass_acl_contract


class AuditLoggerStub:
    def __init__(self) -> None:
        self.events: list[dict] = []

    def emit_authorization_event(self, **kwargs: object) -> None:
        self.events.append(kwargs)


def test_bypass_acl_false_returns_without_audit_event() -> None:
    logger = AuditLoggerStub()

    enforce_bypass_acl_contract(
        bypass_acl=False,
        trusted_system_context=False,
        actor_id="user-123",
        audit_logger=logger,
    )

    assert logger.events == []


def test_bypass_acl_true_and_untrusted_fails_closed_with_onyx_error() -> None:
    logger = AuditLoggerStub()

    with pytest.raises(OnyxError) as exc_info:
        enforce_bypass_acl_contract(
            bypass_acl=True,
            trusted_system_context=False,
            actor_id="user-123",
            audit_logger=logger,
        )

    assert exc_info.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "trusted_system_context=True" in str(exc_info.value)


def test_denied_bypass_emits_retrieval_bypass_acl_deny_audit_event() -> None:
    logger = AuditLoggerStub()

    with pytest.raises(OnyxError):
        enforce_bypass_acl_contract(
            bypass_acl=True,
            trusted_system_context=False,
            actor_id="user-123",
            audit_logger=logger,
        )

    assert len(logger.events) == 1
    event = logger.events[0]
    assert event["action_type"] == "retrieval.bypass_acl.deny"
    assert event["decision"] == "deny"


def test_bypass_acl_true_and_trusted_context_is_allowed() -> None:
    logger = AuditLoggerStub()

    enforce_bypass_acl_contract(
        bypass_acl=True,
        trusted_system_context=True,
        actor_id="service-agent",
        audit_logger=logger,
    )

    assert len(logger.events) == 1


def test_approved_bypass_emits_retrieval_bypass_acl_allow_audit_event() -> None:
    logger = AuditLoggerStub()

    enforce_bypass_acl_contract(
        bypass_acl=True,
        trusted_system_context=True,
        actor_id="service-agent",
        audit_logger=logger,
    )

    event = logger.events[0]
    assert event["action_type"] == "retrieval.bypass_acl.allow"
    assert event["decision"] == "allow"


def test_actor_id_is_preserved_in_audit_event() -> None:
    logger = AuditLoggerStub()

    enforce_bypass_acl_contract(
        bypass_acl=True,
        trusted_system_context=True,
        actor_id="actor-xyz",
        audit_logger=logger,
    )

    assert logger.events[0]["actor_id"] == "actor-xyz"


def test_normal_user_style_request_cannot_enable_bypass_without_trusted_context() -> None:
    logger = AuditLoggerStub()

    with pytest.raises(OnyxError) as exc_info:
        enforce_bypass_acl_contract(
            bypass_acl=True,
            trusted_system_context=False,
            actor_id="normal-user",
            audit_logger=logger,
        )

    assert exc_info.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert logger.events[0]["action_type"] == "retrieval.bypass_acl.deny"
