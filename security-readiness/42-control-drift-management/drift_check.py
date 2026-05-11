#!/usr/bin/env python3
import argparse
from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass(frozen=True)
class DriftRule:
    category: str
    path: str


DRIFT_RULES = [
    DriftRule("policy", "security-readiness/41-change-management/policy-change-approval-workflow.md"),
    DriftRule("policy", "security-readiness/04-controls/onyx-retrieval-authorization-controls.md"),
    DriftRule("retrieval_boundary", "security-readiness/28-knowledge-base-security/chunk-level-authorization-review.md"),
    DriftRule("tool_permission", "security-readiness/17-agent-tool-governance/tool-capability-matrix.md"),
    DriftRule("tool_permission", "security-readiness/41-change-management/tool-permission-change-approval-workflow.md"),
    DriftRule("evidence", "security-readiness/09-evidence"),
    DriftRule("dashboard", "security-readiness/33-monitoring-alerting/launch-gate-drift-alerting.md"),
    DriftRule("dashboard", "security-readiness/33-monitoring-alerting/rules/launch-gate-drift-alerting.yaml"),
    DriftRule("governance", "security-readiness/11-governance/onyx-review-cadence.md"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check control drift by validating required artifacts exist")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()

    missing: list[DriftRule] = []
    for rule in DRIFT_RULES:
        target = root / rule.path
        if not target.exists():
            missing.append(rule)

    if not missing:
        print("drift_check: PASS (no missing required control artifacts)")
        return 0

    print("drift_check: FAIL (required control artifacts missing)")
    for rule in missing:
        print(f"- category={rule.category} missing={rule.path}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
