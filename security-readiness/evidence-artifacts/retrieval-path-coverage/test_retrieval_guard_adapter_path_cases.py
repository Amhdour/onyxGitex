from dataclasses import dataclass

import pytest

from onyx.error_handling.error_codes import OnyxErrorCode
from onyx.error_handling.exceptions import OnyxError
from onyx.security_readiness.control_layer import AuditLogger
from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.control_layer import PolicyDecision
from onyx.security_readiness.control_layer import RuntimeTracer
from onyx.security_readiness.retrieval_guard_adapter import RetrievalGuardDependencies
from onyx.security_readiness.retrieval_guard_adapter import enforce_retrieval_authorization


@dataclass
class DummyUser:
    id: str | None


def _dependencies(accessible: list[str], *, raise_fail_closed: bool = False) -> tuple[RetrievalGuardDependencies, AuditLogger, RuntimeTracer]:
    audit_logger = AuditLogger()
    runtime_tracer = RuntimeTracer()

    def _authorize(_ctx: object, document_set_name: str, policy_map: object) -> PolicyDecision:
        if raise_fail_closed and document_set_name == "finance":
            raise FailClosedError("policy backend unavailable")
        if document_set_name in policy_map:
            return PolicyDecision(True, "Policy allow")
        return PolicyDecision(False, f"Policy deny for {document_set_name}")

    deps = RetrievalGuardDependencies(
        access_filter_fn=lambda _db, _document_sets, _user: accessible,
        authorize_document_fn=_authorize,
        audit_logger=audit_logger,
        runtime_tracer=runtime_tracer,
    )
    return deps, audit_logger, runtime_tracer


def test_multiple_document_sets_with_one_unauthorized_set_fails_closed() -> None:
    deps, _, _ = _dependencies(["finance"])

    with pytest.raises(OnyxError) as exc:
        enforce_retrieval_authorization(
            document_sets=["finance", "hr-restricted"],
            user_id="u-1",
            user=DummyUser(id="u-1"),
            db_session=object(),
            dependencies=deps,
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "hr-restricted" in str(exc.value)


def test_access_filter_partial_access_mixed_allow_deny() -> None:
    deps, _, _ = _dependencies(["engineering"])

    with pytest.raises(OnyxError) as exc:
        enforce_retrieval_authorization(
            document_sets=["engineering", "legal"],
            user_id="u-1",
            user=DummyUser(id="u-1"),
            db_session=object(),
            dependencies=deps,
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "legal" in str(exc.value)


def test_mixed_document_sets_emit_allow_and_deny_audit_events() -> None:
    deps, audit_logger, _ = _dependencies(["finance"])

    with pytest.raises(OnyxError):
        enforce_retrieval_authorization(
            document_sets=["finance", "legal"],
            user_id="u-1",
            user=DummyUser(id="u-1"),
            db_session=object(),
            dependencies=deps,
        )

    decisions = [event["payload"]["decision"] for event in audit_logger.events]
    action_types = [event["payload"]["action_type"] for event in audit_logger.events]
    assert decisions == ["allow", "deny"]
    assert action_types == ["retrieval.allow", "retrieval.deny"]


def test_mixed_document_sets_emit_allow_and_deny_runtime_traces() -> None:
    deps, _, runtime_tracer = _dependencies(["finance"])

    with pytest.raises(OnyxError):
        enforce_retrieval_authorization(
            document_sets=["finance", "legal"],
            user_id="u-1",
            user=DummyUser(id="u-1"),
            db_session=object(),
            dependencies=deps,
        )

    decisions = [trace["attrs"]["decision"] for trace in runtime_tracer.trace_events]
    assert decisions == ["allow", "deny"]


def test_authorize_document_fail_closed_error_converts_to_onyx_error() -> None:
    deps, audit_logger, runtime_tracer = _dependencies(["finance"], raise_fail_closed=True)

    with pytest.raises(OnyxError) as exc:
        enforce_retrieval_authorization(
            document_sets=["finance"],
            user_id="u-1",
            user=DummyUser(id="u-1"),
            db_session=object(),
            dependencies=deps,
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "policy backend unavailable" in str(exc.value)
    assert audit_logger.events[0]["payload"]["action_type"] == "policy.missing_context"
    assert runtime_tracer.trace_events[0]["attrs"]["decision"] == "deny"


def test_missing_identity_fails_closed() -> None:
    deps, _, _ = _dependencies(["finance"])

    with pytest.raises(OnyxError) as exc:
        enforce_retrieval_authorization(
            document_sets=["finance"],
            user_id=None,
            user=DummyUser(id=None),
            db_session=object(),
            dependencies=deps,
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "Missing identity context" in str(exc.value)


def test_missing_permission_context_fails_closed() -> None:
    deps, _, _ = _dependencies(["finance"])

    with pytest.raises(OnyxError) as exc:
        enforce_retrieval_authorization(
            document_sets=["finance"],
            user_id="u-1",
            user=DummyUser(id="u-1"),
            db_session=None,
            dependencies=deps,
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "Missing document permission context" in str(exc.value)
