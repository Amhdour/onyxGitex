# Model Routing Cost Policy

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Policy Goal
Route requests to the lowest-cost model tier that satisfies security, quality, and latency requirements.

## Routing Principles
1. Default to lower-cost approved model tier for standard internal Q&A.
2. Escalate to higher-cost tier only when defined quality/risk criteria are met.
3. Block undocumented routing overrides in production (fail-closed).
4. Log routing decision rationale for audit.

## Cost Governance Matrix
| Cost risk | Abuse scenario | Monitoring source | Threshold | Alert | Control | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| Uncontrolled premium model usage | Attackers/users force premium-tier invocations with crafted prompts | Model selection logs + usage aggregates | Premium tier >20% of requests without approved exception | Governance alert | Routing guardrail policy + exception review | `security-readiness/16-model-provider-governance/model-routing-policy.md` | AI Governance + Platform |
| Routing drift after config change | Misconfiguration silently routes all traffic to expensive models | Config diff + deployment audit trail | Any unapproved routing config change | Change-management alert | Protected config path + dual approval | `security-readiness/20-deployment-environment/runtime-configuration-review.md` | Release Engineering |
| High-cost fallback loop | Repeated provider failures trigger costly fallback tier repeatedly | Fallback event logs + model usage | >3 fallbacks/request chain | Reliability + cost alert | Fallback cap + graceful degrade response | `security-readiness/32-reliability-resilience/model-failure-handling-plan.md` | SRE |
