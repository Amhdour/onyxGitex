from __future__ import annotations

from typing import Any

from onyx.tools.tool_authorization_router import ToolAuthorizationRouter


def _dependency_light_authorize_and_maybe_execute(
    *,
    mode: str,
    tool_name: str,
    available_tools: set[str],
    user_id: str | None,
    tool_policy: dict[str, Any] | None,
    approval_id: str | None,
    authorization_router: ToolAuthorizationRouter | None,
    audit_events: list[dict[str, Any]],
    runtime_trace: list[dict[str, Any]],
) -> bool:
    """Dependency-light helper used only for evidence testing.

    This models fail-closed behavior for RAG_PLUS_TOOLS when authorization router/policy
    context is absent. It does not claim llm_loop runtime wiring.
    """
    if mode == "RAG_PLUS_TOOLS" and (
        authorization_router is None or tool_policy is None
    ):
        raise ValueError("rag_plus_tools_missing_authorization_context")

    if tool_name not in available_tools:
        audit_events.append({"action_type": "tool.deny", "decision": "deny", "reason": "unknown_tool"})
        runtime_trace.append({"event": "tool_authorization", "allowed": False, "reason": "unknown_tool"})
        return False

    assert authorization_router is not None
    decision = authorization_router.authorize(
        tool_name=tool_name,
        user_id=user_id,
        policy=tool_policy,
        approval_id=approval_id,
    )
    runtime_trace.append({"event": "tool_authorization", "allowed": decision.allowed, "reason": decision.reason})
    if not decision.allowed:
        audit_events.append({"action_type": "tool.deny", "decision": "deny", "reason": decision.reason})
    return decision.allowed


def test_unknown_tool_is_denied() -> None:
    audit_events: list[dict[str, Any]] = []
    runtime_trace: list[dict[str, Any]] = []
    allowed = _dependency_light_authorize_and_maybe_execute(
        mode="RAG_PLUS_TOOLS",
        tool_name="fake_unknown_tool",
        available_tools={"fake_low_risk"},
        user_id="u1",
        tool_policy={"fake_low_risk": {"allowed": True, "risk_level": "low"}},
        approval_id=None,
        authorization_router=ToolAuthorizationRouter(),
        audit_events=audit_events,
        runtime_trace=runtime_trace,
    )
    assert allowed is False
    assert audit_events[0]["reason"] == "unknown_tool"


def test_missing_user_identity_is_denied() -> None:
    decision = ToolAuthorizationRouter().authorize(
        tool_name="fake_low_risk",
        user_id=None,
        policy={"fake_low_risk": {"allowed": True, "risk_level": "low"}},
        approval_id=None,
    )
    assert decision.allowed is False
    assert decision.reason == "missing_user_identity"


def test_missing_tool_policy_is_denied() -> None:
    decision = ToolAuthorizationRouter().authorize(
        tool_name="fake_low_risk",
        user_id="u1",
        policy=None,
        approval_id=None,
    )
    assert decision.allowed is False
    assert decision.reason == "missing_tool_policy"


def test_high_risk_tool_without_approval_is_denied() -> None:
    decision = ToolAuthorizationRouter().authorize(
        tool_name="fake_high_risk",
        user_id="u1",
        policy={"fake_high_risk": {"allowed": True, "risk_level": "high"}},
        approval_id=None,
    )
    assert decision.allowed is False
    assert decision.reason == "missing_explicit_approval"


def test_high_risk_tool_with_approval_is_allowed() -> None:
    decision = ToolAuthorizationRouter().authorize(
        tool_name="fake_high_risk",
        user_id="u1",
        policy={"fake_high_risk": {"allowed": True, "risk_level": "high"}},
        approval_id="apr-123",
    )
    assert decision.allowed is True


def test_low_risk_allowed_tool_is_allowed() -> None:
    decision = ToolAuthorizationRouter().authorize(
        tool_name="fake_low_risk",
        user_id="u1",
        policy={"fake_low_risk": {"allowed": True, "risk_level": "low"}},
        approval_id=None,
    )
    assert decision.allowed is True


def test_denied_tool_call_emits_audit_event() -> None:
    audit_events: list[dict[str, Any]] = []
    runtime_trace: list[dict[str, Any]] = []
    _dependency_light_authorize_and_maybe_execute(
        mode="RAG_PLUS_TOOLS",
        tool_name="fake_low_risk",
        available_tools={"fake_low_risk"},
        user_id=None,
        tool_policy={"fake_low_risk": {"allowed": True, "risk_level": "low"}},
        approval_id=None,
        authorization_router=ToolAuthorizationRouter(),
        audit_events=audit_events,
        runtime_trace=runtime_trace,
    )
    assert audit_events[0]["action_type"] == "tool.deny"


def test_denied_tool_call_emits_runtime_trace() -> None:
    audit_events: list[dict[str, Any]] = []
    runtime_trace: list[dict[str, Any]] = []
    _dependency_light_authorize_and_maybe_execute(
        mode="RAG_PLUS_TOOLS",
        tool_name="fake_low_risk",
        available_tools={"fake_low_risk"},
        user_id=None,
        tool_policy={"fake_low_risk": {"allowed": True, "risk_level": "low"}},
        approval_id=None,
        authorization_router=ToolAuthorizationRouter(),
        audit_events=audit_events,
        runtime_trace=runtime_trace,
    )
    assert runtime_trace[0]["event"] == "tool_authorization"
    assert runtime_trace[0]["allowed"] is False


def test_rag_plus_tools_without_router_or_context_fails_closed() -> None:
    try:
        _dependency_light_authorize_and_maybe_execute(
            mode="RAG_PLUS_TOOLS",
            tool_name="fake_low_risk",
            available_tools={"fake_low_risk"},
            user_id="u1",
            tool_policy={"fake_low_risk": {"allowed": True, "risk_level": "low"}},
            approval_id=None,
            authorization_router=None,
            audit_events=[],
            runtime_trace=[],
        )
        assert False, "Expected fail-closed ValueError"
    except ValueError as exc:
        assert str(exc) == "rag_plus_tools_missing_authorization_context"
