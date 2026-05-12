import pytest

from onyx.error_handling.exceptions import OnyxError
from onyx.security_readiness.control_layer import AuditLogger
from onyx.security_readiness.retrieval_guard_adapter import enforce_bypass_acl_contract


def test_bypass_acl_requires_trusted_system_context() -> None:
    logger = AuditLogger()

    with pytest.raises(OnyxError, match="trusted_system_context=True"):
        enforce_bypass_acl_contract(
            bypass_acl=True,
            trusted_system_context=False,
            actor_id="user-1",
            audit_logger=logger,
        )


def test_bypass_acl_without_trusted_context_fails_closed_and_audits() -> None:
    logger = AuditLogger()

    with pytest.raises(OnyxError):
        enforce_bypass_acl_contract(
            bypass_acl=True,
            trusted_system_context=False,
            actor_id="user-2",
            audit_logger=logger,
        )

    assert logger.events
    payload = logger.events[-1]["payload"]
    assert payload["action_type"] == "retrieval.bypass_acl.deny"
    assert payload["fail_closed"] is True


def test_bypass_acl_emits_audit_event_for_trusted_context() -> None:
    logger = AuditLogger()

    enforce_bypass_acl_contract(
        bypass_acl=True,
        trusted_system_context=True,
        actor_id="system-worker",
        audit_logger=logger,
    )

    assert logger.events
    payload = logger.events[-1]["payload"]
    assert payload["action_type"] == "retrieval.bypass_acl.allow"
    assert payload["decision"] == "allow"


def test_normal_user_request_cannot_enable_bypass_acl() -> None:
    logger = AuditLogger()

    with pytest.raises(OnyxError):
        enforce_bypass_acl_contract(
            bypass_acl=True,
            trusted_system_context=False,
            actor_id="normal-user",
            audit_logger=logger,
        )
