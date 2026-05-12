from __future__ import annotations

from collections.abc import Callable
from typing import Any

from onyx.security_readiness.tool_runtime_context_guard import enforce_tool_runtime_context


RunToolCallsFn = Callable[..., Any]


def run_tool_calls_with_runtime_context(
    *,
    launch_mode: str,
    tool_calls: list[Any],
    run_tool_calls_fn: RunToolCallsFn,
    tools: list[Any],
    msg_history: list[Any],
    authorization_router: object | None,
    user_id: str | None,
    tool_policy: dict[str, Any] | None,
    approval_id: str | None = None,
    audit_logger: object | None = None,
    runtime_tracer: object | None = None,
    audit_events: list[dict[str, Any]] | None = None,
    runtime_trace: list[dict[str, Any]] | None = None,
) -> Any:
    """Dependency-light runtime-adjacent contract for llm_loop tool authorization wiring."""
    enforce_tool_runtime_context(
        launch_mode=launch_mode,
        tool_calls_present=bool(tool_calls),
        authorization_router=authorization_router,
        user_id=user_id,
        tool_policy=tool_policy,
        audit_logger=audit_logger,
        runtime_tracer=runtime_tracer,
    )

    return run_tool_calls_fn(
        tools=tools,
        tool_calls=tool_calls,
        msg_history=msg_history,
        authorization_router=authorization_router,
        user_id=user_id,
        tool_policy=tool_policy,
        approval_id=approval_id,
        audit_events=audit_events,
        runtime_trace=runtime_trace,
    )
