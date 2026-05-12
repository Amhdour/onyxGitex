from __future__ import annotations

from typing import Any

from onyx.security_readiness.control_layer import FailClosedError


def _emit_deny_audit(
    *,
    audit_logger: object,
    launch_mode: str,
    reason: str,
    user_id: str | None,
) -> None:
    payload = {
        "action_type": "tool.runtime_context.deny",
        "decision": "deny",
        "reason": reason,
        "launch_mode": launch_mode,
        "user_id": user_id,
        "fail_closed": True,
    }
    emit = getattr(audit_logger, "emit", None)
    if callable(emit):
        emit("tool.runtime_context", payload)


def _emit_deny_trace(
    *,
    runtime_tracer: object,
    launch_mode: str,
    reason: str,
    user_id: str | None,
) -> None:
    attrs = {
        "event": "tool_runtime_context",
        "decision": "deny",
        "reason": reason,
        "launch_mode": launch_mode,
        "user_id": user_id,
        "fail_closed": True,
    }
    emit = getattr(runtime_tracer, "emit", None)
    if callable(emit):
        emit("tool.runtime_context", attrs)


def _deny(
    *,
    launch_mode: str,
    reason: str,
    user_id: str | None,
    audit_logger: object | None,
    runtime_tracer: object | None,
) -> None:
    if audit_logger is not None:
        _emit_deny_audit(
            audit_logger=audit_logger,
            launch_mode=launch_mode,
            reason=reason,
            user_id=user_id,
        )
    if runtime_tracer is not None:
        _emit_deny_trace(
            runtime_tracer=runtime_tracer,
            launch_mode=launch_mode,
            reason=reason,
            user_id=user_id,
        )
    raise FailClosedError(reason)


def enforce_tool_runtime_context(
    *,
    launch_mode: str,
    tool_calls_present: bool,
    authorization_router: object | None,
    user_id: str | None,
    tool_policy: dict[str, Any] | None,
    audit_logger: object | None = None,
    runtime_tracer: object | None = None,
) -> None:
    if launch_mode == "RAG_ONLY":
        if tool_calls_present:
            _deny(
                launch_mode=launch_mode,
                reason="tool_calls_not_allowed_in_rag_only",
                user_id=user_id,
                audit_logger=audit_logger,
                runtime_tracer=runtime_tracer,
            )
        return

    if launch_mode == "RAG_PLUS_TOOLS":
        if authorization_router is None:
            _deny(
                launch_mode=launch_mode,
                reason="missing_authorization_router",
                user_id=user_id,
                audit_logger=audit_logger,
                runtime_tracer=runtime_tracer,
            )
        if not user_id:
            _deny(
                launch_mode=launch_mode,
                reason="missing_user_id",
                user_id=user_id,
                audit_logger=audit_logger,
                runtime_tracer=runtime_tracer,
            )
        if tool_policy is None:
            _deny(
                launch_mode=launch_mode,
                reason="missing_tool_policy",
                user_id=user_id,
                audit_logger=audit_logger,
                runtime_tracer=runtime_tracer,
            )
        return

    _deny(
        launch_mode=launch_mode,
        reason="unsupported_launch_mode",
        user_id=user_id,
        audit_logger=audit_logger,
        runtime_tracer=runtime_tracer,
    )
