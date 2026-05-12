# Main llm_loop Tool Runtime Wiring Review

## Scope
- Wired main `backend/onyx/chat/llm_loop.py` tool execution path to call `run_tool_calls_with_runtime_context(...)` when runtime enforcement is enabled.
- Kept default behavior explicit and unchanged via `tool_runtime_enforcement_mode="DISABLED"`.
- Did not wire `research_agent.py`.
- Did not modify MCP tool internals.

## Fail-Closed Behavior
- `RAG_ONLY`: if tool calls are present, adapter guard raises fail-closed and blocks tool execution.
- `RAG_PLUS_TOOLS`: adapter guard requires `authorization_router`, `user_id`, and `tool_policy`; missing context fails closed.

## Context Passthrough
- Forwarded: `authorization_router`, `user_id`, `tool_policy`, `approval_id`, `audit_events`, `runtime_trace`.

## Status Snapshot
- `main_llm_loop_runtime_adjacent_status`: PASS (based on focused unit tests).
- `full_runtime_status`: NOT_PASS.
- `research_agent_status`: NOT_PASS.
- `mcp_status`: NOT_PASS / MISSING.
- `RAG_PLUS_TOOLS`: NOT_READY.
- `launch_gate`: NOT_ENOUGH_EVIDENCE.
