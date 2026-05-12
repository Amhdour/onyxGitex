from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


RETRIEVAL_REQUIRED_FIELDS = [
    "subject.user_id",
    "subject.role",
    "subject.department",
    "subject.tenant_id",
    "document.owner_department",
    "document.classification",
]

TOOL_REQUIRED_FIELDS = [
    "subject.user_id",
    "subject.role",
    "subject.department",
    "subject.tenant_id",
    "tool.name",
    "tool.risk_level",
    "approval.human_approved",
]


@dataclass
class Decision:
    allow: bool
    reason: str
    policy_id: str
    missing_fields: list[str]
    evidence: dict[str, Any]


class PolicyEvaluator:
    def __init__(self, policy_dir: Path) -> None:
        self.policy_dir = policy_dir
        self.schema = self._read_json("policy_schema.json")
        self.retrieval_policy = self._load_and_validate("retrieval_authorization.yaml")
        self.tool_policy = self._load_and_validate("tool_authorization.yaml")

    def _read_json(self, filename: str) -> dict[str, Any]:
        return json.loads((self.policy_dir / filename).read_text())

    def _load_and_validate(self, filename: str) -> dict[str, Any]:
        policy = self._read_json(filename)
        self._validate_policy_shape(policy, filename)
        return policy

    def _validate_policy_shape(self, policy: dict[str, Any], filename: str) -> None:
        required = self.schema["required"]
        for key in required:
            if key not in policy:
                raise ValueError(f"Invalid policy {filename}: missing required key '{key}'")
        if policy.get("default_effect") != "deny":
            raise ValueError(f"Invalid policy {filename}: default_effect must be deny")
        if policy.get("fail_closed") is not True:
            raise ValueError(f"Invalid policy {filename}: fail_closed must be true")

    def evaluate_retrieval(self, request: dict[str, Any]) -> Decision:
        missing = self._missing_fields(request, RETRIEVAL_REQUIRED_FIELDS)
        policy_id = self.retrieval_policy["policy_id"]
        if missing:
            return Decision(False, "missing_context", policy_id, missing, {"fail_closed": True})

        subject = request["subject"]
        document = request["document"]

        for rule in self.retrieval_policy.get("rules", []):
            when = rule["when"]
            if subject["role"] in when.get("roles_denied", []):
                return Decision(False, "role_denied", policy_id, [], {"rule_id": rule["id"]})
            if subject["role"] not in when.get("roles_allowed", []):
                continue
            if subject["department"] not in when.get("departments_allowed", []):
                continue
            if subject["tenant_id"] not in when.get("tenant_ids_allowed", []):
                continue
            if document["owner_department"] not in when.get("document_owner_departments_allowed", []):
                continue
            if document["classification"] not in when.get("document_classifications_allowed", []):
                continue
            if rule["effect"] == "allow":
                return Decision(True, "matched_allow_rule", policy_id, [], {"rule_id": rule["id"]})

        return Decision(False, "default_deny", policy_id, [], {"fail_closed": True})

    def evaluate_tool(self, request: dict[str, Any]) -> Decision:
        missing = self._missing_fields(request, TOOL_REQUIRED_FIELDS)
        policy_id = self.tool_policy["policy_id"]
        if missing:
            return Decision(False, "missing_context", policy_id, missing, {"fail_closed": True})

        subject = request["subject"]
        tool = request["tool"]
        approved = bool(request["approval"]["human_approved"])

        for tool_rule in self.tool_policy.get("tools", []):
            if tool_rule["tool_name"] != tool["name"]:
                continue
            if subject["role"] in tool_rule.get("roles_denied", []):
                return Decision(False, "role_denied", policy_id, [], {"tool_name": tool["name"]})
            if subject["role"] not in tool_rule.get("roles_allowed", []):
                return Decision(False, "role_not_allowed", policy_id, [], {"tool_name": tool["name"]})
            if tool_rule["tool_risk_level"] != tool["risk_level"]:
                return Decision(False, "risk_level_mismatch", policy_id, [], {"tool_name": tool["name"]})
            if tool_rule["human_approval_required"] and not approved:
                return Decision(False, "approval_required", policy_id, [], {"tool_name": tool["name"]})
            return Decision(True, "matched_allow_rule", policy_id, [], {"tool_name": tool["name"]})

        return Decision(False, "unknown_tool", policy_id, [], {"tool_name": tool["name"], "fail_closed": True})

    def _missing_fields(self, payload: dict[str, Any], required_fields: list[str]) -> list[str]:
        missing: list[str] = []
        for field_path in required_fields:
            cursor: Any = payload
            for part in field_path.split("."):
                if not isinstance(cursor, dict) or part not in cursor or cursor[part] in (None, ""):
                    missing.append(field_path)
                    break
                cursor = cursor[part]
        return missing
