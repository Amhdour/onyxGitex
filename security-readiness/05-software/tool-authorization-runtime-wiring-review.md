# ToolAuthorizationRouter Runtime Wiring Review (RAG_PLUS_TOOLS)

Date: 2026-05-12  
Mode under review: **RAG_PLUS_TOOLS**  
Current launch decision: **NOT_ENOUGH_EVIDENCE** (unchanged)  
Readiness posture for tools: **NOT_READY** (unchanged)

## Scope

Reviewed runtime tool execution wiring and adjacent MCP/tool paths in:

- `backend/onyx/chat/llm_loop.py`
- `backend/onyx/tools/tool_runner.py`
- `backend/onyx/tools/`
- `backend/onyx/mcp_server/`
- tool execution tests under `backend/tests/unit/onyx/tools/` and `backend/tests/unit/onyx/security_readiness/`

No runtime code changes were made.

## Executive finding

`ToolAuthorizationRouter` exists and is enforceable at the `tool_runner` layer, but the primary chat runtime path (`llm_loop.py`) currently calls `run_tool_calls(...)` without passing `authorization_router`, `user_id`, `tool_policy`, or `approval_id`. This leaves authorization **not enforced by default** on the main chat execution path for RAG+tools.

## Tool execution path inventory and enforcement status

### Path A — Main chat loop (primary user-facing path)

- **File path**: `backend/onyx/chat/llm_loop.py` + `backend/onyx/tools/tool_runner.py`
- **Function/class**:
  - Request path: chat loop function invoking `run_tool_calls(...)`
  - Execution path: `run_tool_calls(...)` -> `_safe_run_single_tool(...)`
- **Where tool call is requested**:
  - LLM step output is parsed to `llm_step_result.tool_calls`; then `tool_calls = llm_step_result.tool_calls or []`.
- **Where tool execution happens**:
  - `run_tool_calls(...)` dispatches parallel calls and executes each tool through `_safe_run_single_tool(...)`, which calls `tool.run(...)`.
- **User identity availability**:
  - In this call site, user identity is present earlier in loop context (passed to LLM step), but `run_tool_calls(...)` is invoked without `user_id`, so authorization layer does not receive identity.
- **Tool policy availability**:
  - Not provided at this call site (`tool_policy` omitted).
- **Approval context availability**:
  - Not provided at this call site (`approval_id` omitted).
- **Audit/trace behavior**:
  - `tool_runner` can emit deny audit events/runtime trace **if** authorization path is active and optional lists are supplied; main path currently does not supply router/context.
- **Is ToolAuthorizationRouter currently enforced?**
  - **No** on this default path (router parameter not passed).
- **Required code change**:
  - Wire `ToolAuthorizationRouter` and required context into `llm_loop.py` call to `run_tool_calls(...)`:
    - instantiate/inject router,
    - pass `user_id` from authenticated principal,
    - pass resolved `tool_policy` for this request/tenant,
    - pass `approval_id` for high-risk actions,
    - pass mutable `audit_events` and `runtime_trace` sinks.
  - Add fail-closed behavior if identity/policy context cannot be built for RAG_PLUS_TOOLS mode.
- **Test needed**:
  1. Unit/integration test for llm loop path asserting tool execution is denied when `user_id` missing.
  2. Test asserting high-risk tool call denied without `approval_id`.
  3. Test asserting audit + runtime trace are populated on deny/allow.
- **Risk severity**: **High** (authorization bypass on primary tool execution route).

---

### Path B — `tool_runner` authorization gate (implementation layer)

- **File path**: `backend/onyx/tools/tool_runner.py`, `backend/onyx/tools/tool_authorization_router.py`
- **Function/class**:
  - Gate: `ToolAuthorizationRouter.authorize(...)`
  - Enforcement point: `_safe_run_single_tool(...)` before `tool.run(...)`
- **Where tool call is requested**:
  - `run_tool_calls(...)` composes runnable tool calls from LLM-provided calls.
- **Where tool execution happens**:
  - `_safe_run_single_tool(...)` performs authorization check, then either denies or executes `tool.run(...)`.
- **User identity availability**:
  - Available only if caller passes `user_id`.
- **Tool policy availability**:
  - Available only if caller passes `tool_policy`; missing policy leads to deny in router.
- **Approval context availability**:
  - Available only if caller passes `approval_id`; required for high-risk tools per router policy.
- **Audit/trace behavior**:
  - On deny, emits `tool.deny` audit payload and appends runtime trace authorization event when lists are provided.
  - Unknown tool calls are denied and can also emit audit/trace entries in `run_tool_calls(...)` filtering phase.
- **Is ToolAuthorizationRouter currently enforced?**
  - **Conditionally yes** (only when caller supplies `authorization_router`).
- **Required code change**:
  - Make authorization non-optional for RAG_PLUS_TOOLS path (policy decision required before execution).
  - Optionally enforce a runtime assertion/guard in `run_tool_calls(...)` for RAG_PLUS_TOOLS mode requiring router+context.
