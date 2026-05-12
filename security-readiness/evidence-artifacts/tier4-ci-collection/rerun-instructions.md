# Tier 4 CI Collection Workflow Rerun Instructions

## Manual rerun steps
1. Open GitHub Actions and select **Tier 4 Runtime Collection**.
2. Choose **Run workflow** on the target branch/commit.
3. Wait for all steps to complete (including failures) and verify artifact upload executed.

## Artifacts to download
Download `tier4-runtime-collection` and verify these files exist:
- `dependency-install.log`
- `dependency-import-check.log`
- `pytest-collect.log`
- `runtime-test.log`
- `collection-status.txt`

## Result classification
- If dependency install/import fails, classify as `FAILED_DEPENDENCY_IMPORT`.
- If pytest collection fails, classify as `FAILED_PYTEST_COLLECTION`.
- If runtime tests were executed in a separate runtime workflow and failed, classify as `FAILED_RUNTIME_TESTS`.
- If retrieval-boundary test evidence fails, classify as `FAILED_RETRIEVAL_BOUNDARY`.
- If logs are absent/corrupt, classify as `FAILED_UNKNOWN_NO_LOGS`.

## What not to claim
- Do not claim runtime PASS from this collection-only workflow.
- Do not claim retrieval-boundary PASS without runtime test evidence.
- Do not claim launch readiness from collection logs alone.

## Update `final-run-status.json` after rerun
1. Record the workflow run ID, date (UTC), branch, and commit SHA.
2. Update status fields using evidence-first taxonomy (`VERIFIED`, `PARTIALLY_CONFIRMED`, `NOT_RUN`, `FAILED`, `NOT_ENOUGH_EVIDENCE`).
3. Add artifact references for each status update.
4. Keep unresolved or missing evidence explicitly labeled `UNKNOWN` or `NOT_ENOUGH_EVIDENCE`.
