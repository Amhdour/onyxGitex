# Emergency Change Procedure

## Purpose
Enable urgent risk-reducing changes while maintaining auditability and post-hoc governance.

## Trigger Conditions
- Active security incident or confirmed exploit path.
- Material data exposure risk.
- Critical service instability with security implications.

## Emergency Workflow
1. Open emergency `AI Change Request` with **Change Type = Emergency**.
2. Record immediate risk assessment with known/unknown impacts.
3. Obtain expedited approval (minimum: incident commander + security owner).
4. Implement the smallest safe change (fail-closed preferred).
5. Execute minimum required tests feasible during incident.
6. Capture evidence updates in near-real time.
7. Confirm rollback readiness.
8. Conduct post-incident formal review within 2 business days.
9. Convert emergency change into standard workflow artifacts for permanent remediation.

## Required Control Fields
- **Change Type:** Emergency
- **Risk Assessment:** Required (rapid)
- **Required Tests:** Minimum viable + deferred full suite
- **Evidence Update:** Mandatory during and after incident
- **Approval Owner:** Incident Commander
- **Rollback:** Mandatory
- **Launch Gate Impact:** Immediate reassessment; may force launch hold

## Post-Emergency Requirements
- Full retrospective and control-gap analysis.
- Backfill skipped tests with explicit results.
- Document residual risks and ownership.
