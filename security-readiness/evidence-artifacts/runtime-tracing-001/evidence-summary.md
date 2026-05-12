# runtime-tracing-001 Evidence Summary

Date: 2026-05-12

## Outcome
- Structured runtime trace JSONL generated: **Verified**.
- Retrieval authorization decision trace steps present: **Verified**.
- Tool authorization decision trace steps present (deny/fail-closed): **Verified**.
- Full production API-to-LLM E2E runtime wiring in this task scope: **Partially Confirmed**.

## Commands
1. `pytest -q backend/tests/unit/onyx/security_readiness/test_runtime_tracing_paths.py`
   - Result: failed in local environment due to missing dependency `fastapi_users`.
2. `PYTHONPATH=backend python - <<'PY' ... PY`
   - Result: generated `runtime-trace.jsonl` with 14 structured events.

## Limitations
- Unit test execution path is blocked by environment dependency gap in shared test bootstrap.
- To preserve evidence continuity, a narrow verified local runtime run was executed to generate trace artifacts.

## Artifact references
- `runtime-trace.jsonl`
- `pytest-output.txt`
- `local-run-output.txt`
- `test-command.txt`
- `timestamp.txt`
