# Abuse Monitoring Plan

## Purpose
Define operational monitoring signals for misuse attempts and safety-control failures.

## Monitoring Objectives
1. Detect high-risk misuse behavior quickly.
2. Correlate repeated abuse patterns across users/sessions/tools.
3. Provide incident-ready evidence for containment and review.

## Core Signals

| Signal ID | Signal Name | Trigger Condition | Source | Severity | Linked Controls |
|---|---|---|---|---|---|
| AMS-01 | Unauthorized Retrieval Attempt | ACL mismatch or blocked classified document request. | Retrieval authorization logs | High | CSC-01 |
| AMS-02 | PII Disclosure Block | PII output prevented or redacted. | Output filter logs | Medium | CSC-02 |
| AMS-03 | Overreliance Boundary Trigger | Legal/financial directive request detected. | Classifier + response policy logs | Medium | CSC-03 |
| AMS-04 | Prompt Injection Detection | Injection patterns in retrieved/user instructions. | Context integrity detector | High | CSC-04 |
| AMS-05 | Policy Bypass Pattern | “Ignore rules/system prompt” style bypass attempt. | Input classifier | High | CSC-05 |
| AMS-06 | Unauthorized Tool Request | Disallowed tool/action or invalid arguments attempted. | Tool broker audit logs | High | CSC-06 |
| AMS-07 | Sensitive Ops Exposure Block | Secret/infrastructure-sensitive content suppressed. | Output safety filter | High | CSC-07 |
| AMS-08 | Decision Logging Gap | Missing required audit fields for policy decisions. | Audit pipeline validator | High | CSC-08 |

## Alerting and Triage
- High severity: immediate SOC/on-call notification.
- Medium severity: daily review queue + threshold-based escalation.
- Low severity: trend analysis only.

## Correlation Rules
- 3+ AMS-05 or AMS-06 events for same user in 24h → escalate to potential misuse case.
- AMS-04 followed by AMS-01/AMS-07 in same session → classify as active injection campaign candidate.
- Any AMS-08 in production → treat as control observability defect.

## Retention and Evidence
- Preserve raw events and normalized incident records per enterprise policy.
- Retain linkage: `request_id` ↔ `decision_id` ↔ `incident_id`.
- Redact sensitive payload fragments while preserving forensic utility.

## Verification Status
- **Verified**: Monitoring schema and signal mapping documented.
- **Partially Confirmed**: Integration with live SIEM not validated in this artifact.
