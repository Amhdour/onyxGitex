from pathlib import Path

import pytest

from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.tool_runtime_wiring_adapter import (
    run_tool_calls_with_runtime_context,
)
from onyx.tools.tool_authorization_router import ToolAuthorizationRouter


def _dummy_run_tool_calls(**kwargs):
    return kwargs


def test_main_llm_loop_wiring_uses_runtime_adapter() -> None:
    content = Path("backend/onyx/chat/llm_loop.py").read_text()
    assert "run_tool_calls_with_runtime_context(" in content


def test_rag_only_with_tool_calls_fails_closed_before_tool_runner() -> None:
    called = {"runner": False}

    def should_not_run(**kwargs):
        called["runner"] = True
        return kwargs

    with pytest.raises(FailClosedError, match="tool_calls_not_allowed_in_rag_only"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_ONLY",
            tool_calls=[object()],
            run_tool_calls_fn=should_not_run,
            authorization_router=None,
            user_id=None,
            tool_policy=None,
        )

    assert called["runner"] is False


def test_rag_plus_tools_missing_router_fails_closed() -> None:
    with pytest.raises(FailClosedError, match="missing_authorization_router"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[],
            run_tool_calls_fn=_dummy_run_tool_calls,
            authorization_router=None,
            user_id="u1",
            tool_policy={"search": {"allowed": True}},
        )


def test_rag_plus_tools_missing_user_id_fails_closed() -> None:
    with pytest.raises(FailClosedError, match="missing_user_id"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[],
            run_tool_calls_fn=_dummy_run_tool_calls,
            authorization_router=ToolAuthorizationRouter(),
            user_id=None,
            tool_policy={"search": {"allowed": True}},
        )


def test_rag_plus_tools_missing_tool_policy_fails_closed() -> None:
    with pytest.raises(FailClosedError, match="missing_tool_policy"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[],
            run_tool_calls_fn=_dummy_run_tool_calls,
            authorization_router=ToolAuthorizationRouter(),
            user_id="u1",
            tool_policy=None,
        )


def test_rag_plus_tools_full_context_forwards_all_required_fields() -> None:
    result = run_tool_calls_with_runtime_context(
        launch_mode="RAG_PLUS_TOOLS",
        tool_calls=[],
        run_tool_calls_fn=_dummy_run_tool_calls,
        authorization_router=ToolAuthorizationRouter(),
        user_id="u1",
        tool_policy={"search": {"allowed": True}},
        approval_id="approval-1",
        audit_events=[{"event": "a"}],
        runtime_trace=[{"event": "t"}],
        tools=[],
    )

    assert isinstance(result["authorization_router"], ToolAuthorizationRouter)
    assert result["user_id"] == "u1"
    assert result["tool_policy"] == {"search": {"allowed": True}}
    assert result["approval_id"] == "approval-1"
    assert result["audit_events"] == [{"event": "a"}]
    assert result["runtime_trace"] == [{"event": "t"}]


def test_no_external_tools_are_called() -> None:
    marker = {"called": 0}

    def local_runner(**kwargs):
        marker["called"] += 1
        return kwargs

    run_tool_calls_with_runtime_context(
        launch_mode="RAG_PLUS_TOOLS",
        tool_calls=[],
        run_tool_calls_fn=local_runner,
        authorization_router=ToolAuthorizationRouter(),
        user_id="u1",
        tool_policy={"search": {"allowed": True}},
    )

    assert marker["called"] == 1
