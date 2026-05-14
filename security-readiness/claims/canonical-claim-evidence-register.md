# Canonical Claim-Evidence Register

| claim ID | claim text | claim type | status | evidence path | evidence quality | limitation | external-safe wording | forbidden wording |
|---|---|---|---|---|---|---|---|---|
| CLM-V21-001 | V2.1 defines an artifact-aware evidence validation model. | allowed | ALLOWED | security-readiness/scripts/validate_readiness_evidence.py | STATIC_REVIEW | Does not prove runtime pass | Artifact-aware validation is implemented | Production readiness proven |
| CLM-V21-002 | V2.1 defines P0 runtime proof-pack structure and acceptance criteria. | allowed | ALLOWED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/ | P0_PROOF_STRUCTURE_ONLY | Tests not executed | P0 proof structure exists | P0 runtime controls passed |
| CLM-V21-003 | V2.1 improves reviewability of RAG/agent readiness evidence. | allowed | ALLOWED | START_HERE.md; VERSION_STATUS.md | STATIC_REVIEW | Reviewability != runtime verification | Reviewability improved | Staging or production verified |
| CLM-V21-004 | V2.1 proves all P0 controls pass. | blocked | BLOCKED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json | NONE | controls NOT_EXECUTED | Not claimed | All P0 controls pass |
| CLM-V21-005 | V2.1 proves production readiness. | blocked | BLOCKED | security-readiness/meta/canonical-version-status.json | NONE | production evidence missing | Not claimed | Production-ready |
| CLM-V21-006 | V2.1 proves client readiness. | blocked | BLOCKED | security-readiness/meta/canonical-version-status.json | NONE | client evidence missing | Not claimed | Client-verified |
| CLM-V21-007 | V2.1 proves staging runtime verification. | blocked | BLOCKED | security-readiness/meta/canonical-version-status.json | NONE | staging evidence missing | Not claimed | Staging-verified |
| CLM-V21-008 | V2.1 proves compliance certification. | blocked | BLOCKED | N/A | NONE | no certification evidence | Not claimed | Compliance-certified |
