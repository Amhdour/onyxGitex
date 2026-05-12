from pathlib import Path
import sys

sys.path.append(str(Path("security-readiness/policies").resolve()))

from policy_evaluator import PolicyEvaluator


def _evaluator() -> PolicyEvaluator:
    return PolicyEvaluator(Path("security-readiness/policies"))


def test_authorized_retrieval_allowed() -> None:
    decision = _evaluator().evaluate_retrieval(
        {
            "subject": {
                "user_id": "u-1",
                "role": "advisor",
                "department": "atlas_advisory",
                "tenant_id": "atlas-prod",
            },
            "document": {"owner_department": "atlas_advisory", "classification": "confidential"},
        }
    )
    assert decision.allow is True


def test_unauthorized_retrieval_denied() -> None:
    decision = _evaluator().evaluate_retrieval(
        {
            "subject": {
                "user_id": "u-2",
                "role": "intern",
                "department": "atlas_advisory",
                "tenant_id": "atlas-prod",
            },
            "document": {"owner_department": "atlas_advisory", "classification": "confidential"},
        }
    )
    assert decision.allow is False
    assert decision.reason == "role_denied"


def test_missing_identity_denied() -> None:
    decision = _evaluator().evaluate_retrieval(
        {
            "subject": {
                "role": "advisor",
                "department": "atlas_advisory",
                "tenant_id": "atlas-prod",
            },
            "document": {"owner_department": "atlas_advisory", "classification": "confidential"},
        }
    )
    assert decision.allow is False
    assert "subject.user_id" in decision.missing_fields


def test_missing_document_classification_denied() -> None:
    decision = _evaluator().evaluate_retrieval(
        {
            "subject": {
                "user_id": "u-3",
                "role": "advisor",
                "department": "atlas_advisory",
                "tenant_id": "atlas-prod",
            },
            "document": {"owner_department": "atlas_advisory"},
        }
    )
    assert decision.allow is False
    assert "document.classification" in decision.missing_fields


def test_high_risk_tool_without_approval_denied() -> None:
    decision = _evaluator().evaluate_tool(
        {
            "subject": {
                "user_id": "u-4",
                "role": "advisor",
                "department": "atlas_advisory",
                "tenant_id": "atlas-prod",
            },
            "tool": {"name": "portfolio_export", "risk_level": "high"},
            "approval": {"human_approved": False},
        }
    )
    assert decision.allow is False
    assert decision.reason == "approval_required"


def test_unknown_tool_denied() -> None:
    decision = _evaluator().evaluate_tool(
        {
            "subject": {
                "user_id": "u-5",
                "role": "advisor",
                "department": "atlas_advisory",
                "tenant_id": "atlas-prod",
            },
            "tool": {"name": "terminal_exec", "risk_level": "high"},
            "approval": {"human_approved": True},
        }
    )
    assert decision.allow is False
    assert decision.reason == "unknown_tool"
