from onyx.security_readiness.control_layer import (
    AuditLogger,
    AuthContext,
    FailClosedError,
    LaunchGateEngine,
    PolicyDecisionEngine,
    ReadinessScoringEngine,
    ResourcePolicy,
    RetrievalAuthorizationGuard,
    RuntimeTracer,
    ToolAuthorizationRouter,
    ToolPolicy,
)


def test_policy_decision_engine_allow_and_deny() -> None:
    engine = PolicyDecisionEngine()
    allow_ctx = AuthContext(user_id="alice", groups=frozenset({"eng"}))
    allow_policy = ResourcePolicy(
        resource_id="doc-1",
        allowed_users=frozenset({"alice"}),
        allowed_groups=frozenset({"legal"}),
    )
    allow_decision = engine.evaluate(allow_ctx, allow_policy)
    assert allow_decision.allowed is True
    assert allow_decision.reason == "Policy allow"

    deny_policy = ResourcePolicy(resource_id="doc-2", allowed_users=frozenset({"bob"}))
    deny_decision = engine.evaluate(allow_ctx, deny_policy)
    assert deny_decision.allowed is False
    assert deny_decision.reason == "Policy deny"


def test_policy_decision_engine_fail_closed_on_missing_context_or_policy() -> None:
    engine = PolicyDecisionEngine()
    with __import__("pytest").raises(FailClosedError, match="Missing identity context"):
        engine.evaluate(None, ResourcePolicy(resource_id="doc"))
    with __import__("pytest").raises(FailClosedError, match="Missing policy"):
        engine.evaluate(AuthContext(user_id="alice"), None)


def test_retrieval_authorization_guard_fail_closed_and_allow() -> None:
    guard = RetrievalAuthorizationGuard(PolicyDecisionEngine())
    ctx = AuthContext(user_id="alice", groups=frozenset({"eng"}))
    policy_map = {
        "doc-1": ResourcePolicy(
            resource_id="doc-1",
            allowed_users=frozenset(),
            allowed_groups=frozenset({"eng"}),
        )
    }

    decision = guard.authorize_document(ctx, "doc-1", policy_map)
    assert decision.allowed is True

    with __import__("pytest").raises(FailClosedError, match="Missing document policy map"):
        guard.authorize_document(ctx, "doc-1", None)

    with __import__("pytest").raises(FailClosedError, match="Missing document permission"):
        guard.authorize_document(ctx, "doc-404", policy_map)


def test_tool_authorization_router_fail_closed_and_allow() -> None:
    router = ToolAuthorizationRouter(PolicyDecisionEngine())
    ctx = AuthContext(user_id="alice", groups=frozenset({"ops"}))
    policy_map = {
        "search": ToolPolicy(
            tool_name="search",
            allowed_users=frozenset(),
            allowed_groups=frozenset({"ops"}),
        )
    }

    decision = router.authorize_tool(ctx, "search", policy_map)
    assert decision.allowed is True

    with __import__("pytest").raises(FailClosedError, match="Missing tool policy map"):
        router.authorize_tool(ctx, "search", None)

    with __import__("pytest").raises(FailClosedError, match="Missing tool authorization"):
        router.authorize_tool(ctx, "unknown", policy_map)


def test_audit_logger_and_runtime_tracer_emit_structured_events() -> None:
    audit = AuditLogger()
    event = audit.emit_authorization_event(
        action_type="retrieve",
        decision="ALLOW",
        reason="Policy allow",
        actor_id="alice",
        resource_type="document",
        resource_id="doc-1",
        fail_closed=False,
    )
    assert event["event_type"] == "authorization.audit"
    assert event["payload"]["actor_id"] == "alice"

    tracer = RuntimeTracer()
    trace = tracer.emit_structured(
        trace_id="trace-1",
        span_id="span-1",
        parent_span_id=None,
        request_id="req-1",
        actor_id="alice",
        step_name="policy_eval",
        component="RetrievalAuthorizationGuard",
        decision="ALLOW",
        evidence_ref="unit:test",
        fail_closed=False,
        duration_ms=3,
    )
    assert trace["trace_id"] == "trace-1"
    assert trace["component"] == "RetrievalAuthorizationGuard"


def test_launch_gate_and_readiness_scoring_stay_blocked_with_limited_evidence() -> None:
    scoring = ReadinessScoringEngine()
    score = scoring.calculate(
        {
            "retrieval_guard_runtime": (0.6, 0.0),
            "pure_control_unit_tests": (0.4, 92.0),
        }
    )
    assert score == 36.8

    gate = LaunchGateEngine()
    result = gate.evaluate(score, minimum_score=85.0)
    assert result["gate_status"] == "BLOCK"
