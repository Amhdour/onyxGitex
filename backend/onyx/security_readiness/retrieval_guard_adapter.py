from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from onyx.error_handling.error_codes import OnyxErrorCode
from onyx.error_handling.exceptions import OnyxError
from onyx.security_readiness.control_layer import AuthContext
from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.control_layer import ResourcePolicy


@dataclass(frozen=True)
class RetrievalGuardDependencies:
    access_filter_fn: Callable[[Any, list[str], Any], list[str]]
    authorize_document_fn: Callable[[AuthContext | None, str, dict[str, ResourcePolicy] | None], Any]
    audit_logger: Any
    runtime_tracer: Any


def enforce_retrieval_authorization(
    *,
    document_sets: list[str],
    user_id: str | None,
    user: Any,
    db_session: Any,
    dependencies: RetrievalGuardDependencies,
) -> None:
    if user_id is None:
        raise OnyxError(
            OnyxErrorCode.INSUFFICIENT_PERMISSIONS,
            "Missing identity context for retrieval authorization.",
        )
    if db_session is None:
        raise OnyxError(
            OnyxErrorCode.INSUFFICIENT_PERMISSIONS,
            "Missing document permission context for retrieval authorization.",
        )

    accessible_names = dependencies.access_filter_fn(
        db_session,
        document_sets,
        user,
    )
    policy_map = {
        name: ResourcePolicy(
            resource_id=name,
            allowed_users=frozenset({str(user_id)}),
        )
        for name in accessible_names
    }
    auth_context = AuthContext(user_id=str(user_id))

    for document_set_name in document_sets:
        try:
            decision = dependencies.authorize_document_fn(
                auth_context,
                document_set_name,
                policy_map,
            )
            dependencies.audit_logger.emit_authorization_event(
                action_type="retrieval.allow" if decision.allowed else "retrieval.deny",
                decision="allow" if decision.allowed else "deny",
                reason=decision.reason,
                actor_id=str(user_id),
                resource_type="document_set",
                resource_id=document_set_name,
                policy_id="document_set_access_policy",
            )
            dependencies.runtime_tracer.emit(
                "retrieval.authorization",
                {
                    "document_set": document_set_name,
                    "decision": "allow" if decision.allowed else "deny",
                },
            )
            if not decision.allowed:
                raise OnyxError(
                    OnyxErrorCode.INSUFFICIENT_PERMISSIONS,
                    f"User does not have access to document set: {document_set_name}",
                )
        except FailClosedError as e:
            dependencies.audit_logger.emit_authorization_event(
                action_type="policy.missing_context",
                decision="deny",
                reason=str(e),
                actor_id=str(user_id) if user_id is not None else None,
                resource_type="document_set",
                resource_id=document_set_name,
                policy_id="document_set_access_policy",
                fail_closed=True,
                evidence_status="Partially Confirmed",
            )
            dependencies.runtime_tracer.emit(
                "retrieval.authorization",
                {
                    "document_set": document_set_name,
                    "decision": "deny",
                    "reason": str(e),
                },
            )
            raise OnyxError(OnyxErrorCode.INSUFFICIENT_PERMISSIONS, str(e)) from e
