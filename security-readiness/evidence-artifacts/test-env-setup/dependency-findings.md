# Dependency Findings (fastapi_users focus)

## Is `fastapi_users` missing?
- **No**. `fastapi-users==15.0.4` is explicitly listed in `pyproject.toml` under `[dependency-groups].backend`.

## Is it optional / extra / enterprise-only?
- It is in the **backend group**, not the `ee` group, so it is part of standard backend deps when backend group is installed.

## Imported indirectly or directly?
- **Directly imported** in backend auth modules, e.g., `backend/onyx/auth/users.py` and related auth/db entry points.

## Why previous `ModuleNotFoundError: fastapi_users` can happen
- If backend dependencies were not installed (e.g., running plain `pytest` without `uv sync` / correct environment), import will fail.
- In this session, test execution failed earlier at dependency resolution due to Python 3.14/onnxruntime wheel mismatch, preventing full environment sync.

## Correct dependency installation command
- For local backend + dev test workflow in this repository:
  - `uv sync`
- Narrow backend-only dependency install:
  - `uv sync --no-default-groups --group backend`

## Confidence labels
- `fastapi-users` presence in repository config: **Verified**
- Root cause of historical `fastapi_users` error in this session: **Partially Confirmed** (likely unsynced env previously; current hard blocker is Python version incompatibility)
