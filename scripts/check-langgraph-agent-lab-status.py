#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

STATUS_PATH = Path("agent-security-readiness/23-langgraph-agent-lab/final-run-status.json")

REQUIRED_FIELDS = [
    "evidence_package", "control_area", "schema_version", "status_dimensions", "runtime",
    "claims_allowed", "claims_not_allowed", "artifacts_present", "artifacts_missing",
    "open_blockers", "next_required_action",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> int:
    data = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
    for field in REQUIRED_FIELDS:
        if field not in data:
            fail(f"Missing required field: {field}")

    sd = data["status_dimensions"]
    runtime = data["runtime"]
    ap = set(data.get("artifacts_present", []))
    claims_not = data.get("claims_not_allowed", [])

    launch = sd.get("launch_gate_status")
    evidence = sd.get("evidence_status")
    runtime_status = sd.get("runtime_status")

    if launch == "GO" and evidence in {"NOT_ENOUGH_EVIDENCE", "PARTIAL_EVIDENCE"}:
        fail("launch_gate_status cannot be GO with NOT_ENOUGH_EVIDENCE or PARTIAL_EVIDENCE")

    if launch == "GO" and runtime.get("runtime_trace_verified") is False:
        fail("launch_gate_status cannot be GO when runtime_trace_verified is false")

    if runtime_status == "PASS":
        for needed in [
            "runtime-artifacts/runtime-trace.json",
            "runtime-artifacts/policy-decision-log.json",
        ]:
            if needed not in ap:
                fail(f"runtime_status PASS requires artifact present: {needed}")

    if sd.get("tool_authorization_status") == "MOCK_RUNTIME_VERIFIED":
        required_non_claims = [
            "Production LangGraph deployment is verified.",
            "Real external tool execution is verified.",
            "The autonomous agent is safe to launch.",
        ]
        for nc in required_non_claims:
            if nc not in claims_not:
                fail(f"claims_not_allowed missing required non-claim: {nc}")

    if evidence == "PARTIAL_EVIDENCE" and launch not in {"NO_GO", "CONDITIONAL_GO"}:
        fail("PARTIAL_EVIDENCE requires launch_gate_status NO_GO or CONDITIONAL_GO")

    print("PASS: final-run-status.json consistency checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
