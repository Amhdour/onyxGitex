# ToolAuthorizationRouter Dependency-Light Review (RAG_PLUS_TOOLS)

Date (UTC): 2026-05-12T14:59:20Z

## Scope

Reviewed and produced dependency-light evidence for ToolAuthorizationRouter behavior using:

- `backend/onyx/tools/tool_authorization_router.py`
- `backend/onyx/tools/tool_runner.py`
- `backend/tests/unit/onyx/tools/test_tool_authorization_runtime.py`
- `security-readiness/05-software/tool-authorization-runtime-wiring-review.md`

## Findings

- `ToolAuthorizationRouter` denies unknown/missing-context cases and allows approved policy cases at router decision level.
- `tool_runner` contains conditional authorization/audit/trace behavior, but wiring into main runtime path remains incomplete per existing wiring review.
- Dependency-light test artifact validates fail-closed decision behavior and deny telemetry modeling without claiming full runtime enforcement.

## Test Matrix Results

1. Unknown tool is denied: **Verified**
2. Missing user identity is denied: **Verified**
3. Missing tool policy is denied: **Verified**
4. High-risk tool without approval is denied: **Verified**
5. High-risk tool with approval is allowed: **Verified**
6. Low-risk allowed tool is allowed: **Verified**
7. Denied tool call emits audit event: **Verified** (dependency-light helper trace)
8. Denied tool call emits runtime trace: **Verified** (dependency-light helper trace)
9. RAG_PLUS_TOOLS mode without router/context fails closed in helper logic: **Verified**

## Status

- `dependency_light_status`: **PASS**
- `runtime_wiring_status`: **NOT_PASS**
- `RAG_PLUS_TOOLS`: **NOT_READY**
- `launch_gate`: **NOT_ENOUGH_EVIDENCE**

## Constraints

- This evidence set intentionally avoids heavy runtime dependencies and does not assert `llm_loop.py` enforcement.
- No runtime wiring changes were made.
