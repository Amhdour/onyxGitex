## Current CI Evidence Classification

- workflow_path: .github/workflows/langgraph-agent-lab-evidence.yml
- workflow_run_verified: false
- artifact_downloaded: false
- artifact_verified: false
- ci_workflow_status: CI_NOT_VERIFIED
- ci_artifact_status: CI_ARTIFACT_NOT_VERIFIED
- evidence_status: LOCAL_ONLY_PARTIAL_EVIDENCE
- launch_gate_status: NO_GO

## Evidence Required To Upgrade
1. Workflow run URL or run ID.
2. Job status.
3. Artifact name.
4. Artifact download result.
5. Artifact file list.
6. final-run-status.json from artifact.
7. graph-runtime-summary.json from artifact.
8. ci-artifact-verification-output.json.

## Non-Claims
- CI workflow existence does not prove CI execution.
- Local artifacts do not prove CI artifacts.
- CI artifacts do not prove production safety.
- CI PASS does not equal launch approval.
