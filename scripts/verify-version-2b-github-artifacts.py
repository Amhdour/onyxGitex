#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
V2B = ROOT / "security-readiness/evidence-artifacts/version-2b-ci-artifact-proof"
STATUS_PATH = V2B / "version-2b-ci-artifact-status.json"
REQ_FILES_PATH = V2B / "expected-artifact-file-list.txt"
WORKFLOW_EVIDENCE = V2B / "workflow-run-evidence.json"
ARTIFACT_EVIDENCE = V2B / "artifact-download-evidence.json"
ARTIFACT_FILE_LIST = V2B / "artifact-file-list.txt"
VERIFIED_MANIFEST = V2B / "verified-artifact-manifest.json"


def load_json(path: Path):
    return json.loads(path.read_text())


def expected_files() -> list[str]:
    return [line.strip() for line in REQ_FILES_PATH.read_text().splitlines() if line.strip()]


def has_forbidden_go_claims(obj: dict) -> bool:
    serialized = json.dumps(obj).upper()
    return any(token in serialized for token in ["\"PRODUCTION_READY\": TRUE", "\"GO_DECISION\": TRUE", "\"STAGING_VERIFIED\": TRUE", "\"CLIENT_VERIFIED\": TRUE"])


def mode_local_contract() -> int:
    errors = []
    if not STATUS_PATH.exists():
        errors.append(f"missing status file: {STATUS_PATH}")
    if not REQ_FILES_PATH.exists():
        errors.append(f"missing expected file list: {REQ_FILES_PATH}")
    if errors:
        print("FAIL: local-contract")
        for e in errors:
            print(f" - {e}")
        return 1

    status = load_json(STATUS_PATH)
    state = status.get("status")
    if has_forbidden_go_claims(status):
        errors.append("status contains forbidden true claims for production/go/staging/client")
    if status.get("production_ready") is not False:
        errors.append("production_ready must remain false")
    if status.get("go_decision") is not False:
        errors.append("go_decision must remain false")

    if state == "CI_ARTIFACT_VERIFIED":
        errors.append("local-contract mode forbids CI_ARTIFACT_VERIFIED without recorded-evidence verification")
    elif state not in {"CI_WORKFLOW_CONFIGURED_NOT_VERIFIED", "CI_ARTIFACT_GENERATED_UNVERIFIED", "NOT_ENOUGH_EVIDENCE", "NO_GO"}:
        errors.append(f"unexpected status for local-contract mode: {state}")

    if errors:
        print("FAIL: local-contract")
        for e in errors:
            print(f" - {e}")
        return 1

    print("PASS: local-contract")
    print(f"status={state}")
    return 0


def mode_recorded_evidence() -> int:
    errors = []
    required_paths = [WORKFLOW_EVIDENCE, ARTIFACT_EVIDENCE, ARTIFACT_FILE_LIST, VERIFIED_MANIFEST, STATUS_PATH, REQ_FILES_PATH]
    for p in required_paths:
        if not p.exists():
            errors.append(f"missing required evidence file: {p}")
    if errors:
        print("FAIL: recorded-evidence")
        for e in errors:
            print(f" - {e}")
        return 1

    status = load_json(STATUS_PATH)
    workflow_ev = load_json(WORKFLOW_EVIDENCE)
    artifact_ev = load_json(ARTIFACT_EVIDENCE)
    manifest = load_json(VERIFIED_MANIFEST)
    listed = {line.strip() for line in ARTIFACT_FILE_LIST.read_text().splitlines() if line.strip()}
    req = set(expected_files())

    if workflow_ev.get("run_id") in (None, ""):
        errors.append("workflow-run-evidence run_id must be non-null")
    if workflow_ev.get("job_status") != "success":
        errors.append("workflow-run-evidence job_status must be success")
    if artifact_ev.get("artifact_id") in (None, ""):
        errors.append("artifact-download-evidence artifact_id must be non-null")
    if artifact_ev.get("artifact_download_verified") is not True:
        errors.append("artifact-download-evidence artifact_download_verified must be true")
    if not req.issubset(listed):
        errors.append("artifact-file-list.txt missing one or more required files")

    if manifest.get("verification_status") != "PASS":
        errors.append("verified-artifact-manifest verification_status must be PASS")
    for k in ["required_files_present", "required_json_valid", "version_2a_status_valid", "pytest_output_valid", "production_ready_false", "go_decision_false"]:
        if manifest.get(k) is not True:
            errors.append(f"verified-artifact-manifest {k} must be true")

    if status.get("status") != "CI_ARTIFACT_VERIFIED":
        errors.append("status must be CI_ARTIFACT_VERIFIED in recorded-evidence mode")
    if status.get("production_ready") is not False or status.get("go_decision") is not False:
        errors.append("status must keep production_ready=false and go_decision=false")
    if has_forbidden_go_claims(status):
        errors.append("status contains forbidden true claims for production/go/staging/client")

    if errors:
        print("FAIL: recorded-evidence")
        for e in errors:
            print(f" - {e}")
        return 1

    print("PASS: recorded-evidence")
    print(f"run_id={workflow_ev.get('run_id')} artifact_id={artifact_ev.get('artifact_id')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=["local-contract", "recorded-evidence"])
    args = parser.parse_args()
    if args.mode == "local-contract":
        return mode_local_contract()
    return mode_recorded_evidence()


if __name__ == "__main__":
    sys.exit(main())
