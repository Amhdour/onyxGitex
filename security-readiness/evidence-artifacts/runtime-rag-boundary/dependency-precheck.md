# Dependency Precheck

## Current git commit
- `76d3b85c23c470b6f5d5ec3884eb723ab937bf23`

## Dependency manager detected
- `uv` project detected via root `pyproject.toml` (`[dependency-groups]`) and root `uv.lock`.
- Backend compiled requirements files also present under `backend/requirements/`.

## Files inspected
- Dependency/config discovery command output (`find . -maxdepth 4 ...`) captured these key files:
  - `pyproject.toml`
  - `uv.lock`
  - `backend/uv.lock`
  - `backend/requirements/default.txt`
  - `backend/requirements/dev.txt`
  - `backend/requirements/README.md`
  - Docker and compose files listed in command output.
- Search outputs reviewed:
  - `rg -n "fastapi_users|fastapi-users|FastAPIUsers|fastapi users" .`
  - `rg -n "pytest|dev-dependencies|dependency-groups|optional-dependencies|extras|integration|fastapi" ...`

## fastapi_users import and declaration findings
- `fastapi_users` **is imported** in backend code (for example `backend/onyx/auth/schemas.py:5`).
- `fastapi-users==15.0.4` **is declared** in `pyproject.toml` under `[dependency-groups].backend`.
- `fastapi-users==15.0.4` also appears in `backend/requirements/default.txt`.
- Therefore, blocker classification based on observed evidence: **MISSING_INSTALL_STEP** (dependency declared in project files but unavailable in current Python runtime).

## Lock file presence
- `uv.lock` exists at repository root.
- `backend/uv.lock` exists.
- This precheck did not parse lock internals line-by-line; lock-file presence is verified from file discovery output.

## Pytest startup behavior
- Previous `pytest-output.txt` shows startup import failure before test collection completed.

## Blocker classification
- **MISSING_INSTALL_STEP**

## Previous Pytest Failure Analysis
- Exact exception type: `ModuleNotFoundError`
- Exact missing module: `fastapi_users`
- Importing file in traceback: `onyx/auth/schemas.py:5` (`from fastapi_users import schemas`)
- First project file in stack trace: `tests/conftest.py:7` (loaded via `backend/tests/conftest.py`)
- Failure phase: **import-time during conftest loading** (before test execution)

Exact traceback excerpt from prior artifact:

`ImportError while loading conftest '/workspace/onyxGitex/backend/tests/conftest.py'.`

`E   ModuleNotFoundError: No module named 'fastapi_users'`
