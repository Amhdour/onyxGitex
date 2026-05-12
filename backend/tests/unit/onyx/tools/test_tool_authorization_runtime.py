from typing import Any

from onyx.chat.emitter import Emitter
from onyx.server.query_and_chat.placement import Placement
from onyx.tools.interface import Tool
from onyx.tools.models import ToolCallKickoff
from onyx.tools.models import ToolResponse
from onyx.tools.tool_authorization_router import ToolAuthorizationRouter
from onyx.tools.tool_runner import run_tool_calls


class DummyEmitter(Emitter):
    def emit(self, packet: Any) -> None:
        return None


class DummyTool(Tool):
    name = "dummy_low_risk"
    description = "dummy"
    definition = {}

    def __init__(self) -> None:
        super().__init__(DummyEmitter())
        self.executed = False

    def run(self, *args: Any, **kwargs: Any) -> ToolResponse:
        self.executed = True
        return ToolResponse(rich_response=None, llm_facing_response="ok")


def _call(name: str) -> ToolCallKickoff:
    return ToolCallKickoff(
        tool_call_id=f"call_{name}",
        tool_name=name,
        tool_args={},
        placement=Placement(turn_index=0, tab_index=0),
    )


def test_authorized_low_risk_tool_executes() -> None:
    tool = DummyTool()
    resp = run_tool_calls(
        tool_calls=[_call("dummy_low_risk")],
        tools=[tool],
        message_history=[],
        user_memory_context=None,
        user_info=None,
        citation_mapping={},
        next_citation_num=1,
        authorization_router=ToolAuthorizationRouter(),
        user_id="u1",
        tool_policy={"dummy_low_risk": {"allowed": True, "risk_level": "low"}},
    )
    assert len(resp.tool_responses) == 1
    assert tool.executed is True


def test_denied_call_emits_audit_and_trace() -> None:
    tool = DummyTool()
    audit_events: list[dict[str, Any]] = []
    runtime_trace: list[dict[str, Any]] = []

    resp = run_tool_calls(
        tool_calls=[_call("dummy_low_risk")],
        tools=[tool],
        message_history=[],
        user_memory_context=None,
        user_info=None,
        citation_mapping={},
        next_citation_num=1,
        authorization_router=ToolAuthorizationRouter(),
        user_id=None,
        tool_policy={"dummy_low_risk": {"allowed": True, "risk_level": "low"}},
        audit_events=audit_events,
        runtime_trace=runtime_trace,
    )

    assert len(resp.tool_responses) == 1
    assert tool.executed is False
    assert audit_events[0]["action_type"] == "tool.deny"
    assert audit_events[0]["reason"] == "missing_user_identity"
    assert audit_events[0]["decision"] == "deny"
    assert runtime_trace[0]["event"] == "tool_authorization"


def test_high_risk_requires_approval() -> None:
    router = ToolAuthorizationRouter()
    decision = router.authorize(
        tool_name="python",
        user_id="u1",
        policy={"python": {"allowed": True, "risk_level": "high"}},
        approval_id=None,
    )
    assert decision.allowed is False
    assert decision.reason == "missing_explicit_approval"
