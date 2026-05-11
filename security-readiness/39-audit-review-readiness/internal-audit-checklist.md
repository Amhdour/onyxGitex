# Internal Audit Checklist

## Purpose
Provide a structured internal audit checklist to verify AI Trust & Security Readiness controls before launch-gate decisions.

## Usage
- Complete one row per control/topic under review.
- Mark status as `Not Started`, `In Review`, `Blocked`, `Pass`, or `Fail`.
- Unsupported launch assertions must remain blocked until required evidence is attached.

## Checklist

| ID | Review Criteria | Evidence Required | Reviewer | Status | Finding Severity | Remediation | Sign-off |
|---|---|---|---|---|---|---|---|
| IA-01 | Scope and assumptions are documented and current. | `security-readiness` phase scope docs, dated assumptions log. | Internal Audit Lead | Not Started | N/A | N/A | Pending |
| IA-02 | Identity and authorization boundaries are defined and tested. | Authz design references, test command + output, unresolved gaps list. | Security Architect | Not Started | N/A | N/A | Pending |
| IA-03 | Retrieval controls prevent cross-tenant/private-doc leakage. | Retrieval policy docs, policy tests, negative test results. | AppSec Reviewer | Not Started | N/A | N/A | Pending |
| IA-04 | Unsupported answers are constrained by policy and observable controls. | Runtime policy config, guardrail test output, failure handling evidence. | AI Risk Reviewer | Not Started | N/A | N/A | Pending |
| IA-05 | Tool usage controls enforce least privilege and fail-closed behavior. | Tool policy definitions, execution traces, denied action logs. | Platform Security | Not Started | N/A | N/A | Pending |
| IA-06 | Audit logs/traces support end-to-end event reconstruction. | Audit event schema, sample logs with IDs, trace correlation evidence. | Observability Owner | Not Started | N/A | N/A | Pending |
| IA-07 | Open findings are triaged with owner and target date. | Finding tracker entries with severity and remediation plan. | Risk Manager | Not Started | N/A | N/A | Pending |
| IA-08 | Readiness claim is evidence-backed and independently reproducible. | Evidence pack index with commands, outputs, and references. | Internal Audit Lead | Not Started | N/A | N/A | Pending |

## Reviewer Sign-off
- Reviewer Name:
- Role:
- Date (YYYY-MM-DD):
- Decision: `Approved` / `Conditionally Approved` / `Rejected`
- Notes:
- Signature/Initials:
