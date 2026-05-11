# LLM Provider Security Questionnaire (Priority 38 / Scope 310)

## Purpose
Standardize security and procurement questions for LLM providers used by the internal knowledge assistant.

## Mandatory Gate
- Provider status remains **Not Approved** until all critical questions have **Verified** evidence.

## Questionnaire
| Domain | Questions for Provider | Evidence Required | Criticality | Status |
|---|---|---|---|---|
| Data access | How is tenant isolation enforced for prompts, context, outputs, and fine-tuning data? | Multi-tenant isolation design, IAM model, access logs | High | Unknown |
| Retention | Are prompts/outputs retained by default? Can zero-retention/no-training modes be contractually enforced? | Retention settings docs, contractual commitment, control screenshots | High | Unknown |
| Logging | What events are logged (API auth, requests, policy denials, admin actions)? Can logs be exported to SIEM? | Audit event catalog, API docs, sample exports | High | Unknown |
| Encryption | TLS version requirements? Encryption-at-rest algorithm/key management model? CMK support? | Cryptographic controls documentation | High | Unknown |
| Incident notification | Notification timelines for incidents affecting confidentiality, integrity, or availability? | IR policy + SLA terms | High | Unknown |
| Subcontractors | Which subprocessors may process prompts or telemetry? | Subprocessor register + notice terms | Medium | Unknown |
| Audit rights | Available attestations and frequency (SOC 2 Type II, ISO 27001)? | Latest reports and period coverage | High | Unknown |
| Exit/deletion | How are customer prompts, files, and metadata deleted after termination? | Deletion lifecycle docs + contractual deletion clause | High | Unknown |

## Model-Specific Risk Questions
1. Are customer prompts/outputs used to train foundation models by default?
2. Are safety filters configurable per tenant and logged when overridden?
3. Are model/version changes announced in advance with rollback support?
4. Is regional processing available to meet data residency constraints?
5. Are abuse monitoring signals available without exposing customer content to unauthorized staff?

## Procurement Outcome
- Provider name:
- Intended use tier (pilot/production/high-risk workflow):
- Open gaps:
- Compensating controls required in Onyx:
- Final status: **Not Approved / Conditionally Acceptable / Approved with Evidence**
