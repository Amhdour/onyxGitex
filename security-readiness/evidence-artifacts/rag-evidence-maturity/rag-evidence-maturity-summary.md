# RAG Evidence Maturity Summary

Date (UTC): 2026-05-12

This summary provides a client/interview-friendly view of control evidence maturity tiers for the internal RAG assistant readiness program.

## Tier Scale

- **Tier 0 — Documentation only**
- **Tier 1 — Control code exists**
- **Tier 2 — Dependency-light tests pass**
- **Tier 3 — Runtime-adjacent tests pass**
- **Tier 4 — Full backend/runtime tests pass**
- **Tier 5 — Client-specific production evidence exists**

## Control Classification

| Control | Tier achieved | Current status | Evidence file | What is still missing | Launch gate impact |
|---|---:|---|---|---|---|
| RetrievalAuthorizationGuard | Tier 3 | Runtime-adjacent retrieval-path evidence PASS; full runtime verification blocked | `security-readiness/final-control-status-canonical.md` | Full backend/runtime retrieval authorization PASS artifact in supported environment | Blocks GO; core fail-closed retrieval evidence is incomplete |
| RetrievalGuardAdapter | Tier 3 | Retrieval adapter/path evidence PASS; runtime-complete path still blocked | `security-readiness/evidence-artifacts/test-results/runtime-adjacent-retrieval-guard-tests.json`; `security-readiness/evidence-artifacts/test-results/retrieval-path-coverage-tests.json` | Full runtime integration PASS proving adapter behavior in backend execution | Partial confidence only; cannot unblock GO |
| BypassACLContract | Tier 2 | Dependency-light bypass ACL evidence PASS | `security-readiness/evidence-artifacts/test-results/bypass-acl-contract-tests.json`; `security-readiness/evidence-artifacts/bypass-acl-contract/dependency-light-evidence-summary.md` | Runtime-adjacent and full runtime ACL bypass proof across live retrieval flows | Partial confidence only; remains under NOT_ENOUGH_EVIDENCE |
| TrustedSystemContextInputBoundary | Tier 2 | Schema-boundary dependency-light evidence PASS | `security-readiness/evidence-artifacts/test-results/trusted-system-context-input-tests.json`; `security-readiness/evidence-artifacts/trusted-system-context-input/schema-injection-evidence-summary.md` | Runtime invocation evidence showing same boundary in live runtime prompt construction | Partial confidence only; does not satisfy runtime gating |
| CitationSourceLeakageFilter | Tier 2 | Citation/source leakage dependency-light evidence PASS | `security-readiness/evidence-artifacts/test-results/citation-source-leakage-tests.json`; `security-readiness/evidence-artifacts/citation-source-leakage/evidence-summary.md` | Full runtime citation leakage PASS with backend retrieval and citation pipeline | GO remains blocked until runtime citation leakage evidence passes |
| PromptInjectionBoundary | Tier 2 | Prompt-injection boundary dependency-light evidence PASS | `security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json` | Full runtime prompt-injection + red-team PASS in supported backend runtime | GO remains blocked until runtime prompt-injection evidence passes |
| ToolAuthorizationRouter | Tier 1 | Control implementation exists; runtime enforcement path incomplete/blocked | `security-readiness/final-control-status-canonical.md` | Main chat runtime wiring (`authorization_router`, `user_id`, `tool_policy`) + passing runtime tests | Critical for tool-misuse boundary; current gap contributes to NOT_ENOUGH_EVIDENCE |
| AuditLogger | Tier 3 | Runtime-adjacent evidence PASS; broader end-to-end runtime proof still incomplete | `security-readiness/evidence-artifacts/audit-logging-001/evidence-summary.md` | Additional full runtime runs proving reliable on-demand audit event generation | Supports traceability, but does not overcome blocked critical controls |
| RuntimeTracer | Tier 3 | Runtime-adjacent evidence PASS; full backend runtime trace coverage incomplete | `security-readiness/final-control-status-canonical.md` | Full runtime retrieval/tool trace PASS evidence in supported environment | Improves observability confidence; GO still blocked by control evidence gaps |
| LaunchGateEngine | Tier 3 | Launch-gate logic executes and returns NOT_ENOUGH_EVIDENCE | `security-readiness/evidence-artifacts/launch-gate/launch-gate-result.json`; `security-readiness/evidence-artifacts/launch-gate/launch-gate-summary.md` | Upstream required runtime evidence to allow transition from NOT_ENOUGH_EVIDENCE | Correctly fail-closed; must remain NOT_ENOUGH_EVIDENCE until blockers are closed |

## Overall Maturity Readout

- Highest currently supported maturity across critical RAG controls: **Tier 3 (runtime-adjacent)**.
- Critical controls still missing Tier 4 full backend/runtime PASS evidence.
- Launch decision remains **NOT_ENOUGH_EVIDENCE** and must not be promoted to GO.
