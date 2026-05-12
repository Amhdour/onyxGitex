# Artifact Output Map

## Runner artifacts
- Run root: `security-readiness/evidence-artifacts/tier4-runtime-runner/runs/<UTC_TIMESTAMP>/`
- Per-command logs:
  - `runner.log`
  - `<check_or_suite>.stdout.txt`
  - `<check_or_suite>.stderr.txt`
- Summary: `summary.md`
- Path checks: `path-checks.txt`

## Launch-blocker artifacts expected from Tier 4 suite success
- `security-readiness/evidence-artifacts/test-results/retrieval-authorization-tests.json`
- `security-readiness/evidence-artifacts/test-results/citation-leakage-tests.json`
- `security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json`

## Follow-on validation artifacts (outside this runner)
- `security-readiness/evidence-artifacts/risk/open-risk-summary.json`
- `security-readiness/evidence-artifacts/evidence-pack/evidence-pack-status.json`
