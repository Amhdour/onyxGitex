# AI Failure Mode Register

**Priority:** 18 — Business & Use-Case Risk  
**Use Case:** Internal Company Knowledge Assistant  
**Date:** 2026-05-11

## 1) Register Purpose

Track major failure modes, impact, detection, containment expectations, and launch implications for business-critical use.

## 2) Failure Modes

| ID | Failure Mode | Business Process Supported | User Groups Affected | Potential Harm Types | Detection Signal | Containment Expectation | Launch Condition Link | Residual Risk |
|---|---|---|---|---|---|---|---|---|
| FM-01 | Unauthorized document retrieval | Policy/procedure lookup | All users; highest impact to sensitive teams | Confidentiality, trust harm | Access anomaly alerts, negative auth tests | Immediate deny, incident triage, scope revocation | Retrieval auth verification required | Medium-High |
| FM-02 | Hallucinated procedural guidance | Operations/support knowledge | Support, engineering, new hires | Informational, operational, career harm | Citation-missing rate, contradiction sampling | Low-confidence warning, human escalation | Grounding + uncertainty controls required | Medium |
| FM-03 | Stale knowledge retrieval | Incident/change workflows | On-call, support, operations | Operational delay, incorrect action | Freshness lag metrics, index drift checks | Fallback to canonical docs, refresh pipeline | Freshness SLO + fallback required | Medium |
| FM-04 | Tool misuse/overreach | Action-assisted tasks | Ops/admin users | Operational, security harm | Tool policy violations, abnormal call patterns | Block, rate-limit, credential isolation | Tool policy gate + audit trail required | Medium-High |
| FM-05 | Identity-context mismatch | Role-based guidance | All users | Confidentiality, integrity harm | Claim mismatch logs, session anomalies | Fail-closed, re-authentication, session kill | IAM dependency tests required | Medium-High |
| FM-06 | Observability failure | All workflows | Operators, governance teams | Auditability harm, delayed response | Missing-log detectors, trace gap alerts | Degrade/stop high-risk features until restored | Audit completeness threshold required | Medium |
| FM-07 | Dependency outage (model/index/IAM) | All workflows | All users | Availability, workload harm | Health checks, SLO breach alerts | Degraded mode + manual fallback | Degraded-mode tests required | Medium |

## 3) High-Risk Decisions (Cross-Cutting)

The system must not autonomously finalize high-risk decisions (access changes, incident severity declaration, customer-impacting change approvals, regulated data handling). These require human authority.

## 4) Misuse Paths (Cross-Cutting)

- Prompt-injection-driven exfiltration attempts.
- Tool invocation through instruction laundering.
- Social engineering through authoritative tone.

## 5) Launch Conditions

- All FM-01 to FM-07 have mapped controls, owners, and response runbooks.
- Detection signals are observable in pre-launch validation.
- Residual risk for each failure mode is acknowledged by business/security stakeholders.

## 6) No-Go Conditions

- Any high-severity failure mode lacks containment runbook.
- Detection is absent for unauthorized retrieval or tool misuse.
- Failure mode evidence is incomplete for critical workflows.

## 7) Residual Risk Summary

Residual risk across the register is **Medium to Medium-High** and explicitly **not eliminated**. Current status is **Partially Confirmed** pending broader abuse-case execution and integrated control verification.

## 8) Legal/Compliance Note

This register provides operational risk analysis only and makes **no legal or compliance conclusions**.
