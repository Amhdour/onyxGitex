# Observability Vendor Security Review (Priority 38 / Scope 312)

## Purpose
Assess vendors used for logs, metrics, traces, and security telemetry in the AI assistant stack.

## Approval Principle
- Observability vendor is **not approved** until required telemetry protection and access controls are evidenced.

## Review Checklist
| Area | Control Questions | Evidence Required | Status |
|---|---|---|---|
| Data access | Can telemetry access be segmented by role, environment, and tenant? Is just-in-time admin access supported? | IAM/RBAC documentation, role matrix, support access controls | Unknown |
| Retention | Can logs/traces be retained per policy and legal hold requirements? | Retention configuration docs, lifecycle settings | Unknown |
| Logging | Are audit logs generated for dashboard edits, query access, exports, and alert changes? | Audit log catalog + sample events | Unknown |
| Encryption | Is telemetry encrypted in transit and at rest, including archived storage? | Encryption/key management docs | Unknown |
| Incident notification | Are outages and security incidents communicated with committed timelines? | Incident comms policy + contractual SLA | Unknown |
| Subcontractors | Which subprocessors support storage, alerting, or support? | Subprocessor list + regional processing details | Unknown |
| Audit rights | Are independent attestations available and current? | SOC 2 Type II / ISO certs + report dates | Unknown |
| Exit/deletion | Can historical telemetry be exported and securely deleted at contract end? | Export/deletion playbook + deletion confirmation process | Unknown |

## AI-Specific Telemetry Risks
- Prompt/response content may appear in traces; verify redaction and field-level filtering.
- Verify API keys/secrets masking in logs by default.
- Verify alert routes do not leak sensitive data to unmanaged channels.

## Review Outcome
- Vendor:
- Sensitive telemetry exposure risk:
- Required mitigations:
- Recommended procurement status:
