# OWASP LLM Top 10 Readiness Mapping (Priority 13)

**Date:** 2026-05-11  
**Scope:** Readiness mapping only (not certification and not legal compliance determination).

| OWASP LLM Risk Theme | Onyx Readiness Control | Evidence Artifact | Status | Gap | Owner |
|---|---|---|---|---|---|
| LLM01 Prompt Injection | Prompt injection readiness controls and policy tests | `security-readiness/12-portfolio-case-studies/02-prompt-injection-readiness.md`; `security-readiness/19-ci-cd-secure-delivery/policy-test-ci-pipeline.md` | Partially Confirmed | Need expanded adversarial test corpus coverage and measurable block rate | AI Security Testing |
| LLM02 Insecure Output Handling | Fail-closed behavior and runtime control points | `security-readiness/04-controls/onyx-fail-closed-rules.md`; `security-readiness/04-controls/onyx-runtime-control-points.md` | Partially Confirmed | Need integration tests proving downstream sanitization enforcement | Application Security |
| LLM06 Sensitive Information Disclosure | Retrieval authorization and data classification mapping | `security-readiness/04-controls/onyx-retrieval-authorization-controls.md`; `security-readiness/02-mapping/onyx-data-classification-map.md` | Verified | Need evidence of periodic access review and revoked-access tests | Data Protection Owner |
| LLM07 Insecure Plugin Design / Tooling | Agent tool governance and human confirmation policy | `security-readiness/17-agent-tool-governance/tool-capability-matrix.md`; `security-readiness/17-agent-tool-governance/human-confirmation-policy.md` | Partially Confirmed | Need production policy enforcement telemetry for high-risk tools | Agent Platform Owner |
| LLM08 Excessive Agency | Agent autonomy assessment and kill-switch runbook | `security-readiness/17-agent-tool-governance/agent-autonomy-level-assessment.md`; `security-readiness/17-agent-tool-governance/agent-kill-switch-runbook.md` | Partially Confirmed | Need live exercise evidence for emergency disable workflows | Operations Lead |
| LLM09 Overreliance | Launch-gate checklist with evidence requirements | `security-readiness/19-ci-cd-secure-delivery/release-readiness-checklist.md`; `security-readiness/12-portfolio-case-studies/07-full-mini-readiness-review.md` | Partially Confirmed | Need documented human-review thresholds for high-impact outputs | Product Risk Owner |

## Notes
- OWASP categories are mapped as risk themes for internal assurance planning.
- No claim is made that all OWASP LLM risks are fully mitigated.
