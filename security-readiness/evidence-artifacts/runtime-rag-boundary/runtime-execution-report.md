# Runtime RAG Boundary Execution Report

## 1. Execution summary
Runtime RAG retrieval-boundary evidence execution was attempted via the package runner script. Execution did not reach test logic due to a backend dependency import failure.

## 2. Repository commit
`f90f2639edf5f477d1e595539956ce1c845a47db`

## 3. Command executed
`bash security-readiness/evidence-artifacts/runtime-rag-boundary/scripts/run-runtime-rag-boundary-check.sh`

Script test command:
`cd backend && python -m pytest -xv tests/integration/tests/chat/test_chat_document_set_access.py -k "rag or boundary or document_set or access"`

## 4. Environment availability
- Backend path: available
- Python: available
- Pytest: available
- Docker CLI: unavailable
- Docker Compose: unavailable

## 5. Test path discovery
Exact test path exists:
`backend/tests/integration/tests/chat/test_chat_document_set_access.py`

## 6. Test execution result
Result: `DEPENDENCY_FAILURE`

Observed blocking error:
`ModuleNotFoundError: No module named 'fastapi_users'`

## 7. Artifacts produced
- `runtime-status.txt`
- `pytest-output.txt`
- `git-commit.txt`
- `timestamp.txt`
- `test-command.txt`
- `env-manifest-redacted.txt`
- `docker-compose-ps.txt`
- `execution-precheck.md`
- `final-run-status.json` (updated)

## 8. Evidence conclusion
**BLOCKED_DEPENDENCY**

## 9. Launch-gate impact
Launch decision remains **NOT_ENOUGH_EVIDENCE / NO-GO FOR REAL CLIENT LAUNCH**.

## 10. Remaining blockers
1. Missing Python dependency `fastapi_users` in current backend test environment.
2. Backend runtime logs (`backend-logs.txt`) not yet captured.

## 11. Next action
Install backend/integration test dependencies, rerun the runtime boundary script, and capture backend logs alongside pytest output.

## Dependency Resolution Attempt
- Previous blocker: missing `fastapi_users` during pytest startup.
- Dependency manager detected: `uv` (root `pyproject.toml` with `[dependency-groups]` and `uv.lock`).
- Fix attempted: validated declaration and ran `uv sync --group backend --group dev`.
- Files changed: dependency precheck/resolution docs, status JSON, and evidence index artifacts in this package.
- Install/validation commands run:
  - `uv sync --group backend --group dev`
  - Python import validation for `fastapi_users`
- New runtime status: script rerun still ended with `DEPENDENCY_FAILURE` in `runtime-status.txt` and pytest import failure.
- Pytest collection advanced beyond previous failure: **No**.
- Current blocker: package resolution/install blocked because `onnxruntime==1.20.1` has no wheel/sdist for CPython 3.14, leaving `fastapi_users` unavailable.

Conclusion: **BLOCKED_PACKAGE_RESOLUTION**

## Python Runtime Compatibility Attempt
- Previous blocker: `BLOCKED_PACKAGE_RESOLUTION` from CPython 3.14 and `onnxruntime==1.20.1` wheel incompatibility.
- Supported Python version discovered/inferred: repo metadata supports `>=3.11`; Docker baseline is Python 3.11.
- Selected evidence runtime: Python 3.12 (available locally and compatible with onnxruntime wheel tags).
- Runtime configuration changes made: pinned `.python-version` to `3.12`, added runtime precheck and runtime-environment documentation, added interpreter guard in runner.
- Dependency sync command attempted: `uv sync --python 3.12 --group backend --group dev`.
- Dependency sync advanced past onnxruntime: **Yes** (onnxruntime cp314 mismatch no longer the immediate blocker).
- fastapi_users availability: **No** (sync aborted before completion due to numpy download tunnel error).
- Pytest collection advanced beyond previous conftest failure: **No** (`ModuleNotFoundError: fastapi_users` remains).
- Latest runtime status: `BLOCKED / PARTIAL_COLLECTION / NOT_ENOUGH_EVIDENCE`.
- Current blocker: `DEPENDENCY_FAILURE` (effective root issue: incomplete dependency install after network tunnel failure).
- Next action: restore dependency download connectivity, rerun sync under Python 3.12, then rerun runtime boundary script.

Conclusion: **BLOCKED_DEPENDENCY**

## Dependency Sync Stabilization Attempt

- Previous blocker: Python 3.12 sync advanced past onnxruntime but failed downloading numpy==2.4.1.
- numpy direct/transitive: direct dependency (also used transitively).
- Failure type: network/download tunnel error while fetching wheels.
- Sync command: `uv sync --python 3.12 --group backend --group dev`.
- Sync result: `BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD`.
- Import-check result: fastapi_users/numpy/onnxruntime/pytest = blocked (uv run unavailable because sync incomplete).
- Pytest collection beyond conftest: No.
- Latest runtime status: `BLOCKED`.
- Current blocker: `BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD`.
- Next action: restore dependency download connectivity and rerun sync + runtime script.

Conclusion: **BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD**


## GitHub Actions Evidence Workflow Added

- Reason: local/Codex execution remains blocked by network/tunnel dependency download failures.
- Workflow path: `.github/workflows/rag-boundary-runtime-evidence.yml`
- Workflow name: `RAG Boundary Runtime Evidence`
- Artifact name: `rag-boundary-runtime-evidence`
- Workflow execution scope: runs `sync-rag-evidence-env.sh` then `run-runtime-rag-boundary-check.sh`, performs artifact inspection, and uploads the full runtime-rag-boundary evidence directory.
- Current CI status: `CI_WORKFLOW_DEFINED / CI_NOT_RUN`
- Current runtime status: preserve latest known `BLOCKED / PARTIAL_COLLECTION / NOT_ENOUGH_EVIDENCE` until CI run evidence exists.
- Next required action: trigger workflow and review/download uploaded artifact package before updating launch-gate conclusions.


## GitHub Actions Runtime Evidence Run

- Workflow path: `.github/workflows/rag-boundary-runtime-evidence.yml`
- Run trigger method: attempted via `gh workflow run` from Codex environment
- Run ID: Not available
- Run URL: Not available
- Artifact name: `rag-boundary-runtime-evidence`
- Artifact download status: Not attempted (no CI run ID available)
- Dependency sync status from CI: `NOT_AVAILABLE_FROM_CI`
- Runtime status from CI: `NOT_AVAILABLE_FROM_CI`
- Pytest status from CI: `NOT_AVAILABLE_FROM_CI`
- Pytest collection/execution advanced: Unknown (no CI run evidence)
- Evidence conclusion: `CI_NOT_RUN`
- Remaining blockers: `CI_TRIGGER_OR_RUN_UNAVAILABLE`
- Launch-gate impact: remains `NOT_ENOUGH_EVIDENCE / NO-GO FOR REAL CLIENT LAUNCH`.
