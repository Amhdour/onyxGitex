# Human Confirmation Policy

Date: 2026-05-11
Status: **Proposed Control (Not Fully Verified in Runtime Code)**

## Policy
A tool call MUST require explicit human confirmation when any of the following are true:
1. Tool is classified High-Risk.
2. Tool call can execute code, mutate external systems, or access external network resources.
3. Tool call includes sensitive scopes (tenant-wide, admin, credentials, document export).

## Required Decision Fields
- request_id
- user_id
- assistant_id
- tool_name
- risk_level
- requested_inputs_hash
- approval_decision (`approved` / `denied`)
- approver_id
- decision_timestamp
- expiration_timestamp

## Enforcement Requirements
- Fail closed when approval record is absent, expired, or mismatched to input hash.
- Denied decision must block execution and emit audit event.
- Approval must be single-use unless explicitly marked reusable with TTL.

## Current Verification State
- API-layer authorization checks are present for tool management and listing endpoints.
- Runtime per-call human approval check in tool execution path is **Unknown**.

## Evidence Needed
- Unit/integration tests proving:
  - missing approval blocks high-risk tool,
  - mismatched approval hash blocks execution,
  - approval decision audit event emitted.
