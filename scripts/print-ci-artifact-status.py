#!/usr/bin/env python3
import json
from pathlib import Path

status_path = Path("security-readiness/evidence-artifacts/version-2b-ci-artifact-proof/version-2b-ci-artifact-status.json")
status = json.loads(status_path.read_text())

workflow = status.get("workflow", {})
artifacts = status.get("artifacts", {})
fields = [
    ("version", status.get("version")),
    ("gate", status.get("gate")),
    ("status", status.get("status")),
    ("production_ready", status.get("production_ready")),
    ("go_decision", status.get("go_decision")),
    ("ci_artifact_verified", status.get("ci_artifact_verified")),
    ("workflow_file", workflow.get("workflow_file")),
    ("workflow_name", workflow.get("workflow_name")),
    ("workflow_configured", workflow.get("configured")),
    ("workflow_run_verified", workflow.get("run_verified")),
    ("run_id", workflow.get("run_id")),
    ("job_status", workflow.get("job_status")),
    ("expected_artifact_name", artifacts.get("expected_artifact_name")),
    ("artifact_download_verified", artifacts.get("artifact_download_verified")),
    ("required_files_verified_in_downloaded_artifact", artifacts.get("required_files_verified_in_downloaded_artifact")),
    ("next_required_action", status.get("next_required_action")),
]
for k, v in fields:
    print(f"{k}: {v}")
