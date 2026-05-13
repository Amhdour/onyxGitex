# CI Rerun and Artifact Instructions

1. Open GitHub Actions.
2. Select **LangGraph Agent Lab Evidence** workflow.
3. Run workflow on `main` or the PR branch.
4. Wait for completion.
5. Record run URL and run ID.
6. Download artifact named `langgraph-agent-lab-evidence`.
7. Extract into `agent-security-readiness/23-langgraph-agent-lab/ci-downloaded-artifact/`.
8. Run `verify-ci-artifacts-local.py`.
9. Update `ci-result-summary.md` only from real verifier output.
10. Keep launch gate `NO_GO`.
