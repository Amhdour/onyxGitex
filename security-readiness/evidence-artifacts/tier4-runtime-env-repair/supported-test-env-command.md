# Supported Backend Integration Test Environment Command

Date (UTC): 2026-05-12
Launch gate: **NOT_ENOUGH_EVIDENCE**

## Repo-supported dependency setup
From `backend/requirements/README.md`, install backend + dev groups with uv:

```bash
uv sync --python 3.11 --no-default-groups --group backend --group dev
```

For this repository's integration tests, backend dependencies are required because integration conftest imports app modules that depend on `fastapi-users` and `fastapi-users-db-sqlalchemy`.

## Repo-supported dependency import verification
Before pytest collection, verify backend dependency imports in the same Python 3.11 runtime:

```bash
uv run --python 3.11 python -c "import fastapi_users; import fastapi_users_db_sqlalchemy; print('fastapi-users imports ok')"
```

## Repo-supported integration invocation
From `backend/tests/README.md`:

```bash
python -m dotenv -f .vscode/.env run -- pytest backend/tests/integration
```

For Tier 4 collection-only scope, this same pattern is narrowed to explicit files plus `--collect-only` and run via uv under Python 3.11.
