from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


class FailClosedError(PermissionError):
    """Raised when required authorization context is missing."""


@dataclass(frozen=True)
class AuthContext:
    user_id: str | None
    groups: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class ResourcePolicy:
    resource_id: str
    allowed_users: frozenset[str] = field(default_factory=frozenset)
    allowed_groups: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class ToolPolicy:
    tool_name: str
    allowed_users: frozenset[str] = field(default_factory=frozenset)
    allowed_groups: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str


class PolicyDecisionEngine:
    def evaluate(
        self, auth_context: AuthContext | None, policy: ResourcePolicy | ToolPolicy | None
    ) -> PolicyDecision:
        if auth_context is None or auth_context.user_id is None:
            raise FailClosedError("Missing identity context")
        if policy is None:
            raise FailClosedError("Missing policy")

        user_allowed = auth_context.user_id in policy.allowed_users
        group_allowed = bool(auth_context.groups.intersection(policy.allowed_groups))

        if user_allowed or group_allowed:
            return PolicyDecision(allowed=True, reason="Policy allow")
        return PolicyDecision(allowed=False, reason="Policy deny")


class RetrievalAuthorizationGuard:
    def __init__(self, policy_engine: PolicyDecisionEngine) -> None:
        self._policy_engine = policy_engine

    def authorize_document(
        self,
        auth_context: AuthContext | None,
        document_id: str,
        policy_map: dict[str, ResourcePolicy] | None,
    ) -> PolicyDecision:
        if policy_map is None:
            raise FailClosedError("Missing document policy map")
        policy = policy_map.get(document_id)
        if policy is None:
            raise FailClosedError(f"Missing document permission for {document_id}")
        return self._policy_engine.evaluate(auth_context, policy)


class ToolAuthorizationRouter:
    def __init__(self, policy_engine: PolicyDecisionEngine) -> None:
        self._policy_engine = policy_engine

    def authorize_tool(
        self,
        auth_context: AuthContext | None,
        tool_name: str,
        policy_map: dict[str, ToolPolicy] | None,
    ) -> PolicyDecision:
        if policy_map is None:
            raise FailClosedError("Missing tool policy map")
        tool_policy = policy_map.get(tool_name)
        if tool_policy is None:
            raise FailClosedError(f"Missing tool authorization for {tool_name}")
        return self._policy_engine.evaluate(auth_context, tool_policy)


class AuditLogger:
    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def emit(self, event_type: str, payload: dict[str, Any]) -> dict[str, Any]:
        event = {
            "event_type": event_type,
            "timestamp": datetime.now(UTC).isoformat(),
            "payload": payload,
        }
        self.events.append(event)
        return event


class RuntimeTracer:
    def __init__(self) -> None:
        self.trace_events: list[dict[str, Any]] = []

    def emit(self, trace_name: str, attrs: dict[str, Any]) -> dict[str, Any]:
        event = {
            "trace_name": trace_name,
            "timestamp": datetime.now(UTC).isoformat(),
            "attrs": attrs,
        }
        self.trace_events.append(event)
        return event


def fail_closed_if_missing(value: Any, missing_message: str) -> Any:
    if value is None:
        raise FailClosedError(missing_message)
    return value


class EvidencePackGenerator:
    def generate_manifest(self, control_results: dict[str, str]) -> dict[str, Any]:
        return {
            "generated_at": datetime.now(UTC).isoformat(),
            "controls": control_results,
            "verified_count": sum(1 for status in control_results.values() if status == "Verified"),
            "unknown_count": sum(1 for status in control_results.values() if status == "Unknown"),
        }


class LaunchGateEngine:
    def evaluate(self, readiness_score: float, minimum_score: float = 85.0) -> dict[str, Any]:
        passed = readiness_score >= minimum_score
        return {
            "minimum_score": minimum_score,
            "readiness_score": readiness_score,
            "gate_status": "PASS" if passed else "BLOCK",
        }


class ReadinessScoringEngine:
    def calculate(self, weighted_controls: dict[str, tuple[float, float]]) -> float:
        total_weight = sum(weight for weight, _ in weighted_controls.values())
        if total_weight <= 0:
            raise ValueError("Total weight must be greater than zero")
        weighted_sum = sum(weight * score for weight, score in weighted_controls.values())
        return round(weighted_sum / total_weight, 2)


class DashboardDataExporter:
    def export_json(self, payload: dict[str, Any], output_path: Path) -> Path:
        output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return output_path

    def export_csv(self, rows: list[dict[str, Any]], output_path: Path) -> Path:
        if not rows:
            raise ValueError("Rows cannot be empty")

        fieldnames = sorted(rows[0].keys())
        with output_path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        return output_path
