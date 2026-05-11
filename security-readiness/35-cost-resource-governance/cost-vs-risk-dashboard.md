# Cost vs Risk Dashboard

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Dashboard Objective
Expose the relationship between spend signals and abuse/security risk so response teams can act before budget or control failure.

## Core Panels
1. Tenant spend trend (`llm_cost_cents`) vs abuse-event counts.
2. Token usage percentiles by actor/group.
3. High-cost model routing share and exception counts.
4. High-cost tool invocation trend + denial rates.
5. Budget threshold breach timeline (70/85/100%).

## KPI-Control Mapping
| Cost risk | Abuse scenario | Monitoring source | Threshold | Alert | Control | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| Rising spend without matching business volume | Abuse automation or misrouted workloads | Spend metrics + request throughput | Spend/request ratio >2x baseline | Governance anomaly alert | Routing policy review + throttling | `backend/onyx/db/usage.py`, `security-readiness/35-cost-resource-governance/model-routing-cost-policy.md` | FinOps + Governance |
| Increased denied-tool events + token growth | Prompt injection probing for costly actions | Tool denial logs + token telemetry | Denied-tool spikes plus >1.5x token growth | High abuse-cost alert | Session containment + investigation | `security-readiness/33-monitoring-alerting/tool-misuse-alerting.md`, `backend/onyx/llm/model_response.py` | SOC |
| Budget-critical events increasing | Control drift or sustained abuse pressure | Budget threshold events | >3 critical breaches/week/tenant | Launch-gate risk alert | Launch hold pending remediation | `security-readiness/33-monitoring-alerting/launch-gate-drift-alerting.md` | Launch Authority |

## Data Handling Constraints
- No real billing invoice data is ingested in this dashboard specification.
- Data sources are internal telemetry, counters, and audit events only.
