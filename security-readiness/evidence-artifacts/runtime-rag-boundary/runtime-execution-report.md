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
