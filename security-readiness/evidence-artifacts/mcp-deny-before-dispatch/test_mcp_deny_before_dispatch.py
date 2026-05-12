from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from onyx.tools.tool_authorization_router import ToolAuthorizationRouter

GENERIC_TOOL_ERROR_MESSAGE = "Tool failed with error: {error}"


@dataclass
class FakeToolResponse:
    llm_facing_response: str


@dataclass
class FakeMCPTool:
    name: str = "mcp"
    run_called: bool = False

    def run(self, **_: Any) -> FakeToolResponse:
        self.run_called = True
        return FakeToolResponse(llm_facing_response="ok")


def deny_before_dispatch_gate(
    *,
    tool: FakeMCPTool,
    authorization_router: ToolAuthorizationRouter,
    user_id: str | None,
    tool_policy: dict[str, Any] | None,
    approval_id: str | None = None,
    audit_events: list[dict[str, Any]] | None = None,
    runtime_trace: list[dict[str, Any]] | None = None,
) -> FakeToolResponse:
    """Runtime-adjacent harness matching _safe_run_single_tool deny path semantics."""
    decision = authorization_router.authorize(
        tool_name=tool.name,
        user_id=user_id,
        policy=tool_policy,
        approval_id=approval_id,
    )
    if runtime_trace is not None:
        runtime_trace.append(
            {
                "event": "tool_authorization",
                "tool_name": tool.name,
                "allowed": decision.allowed,
                "reason": decision.reason,
                "risk_level": decision.risk_level,
            }
        )

    if not decision.allowed:
        if audit_events is not None:
            audit_events.append(
                {
                    "action_type": "tool.deny",
                    "decision": "deny",
                    "reason": decision.reason,
                }
            )
        return FakeToolResponse(
            llm_facing_response=GENERIC_TOOL_ERROR_MESSAGE.format(
                error=f"Authorization denied: {decision.reason}"
            )
        )

    return tool.run()


def test_unauthorized_mcp_tool_call_is_denied_before_run() -> None:
    tool = FakeMCPTool()
    result = deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"mcp": {"allowed": False, "risk_level": "low"}},
    )
    assert "Authorization denied: tool_not_allowed" in result.llm_facing_response
    assert tool.run_called is False


def test_missing_user_id_fails_closed_before_dispatch() -> None:
    tool = FakeMCPTool()
    result = deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id=None,
        tool_policy={"mcp": {"allowed": True, "risk_level": "low"}},
    )
    assert "missing_user_identity" in result.llm_facing_response
    assert tool.run_called is False


def test_missing_tool_policy_fails_closed_before_dispatch() -> None:
    tool = FakeMCPTool()
    result = deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy=None,
    )
    assert "missing_tool_policy" in result.llm_facing_response
    assert tool.run_called is False


def test_high_risk_without_approval_denied_before_dispatch() -> None:
    tool = FakeMCPTool()
    result = deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"mcp": {"allowed": True, "risk_level": "high"}},
        approval_id=None,
    )
    assert "missing_explicit_approval" in result.llm_facing_response
    assert tool.run_called is False


def test_allowed_mcp_with_policy_and_approval_reaches_runner() -> None:
    tool = FakeMCPTool()
    result = deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"mcp": {"allowed": True, "risk_level": "high"}},
        approval_id="approval-1",
    )
    assert result.llm_facing_response == "ok"
    assert tool.run_called is True


def test_deny_event_emits_audit_record() -> None:
    tool = FakeMCPTool()
    audit_events: list[dict[str, Any]] = []
    deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"mcp": {"allowed": False, "risk_level": "low"}},
        audit_events=audit_events,
    )
    assert len(audit_events) == 1
    assert audit_events[0]["action_type"] == "tool.deny"


def test_deny_event_emits_runtime_trace() -> None:
    tool = FakeMCPTool()
    runtime_trace: list[dict[str, Any]] = []
    deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"mcp": {"allowed": False, "risk_level": "low"}},
        runtime_trace=runtime_trace,
    )
    assert len(runtime_trace) == 1
    assert runtime_trace[0]["event"] == "tool_authorization"
    assert runtime_trace[0]["allowed"] is False


def test_no_external_mcp_server_contacted() -> None:
    tool = FakeMCPTool()
    deny_before_dispatch_gate(
        tool=tool,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"mcp": {"allowed": False, "risk_level": "low"}},
    )
    assert tool.run_called is False
