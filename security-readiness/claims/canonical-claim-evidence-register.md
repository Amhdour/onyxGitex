# Canonical Claim-Evidence Register

| claim ID | claim text | claim type | status | evidence path | evidence quality | limitation | external-safe wording | forbidden wording |
|---|---|---|---|---|---|---|---|---|
| CLM-V222H-001 | V2.2.2 produced LOCAL_HARNESS evidence for four P0 controls. | allowed | ALLOWED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json | LOCAL_HARNESS_PARTIAL | Helper-level evidence only | Four controls passed in local harness scope | Full runtime proven |
| CLM-V222H-002 | V2.2.2-hotfix corrected stale aggregate wording to reflect the mixed result. | allowed | ALLOWED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json | STATUS_WORDING_CORRECTION | Metadata correction only | Mixed-result wording corrected | All controls blocked/no control passed |
| CLM-V222H-003 | Four P0 controls reached assertions and passed at helper-level. | allowed | ALLOWED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json | LOCAL_HARNESS_PARTIAL | Not LOCAL_RUNTIME | Four helper-level controls passed | Full runtime passed |
| CLM-V222H-004 | Three P0 controls remain blocked by import/dependency setup. | allowed | ALLOWED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json | BLOCKED_IMPORT_DEPENDENCY | Missing fastapi_users | Three controls remain blocked | All controls passed |
| CLM-V222H-005 | Launch remains NO_GO. | allowed | ALLOWED | security-readiness/launch-gates/canonical-launch-gate-decision.json | LAUNCH_GATE_CANONICAL | P0 blockers remain | Launch remains NO_GO | Launch GO supported |
| CLM-V222H-006 | All seven P0 controls passed. | blocked | BLOCKED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json | NONE | Contradicted by counters | Not claimed | All seven passed |
| CLM-V222H-007 | All seven P0 controls have full runtime proof. | blocked | BLOCKED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json | NONE | controls_local_runtime_passed = 0 | Not claimed | Full runtime proof exists |
| CLM-V222H-008 | The project is production ready. | blocked | BLOCKED | security-readiness/meta/canonical-version-status.json | NONE | production_ready false | Not claimed | Production ready |
| CLM-V222H-009 | The project is client ready. | blocked | BLOCKED | security-readiness/meta/canonical-version-status.json | NONE | client_verified false | Not claimed | Client verified |
| CLM-V222H-010 | The project is staging verified. | blocked | BLOCKED | security-readiness/meta/canonical-version-status.json | NONE | staging_verified false | Not claimed | Staging verified |
| CLM-V222H-011 | The project is compliance certified. | blocked | BLOCKED | N/A | NONE | No certification evidence | Not claimed | Compliance certified |
| CLM-V222H-012 | The project is safe to launch. | blocked | BLOCKED | security-readiness/launch-gates/canonical-launch-gate-decision.json | NONE | NO_GO | Not claimed | Safe to launch |
| CLM-V222H-013 | LOCAL_HARNESS evidence is equivalent to full runtime evidence. | blocked | BLOCKED | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/result-taxonomy.md | NONE | Taxonomy forbids equivalence | Not claimed | Equivalent evidence levels |
