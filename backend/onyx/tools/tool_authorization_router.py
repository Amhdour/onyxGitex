from __future__ import annotations

from dataclasses import dataclass
from typing import Any


HIGH_RISK_TOOLS = {"python", "code_interpreter", "coding_agent", "mcp", "openapi"}


@dataclass(frozen=True)
class ToolAuthorizationDecision:
    allowed: bool
    reason: str
    risk_level: str


class ToolAuthorizationRouter:
    """Fail-closed tool authorization gate for runtime execution."""

    def authorize(
        self,
        *,
        tool_name: str,
        user_id: str | None,
        policy: dict[str, Any] | None,
        approval_id: str | None,
    ) -> ToolAuthorizationDecision:
        if not policy:
            return ToolAuthorizationDecision(False, "missing_tool_policy", "unknown")

        rules = policy.get(tool_name)
        if rules is None:
            return ToolAuthorizationDecision(False, "unknown_tool", "unknown")

        if not user_id:
            return ToolAuthorizationDecision(False, "missing_user_identity", "unknown")

        risk_level = str(rules.get("risk_level", "low")).lower()
        if risk_level == "high" and not approval_id:
            return ToolAuthorizationDecision(False, "missing_explicit_approval", "high")

        if not bool(rules.get("allowed", False)):
            return ToolAuthorizationDecision(False, "tool_not_allowed", risk_level)

        return ToolAuthorizationDecision(True, "authorized", risk_level)
