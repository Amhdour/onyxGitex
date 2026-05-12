# Tier 4 Runtime Dependency Root Cause

Date (UTC): 2026-05-12
Status: **BLOCKED**
Launch gate: **NOT_ENOUGH_EVIDENCE**

## Observed failure
The runtime collection attempt previously failed before test collection with missing backend auth dependencies (`fastapi_users` / `fastapi_users_db_sqlalchemy`).

## Dependency source of truth
From repository dependency configuration:

- `fastapi-users==15.0.4` is declared in root `pyproject.toml` under `[dependency-groups].backend`.
- `fastapi-users-db-sqlalchemy==7.0.0` is declared in root `pyproject.toml` under `[dependency-groups].backend`.

This means these modules are provided by the **backend dependency group**, not by base/system Python packages.

## Additional environment blocker found during repair attempt
The environment default interpreter is Python 3.14. `uv sync --no-default-groups --group backend --group dev` failed because `onnxruntime==1.20.1` has no cp314 wheel in the lock target set.

A second repo-supported attempt using `uv sync --python 3.11 --no-default-groups --group backend --group dev` then failed due network download failure for the uv-managed CPython 3.11 runtime artifact.

## Conclusion
- Correct dependency group for `fastapi_users*`: **backend**.
- Runtime dependency repair is still **Partially Confirmed** (command identified and attempted) but not fully installed in this host due interpreter/platform + runtime-download constraints.
