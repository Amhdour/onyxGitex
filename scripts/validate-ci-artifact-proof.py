#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
V2A_DIR = ROOT / "security-readiness/evidence-artifacts/version-2a-rag-runtime"
V2B_DIR = ROOT / "security-readiness/evidence-artifacts/version-2b-ci-artifact-proof"
STATUS_PATH = V2B_DIR / "version-2b-ci-artifact-status.json"
WORKFLOW_PATH = ROOT / ".github/workflows/version-2b-rag-runtime-evidence.yml"
WORKFLOW_CONTRACT = V2B_DIR / "workflow-contract.json"
ARTIFACT_CONTRACT = V2B_DIR / "artifact-contract.json"
EXPECTED_LIST = V2B_DIR / "expected-artifact-file-list.txt"


def load_json(path: Path):
    return json.loads(path.read_text())


def required_files():
    return [l.strip() for l in EXPECTED_LIST.read_text().splitlines() if l.strip()]


def validate_v2a_dir(base: Path, errors: list[str]):
    for f in required_files():
        if not (base / f).exists():
            errors.append(f"missing required file: {base / f}")
    status_file = base / "rag-runtime-final-status.json"
    if status_file.exists():
        try:
            s = load_json(status_file)
            if s.get("launch_status") != "PARTIAL_RUNTIME_EVIDENCE":
                errors.append("rag-runtime-final-status.json launch_status must be PARTIAL_RUNTIME_EVIDENCE")
            if s.get("production_ready") is not False:
                errors.append("rag-runtime-final-status.json production_ready must be false")
            if s.get("go_decision") is not False:
                errors.append("rag-runtime-final-status.json go_decision must be false")
        except Exception as e:
            errors.append(f"invalid JSON in {status_file}: {e}")


def mode_local_contract() -> int:
    errors = []
    for p in [WORKFLOW_PATH, STATUS_PATH, WORKFLOW_CONTRACT, ARTIFACT_CONTRACT, EXPECTED_LIST, V2A_DIR]:
        if not p.exists():
            errors.append(f"missing required path: {p}")
    if not errors:
        validate_v2a_dir(V2A_DIR, errors)
        try:
            s = load_json(STATUS_PATH)
            if s.get("production_ready") is not False:
                errors.append("Version 2B status must keep production_ready=false")
            if s.get("go_decision") is not False:
                errors.append("Version 2B status must keep go_decision=false")
            status = s.get("status")
            workflow = s.get("workflow", {})
            artifacts = s.get("artifacts", {})
            if s.get("production_ready") is True or s.get("go_decision") is True:
                errors.append("Version 2B must not claim production_ready/go_decision true")
            if status == "CI_ARTIFACT_VERIFIED":
                for rf in ["workflow-run-evidence.json", "artifact-download-evidence.json", "artifact-file-list.txt", "verified-artifact-manifest.json"]:
                    if not (V2B_DIR / rf).exists():
                        errors.append(f"CI_ARTIFACT_VERIFIED requires {rf}")
                if workflow.get("run_id") in (None, ""):
                    errors.append("CI_ARTIFACT_VERIFIED requires workflow.run_id")
                if workflow.get("job_status") != "success":
                    errors.append("CI_ARTIFACT_VERIFIED requires workflow.job_status=success")
                if artifacts.get("artifact_id") in (None, ""):
                    errors.append("CI_ARTIFACT_VERIFIED requires artifacts.artifact_id")
                if artifacts.get("artifact_download_verified") is not True:
                    errors.append("CI_ARTIFACT_VERIFIED requires artifacts.artifact_download_verified=true")
                if artifacts.get("required_files_verified_in_downloaded_artifact") is not True:
                    errors.append("CI_ARTIFACT_VERIFIED requires artifacts.required_files_verified_in_downloaded_artifact=true")
            if status == "CI_WORKFLOW_CONFIGURED_NOT_VERIFIED":
                if s.get("ci_artifact_verified") is not False:
                    errors.append("CI_WORKFLOW_CONFIGURED_NOT_VERIFIED requires ci_artifact_verified=false")
                if workflow.get("run_verified") is not False:
                    errors.append("CI_WORKFLOW_CONFIGURED_NOT_VERIFIED requires workflow.run_verified=false")
                if artifacts.get("artifact_download_verified") is not False:
                    errors.append("CI_WORKFLOW_CONFIGURED_NOT_VERIFIED requires artifacts.artifact_download_verified=false")
            serialized = json.dumps(s).upper()
            for forbidden in ["\"STAGING_VERIFIED\": TRUE", "\"CLIENT_VERIFIED\": TRUE", "\"GO\""]:
                if forbidden in serialized:
                    errors.append(f"forbidden claim detected: {forbidden}")
        except Exception as e:
            errors.append(f"invalid Version 2B status JSON: {e}")

    out = V2B_DIR / "ci-local-validation-result.txt"
    if errors:
        out.write_text("FAIL\n" + "\n".join(errors) + "\n")
        print("FAIL: local-ci-contract")
        for e in errors:
            print(f" - {e}")
        return 1

    out.write_text(
        "PASS\nmode=local-ci-contract\ntimestamp_utc="
        + datetime.now(timezone.utc).isoformat()
        + "\n"
    )
    print("PASS: local-ci-contract")
    return 0


def mode_artifact_dir(artifact_dir: str | None) -> int:
    if not artifact_dir:
        print("FAIL: --artifact-dir is required when --mode artifact-directory")
        return 1
    base = Path(artifact_dir)
    errors = []
    if not base.exists() or not base.is_dir():
        errors.append(f"artifact directory not found: {base}")
    else:
        validate_v2a_dir(base, errors)
        py_out = base / "rag-pytest-output.txt"
        if py_out.exists():
            text = py_out.read_text(errors="ignore")
            if "8 passed" not in text and "8 passed," not in text:
                errors.append("rag-pytest-output.txt does not contain '8 passed' evidence")
        lgr = base / "rag-launch-gate-result.json"
        if lgr.exists():
            try:
                lg = load_json(lgr)
                if lg.get("go_decision") is True:
                    errors.append("rag-launch-gate-result.json must not claim GO")
            except Exception as e:
                errors.append(f"invalid JSON in {lgr}: {e}")
    if errors:
        print("FAIL: artifact-directory")
        for e in errors:
            print(f" - {e}")
        return 1
    print("PASS: artifact-directory")
    print(f"validated_artifact_dir={base}")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=["local-ci-contract", "artifact-directory"])
    parser.add_argument("--artifact-dir")
    args = parser.parse_args()
    if args.mode == "local-ci-contract":
        rc = mode_local_contract()
    else:
        rc = mode_artifact_dir(args.artifact_dir)
    raise SystemExit(rc)


if __name__ == "__main__":
    main()
