# Expected Workflow Command (Collection Only)

Date: 2026-05-12

The workflow must execute the following command in CI for collection only:

```bash
uv run --python 3.11 python -m dotenv -f .vscode/.env run -- pytest --collect-only \
  backend/tests/integration/tests/chat/test_retrieval_authorization_runtime.py \
  backend/tests/integration/tests/chat/test_citation_leakage_runtime.py \
  backend/tests/integration/tests/chat/test_prompt_injection_boundary_runtime.py
```

## Required Dependency Installation Command

```bash
uv sync --python 3.11 --no-default-groups --group backend --group dev
```

## Posture Guardrails
- Collection-only; no runtime PASS claim.
- No validator GO claim.
- Launch posture remains `NOT_ENOUGH_EVIDENCE`.
- Success classification is `COLLECTED_SKIPPED`.
