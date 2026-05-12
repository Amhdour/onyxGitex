from __future__ import annotations

from typing import Any

import pytest

from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.tool_runtime_wiring_adapter import (
    run_tool_calls_with_runtime_context,
)
from onyx.tools.tool_authorization_router import ToolAuthorizationRouter


class FakeEmitter:
    def __init__(self) -> None:
        self.events: list[tuple[str, dict[str, Any]]] = []

    def emit(self, event_name: str, payload: dict[str, Any]) -> None:
        self.events.append((event_name, payload))


@pytest.fixture
def fake_call() -> dict[str, Any]:
    return {"tool_name": "python"}


def test_rag_only_denies_tool_calls_before_run_tool_calls(fake_call: dict[str, Any]) -> None:
    called = False

    def _should_not_run(**_: Any) -> None:
        nonlocal called
        called = True

    with pytest.raises(FailClosedError, match="tool_calls_not_allowed_in_rag_only"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_ONLY",
            tool_calls=[fake_call],
            run_tool_calls_fn=_should_not_run,
            authorization_router=ToolAuthorizationRouter(),
            user_id="user-1",
            tool_policy={"python": {"allowed": True, "risk_level": "low"}},
        )

    assert called is False


def test_rag_plus_tools_missing_router_fails_closed(fake_call: dict[str, Any]) -> None:
    with pytest.raises(FailClosedError, match="missing_authorization_router"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[fake_call],
            run_tool_calls_fn=lambda **_: None,
            authorization_router=None,
            user_id="user-1",
            tool_policy={"python": {"allowed": True, "risk_level": "low"}},
        )


def test_rag_plus_tools_missing_identity_fails_closed(fake_call: dict[str, Any]) -> None:
    with pytest.raises(FailClosedError, match="missing_user_id"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[fake_call],
            run_tool_calls_fn=lambda **_: None,
            authorization_router=ToolAuthorizationRouter(),
            user_id=None,
            tool_policy={"python": {"allowed": True, "risk_level": "low"}},
        )


def test_rag_plus_tools_missing_policy_fails_closed(fake_call: dict[str, Any]) -> None:
    with pytest.raises(FailClosedError, match="missing_tool_policy"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[fake_call],
            run_tool_calls_fn=lambda **_: None,
            authorization_router=ToolAuthorizationRouter(),
            user_id="user-1",
            tool_policy=None,
        )


def test_rag_plus_tools_full_context_calls_mock_runner(fake_call: dict[str, Any]) -> None:
    called = False

    def _mock_run_tool_calls(**_: Any) -> str:
        nonlocal called
        called = True
        return "ok"

    result = run_tool_calls_with_runtime_context(
        launch_mode="RAG_PLUS_TOOLS",
        tool_calls=[fake_call],
        run_tool_calls_fn=_mock_run_tool_calls,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"python": {"allowed": True, "risk_level": "low"}},
    )

    assert called is True
    assert result == "ok"


def test_rag_plus_tools_full_context_forwards_required_authorization_fields(
    fake_call: dict[str, Any],
) -> None:
    captured: dict[str, Any] = {}

    def _mock_run_tool_calls(**kwargs: Any) -> str:
        captured.update(kwargs)
        return "ok"

    policy = {"python": {"allowed": True, "risk_level": "low"}}
    router = ToolAuthorizationRouter()
    audit_events: list[dict[str, Any]] = []
    runtime_trace: list[dict[str, Any]] = []

    result = run_tool_calls_with_runtime_context(
        launch_mode="RAG_PLUS_TOOLS",
        tool_calls=[fake_call],
        run_tool_calls_fn=_mock_run_tool_calls,
        authorization_router=router,
        user_id="user-1",
        tool_policy=policy,
        approval_id="approval-123",
        audit_events=audit_events,
        runtime_trace=runtime_trace,
    )

    assert result == "ok"
    assert captured["authorization_router"] is router
    assert captured["user_id"] == "user-1"
    assert captured["tool_policy"] == policy
    assert captured["approval_id"] == "approval-123"
    assert captured["audit_events"] is audit_events
    assert captured["runtime_trace"] is runtime_trace


def test_high_risk_tool_without_approval_is_denied_by_mocked_router_runner(
    fake_call: dict[str, Any],
) -> None:
    def _mock_run_tool_calls(**kwargs: Any) -> dict[str, Any]:
        decision = kwargs["authorization_router"].authorize(
            tool_name="python",
            user_id=kwargs["user_id"],
            policy=kwargs["tool_policy"],
            approval_id=kwargs["approval_id"],
        )
        return {"allowed": decision.allowed, "reason": decision.reason}

    result = run_tool_calls_with_runtime_context(
        launch_mode="RAG_PLUS_TOOLS",
        tool_calls=[fake_call],
        run_tool_calls_fn=_mock_run_tool_calls,
        authorization_router=ToolAuthorizationRouter(),
        user_id="user-1",
        tool_policy={"python": {"allowed": True, "risk_level": "high"}},
        approval_id=None,
    )

    assert result == {"allowed": False, "reason": "missing_explicit_approval"}


def test_deny_path_emits_audit_event_on_guard_failure(fake_call: dict[str, Any]) -> None:
    audit = FakeEmitter()

    with pytest.raises(FailClosedError, match="missing_user_id"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[fake_call],
            run_tool_calls_fn=lambda **_: None,
            authorization_router=ToolAuthorizationRouter(),
            user_id=None,
            tool_policy={"python": {"allowed": True, "risk_level": "low"}},
            audit_logger=audit,
        )

    assert len(audit.events) == 1
    event_name, payload = audit.events[0]
    assert event_name == "tool.runtime_context"
    assert payload["decision"] == "deny"


def test_deny_path_emits_runtime_trace_on_guard_failure(fake_call: dict[str, Any]) -> None:
    tracer = FakeEmitter()

    with pytest.raises(FailClosedError, match="missing_tool_policy"):
        run_tool_calls_with_runtime_context(
            launch_mode="RAG_PLUS_TOOLS",
            tool_calls=[fake_call],
            run_tool_calls_fn=lambda **_: None,
            authorization_router=ToolAuthorizationRouter(),
            user_id="user-1",
            tool_policy=None,
            runtime_tracer=tracer,
        )

    assert len(tracer.events) == 1
    event_name, payload = tracer.events[0]
    assert event_name == "tool.runtime_context"
    assert payload["decision"] == "deny"
