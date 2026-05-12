from __future__ import annotations

import pytest

from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.tool_runtime_context_guard import enforce_tool_runtime_context


class FakeAuditLogger:
    def __init__(self) -> None:
        self.events: list[tuple[str, dict[str, object]]] = []

    def emit(self, event_type: str, payload: dict[str, object]) -> None:
        self.events.append((event_type, payload))


class FakeRuntimeTracer:
    def __init__(self) -> None:
        self.events: list[tuple[str, dict[str, object]]] = []

    def emit(self, trace_name: str, attrs: dict[str, object]) -> None:
        self.events.append((trace_name, attrs))


def test_rag_only_with_no_tool_calls_allowed() -> None:
    enforce_tool_runtime_context(
        launch_mode="RAG_ONLY",
        tool_calls_present=False,
        authorization_router=None,
        user_id=None,
        tool_policy=None,
    )


def test_rag_only_with_tool_calls_fails_closed() -> None:
    with pytest.raises(FailClosedError, match="tool_calls_not_allowed_in_rag_only"):
        enforce_tool_runtime_context(
            launch_mode="RAG_ONLY",
            tool_calls_present=True,
            authorization_router=None,
            user_id=None,
            tool_policy=None,
        )


def test_rag_plus_tools_missing_router_fails_closed() -> None:
    with pytest.raises(FailClosedError, match="missing_authorization_router"):
        enforce_tool_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls_present=True,
            authorization_router=None,
            user_id="u1",
            tool_policy={"dummy": {"allowed": True}},
        )


def test_rag_plus_tools_missing_user_id_fails_closed() -> None:
    with pytest.raises(FailClosedError, match="missing_user_id"):
        enforce_tool_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls_present=True,
            authorization_router=object(),
            user_id=None,
            tool_policy={"dummy": {"allowed": True}},
        )


def test_rag_plus_tools_missing_tool_policy_fails_closed() -> None:
    with pytest.raises(FailClosedError, match="missing_tool_policy"):
        enforce_tool_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls_present=True,
            authorization_router=object(),
            user_id="u1",
            tool_policy=None,
        )


def test_rag_plus_tools_with_full_context_allowed() -> None:
    enforce_tool_runtime_context(
        launch_mode="RAG_PLUS_TOOLS",
        tool_calls_present=True,
        authorization_router=object(),
        user_id="u1",
        tool_policy={"dummy": {"allowed": True}},
    )


def test_deny_emits_audit_event() -> None:
    audit_logger = FakeAuditLogger()

    with pytest.raises(FailClosedError, match="missing_user_id"):
        enforce_tool_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls_present=True,
            authorization_router=object(),
            user_id=None,
            tool_policy={"dummy": {"allowed": True}},
            audit_logger=audit_logger,
        )

    assert len(audit_logger.events) == 1
    event_type, payload = audit_logger.events[0]
    assert event_type == "tool.runtime_context"
    assert payload["decision"] == "deny"
    assert payload["reason"] == "missing_user_id"


def test_deny_emits_runtime_trace() -> None:
    runtime_tracer = FakeRuntimeTracer()

    with pytest.raises(FailClosedError, match="missing_tool_policy"):
        enforce_tool_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls_present=True,
            authorization_router=object(),
            user_id="u1",
            tool_policy=None,
            runtime_tracer=runtime_tracer,
        )

    assert len(runtime_tracer.events) == 1
    trace_name, attrs = runtime_tracer.events[0]
    assert trace_name == "tool.runtime_context"
    assert attrs["decision"] == "deny"
    assert attrs["reason"] == "missing_tool_policy"
