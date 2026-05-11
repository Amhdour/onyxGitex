from pathlib import Path

import pytest

from onyx.security_readiness.control_layer import AuditLogger
from onyx.security_readiness.control_layer import AuthContext
from onyx.security_readiness.control_layer import DashboardDataExporter
from onyx.security_readiness.control_layer import EvidencePackGenerator
from onyx.security_readiness.control_layer import FailClosedError
from onyx.security_readiness.control_layer import LaunchGateEngine
from onyx.security_readiness.control_layer import PolicyDecisionEngine
from onyx.security_readiness.control_layer import ReadinessScoringEngine
from onyx.security_readiness.control_layer import ResourcePolicy
from onyx.security_readiness.control_layer import RetrievalAuthorizationGuard
from onyx.security_readiness.control_layer import RuntimeTracer
from onyx.security_readiness.control_layer import ToolAuthorizationRouter
from onyx.security_readiness.control_layer import ToolPolicy
from onyx.security_readiness.control_layer import fail_closed_if_missing


def test_policy_decision_engine_allows_group_match() -> None:
    engine = PolicyDecisionEngine()
    context = AuthContext(user_id="u1", groups=frozenset({"eng"}))
    policy = ResourcePolicy(resource_id="doc-1", allowed_groups=frozenset({"eng"}))
    decision = engine.evaluate(context, policy)
    assert decision.allowed is True


def test_policy_decision_engine_missing_identity_fails_closed() -> None:
    engine = PolicyDecisionEngine()
    with pytest.raises(FailClosedError, match="Missing identity"):
        engine.evaluate(None, ResourcePolicy(resource_id="doc-1"))


def test_policy_decision_engine_missing_policy_fails_closed() -> None:
    engine = PolicyDecisionEngine()
    with pytest.raises(FailClosedError, match="Missing policy"):
        engine.evaluate(AuthContext(user_id="u1"), None)


def test_retrieval_guard_missing_document_permission_fails_closed() -> None:
    guard = RetrievalAuthorizationGuard(PolicyDecisionEngine())
    with pytest.raises(FailClosedError, match="Missing document permission"):
        guard.authorize_document(AuthContext(user_id="u1"), "doc-x", {})


def test_retrieval_guard_denied_when_not_authorized() -> None:
    guard = RetrievalAuthorizationGuard(PolicyDecisionEngine())
    policy_map = {"doc-1": ResourcePolicy(resource_id="doc-1", allowed_users=frozenset({"u2"}))}
    decision = guard.authorize_document(AuthContext(user_id="u1"), "doc-1", policy_map)
    assert decision.allowed is False


def test_tool_router_missing_tool_authorization_fails_closed() -> None:
    router = ToolAuthorizationRouter(PolicyDecisionEngine())
    with pytest.raises(FailClosedError, match="Missing tool authorization"):
        router.authorize_tool(AuthContext(user_id="u1"), "delete_docs", {})


def test_audit_logger_emits_event() -> None:
    logger = AuditLogger()
    event = logger.emit("policy_decision", {"allowed": False})
    assert event["event_type"] == "policy_decision"
    assert logger.events


def test_runtime_tracer_emits_event() -> None:
    tracer = RuntimeTracer()
    event = tracer.emit("retrieval.authorization", {"decision": "deny"})
    assert event["trace_name"] == "retrieval.authorization"
    assert tracer.trace_events


def test_fail_closed_helper() -> None:
    with pytest.raises(FailClosedError):
        fail_closed_if_missing(None, "missing")


def test_evidence_manifest_generation() -> None:
    manifest = EvidencePackGenerator().generate_manifest({"C53": "Verified", "C54": "Unknown"})
    assert manifest["verified_count"] == 1
    assert manifest["unknown_count"] == 1


def test_launch_gate_engine_block() -> None:
    decision = LaunchGateEngine().evaluate(readiness_score=72.0, minimum_score=85.0)
    assert decision["gate_status"] == "BLOCK"


def test_readiness_score_calculation() -> None:
    score = ReadinessScoringEngine().calculate({"C53": (0.6, 90.0), "C54": (0.4, 80.0)})
    assert score == 86.0


def test_dashboard_export_json_and_csv(tmp_path: Path) -> None:
    exporter = DashboardDataExporter()
    json_path = exporter.export_json({"status": "Partially Confirmed"}, tmp_path / "dashboard.json")
    csv_path = exporter.export_csv(
        [{"control": "C53", "status": "Verified"}, {"control": "C54", "status": "Unknown"}],
        tmp_path / "dashboard.csv",
    )
    assert json_path.exists()
    assert csv_path.exists()


def test_retrieval_guard_missing_policy_map_fails_closed() -> None:
    guard = RetrievalAuthorizationGuard(PolicyDecisionEngine())
    with pytest.raises(FailClosedError, match="Missing document policy map"):
        guard.authorize_document(AuthContext(user_id="u1"), "doc-1", None)


def test_tool_router_missing_tool_policy_map_fails_closed() -> None:
    router = ToolAuthorizationRouter(PolicyDecisionEngine())
    with pytest.raises(FailClosedError, match="Missing tool policy map"):
        router.authorize_tool(AuthContext(user_id="u1"), "search", None)


def test_tool_router_denied_when_not_authorized() -> None:
    router = ToolAuthorizationRouter(PolicyDecisionEngine())
    decision = router.authorize_tool(
        AuthContext(user_id="u1"),
        "search",
        {"search": ToolPolicy(tool_name="search", allowed_users=frozenset({"u2"}))},
    )
    assert decision.allowed is False


def test_readiness_score_calculation_rejects_zero_total_weight() -> None:
    with pytest.raises(ValueError, match="Total weight"):
        ReadinessScoringEngine().calculate({"C53": (0.0, 90.0)})


def test_dashboard_export_csv_rejects_empty_rows(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Rows cannot be empty"):
        DashboardDataExporter().export_csv([], tmp_path / "dashboard.csv")
