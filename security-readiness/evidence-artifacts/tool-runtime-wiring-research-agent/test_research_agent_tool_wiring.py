from pathlib import Path

import pytest

from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.tool_runtime_wiring_adapter import run_tool_calls_with_runtime_context


RESEARCH_AGENT_FILE = Path("backend/onyx/tools/fake_tools/research_agent.py")


def test_research_agent_path_uses_run_tool_calls_with_runtime_context():
    content = RESEARCH_AGENT_FILE.read_text()
    assert "_run_research_agent_tool_calls(" in content
    assert "run_tool_calls_with_runtime_context(" in content


def test_rag_only_with_tool_calls_fails_closed_before_tool_runner():
    called = {"runner": False}

    def runner(**kwargs):
        called["runner"] = True
        return object()

    with pytest.raises(FailClosedError, match="tool_calls_not_allowed_in_rag_only"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_ONLY",
            tool_calls=[object()],
            run_tool_calls_fn=runner,
            authorization_router=object(),
            user_id="u1",
            tool_policy={"k": "v"},
        )

    assert called["runner"] is False


def test_rag_plus_tools_missing_router_fails_closed():
    with pytest.raises(FailClosedError, match="missing_authorization_router"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[object()],
            run_tool_calls_fn=lambda **kwargs: object(),
            authorization_router=None,
            user_id="u1",
            tool_policy={"k": "v"},
        )


def test_rag_plus_tools_missing_user_id_fails_closed():
    with pytest.raises(FailClosedError, match="missing_user_id"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[object()],
            run_tool_calls_fn=lambda **kwargs: object(),
            authorization_router=object(),
            user_id=None,
            tool_policy={"k": "v"},
        )


def test_rag_plus_tools_missing_tool_policy_fails_closed():
    with pytest.raises(FailClosedError, match="missing_tool_policy"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[object()],
            run_tool_calls_fn=lambda **kwargs: object(),
            authorization_router=object(),
            user_id="u1",
            tool_policy=None,
        )


def test_rag_plus_tools_full_context_forwards_router_user_policy_approval_audit_trace():
    captured = {}

    def runner(**kwargs):
        captured.update(kwargs)
        return "ok"

    router = object()
    policy = {"policy": "strict"}
    audit_events = []
    runtime_trace = []

    result = run_tool_calls_with_runtime_context(
        launch_mode="RAG_PLUS_TOOLS",
        tool_calls=[object()],
        run_tool_calls_fn=runner,
        authorization_router=router,
        user_id="user-123",
        tool_policy=policy,
        approval_id="approval-9",
        audit_events=audit_events,
        runtime_trace=runtime_trace,
    )

    assert result == "ok"
    assert captured["authorization_router"] is router
    assert captured["user_id"] == "user-123"
    assert captured["tool_policy"] is policy
    assert captured["approval_id"] == "approval-9"
    assert captured["audit_events"] is audit_events
    assert captured["runtime_trace"] is runtime_trace


def test_no_external_tools_are_called():
    content = RESEARCH_AGENT_FILE.read_text()
    assert "MCPTool" not in content
