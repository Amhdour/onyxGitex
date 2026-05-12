# Tier 4 CI Collection Plan

Date: 2026-05-12

## Objective
Provide a reproducible GitHub Actions path for **Tier 4 runtime test collection only** using Python 3.11 and repository-supported backend dependency installation.

## Constraints and Launch Posture
- Local host runtime execution is currently blocked by toolchain and environment constraints.
- This workflow does **not** execute runtime assertions as a launch gate pass.
- Launch posture remains **NOT_ENOUGH_EVIDENCE**.
- Collection outcome label is **COLLECTED_SKIPPED** when collection completes.

## CI Execution Plan
1. Manually trigger `.github/workflows/tier4-runtime-collection.yml` via `workflow_dispatch`.
2. Use `ubuntu-latest` runner.
3. Set up Python 3.11 via `actions/setup-python`.
4. Install `uv`.
5. Install backend + dev groups with:
   - `uv sync --python 3.11 --no-default-groups --group backend --group dev`
6. Run pytest collection-only command for Tier 4 runtime skeleton files.
7. Persist logs regardless of success/failure.
8. Upload artifacts for audit traceability.

## Evidence Expectations
- If collection succeeds:
  - Record collection output and preserve status as `COLLECTED_SKIPPED`.
  - Do not claim PASS.
  - Do not claim launch GO.
- If collection fails:
  - Preserve failure logs in artifacts.
  - Keep posture as `NOT_ENOUGH_EVIDENCE`.

## Verification Status
- Workflow added: **Verified** (repository artifact).
- Runtime test pass evidence: **Unknown** (not executed as pass/fail gate in this task).
- Launch gate closure: **Unknown/Not Claimed**.
