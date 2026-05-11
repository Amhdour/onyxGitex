# SOC 2-Style Control Readiness Mapping (Priority 13)

**Date:** 2026-05-11  
**Scope:** Readiness mapping only (not attestation and not legal compliance determination).

| SOC 2 Theme (TSC-style) | Onyx Readiness Control | Evidence Artifact | Status | Gap | Owner |
|---|---|---|---|---|---|
| Security: logical access and least privilege | Retrieval authorization controls and auth/access path map | `security-readiness/04-controls/onyx-retrieval-authorization-controls.md`; `security-readiness/00-repo-audit/onyx-auth-access-paths.md` | Partially Confirmed | Need formal user access recertification evidence | Identity & Access Mgmt |
| Security: change management and secure deployment | CI security test pipeline and launch-gate checks | `security-readiness/19-ci-cd-secure-delivery/security-test-ci-pipeline.md`; `security-readiness/19-ci-cd-secure-delivery/launch-gate-ci-check.md` | Verified | Need change-approval sampling tied to production releases | DevSecOps Owner |
| Availability: resilience and incident preparedness | Kill-switch runbook and release readiness checklist | `security-readiness/17-agent-tool-governance/agent-kill-switch-runbook.md`; `security-readiness/19-ci-cd-secure-delivery/release-readiness-checklist.md` | Partially Confirmed | Need incident simulation evidence and recovery time objectives | SRE Lead |
| Confidentiality: data handling controls | Data classification map and retrieval-path audit | `security-readiness/02-mapping/onyx-data-classification-map.md`; `security-readiness/00-repo-audit/onyx-retrieval-paths.md` | Partially Confirmed | Need data retention/deletion control verification evidence | Data Governance |
| Processing Integrity: accurate and complete processing | Policy tests, regression test pack, and control drift detection | `security-readiness/19-ci-cd-secure-delivery/policy-test-ci-pipeline.md`; `security-readiness/19-ci-cd-secure-delivery/regression-test-pack.md`; `security-readiness/19-ci-cd-secure-delivery/control-drift-detection.md` | Partially Confirmed | Need exception-handling metrics and integrity KPI thresholds | QA & Controls |

## Notes
- This document maps readiness controls to SOC 2-style trust service themes and is not an audit opinion.
