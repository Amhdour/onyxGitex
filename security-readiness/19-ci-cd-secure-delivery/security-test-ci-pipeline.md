# Security Test CI Pipeline

Date: 2026-05-11  
Status: **Plan (Partially Confirmed)**

## Objective
Define a minimal additive CI pipeline that runs security-readiness test signals without changing existing product CI behavior.

## Existing CI Evidence Reviewed
- `.github/workflows/pr-quality-checks.yml`
- `.github/workflows/pr-python-tests.yml`
- `.github/workflows/pr-integration-tests.yml`
- `.github/workflows/zizmor.yml`

## Proposed Minimal Additive Workflow
1. Add `readiness-ci.yml` with:
   - `pull_request` trigger scoped to `security-readiness/**` and `.github/scripts/readiness_launch_gate_check.sh`.
   - `workflow_dispatch` trigger for manual runs.
2. Security test step (readiness-focused):
   - Validate required Build Priority 11 artifacts exist.
   - Fail within step when required files are missing.
3. Non-blocking rollout mode:
   - Job remains `continue-on-error: true` for first phase.
   - Findings are uploaded as artifacts for review, not launch approval.

## Security Evidence Policy
- **Verified**: CI includes pinned actions in existing workflows.
- **Partially Confirmed**: New readiness checks can run in GitHub Actions context.
- **Unknown**: Coverage of runtime security abuse tests in CI until test commands are finalized by control owners.

## Commands Executed
1. `rg --files .github/workflows`
2. `sed -n '1,220p' .github/workflows/pr-quality-checks.yml`

## Gaps / Next Actions
- Add targeted commands for abuse-case and control tests once canonical test targets are approved.
- Move from non-blocking to blocking after two consecutive green runs with accepted evidence.
