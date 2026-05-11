# AI Vendor Due Diligence Checklist (Priority 38 / Scope 309)

## Purpose
Provide procurement and security teams with a practical, evidence-based checklist for evaluating AI vendors before onboarding.

## Decision Rule
- **No Approval Without Evidence:** A vendor cannot be marked **Approved** until each required control below is rated **Verified** with attached evidence.
- Interim outcomes are **Conditionally Acceptable** (gaps with deadlines) or **Rejected**.

## Status Legend
- **Verified:** Reliable evidence reviewed.
- **Partially Confirmed:** Some evidence exists but is incomplete.
- **Unknown:** No reliable evidence provided.
- **Not Applicable:** Must include rationale and approver.

## Vendor Profile
- Vendor legal name:
- Product/service name:
- Service type (LLM, vector DB, observability, MCP tooling, other):
- Data processing role (processor/controller/subprocessor):
- Procurement owner:
- Security reviewer:
- Review date (YYYY-MM-DD):

## Core Security & Privacy Controls Checklist
| Control Area | Required Questions | Minimum Evidence Required | Status | Notes / Gaps |
|---|---|---|---|---|
| Data access | How is tenant access isolated? Are RBAC/ABAC controls enforced? Are privileged support accesses controlled and logged? | Architecture diagram, access control docs, admin role matrix, support access policy | Unknown |  |
| Retention | What default retention periods apply to prompts, outputs, metadata, and logs? Can retention be customer-configured? | Retention policy, product config screenshots, contract retention terms | Unknown |  |
| Logging | What security/audit logs are produced? Are logs immutable, exportable, and timestamped? | Audit logging documentation, sample log schema, export/API references | Unknown |  |
| Encryption | Is encryption used in transit and at rest? Who manages keys? Is customer-managed key support available? | Encryption whitepaper, TLS/KMS configuration docs, key management controls | Unknown |  |
| Incident notification | What breach/incident notification SLA applies? What severity levels trigger notice? | Incident response policy, contractual SLA clause, escalation matrix | Unknown |  |
| Subcontractors | Which subprocessors handle customer data? How are new subprocessors disclosed? | Subprocessor list, change-notice policy, DPA terms | Unknown |  |
| Audit rights | Are audit reports provided (SOC 2/ISO 27001)? Are customer audits/assessments allowed? | Latest attestation reports, bridge letter, audit rights clause | Unknown |  |
| Exit/deletion | Can customer data be exported and deleted on demand and at termination? Is deletion verifiable? | Data export/deletion procedure, termination playbook, deletion certificate sample | Unknown |  |

## Evidence Intake Checklist
- Security package received (SOC 2, ISO certs, pen test summaries).
- Contract terms received (MSA, DPA, security addendum).
- Product technical controls reviewed against intended use.
- Exceptions documented with compensating controls and due date.

## Procurement Recommendation
- Recommendation: **Pending / Conditionally Acceptable / Rejected / Approved**
- Approval prerequisites remaining:
- Residual risk summary:
- Target remediation date:
- Final approvers (Security, Legal, Procurement, Service Owner):
