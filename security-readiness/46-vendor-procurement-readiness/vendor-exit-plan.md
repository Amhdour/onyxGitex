# Vendor Exit Plan (Priority 38 / Scope 315)

## Purpose
Ensure controlled disengagement from AI vendors without data residue, access persistence, or evidence gaps.

## Exit Triggers
- Contract termination/non-renewal.
- Material security breach or unresolved control failure.
- Strategic migration to alternate provider.

## Pre-Exit Readiness Requirements
- Export format and API capabilities documented.
- Data ownership and portability terms validated in contract.
- Deletion timelines and certificate format agreed.
- Dependency map completed (integrations, keys, pipelines, dashboards).

## Exit Execution Checklist
| Step | Required Action | Evidence Required | Status |
|---|---|---|---|
| 1 | Freeze new data flow to vendor (ingest, sync, tool calls). | Change ticket + config diff | Unknown |
| 2 | Export required business/security records. | Export job logs + checksum/hash validation | Unknown |
| 3 | Revoke credentials, API keys, and federation trust. | IAM change logs + failed auth verification | Unknown |
| 4 | Remove vendor from runtime allowlists and integrations. | Config snapshots + deployment logs | Unknown |
| 5 | Trigger contractual deletion workflow. | Vendor deletion request and acknowledgment | Unknown |
| 6 | Validate deletion of primary and backup data. | Deletion certificate + follow-up confirmation | Unknown |
| 7 | Archive audit evidence for retention period. | Evidence repository entry and access controls | Unknown |

## Control Validation Areas
- Data access removed for both customer users and vendor support paths.
- Retention obligations closed (including backups and replicas).
- Logging preserved for legal/audit retention before vendor cutoff.
- Encryption keys rotated or destroyed where shared control existed.
- Incident notification channel remains active through transition window.
- Subprocessor exposure closed through primary vendor termination.

## Exit Sign-Off
- Security owner:
- Procurement owner:
- Legal owner:
- Service owner:
- Exit completion date (YYYY-MM-DD):
- Residual risks (if any):

## Final Rule
- Vendor exit is not complete until deletion and access revocation are **Verified** with evidence.
