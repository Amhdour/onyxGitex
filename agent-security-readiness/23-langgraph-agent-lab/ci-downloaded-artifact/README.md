# LangGraph CI Downloaded Artifact Staging

This directory is intentionally for manually downloaded GitHub Actions artifacts.

- Do not fabricate artifacts.
- Do not commit large zipped artifacts unless necessary.
- Place extracted artifact files here only after downloading from GitHub Actions.
- Run:

```bash
python agent-security-readiness/23-langgraph-agent-lab/verify-ci-artifacts-local.py --artifact-dir agent-security-readiness/23-langgraph-agent-lab/ci-downloaded-artifact/
```

- If no artifact is present, status remains `CI_ARTIFACT_NOT_AVAILABLE`.
- If artifact validates, update `ci-result-summary.md` and `final-run-status.json` based only on direct proof.
