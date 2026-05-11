# Expensive Tool Execution Policy

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Policy Intent
Prevent abuse-driven infrastructure and external API cost spikes from autonomous tool execution.

## Policy Rules
1. Classify tools into cost tiers (`low`, `moderate`, `high`).
2. Require stricter controls for `high` tools:
   - explicit policy allowlist,
   - per-session invocation cap,
   - optional human approval for repeated use.
3. Deny by default when tool risk/cost classification is missing (fail-closed).

## Cost-Abuse Control Table
| Cost risk | Abuse scenario | Monitoring source | Threshold | Alert | Control | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| External API overuse | Agent tricked into repeated costly API calls | Tool invocation audit logs | >5 high-cost tool calls/session | High alert + temporary tool lock | High-cost tool cap + deny-on-cap | `security-readiness/17-agent-tool-governance/tool-execution-evidence-log.md` | Agent Platform Team |
| Compute-heavy local processing abuse | User triggers repeated expensive document/tool operations | Tool duration + invocation telemetry | P95 tool runtime doubles baseline for 30 min | Capacity + abuse alert | Per-user concurrency limits; emergency kill switch | `security-readiness/17-agent-tool-governance/agent-kill-switch-runbook.md` | SRE + Security |
| Cross-boundary data extraction attempts with tool chaining | Prompt injection forces iterative export-like calls | Tool call denied events and risk tags | Any critical exfiltration pattern | Critical SOC incident | Policy-based deny + actor/session containment | `security-readiness/33-monitoring-alerting/tool-misuse-alerting.md` | SOC |
