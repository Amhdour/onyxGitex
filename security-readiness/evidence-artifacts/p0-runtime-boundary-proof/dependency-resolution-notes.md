# Dependency Resolution Notes

- Dependencies are defined in `pyproject.toml`, `uv.lock`, and `backend/requirements/default.txt`.
- `fastapi-users` is listed in those files.
- The observed blocker is runtime environment mismatch where `fastapi_users` import is unavailable during pytest collection.
- Backend tests currently load heavy `backend/tests/conftest.py` dependencies.
- Candidate command, not executed in this milestone: `uv sync` (from lockfile-managed environment).
- Candidate command, not executed in this milestone: `pip install fastapi-users==15.0.4`.
- Recommended next action: align local test environment with repository lock/dependency workflow, then rerun P0 proof.
