# MCP Hardening Test Plan

Date (UTC): 2026-05-12
MCP Status: **Present**

## Objective
Validate identity enforcement, tool authorization behavior, fail-closed defaults, and audit evidence for MCP tool execution.

## Existing Coverage Identified
- `backend/tests/integration/tests/mcp/test_mcp_server_auth.py`
  - missing token denied
  - invalid token denied
  - valid token accepted
- `backend/tests/integration/tests/mcp/test_mcp_server_search.py`
  - end-to-end search flow
  - ACL behavior for document retrieval

## Required Hardening Tests (Target)
1. Unauthenticated MCP request denied.  
   - Status: **Covered** (existing integration test).
2. Unknown tool denied.  
   - Status: **Partially Covered** (no dedicated assertion found in reviewed suite).
3. High-risk MCP tool requires approval.  
   - Status: **Unknown** (policy/approval mechanism not confirmed in reviewed MCP code).
4. Prompt-injected tool call denied.  
   - Status: **Unknown** (no explicit prompt-injection denial gate found in reviewed MCP code).
5. Audit event emitted on tool decision.  
   - Status: **Partially Confirmed** (logs present; structured audit event contract not confirmed).
6. Missing identity fails closed.  
   - Status: **Covered/Partially Covered** (`require_access_token()` + auth integration tests).

## Feasibility of Adding Tests Now
- Tests can be added for items (2) and parts of (6) without changing product behavior.
- Items (3), (4), (5) depend on controls not yet clearly implemented in MCP path; adding strict pass/fail tests now may create false expectations.

## Proposed Next Test Additions
1. Integration test: call unknown MCP tool and assert protocol error/denial.
2. Unit test: `require_access_token()` raises when token missing.
3. (After control implementation) policy tests for:
   - high-risk tool approval requirement
   - prompt-injection deny rules
   - structured audit event emission

## Execution Notes
- Run narrow MCP integration tests first.
- Record exact command and raw output under evidence artifact folder.
