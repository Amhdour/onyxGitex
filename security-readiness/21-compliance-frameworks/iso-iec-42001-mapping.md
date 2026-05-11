# ISO/IEC 42001 Readiness Mapping (Priority 13)

**Date:** 2026-05-11  
**Scope:** Readiness mapping only (not certification and not legal compliance determination).

| ISO/IEC 42001 Requirement Theme | Onyx Readiness Control | Evidence Artifact | Status | Gap | Owner |
|---|---|---|---|---|---|
| AI management system governance and accountability | Control ownership matrix and launch decision artifacts | `security-readiness/04-controls/onyx-control-ownership-matrix.md`; `security-readiness/19-ci-cd-secure-delivery/artifacts/launch-gate-summary.md` | Partially Confirmed | Need formal AIMS policy set and management-review minutes | AI Program Manager |
| Risk and impact assessment process | Threat modeling and abuse-case documentation | `security-readiness/12-portfolio-case-studies/02-prompt-injection-readiness.md`; `security-readiness/12-portfolio-case-studies/04-mcp-server-risk-readiness.md` | Partially Confirmed | Need recurring risk re-assessment schedule with acceptance criteria | Security Risk Lead |
| Operational controls and fail-safe behavior | Fail-closed rules and retrieval authorization controls | `security-readiness/04-controls/onyx-fail-closed-rules.md`; `security-readiness/04-controls/onyx-retrieval-authorization-controls.md` | Verified | Need production validation evidence for enforcement effectiveness | Platform Security |
| Monitoring, logging, and incident-readiness support | Auditability readiness and observability path mapping | `security-readiness/12-portfolio-case-studies/05-ai-auditability-readiness.md`; `security-readiness/00-repo-audit/onyx-observability-paths.md` | Partially Confirmed | Need incident-response integration test records and drill outcomes | Detection & Response |
| Continual improvement and control verification | CI policy tests and control drift detection | `security-readiness/19-ci-cd-secure-delivery/policy-test-ci-pipeline.md`; `security-readiness/19-ci-cd-secure-delivery/control-drift-detection.md` | Partially Confirmed | Need KPI baseline and periodic management reporting loop | AI Quality Owner |

## Notes
- This is an implementation-readiness crosswalk to ISO/IEC 42001 themes, not an accredited certification result.
