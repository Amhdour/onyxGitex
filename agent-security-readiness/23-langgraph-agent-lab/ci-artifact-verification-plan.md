Purpose: verify CI artifacts for .github/workflows/langgraph-agent-lab-evidence.yml.
Required evidence: run ID, job status, artifact name, file list, downloaded contents, artifact final-run-status.json, artifact graph-runtime-summary.json.
Proves: CI executed and produced expected evidence files.
Does not prove: production safety, external side-effect safety, launch approval.
Statuses: CI_NOT_RUN, CI_RUNNING, CI_PASS, CI_FAIL, CI_ARTIFACT_MISSING, CI_ARTIFACT_VERIFIED.
Next action: trigger workflow and download artifact via GitHub Actions evidence process.
