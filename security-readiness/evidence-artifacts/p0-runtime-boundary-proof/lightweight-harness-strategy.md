# Lightweight Harness Strategy

Current problem: lightweight harness tests under backend paths trigger heavy backend conftest loading.

Recommended structure:
- `tests/security_readiness/` for lightweight harness tests (LOCAL_HARNESS).
- `backend/tests/integration/` for real runtime/integration tests (LOCAL_RUNTIME or CI_RUNTIME).

Recommended commands:
- `PYTHONPATH=backend python3 -m pytest -q tests/security_readiness/`
- backend integration command only after full backend dependencies are installed.
