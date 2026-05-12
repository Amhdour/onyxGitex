# Python Runtime Precheck

1. Current git commit
- `9c8d58132ad571835434cd392ba425313c6d81d3`

2. Current interpreter version
- `python --version`: `Python 3.12.13`
- `python -c "import sys; print(sys.version); print(sys.executable)"`:
  - `3.12.13 (main, May  1 2026, 05:53:44) [GCC 13.3.0]`
  - `/root/.pyenv/versions/3.12.13/bin/python`

3. Supported Python version declared by repo
- Root `pyproject.toml` declares `requires-python = ">=3.11"`.
- Root `pyproject.toml` also declares `python-version = "3.11"`.
- `backend/uv.lock` declares `requires-python = ">=3.11"`.

4. Python versions used by Dockerfiles
- `backend/Dockerfile` uses `FROM python:3.11-slim`.
- `backend/tests/integration/mock_services/mock_connector_server/Dockerfile` uses `FROM python:3.11-slim`.

5. Python version implied by pyproject/uv metadata
- Project-compatible range is Python 3.11+.
- Container/runtime baseline is Python 3.11.

6. Reason CPython 3.14 is incompatible for this evidence run
- Prior evidence output shows `onnxruntime==1.20.1` has no `cp314` wheel/sdist in this environment, which blocks `uv sync` and prevents downstream `fastapi_users` availability.

7. Recommended evidence runtime Python version
- Python `3.12` for this run.

8. Recommendation basis
- Based on repo metadata + local runtime availability:
  - Repo supports `>=3.11`.
  - Docker baseline is 3.11.
  - Local executable Python available in-session is 3.12.
  - 3.14 is explicitly blocked by `onnxruntime` artifact availability.

9. Precheck decision
- `PYTHON_VERSION_CONFIRMED`

## Selected Evidence Runtime
- selected_python_version: `3.12`
- selection_basis: `Repository supports >=3.11; local host has 3.12 executable; cp314 explicitly blocked for onnxruntime==1.20.1.`
- rejected_python_versions: `3.14`
- reason_python_3_14_rejected: `onnxruntime==1.20.1 does not provide compatible cp314 distribution in current environment.`
- expected_next_command: `uv sync --python 3.12 --group backend --group dev`
