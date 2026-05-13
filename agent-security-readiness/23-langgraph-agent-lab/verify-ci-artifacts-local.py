#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

LAB = Path(__file__).resolve().parent
DEFAULT_OUTPUT = LAB / "ci-artifact-verification-output.json"
DEFAULT_ARTIFACT_DIR = LAB / "ci-downloaded-artifact"

REQUIRED_FILES = [
    "final-run-status.json",
    "runtime-execution-report.md",
    "evidence-manifest.md",
    "runtime-artifacts/langgraph-dependency-check.json",
    "graph-runtime-artifacts/graph-runtime-summary.json",
    "graph-runtime-artifacts/graph-runtime-trace.json",
    "graph-runtime-artifacts/graph-policy-decision-log.json",
    "graph-runtime-artifacts/graph-audit-events.json",
    "graph-runtime-artifacts/graph-memory-boundary-log.json",
    "graph-runtime-artifacts/graph-sandboxed-tool-results.json",
    "graph-runtime-artifacts/graph-incident-timeline.json",
]
JSON_REQUIRED = [path for path in REQUIRED_FILES if path.endswith(".json")]


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate downloaded LangGraph CI evidence artifacts.")
    parser.add_argument("--artifact-dir", default=str(DEFAULT_ARTIFACT_DIR), help="Directory containing extracted CI artifact files.")
    parser.add_argument("--write-summary", default=str(DEFAULT_OUTPUT), help="Path to write JSON verification summary.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    artifact_dir = Path(args.artifact_dir).resolve()
    summary_path = Path(args.write_summary).resolve()

    artifact_exists = artifact_dir.exists() and artifact_dir.is_dir()
    required_files_present: list[str] = []
    required_files_missing: list[str] = []
    json_validation: dict[str, str] = {}

    verification_status = "CI_ARTIFACT_NOT_AVAILABLE"

    if artifact_exists:
        for rel in REQUIRED_FILES:
            path = artifact_dir / rel
            if path.exists():
                required_files_present.append(rel)
            else:
                required_files_missing.append(rel)

        for rel in JSON_REQUIRED:
            path = artifact_dir / rel
            if not path.exists():
                json_validation[rel] = "MISSING"
                continue
            try:
                json.loads(path.read_text())
                json_validation[rel] = "VALID"
            except Exception as exc:  # noqa: BLE001
                json_validation[rel] = f"INVALID: {exc}"

        has_invalid_json = any(state != "VALID" for state in json_validation.values())
        if required_files_missing or has_invalid_json:
            verification_status = "CI_ARTIFACT_INCOMPLETE"
        else:
            verification_status = "CI_ARTIFACT_VERIFIED"

    summary = {
        "artifact_dir": str(artifact_dir),
        "artifact_dir_exists": artifact_exists,
        "required_files_total": len(REQUIRED_FILES),
        "required_files_present": required_files_present,
        "required_files_missing": required_files_missing,
        "json_validation": json_validation,
        "verification_status": verification_status,
        "evidence_implication": "Direct CI artifact verification is present."
        if verification_status == "CI_ARTIFACT_VERIFIED"
        else "CI artifact proof is not yet verified from downloaded artifacts.",
        "launch_gate_implication": "NO_GO",
        "checked_at_utc": now_utc(),
    }

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")

    print("LangGraph CI artifact verification")
    print(f"- Artifact directory: {artifact_dir}")
    print(f"- Artifact directory exists: {artifact_exists}")
    print(f"- Verification status: {verification_status}")
    print(f"- Required files present: {len(required_files_present)}/{len(REQUIRED_FILES)}")
    if required_files_missing:
        print("- Missing required files:")
        for missing in required_files_missing:
            print(f"  * {missing}")
    invalid_json = {k: v for k, v in json_validation.items() if v != "VALID"}
    if invalid_json:
        print("- JSON validation issues:")
        for rel, reason in invalid_json.items():
            print(f"  * {rel}: {reason}")
    print(f"- Summary written to: {summary_path}")

    if verification_status == "CI_ARTIFACT_INCOMPLETE":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
