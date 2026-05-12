# MCP Deny-Before-Dispatch Hardening Review (Runtime-Adjacent)

Date: 2026-05-12 (UTC)

## Objective

Demonstrate that MCP tool calls can be denied before any remote MCP dispatch attempt in runtime-adjacent evidence.

## Code paths inspected

- `backend/onyx/tools/tool_implementations/mcp/mcp_tool.py`
- `backend/onyx/mcp_server/`
- `backend/onyx/tools/tool_runner.py`
- `backend/onyx/tools/tool_authorization_router.py`
- `backend/onyx/security_readiness/tool_runtime_wiring_adapter.py`
- `security-readiness/05-software/tool-authorization-runtime-wiring-review.md`

## Runtime-adjacent evidence approach

This evidence package uses a deterministic runtime-adjacent test harness that mirrors the deny branch semantics in `_safe_run_single_tool(...)` and calls the real `ToolAuthorizationRouter.authorize(...)` implementation.

The harness proves ordering constraints:

1. Authorization decision happens first.
2. Deny decisions immediately return an authorization-denied response.
3. MCP tool `run()` is not called on deny.
4. Therefore, downstream MCP remote dispatch cannot occur.

## Test matrix and outcomes

1. Unauthorized MCP tool call denied before `run()` call: **PASS**
2. Missing `user_id` fails closed before dispatch: **PASS**
3. Missing `tool_policy` fails closed before dispatch: **PASS**
4. High-risk MCP without approval denied before dispatch: **PASS**
5. Allowed MCP with policy + approval reaches mocked runner: **PASS**
6. Deny event emits audit record: **PASS**
7. Deny event emits runtime trace: **PASS**
8. No external MCP server contacted: **PASS**

## Status updates

- `mcp_deny_before_dispatch_adjacent_status`: **PASS**
- `full_mcp_runtime_status`: **NOT_PASS** (unchanged)
- `RAG_PLUS_TOOLS`: **NOT_READY** (unchanged)
- `launch_gate`: **NOT_ENOUGH_EVIDENCE** (unchanged)

## Constraints and non-claims

- No real MCP server was called.
- This is runtime-adjacent evidence, not production end-to-end proof.
- This review does **not** claim full MCP hardening completion.
