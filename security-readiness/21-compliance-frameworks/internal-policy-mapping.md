# Internal Policy Readiness Mapping (Priority 13)

**Date:** 2026-05-11  
**Scope:** Internal readiness mapping only (not policy approval and not legal compliance determination).

| Internal Policy Theme | Onyx Readiness Control | Evidence Artifact | Status | Gap | Owner |
|---|---|---|---|---|---|
| AI acceptable-use and safety constraints | Fail-closed rules and runtime control points | `security-readiness/04-controls/onyx-fail-closed-rules.md`; `security-readiness/04-controls/onyx-runtime-control-points.md` | Partially Confirmed | Need approved policy text mapped to enforceable control statements | AI Policy Owner |
| Identity, authorization, and segregation of access | Retrieval authorization controls and auth/access paths | `security-readiness/04-controls/onyx-retrieval-authorization-controls.md`; `security-readiness/00-repo-audit/onyx-auth-access-paths.md` | Verified | Need quarterly access review records and exception handling flow | IAM Owner |
| Audit logging and evidence retention | Policy decision log requirements and tool execution evidence log | `security-readiness/04-controls/onyx-policy-decision-log-requirements.md`; `security-readiness/17-agent-tool-governance/tool-execution-evidence-log.md` | Partially Confirmed | Need retention schedule approvals and immutable storage evidence | Audit & Compliance |
| Third-party and connector risk governance | MCP server risk readiness and high-risk tool classification | `security-readiness/12-portfolio-case-studies/04-mcp-server-risk-readiness.md`; `security-readiness/17-agent-tool-governance/high-risk-tool-classification.md` | Partially Confirmed | Need standardized third-party onboarding checklist and sign-off trail | Third-Party Risk |
| Release governance and launch approval | Launch-gate checks and full readiness review | `security-readiness/19-ci-cd-secure-delivery/launch-gate-ci-check.md`; `security-readiness/12-portfolio-case-studies/07-full-mini-readiness-review.md` | Partially Confirmed | Need formal governance committee approval workflow and minutes template | Release Governance Chair |

## Notes
- This mapping supports internal control alignment work and identifies gaps for policy completion.
- No claim is made that internal policy obligations are fully satisfied.
