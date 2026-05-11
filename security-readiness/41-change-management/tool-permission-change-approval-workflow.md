# Tool Permission Change Approval Workflow

## Scope
Controls for enabling/disabling tools, adjusting tool scopes, and changing agent execution permissions.

## Workflow
1. Submit `AI Change Request` with **Change Type = Tool Permission**.
2. Perform risk assessment on privilege escalation, external action risk, and misuse blast radius.
3. Execute required tests:
   - authorization tests per role,
   - deny-by-default/fail-closed checks,
   - abuse-case execution tests,
   - audit log verification for tool calls.
4. Update evidence with permission diffs, test outputs, and audit event references.
5. Obtain approvals from tool owner, security reviewer, and service owner.
6. Deploy with immediate rollback capability.
7. Reassess launch gate impact for agentic risk posture.

## Required Control Fields
- **Change Type:** Tool Permission
- **Risk Assessment:** Mandatory
- **Required Tests:** Mandatory
- **Evidence Update:** Mandatory
- **Approval Owner:** Tool Governance Owner
- **Rollback:** Required (permission profile revert)
- **Launch Gate Impact:** Required

## Minimum Approval Criteria
- No unauthorized tool invocation in tests.
- High-risk tools have explicit justification and ownership.
- Auditability of tool decisions is preserved.
