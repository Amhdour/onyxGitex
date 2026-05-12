# Tool Authorization Runtime Integration

Date: 2026-05-12
Status: **Partially Confirmed**

## Integration point
- Integrated `ToolAuthorizationRouter` into `backend/onyx/tools/tool_runner.py` at the pre-execution choke point in `_safe_run_single_tool(...)`.
- `run_tool_calls(...)` now supports passing authorization context (`user_id`, `tool_policy`, `approval_id`) plus sinks for denied-call audit events and runtime trace records.

## Enforced behavior
1. Unknown tool in call batch is denied and logged as a deny audit event.
2. Missing user identity is denied when policy-based router is enabled.
3. Missing tool policy is denied fail-closed.
4. High-risk tools require explicit approval token.
5. Authorized low-risk tools execute.
6. Denied tool calls emit audit events.
7. Authorization decisions are appended to runtime trace.

## Scope and constraints
- No external side effects were enabled for verification tests.
- Runtime integration is constrained to the centralized chat tool-runner path.
- This does **not** claim complete agent safety coverage for all non-chat execution paths.
