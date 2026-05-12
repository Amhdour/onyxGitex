from dataclasses import dataclass

import pytest

from onyx.error_handling.exceptions import OnyxError
from onyx.security_readiness.control_layer import AuditLogger
from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.control_layer import PolicyDecision
from onyx.security_readiness.control_layer import ResourcePolicy
from onyx.security_readiness.control_layer import RuntimeTracer
from onyx.security_readiness.retrieval_guard_adapter import RetrievalGuardDependencies
from onyx.security_readiness.retrieval_guard_adapter import enforce_retrieval_authorization


@dataclass
class DummyUser:
    id: int | None


def test_authorized_document_set_allowed() -> None:
    deps = RetrievalGuardDependencies(
        access_filter_fn=lambda _db, names, _user: names,
        authorize_document_fn=lambda _ctx, _doc, _map: PolicyDecision(True, "Policy allow"),
        audit_logger=AuditLogger(),
        runtime_tracer=RuntimeTracer(),
    )

    enforce_retrieval_authorization(
        document_sets=["finance"],
        user_id="123",
        user=DummyUser(id=123),
        db_session=object(),
        dependencies=deps,
    )


def test_unauthorized_document_set_denied() -> None:
    deps = RetrievalGuardDependencies(
        access_filter_fn=lambda _db, _names, _user: [],
        authorize_document_fn=lambda _ctx, doc, policy_map: (_ for _ in ()).throw(
            FailClosedError(f"Missing document permission for {doc}")
        )
        if doc not in policy_map
        else PolicyDecision(True, "Policy allow"),
        audit_logger=AuditLogger(),
        runtime_tracer=RuntimeTracer(),
    )

    with pytest.raises(OnyxError, match="Missing document permission for finance"):
        enforce_retrieval_authorization(
            document_sets=["finance"],
            user_id="123",
            user=DummyUser(id=123),
            db_session=object(),
            dependencies=deps,
        )


def test_missing_identity_fails_closed() -> None:
    deps = RetrievalGuardDependencies(
        access_filter_fn=lambda _db, names, _user: names,
        authorize_document_fn=lambda _ctx, _doc, _map: PolicyDecision(True, "Policy allow"),
        audit_logger=AuditLogger(),
        runtime_tracer=RuntimeTracer(),
    )

    with pytest.raises(OnyxError, match="Missing identity context"):
        enforce_retrieval_authorization(
            document_sets=["finance"],
            user_id=None,
            user=DummyUser(id=None),
            db_session=object(),
            dependencies=deps,
        )


def test_missing_permission_context_fails_closed() -> None:
    deps = RetrievalGuardDependencies(
        access_filter_fn=lambda _db, names, _user: names,
        authorize_document_fn=lambda _ctx, _doc, _map: PolicyDecision(True, "Policy allow"),
        audit_logger=AuditLogger(),
        runtime_tracer=RuntimeTracer(),
    )

    with pytest.raises(OnyxError, match="Missing document permission context"):
        enforce_retrieval_authorization(
            document_sets=["finance"],
            user_id="123",
            user=DummyUser(id=123),
            db_session=None,
            dependencies=deps,
        )


def test_audit_event_emitted_for_allow_and_runtime_trace() -> None:
    audit_logger = AuditLogger()
    runtime_tracer = RuntimeTracer()
    deps = RetrievalGuardDependencies(
        access_filter_fn=lambda _db, names, _user: names,
        authorize_document_fn=lambda _ctx, _doc, _map: PolicyDecision(True, "Policy allow"),
        audit_logger=audit_logger,
        runtime_tracer=runtime_tracer,
    )

    enforce_retrieval_authorization(
        document_sets=["finance"],
        user_id="123",
        user=DummyUser(id=123),
        db_session=object(),
        dependencies=deps,
    )

    assert audit_logger.events[-1]["payload"]["action_type"] == "retrieval.allow"
    assert runtime_tracer.trace_events[-1]["attrs"]["decision"] == "allow"


def test_audit_event_emitted_for_deny_and_runtime_trace() -> None:
    audit_logger = AuditLogger()
    runtime_tracer = RuntimeTracer()

    def deny_authorize(_ctx: object, doc: str, _map: dict[str, ResourcePolicy] | None) -> PolicyDecision:
        return PolicyDecision(False, f"Policy deny for {doc}")

    deps = RetrievalGuardDependencies(
        access_filter_fn=lambda _db, names, _user: names,
        authorize_document_fn=deny_authorize,
        audit_logger=audit_logger,
        runtime_tracer=runtime_tracer,
    )

    with pytest.raises(OnyxError, match="User does not have access to document set: finance"):
        enforce_retrieval_authorization(
            document_sets=["finance"],
            user_id="123",
            user=DummyUser(id=123),
            db_session=object(),
            dependencies=deps,
        )

    assert audit_logger.events[-1]["payload"]["action_type"] == "retrieval.deny"
    assert runtime_tracer.trace_events[-1]["attrs"]["decision"] == "deny"
