# Tool Risk Metrics

Date: 2026-05-11  
Status: Draft for Build Priority 26  
Classification: Internal

## Metric Catalog

| Metric Name | Calculation | Data Source | Target Threshold | Warning Threshold | Critical Threshold | Dashboard Field | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| Unauthorized Tool Invocation Rate | (Denied tool calls / Total tool call attempts) × 100 | Tool broker authorization logs | <= 0.5% (after tuning) | > 0.5% to 2.0% | > 2.0% | `tools.unauthorized_invocation_rate_pct` | **Investigate control drift** at Warning; **block** if Critical |
| High-Risk Tool Invocation Share | (High-risk tool calls / Total tool calls) × 100 | Tool classification registry + execution logs | <= 10% | > 10% to 20% | > 20% | `tools.high_risk_invocation_share_pct` | **Require approval evidence** at Warning; **block** if uncontrolled Critical |
| Tool Policy Violation Incidents | Count of confirmed policy-violating tool executions | Incident reports + runtime traces | 0 | 1 | >= 2 | `tools.policy_violation_incidents` | **Immediate launch block** at >= 1 pending containment |
| Tool Execution Audit Completeness | (Tool executions with full audit tuple / Total tool executions) × 100 | Audit event stream validation | 100% | 98% to < 100% | < 98% | `tools.audit_completeness_pct` | **Block launch** if < 100% without approved exception |
| Tool Failure Safe-Handling Rate | (Tool failures handled fail-closed / Total tool failures) × 100 | Runtime error handling logs + test cases | 100% | 95% to < 100% | < 95% | `tools.fail_closed_failure_handling_pct` | **Immediate launch block** if Critical |

## Dependencies and Availability Notes

- Tool risk classification inventory is a **dependency** if not finalized.
- Runtime trace-to-incident correlation may require SIEM mapping (**dependency**).
- If audit tuple fields are missing from schema, metric remains **Partially Confirmed**.

## Measurement Notes

- Define “full audit tuple” explicitly (actor, tool, parameters hash, decision, outcome, timestamp, trace ID).
- Exclude synthetic health checks from denominators unless they can trigger user-visible behavior.
- Recompute thresholds quarterly against observed baseline and threat trend.
