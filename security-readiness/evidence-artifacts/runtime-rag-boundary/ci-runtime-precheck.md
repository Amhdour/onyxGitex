# CI Runtime Precheck — RAG Boundary Evidence

- Date (UTC): 2026-05-12
- Current git commit: `1d1f795c8e88fd899e5582f168021856e4a3dc18`

## 1) Existing workflow files
- `.github/workflows/deployment.yml`
- `.github/workflows/docker-tag-beta.yml`
- `.github/workflows/docker-tag-latest.yml`
- `.github/workflows/evidence-artifact-validation.yml`
- `.github/workflows/helm-chart-releases.yml`
- `.github/workflows/merge-group.yml`
- `.github/workflows/nightly-close-stale-issues.yml`
- `.github/workflows/nightly-external-dependency-unit-tests.yml`
- `.github/workflows/nightly-llm-provider-chat.yml`
- `.github/workflows/post-merge-beta-cherry-pick.yml`
- `.github/workflows/pr-database-tests.yml`
- `.github/workflows/pr-desktop-build.yml`
- `.github/workflows/pr-external-dependency-unit-tests.yml`
- `.github/workflows/pr-golang-tests.yml`
- `.github/workflows/pr-helm-chart-testing.yml`
- `.github/workflows/pr-integration-tests.yml`
- `.github/workflows/pr-jest-tests.yml`
- `.github/workflows/pr-labeler.yml`
- `.github/workflows/pr-linear-check.yml`
- `.github/workflows/pr-playwright-tests.yml`
- `.github/workflows/pr-python-checks.yml`
- `.github/workflows/pr-python-connector-tests.yml`
- `.github/workflows/pr-python-model-tests.yml`
- `.github/workflows/pr-python-tests.yml`
- `.github/workflows/pr-quality-checks.yml`
- `.github/workflows/preview.yml`
- `.github/workflows/readiness-ci.yml`
- `.github/workflows/release-cli.yml`
- `.github/workflows/release-devcontainer.yml`
- `.github/workflows/release-devtools.yml`
- `.github/workflows/release-opal.yml`
- `.github/workflows/reusable-nightly-llm-provider-chat.yml`
- `.github/workflows/sandbox-deployment.yml`
- `.github/workflows/security-readiness.yml`
- `.github/workflows/storybook-deploy.yml`
- `.github/workflows/sync_foss.yml`
- `.github/workflows/tag-nightly.yml`
- `.github/workflows/tier4-runtime-collection.yml`
- `.github/workflows/zizmor.yml`

## 2) Existing evidence scripts
- `security-readiness/evidence-artifacts/runtime-rag-boundary/scripts/sync-rag-evidence-env.sh`
- `security-readiness/evidence-artifacts/runtime-rag-boundary/scripts/run-runtime-rag-boundary-check.sh`

## 3) Current local/Codex blocker
- `BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD` from repeated wheel fetch tunnel errors in dependency sync.

## 4) Reason for GitHub Actions rerun
- GitHub-hosted CI may provide a cleaner dependency download path than local/Codex tunnel conditions.
- CI provides an auditable and reproducible artifact upload channel for evidence review.

## 5) What CI will prove
- The exact sync + runtime scripts can execute under GitHub Actions with Python 3.12.
- The evidence package can be generated and uploaded as downloadable artifacts.
- Actual status (`PASS`, `FAIL`, or `BLOCKED`) can be captured with logs.

## 6) What CI will not prove
- Workflow definition alone does not prove control effectiveness.
- Artifact upload alone does not prove RAG boundary enforcement.
- Runtime enforcement claim requires pytest execution and pass results.
- Launch GO decision cannot be claimed from workflow creation alone.

## 7) Precheck decision
- `READY_FOR_CI_EVIDENCE_WORKFLOW`
