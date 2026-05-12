# Dependency Resolution

## 1) Problem
Runtime RAG boundary pytest startup failed with `ModuleNotFoundError: No module named 'fastapi_users'` during conftest import.

## 2) Root cause classification
**BLOCKED_PACKAGE_RESOLUTION** in this environment.

Observed facts supporting classification:
- `fastapi-users` is declared in `pyproject.toml` backend dependency group.
- Attempting to sync backend/dev dependencies with `uv` failed due to Python/platform wheel incompatibility for `onnxruntime==1.20.1` on CPython 3.14.
- After the attempted sync, `fastapi_users` import availability check remained `False`.

## 3) Files changed
- `security-readiness/evidence-artifacts/runtime-rag-boundary/dependency-precheck.md`
- `security-readiness/evidence-artifacts/runtime-rag-boundary/dependency-resolution.md`
- `security-readiness/evidence-artifacts/runtime-rag-boundary/dependency-install-output.txt`
- runtime evidence/status artifacts updated by rerun and reporting updates.

## 4) Commands run
- `uv sync --group backend --group dev`
- Python import validation snippet for `fastapi_users`
- `bash security-readiness/evidence-artifacts/runtime-rag-boundary/scripts/run-runtime-rag-boundary-check.sh`

## 5) Whether dependency was installed/resolved
- **No.** Dependency remained unavailable in the active runtime after attempted sync.

## 6) Whether pytest collection now proceeds
- **No.** Pytest still fails during conftest import with the same `fastapi_users` missing module error.

## 7) Remaining blockers
1. Package resolution/install cannot complete in current interpreter because `onnxruntime==1.20.1` has no wheel/sdist for CPython 3.14 in this environment.
2. `fastapi_users` remains unavailable in the active environment.
3. Runtime test cannot execute, so backend runtime logs for control behavior remain unavailable.

## 8) Launch-gate implication
Runtime RAG boundary evidence remains **NOT_ENOUGH_EVIDENCE / NO-GO FOR REAL CLIENT LAUNCH**. No runtime pass claim is supported.

## Python Runtime Follow-Up
- `fastapi_users` was not the root declaration issue; it is declared in project dependencies but unavailable because environment sync remained incomplete.
- CPython 3.14 blocked prior `uv sync` because `onnxruntime==1.20.1` lacks a compatible cp314 distribution in this environment.
- Selected Python version: `3.12`.
- `uv sync` retried with selected version: **Yes** (`uv sync --python 3.12 --group backend --group dev`).
- Result: resolver advanced past onnxruntime mismatch, but install failed on `numpy==2.4.1` download (`tunnel error: unsuccessful`).
- Remaining blocker: dependency installation incomplete; `fastapi_users` import remains unavailable; pytest still blocked during conftest import.
