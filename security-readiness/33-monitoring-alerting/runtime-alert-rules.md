# Runtime Alert Rules

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Objective
Define baseline runtime alert rules for the internal knowledge assistant with explicit ties to audit/trace events and launch-gate decision impact.

## Scope
- Runtime event monitoring requirements only.
- No live alert routing/integration is implemented in this artifact.

## Runtime Alert Catalog

| Alert ID | Signal | Severity | Threshold | Owner | Evidence Source | Response Action | Launch Gate Impact |
|---|---|---|---|---|---|---|---|
| RA-001 | `policy.decision=deny` spike | High | >20 denies in 5 minutes per tenant/app | AI Security | Policy decision audit events + trace spans | Trigger security triage; verify policy health and abuse indicators | Blocks launch if sustained for 3 consecutive intervals without explained maintenance window |
| RA-002 | Missing required audit fields (`control_id`, `decision_id`) | Critical | Any event missing mandatory fields | Platform Observability | Structured audit logs schema validation traces | Open incident; fail evidence pipeline step | Immediate launch-gate hold until schema compliance restored |
| RA-003 | Retrieval authorization denials anomaly | Medium | Denial rate >2x 7-day baseline for 30 minutes | Retrieval Security | Retrieval auth decision logs + request traces | Investigate index ACL drift and user-role mapping changes | Conditional hold if unexplained anomaly persists >24h |
| RA-004 | Tool invocation denied for policy reasons | High | >10 denied tool calls in 10 minutes per tool | Agent Platform + AI Security | Tool authorization audit events + tool traces | Disable risky tool route if misuse pattern confirmed | Required security sign-off before launch continuation |
| RA-005 | Data leakage classifier hit (`exfiltration_risk=true`) | Critical | Any confirmed high-confidence hit | AI Trust Office | Output safety audit events + response trace snapshots (`[REDACTED]`) | Immediate incident response + session containment | Automatic launch-gate fail until incident closure evidence exists |
| RA-006 | Evidence job failure (`evidence_manifest_invalid`) | High | Any failed daily evidence run | GRC + Security PMO | Evidence pipeline logs + manifest validation trace | Re-run pipeline, identify control evidence gap | Blocks readiness declaration for affected control domain |
| RA-007 | Launch readiness drift (`readiness_score` below threshold) | High | Score < approved minimum for 2 consecutive evaluations | Launch Governance | Readiness score logs + control verification traces | Escalate to launch review board; pause promotion | Launch-gate pause pending remediation plan approval |

## Verification Status
- **Verified**: Alert definitions and routing ownership documented.
- **Partially Confirmed**: Threshold effectiveness pending runtime tuning exercises.
- **Unknown**: Live paging/notification behavior until integrated by operations.
