# Runtime Execution Report — LangGraph Agent Lab

## 1. Purpose
Collect executable local evidence for autonomous-agent tool authorization controls, approval gating, fail-closed behavior, and audit event generation using a deterministic LangGraph-style mock runtime harness.

## 2. Execution summary
- Harness script executed locally and completed all configured scenarios.
- All expected decision outcomes matched actual decisions (7/7).
- Runtime artifacts were generated under `agent-security-readiness/23-langgraph-agent-lab/runtime-artifacts/`.

## 3. Runtime type
LangGraph-style deterministic mock harness (local deterministic graph; no `langgraph` package required in this run).

## 4. Scenarios executed
1. LG-ALLOW-001 authorized_read_document
2. LG-DENY-001 unauthorized_send_email_without_approval
3. LG-APPROVAL-001 manager_send_email_without_approval
4. LG-ALLOW-APPROVED-001 manager_send_email_with_approval
5. LG-FAILCLOSED-UNKNOWN-001 unknown_tool_fail_closed
6. LG-FAILCLOSED-IDENTITY-001 missing_identity_fail_closed
7. LG-INJECTION-001 prompt_injection_tool_escalation_denied

## 5. Decisions observed
- ALLOW
- DENY
- REQUIRE_APPROVAL
- ALLOW_WITH_APPROVAL
- DENY_FAIL_CLOSED

## 6. Expected vs actual result
- Passed cases: 7
- Failed cases: 0
- Runtime status: PASS (mock-runtime scope)

## 7. Audit events generated
- tool_allowed
- tool_denied_role
- approval_required
- tool_allowed_with_approval
- unknown_tool_denied
- identity_missing
- prompt_injection_tool_escalation_denied

## 8. Evidence artifacts produced
- allowed-tool-call-log.json
- denied-tool-call-log.json
- human-approval-required-log.json
- fail-closed-log.json
- runtime-trace.json
- policy-decision-log.json
- audit-events.json
- harness-summary.json
- harness-output.txt
- timestamp.txt
- git-commit.txt

## 9. What this proves
- A deterministic local LangGraph-style runtime control flow executed.
- Policy decisions for allow/deny/approval/fail-closed were exercised.
- Prompt-injection tool-escalation attempt was denied in mock runtime.
- Audit events were produced for each scenario decision.

## 10. What this does not prove
This is partial mock-runtime evidence. It does not prove a production LangGraph deployment, real external tool execution, or complete agent safety.

## 11. Launch-gate impact
- Evidence status: PARTIAL_EVIDENCE
- Launch gate: NO_GO

## 12. Next required action
Run production-representative LangGraph runtime tests with sandboxed real tool execution controls, memory-boundary validation, and incident-response correlation evidence.
