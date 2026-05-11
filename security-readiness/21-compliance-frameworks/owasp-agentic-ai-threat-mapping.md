# OWASP Agentic AI Threat Readiness Mapping (Priority 13)

**Date:** 2026-05-11  
**Scope:** Readiness mapping only (not certification and not legal compliance determination).

| Agentic Threat Theme | Onyx Readiness Control | Evidence Artifact | Status | Gap | Owner |
|---|---|---|---|---|---|
| Unauthorized tool execution | Tool authorization readiness and capability matrix | `security-readiness/12-portfolio-case-studies/03-tool-authorization-readiness.md`; `security-readiness/17-agent-tool-governance/tool-capability-matrix.md` | Partially Confirmed | Need denial-path coverage for every high-risk tool class | Tooling Security Owner |
| Excessive autonomy and unsafe action chaining | Autonomy assessment and human confirmation policy | `security-readiness/17-agent-tool-governance/agent-autonomy-level-assessment.md`; `security-readiness/17-agent-tool-governance/human-confirmation-policy.md` | Partially Confirmed | Need scenario-based stress tests for multi-step agent plans | Agent Safety Lead |
| External connector/supply-chain abuse | MCP server and third-party risk readiness artifacts | `security-readiness/12-portfolio-case-studies/04-mcp-server-risk-readiness.md`; `security-readiness/17-agent-tool-governance/high-risk-tool-classification.md` | Partially Confirmed | Need signed supplier assurance checklist and onboarding gate | Third-Party Risk Owner |
| Policy bypass and weak guardrails | Policy decision log requirements and control matrix | `security-readiness/04-controls/onyx-policy-decision-log-requirements.md`; `security-readiness/04-controls/onyx-control-matrix.md` | Partially Confirmed | Need sampled policy decision records proving fail-closed outcomes | Control Engineering |
| Poor observability and weak forensic trace | Tool execution evidence log and observability path map | `security-readiness/17-agent-tool-governance/tool-execution-evidence-log.md`; `security-readiness/00-repo-audit/onyx-observability-paths.md` | Partially Confirmed | Need end-to-end trace correlation IDs validated in runtime | Observability Engineering |

## Notes
- Threat themes are used for agentic risk mapping and prioritization, not as a statement of comprehensive conformance.