- **Test needed**:
  1. Negative test: RAG_PLUS_TOOLS invocation without router/context fails closed.
  2. Positive test: low-risk allowed tool executes with full context.
- **Risk severity**: **Medium-High** (gate exists but is bypassable by call-site omission).

---

### Path C — Research agent / nested tool loop path

- **File path**: `backend/onyx/tools/fake_tools/research_agent.py` + `backend/onyx/tools/tool_runner.py`
- **Function/class**:
  - Request path: research agent loop calling `run_tool_calls(...)`
  - Execution path: `run_tool_calls(...)` -> `_safe_run_single_tool(...)`
- **Where tool call is requested**:
  - Agent-produced `tool_calls` in iterative research loop.
- **Where tool execution happens**:
  - Same `tool_runner` execution path as primary loop.
- **User identity availability**:
  - Not passed at this call site.
- **Tool policy availability**:
  - Not passed.
- **Approval context availability**:
  - Not passed.
- **Audit/trace behavior**:
  - Not wired at call site for authorization events.
- **Is ToolAuthorizationRouter currently enforced?**
  - **No** on this call path as written.
- **Required code change**:
  - Mirror main-path wiring: pass router, user identity, policy, approval context, audit trace sinks.
- **Test needed**:
  1. Research-agent tool deny test without policy/identity.
  2. Research-agent high-risk approval enforcement test.
- **Risk severity**: **High** (secondary execution path can bypass gate).

---

### Path D — MCP tool execution internals (post-dispatch)

- **File path**: `backend/onyx/tools/tool_implementations/mcp/mcp_tool.py`
- **Function/class**: `MCPTool.run(...)`
- **Where tool call is requested**:
  - Upstream tool dispatch selects MCP tool and calls its `run(...)` via tool runner.
- **Where tool execution happens**:
  - `MCPTool.run(...)` builds headers/auth and calls `call_mcp_tool(...)`.
- **User identity availability**:
  - MCP tool object can hold `user_id`, user email, oauth token.
- **Tool policy availability**:
  - No local authorization policy decision in `MCPTool.run(...)`; relies on outer runtime gate.
- **Approval context availability**:
  - Not present in MCP tool runtime method.
- **Audit/trace behavior**:
  - Logs success/failure and emits tool delta packets; no explicit ToolAuthorizationRouter check inside MCP tool.
- **Is ToolAuthorizationRouter currently enforced?**
  - **Only if enforced upstream** in `tool_runner`; not enforced locally here.
- **Required code change**:
  - No direct change required if centralized runner enforcement becomes mandatory.
  - Optional defense-in-depth: annotate MCP executions with explicit authorization decision metadata in trace payload.
- **Test needed**:
  1. End-to-end test proving MCP tool is denied when router denies in RAG_PLUS_TOOLS path.
  2. Test for trace continuity: authorization decision precedes MCP call attempt.
- **Risk severity**: **Medium-High** (sensitive remote capability depends on upstream gate wiring).

## Test evidence reviewed

- `backend/tests/unit/onyx/tools/test_tool_authorization_runtime.py`
  - Confirms authorization behavior in `run_tool_calls(...)` when router/context are provided.
  - Confirms deny on missing identity and high-risk approval requirement behavior.
- `backend/tests/unit/onyx/security_readiness/test_runtime_tracing_paths.py`
  - Confirms modeled runtime tracing sequence includes tool authorization checkpoints.

## Gaps and required verification work

1. Missing llm loop integration test that proves primary runtime enforces ToolAuthorizationRouter in RAG_PLUS_TOOLS mode.
2. Missing research-agent path test for enforced authorization.
3. Missing MCP E2E test proving deny-before-dispatch for unauthorized calls.
4. Missing explicit mode-gated fail-closed assertion that RAG_PLUS_TOOLS cannot run tools without policy and identity context.

## Readiness statement (phase status)

- **RAG_ONLY**: out of scope for this review.
- **RAG_PLUS_TOOLS**: **NOT_READY**.
- **Launch gate**: **NOT_ENOUGH_EVIDENCE**.

Rationale: runtime gate exists but is not yet consistently wired/enforced in the primary and secondary tool execution call sites.

## 2026-05-12 Addendum — MCP deny-before-dispatch runtime-adjacent evidence

New runtime-adjacent evidence artifacts were added under:

- `security-readiness/evidence-artifacts/mcp-deny-before-dispatch/`
- `security-readiness/evidence-artifacts/test-results/mcp-deny-before-dispatch-tests.json`

Outcome of this evidence bundle:

- `mcp_deny_before_dispatch_adjacent_status`: **PASS**
- `full_mcp_runtime_status`: **NOT_PASS** (unchanged)
- `RAG_PLUS_TOOLS`: **NOT_READY** (unchanged)
- `launch_gate`: **NOT_ENOUGH_EVIDENCE** (unchanged)

This addendum remains runtime-adjacent and does not claim complete production MCP hardening.
