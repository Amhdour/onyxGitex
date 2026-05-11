# NIST AI RMF Readiness Mapping (Priority 13)

**Date:** 2026-05-11  
**Scope:** Readiness mapping only (not certification and not legal compliance determination).

| NIST AI RMF Theme | Onyx Readiness Control | Evidence Artifact | Status | Gap | Owner |
|---|---|---|---|---|---|
| Govern (GV): documented roles, accountability, and oversight | Control ownership and decision accountability matrix | `security-readiness/04-controls/onyx-control-ownership-matrix.md` | Partially Confirmed | Need formal governance cadence and executive approval records | AI Governance Lead |
| Map (MP): system context and boundaries are documented | System map, trust boundaries, and data flow mapping | `security-readiness/02-mapping/onyx-system-map.md`; `security-readiness/02-mapping/onyx-trust-boundary-map.md`; `security-readiness/02-mapping/onyx-data-flow-map.md` | Verified | Need periodic re-validation checkpoint and change trigger policy | Security Architecture |
| Measure (ME): risks and control efficacy are evaluated | Security testing and regression readiness artifacts | `security-readiness/19-ci-cd-secure-delivery/security-test-ci-pipeline.md`; `security-readiness/19-ci-cd-secure-delivery/regression-test-pack.md` | Partially Confirmed | Add quantitative risk scoring thresholds and trend dashboard evidence | Security Testing Lead |
| Manage (MG): risk treatment and lifecycle management | Launch-gate checks and residual-risk decision artifacts | `security-readiness/19-ci-cd-secure-delivery/launch-gate-ci-check.md`; `security-readiness/19-ci-cd-secure-delivery/artifacts/launch-gate-summary.md` | Partially Confirmed | Add documented exception workflow with expiration tracking | Risk Manager |
| Cross-cutting: traceability and auditable evidence | Policy decision logging requirements and auditability case study | `security-readiness/04-controls/onyx-policy-decision-log-requirements.md`; `security-readiness/12-portfolio-case-studies/05-ai-auditability-readiness.md` | Partially Confirmed | Need end-to-end sampled logs demonstrating complete control traceability | Observability Owner |

## Notes
- Mapping aligns to NIST AI RMF function themes (GV, MP, ME, MG) for internal readiness tracking.
- No statement in this document should be interpreted as NIST conformity certification.
