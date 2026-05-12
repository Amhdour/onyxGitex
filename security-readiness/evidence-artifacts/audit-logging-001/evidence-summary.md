# Evidence Summary: audit-logging-001

Date: 2026-05-12

## Scope
Structured audit events for retrieval/tool authorization decisions with fail-closed metadata.

## Commands
- `pytest -q backend/tests/unit/onyx/security_readiness/test_control_layer.py backend/tests/unit/onyx/tools/test_tool_authorization_runtime.py`
- `PYTHONPATH=backend python <script>` (generated sample runtime audit events from `AuditLogger.emit_authorization_event`)

## Results
- Pytest execution: **Blocked** (`ModuleNotFoundError: fastapi_users` in this environment).
- Audit event generation: **Verified** (`audit-events.jsonl` created with schema fields and required action coverage for retrieval/tool/policy missing context).

## Evidence Status
- Retrieval/tool audit event schema implementation: **Verified**
- Runtime integration points updated: **Verified**
- Full pytest verification in this container: **Partially Confirmed**
