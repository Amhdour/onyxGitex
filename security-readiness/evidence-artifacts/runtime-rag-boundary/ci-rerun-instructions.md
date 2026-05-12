# CI Rerun Instructions — RAG Boundary Runtime Evidence

## 1) Purpose
Run the RAG boundary runtime evidence flow in GitHub Actions to collect reproducible, downloadable artifacts when local/Codex dependency downloads are blocked.

## 2) Workflow
- Name: `RAG Boundary Runtime Evidence`
- Path: `.github/workflows/rag-boundary-runtime-evidence.yml`

## 3) Manual run steps (GitHub UI)
1. Open repository **Actions** tab.
2. Select **RAG Boundary Runtime Evidence**.
3. Click **Run workflow** (`workflow_dispatch`).

## 4) How to inspect result
1. Open workflow run logs.
2. Download artifact: `rag-boundary-runtime-evidence`.
3. Inspect:
   - `final-run-status.json`
   - `dependency-sync-status.txt`
   - `runtime-status.txt`
   - `pytest-output.txt`

## 5) Expected possible statuses
- `PASS`
- `FAIL`
- `BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD`
- `BLOCKED_PACKAGE_RESOLUTION`
- `BLOCKED_DEPENDENCY`
- `UNSUPPORTED_PYTHON_VERSION`
- `NOT_ENOUGH_EVIDENCE`

## 6) How to update status after CI run
- Update `final-run-status.json` CI fields (`ci_run_status`, `ci_run_url`) with actual run metadata.
- Update `runtime-execution-report.md`, `evidence-manifest.md`, and launch-gate index with observed evidence.
- Keep `runtime_verified=false` unless pytest execution and pass are confirmed.

## 7) What can be claimed
- Workflow execution details and artifact availability can be claimed.
- Observed runtime status can be claimed exactly as recorded in artifacts.

## 8) What cannot be claimed
- Workflow definition alone cannot prove RAG boundary enforcement.
- Artifact upload alone cannot prove control effectiveness.
- Full launch GO cannot be claimed without verified critical controls.

## 9) Screenshot checklist
- [ ] Workflow run page
- [ ] Dependency sync step
- [ ] Runtime evidence step
- [ ] Artifact upload step
- [ ] `final-run-status.json` inside artifact

## 10) Launch-gate rule
Full GO remains prohibited unless all critical controls are runtime-verified with sufficient evidence.


## Latest CI Run Review

- Date (UTC): 2026-05-12
- Run ID/URL: Not available
- Artifact status: `CI_NOT_RUN`
- Result classification: `CI_TRIGGER_UNAVAILABLE` leading to `CI_NOT_RUN`
- Next action: Trigger `RAG Boundary Runtime Evidence` from GitHub UI or a gh-authenticated shell, then capture run metadata/logs/artifact outputs.
