# llm_loop Runtime-Adjacent Tool Wiring Plan (RAG_PLUS_TOOLS)

Date: 2026-05-12

## Objective
Provide a narrow, dependency-light proof that the llm loop tool call contract can fail closed and propagate authorization context before `run_tool_calls` execution.

## Approach
1. Add `backend/onyx/security_readiness/tool_runtime_wiring_adapter.py` as a runtime-adjacent adapter.
2. Adapter enforces `enforce_tool_runtime_context(...)` before invoking injected `run_tool_calls_fn`.
3. Keep production wiring unchanged; use dependency-light tests with mocked `run_tool_calls`.

## Contract Covered
- RAG_ONLY + tool calls => deny before tool execution.
- RAG_PLUS_TOOLS + missing router => deny.
- RAG_PLUS_TOOLS + missing user_id => deny.
- RAG_PLUS_TOOLS + missing tool_policy => deny.
- RAG_PLUS_TOOLS + complete context => pass `authorization_router`, `user_id`, `tool_policy`, `approval_id` into runner.
- High-risk tool + no approval => deny via mocked router/runner path.
- Deny path emits audit event.
- Deny path emits runtime trace event.

## Status Boundaries
- runtime_adjacent_status: PASS (if tests pass)
- full_runtime_status: NOT_PASS
- RAG_PLUS_TOOLS: NOT_READY
- launch_gate: NOT_ENOUGH_EVIDENCE
