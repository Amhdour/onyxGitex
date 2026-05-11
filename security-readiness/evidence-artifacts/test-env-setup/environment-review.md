# Backend Test Environment Review

Date (UTC): See `timestamp.txt`.

## Files inspected
- `pyproject.toml`
- `uv.lock`
- `backend/uv.lock`
- `backend/requirements/README.md`
- `backend/requirements/default.txt`, `dev.txt`, `ee.txt`, `model_server.txt`, `combined.txt`
- `backend/tests/README.md`
- `backend/Dockerfile`

## Key observations
- Repository dependency source of truth is `pyproject.toml` with `uv.lock` as unified lock.
- Backend dependency install flow is documented as `uv sync` (dev/default groups) or `uv sync --no-default-groups --group backend` for backend-only.
- Backend Docker image is pinned to Python 3.11 (`python:3.11-slim`), aligning with `requires-python = ">=3.11"` and many pinned wheel constraints.
- Local execution environment currently reports Python 3.14.4 and `uv 0.7.22`.

## Environment compatibility conclusion
- **Partially Confirmed**: Backend test setup procedure is documented and clear.
- **Verified blocker**: Current local Python (3.14) is incompatible with at least one pinned dependency (`onnxruntime==1.20.1`) required by lock resolution in this repo.
