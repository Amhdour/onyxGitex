# Content Safety Control Matrix

## Purpose
Map misuse risks to concrete controls and test coverage for auditability.

| Control ID | Risk Scenario | Control Description | Enforcement Point | Test Case IDs | Expected Result |
|---|---|---|---|---|---|
| CSC-01 | Private document extraction | Retrieval authorization gating by user/document ACL and classification. | Retrieval layer | SET-01, SET-02 | Unauthorized docs not returned; refusal generated |
| CSC-02 | Employee data misuse | PII minimization and purpose validation before disclosure. | Response policy layer | SET-03, SET-04 | PII withheld or redacted; audit event logged |
| CSC-03 | Legal/financial overreliance | Advice boundary policy with disclaimer + escalation path. | Output generation layer | SET-05 | Non-authoritative guidance with escalation recommendation |
| CSC-04 | Prompt injection | Untrusted context isolation + instruction hierarchy enforcement. | Context assembly layer | SET-06, SET-07 | Injected instructions ignored; safe output only |
| CSC-05 | Policy bypass attempts | Refusal templates and bypass phrase detection rules. | Input classification layer | SET-08 | Refusal and abuse flag emitted |
| CSC-06 | Tool misuse | Tool allowlist, argument validation, and deny-by-default. | Tool broker | SET-09, SET-10 | Tool execution blocked when unauthorized |
| CSC-07 | Sensitive operational exposure | Secret/pattern detection and suppression/redaction. | Output filtering layer | SET-11 | Sensitive tokens withheld; high-level substitute provided |
| CSC-08 | Cross-control accountability | Policy decision logging with control IDs and outcomes. | Audit logging pipeline | SET-12 | Evidence record includes triggered controls |

## Evidence Notes
- Test case mappings are defined in `safety-evaluation-test-set.md`.
- Monitoring linkage is defined in `abuse-monitoring-plan.md`.
- Incident action linkage is defined in `safety-incident-playbook.md`.

## Verification Status
- **Verified**: Matrix-to-test mapping documented.
- **Unknown**: End-to-end pass/fail results pending execution.
