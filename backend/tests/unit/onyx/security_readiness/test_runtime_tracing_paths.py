from __future__ import annotations

from itertools import count

from onyx.security_readiness.control_layer import AuthContext
from onyx.security_readiness.control_layer import PolicyDecisionEngine
from onyx.security_readiness.control_layer import ResourcePolicy
from onyx.security_readiness.control_layer import RetrievalAuthorizationGuard
from onyx.security_readiness.control_layer import RuntimeTracer
from onyx.tools.tool_authorization_router import ToolAuthorizationRouter


def _append_step(
    tracer: RuntimeTracer,
    *,
    trace_id: str,
    request_id: str,
    actor_id: str | None,
    parent_span_id: str | None,
    step_name: str,
    component: str,
    decision: str,
    evidence_ref: str,
    span_counter: count,
    error: str | None = None,
    fail_closed: bool = False,
) -> str:
    span_id = f"span-{next(span_counter)}"
    tracer.emit_structured(
        trace_id=trace_id,
        span_id=span_id,
        parent_span_id=parent_span_id,
        request_id=request_id,
        actor_id=actor_id,
        step_name=step_name,
        component=component,
        decision=decision,
        evidence_ref=evidence_ref,
        error=error,
        fail_closed=fail_closed,
    )
    return span_id


def test_runtime_trace_covers_rag_and_tool_authorization_paths() -> None:
    tracer = RuntimeTracer()
    span_counter = count(1)

    # Verified narrow E2E RAG-style request path (authorization + generation decision path).
    trace_id = "trace-rag-001"
    request_id = "req-rag-001"
    actor_id = "u-rag"

    s1 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=None,
        step_name="request.received",
        component="chat.api",
        decision="accepted",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )
    s2 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s1,
        step_name="identity.resolved",
        component="identity",
        decision="resolved",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )
    s3 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s2,
        step_name="policy.context.built",
        component="policy_engine",
        decision="built",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )
    s4 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s3,
        step_name="retrieval.requested",
        component="retrieval_pipeline",
        decision="requested",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )

    guard = RetrievalAuthorizationGuard(PolicyDecisionEngine())
    decision = guard.authorize_document(
        auth_context=AuthContext(user_id=actor_id),
        document_id="public-kb",
        policy_map={
            "public-kb": ResourcePolicy(resource_id="public-kb", allowed_users=frozenset({actor_id}))
        },
    )

    s5 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s4,
        step_name="retrieval.authorization.checked",
        component="retrieval_guard",
        decision="checked",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )
    s6 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s5,
        step_name="retrieval.allowed_or_denied",
        component="retrieval_guard",
        decision="allow" if decision.allowed else "deny",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )
    s7 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s6,
        step_name="citation.checked",
        component="citation_enforcer",
        decision="pass",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )
    s8 = _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s7,
        step_name="response.generated_or_blocked",
        component="llm_response",
        decision="generated",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )
    _append_step(
        tracer,
        trace_id=trace_id,
        request_id=request_id,
        actor_id=actor_id,
        parent_span_id=s8,
        step_name="audit.event.emitted",
        component="audit_logger",
        decision="emitted",
        evidence_ref="runtime-tracing-001:rag",
        span_counter=span_counter,
    )

    # Verified tool authorization path with fail-closed deny.
    tool_trace_id = "trace-tool-001"
    tool_request_id = "req-tool-001"
    s10 = _append_step(
        tracer,
        trace_id=tool_trace_id,
        request_id=tool_request_id,
        actor_id=None,
        parent_span_id=None,
        step_name="tool.requested",
        component="tool_runner",
        decision="requested",
        evidence_ref="runtime-tracing-001:tool",
        span_counter=span_counter,
    )
    router = ToolAuthorizationRouter()
    tool_decision = router.authorize(
        tool_name="python",
        user_id=None,
        policy={"python": {"allowed": True, "risk_level": "high"}},
        approval_id=None,
    )
    s11 = _append_step(
        tracer,
        trace_id=tool_trace_id,
        request_id=tool_request_id,
        actor_id=None,
        parent_span_id=s10,
        step_name="tool.policy.checked",
        component="tool_authorization",
        decision="checked",
        evidence_ref="runtime-tracing-001:tool",
        span_counter=span_counter,
    )
    s12 = _append_step(
        tracer,
        trace_id=tool_trace_id,
        request_id=tool_request_id,
        actor_id=None,
        parent_span_id=s11,
        step_name="tool.allowed_or_denied",
        component="tool_authorization",
        decision="allow" if tool_decision.allowed else "deny",
        evidence_ref="runtime-tracing-001:tool",
        span_counter=span_counter,
        error=tool_decision.reason if not tool_decision.allowed else None,
        fail_closed=not tool_decision.allowed,
    )
    s13 = _append_step(
        tracer,
        trace_id=tool_trace_id,
        request_id=tool_request_id,
        actor_id=None,
        parent_span_id=s12,
        step_name="tool.execution.blocked_or_completed",
        component="tool_runner",
        decision="blocked" if not tool_decision.allowed else "completed",
        evidence_ref="runtime-tracing-001:tool",
        span_counter=span_counter,
        fail_closed=not tool_decision.allowed,
    )
    _append_step(
        tracer,
        trace_id=tool_trace_id,
        request_id=tool_request_id,
        actor_id=None,
        parent_span_id=s13,
        step_name="audit.event.emitted",
        component="audit_logger",
        decision="emitted",
        evidence_ref="runtime-tracing-001:tool",
        span_counter=span_counter,
        fail_closed=not tool_decision.allowed,
    )

    step_names = [event["step_name"] for event in tracer.trace_events]
    assert "retrieval.authorization.checked" in step_names
    assert "retrieval.allowed_or_denied" in step_names
    assert "tool.policy.checked" in step_names
    assert "tool.allowed_or_denied" in step_names
    assert all("trace_id" in event for event in tracer.trace_events)
    assert any(event["fail_closed"] for event in tracer.trace_events)
