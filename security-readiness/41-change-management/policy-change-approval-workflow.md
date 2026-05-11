# Policy Change Approval Workflow

## Scope
Controls for changes to security, safety, content, retrieval authorization, and runtime decision policies.

## Workflow
1. Submit `AI Change Request` with **Change Type = Policy**.
2. Perform risk assessment of policy relaxation/tightening effects and control dependencies.
3. Execute required tests:
   - policy decision tests,
   - negative/abuse tests,
   - compatibility tests with existing prompts/models/tools,
   - logging and explainability checks.
4. Update evidence with policy diffs, decision logs, and outcome comparisons.
5. Route approvals to policy owner, security governance, and service owner.
6. Deploy with controlled rollout and rollback checkpoints.
7. Update launch gate status based on residual risk.

## Required Control Fields
- **Change Type:** Policy
- **Risk Assessment:** Mandatory
- **Required Tests:** Mandatory
- **Evidence Update:** Mandatory
- **Approval Owner:** Security Policy Owner
- **Rollback:** Required (policy version rollback)
- **Launch Gate Impact:** Required

## Minimum Approval Criteria
- Policy behavior is test-backed and auditable.
- No unapproved policy bypass introduced.
- Residual risk documented and accepted by owner.
