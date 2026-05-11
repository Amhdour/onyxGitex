import pytest

from onyx.tools.models import ToolCallKickoff
from onyx.server.query_and_chat.placement import Placement


def _kickoff(tool_name: str, tool_args: dict[str, object]) -> ToolCallKickoff:
    return ToolCallKickoff(
        tool_call_id="call_governance",
        tool_name=tool_name,
        tool_args=tool_args,
        placement=Placement(turn_index=0, tab_index=0),
    )


@pytest.mark.xfail(
    reason="Central unauthorized tool-call enforcement hook not yet implemented",
    strict=False,
)
def test_unauthorized_tool_call_blocked() -> None:
    call = _kickoff("python", {"code": "print('x')"})
    # Expected future behavior: unauthorized principal receives deny decision.
    assert getattr(call, "authorization_decision", None) == "denied"


@pytest.mark.xfail(
    reason="Human confirmation policy gate not yet implemented in runtime path",
    strict=False,
)
def test_missing_approval_blocks_high_risk_tool() -> None:
    call = _kickoff("python", {"code": "print('x')"})
    # Expected future behavior: missing approval forces fail-closed block.
    assert getattr(call, "approval_required", True) is False


@pytest.mark.xfail(
    reason="High-risk tool classification enforcement not yet implemented centrally",
    strict=False,
)
def test_high_risk_tool_blocked_without_policy_allow() -> None:
    call = _kickoff("python", {"code": "print('x')"})
    # Expected future behavior: policy classification marks and blocks call.
    assert getattr(call, "risk_level", "high") != "high"


@pytest.mark.xfail(
    reason="Structured audit event emission for governance decisions not yet verified",
    strict=False,
)
def test_audit_event_emitted_for_tool_decision() -> None:
    call = _kickoff("open_url", {"urls": ["https://example.com"]})
    # Expected future behavior: audit event id attached for every tool decision.
    assert getattr(call, "audit_event_id", None) is not None
