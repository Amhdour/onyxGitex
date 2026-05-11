# Vector Database Security Questionnaire (Priority 38 / Scope 311)

## Purpose
Evaluate vector database vendors that store embeddings and retrieval metadata for confidentiality, isolation, and deletion assurances.

## Non-Negotiable Approval Condition
- Do not mark vendor approved unless access, encryption, retention, and deletion controls are **Verified** with evidence.

## Security Questionnaire
| Control Area | Questions | Evidence Required | Status |
|---|---|---|---|
| Data access | Is namespace/tenant isolation enforced? Are collection-level ACLs and service account scopes available? | Access model docs, RBAC examples, admin screenshots | Unknown |
| Retention | Can index data, snapshots, and backups be retained per customer policy? | Retention config docs and backup policy | Unknown |
| Logging | Are query, admin, and auth events logged with actor identity and timestamp? | Audit log samples + export method | Unknown |
| Encryption | Is TLS mandatory in transit? Are vectors, metadata, and backups encrypted at rest? | Encryption architecture + key management details | Unknown |
| Incident notification | What SLA governs incidents impacting stored vectors/metadata? | IR SLA in contract + response policy | Unknown |
| Subcontractors | Do hosting/cloud subprocessors access customer vector data? | Subprocessor list + data handling scope | Unknown |
| Audit rights | Can customer review independent audit reports and request control clarifications? | SOC/ISO reports + audit response process | Unknown |
| Exit/deletion | How are vectors, metadata, and backups deleted and verified at termination? | Secure deletion runbook + deletion attestation format | Unknown |

## Implementation Fit Questions
- Does vendor support private networking, IP allowlists, and customer VPC/VNet options?
- Are restore operations logged and approval-gated?
- Are backup encryption keys customer-controlled or vendor-controlled?
- Can dataset-level deletion be executed without full cluster teardown?

## Decision Record
- Vendor:
- Workload classification:
- Key unresolved risks:
- Required mitigations before production:
- Final decision: **Pending Evidence / Conditionally Acceptable / Rejected / Approved**
