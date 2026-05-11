# Tool Execution Evidence Log

Date: 2026-05-11
Status: **Initial Evidence + Gaps**

## Repository Evidence Inspected
- `backend/onyx/tools/built_in_tools.py`
- `backend/onyx/tools/tool_runner.py`
- `backend/onyx/server/features/tool/api.py`
- `backend/onyx/server/features/mcp/api.py`
- `security-readiness/00-repo-audit/onyx-tool-mcp-paths.md`

## Commands Executed
1. `rg --files -g 'AGENTS.md'`
2. `rg --files security-readiness | head -n 60`
3. `sed -n '1,220p' security-readiness/00-repo-audit/onyx-tool-mcp-paths.md`
4. `sed -n '1,260p' backend/onyx/server/features/tool/api.py`
5. `sed -n '1,260p' backend/onyx/tools/tool_runner.py`
6. `rg -n "tool_runner|built_in_tools|mcp|tool call|audit" backend/onyx -g '*test*'`

## Observed Findings
- Tool CRUD and visibility endpoints include role/ownership checks (**Verified**).
- Tool execution path supports error tracing spans and emits section-end packets (**Verified**).
- Centralized human approval gate before high-risk execution (**Unknown**).
- Explicit high-risk classification runtime enforcement hook (**Unknown**).
- Uniform audit event schema proving allow/deny policy decisions across tools (**Partially Confirmed**).

## Required Additional Evidence
- Runtime tests for unauthorized call block, missing-approval block, high-risk block, and audit emission.
- Representative logs showing policy decision records with actor and tool metadata.
