# Internal Company Knowledge Assistant Readiness Case Study (Onyx)

## 1) Project title
**Internal Company Knowledge Assistant — AI Trust & Security Readiness Case Study (Onyx)**

## 2) One-sentence value proposition
This project shows how to evaluate an internal RAG assistant with evidence-backed controls, tests, and launch-gate logic before any production claim.

## 3) Problem
Internal knowledge assistants can fail in ways that are not immediately visible: they may retrieve restricted content, answer without support, invoke risky tools, or operate without adequate audit traces. This case study focuses on reducing those risks through explicit controls and evidence-driven review.

## 4) Scenario: fictional Atlas Advisory Group
Atlas Advisory Group (fictional) wants to use an Onyx-based assistant for internal knowledge retrieval while preventing cross-boundary data leakage and ensuring that risky actions are governed and traceable. “Morgan Stanley style” is used here as a public inspiration pattern for rigor, not as a client relationship.

## 5) What was built
- A readiness artifact program under `security-readiness/` spanning scope, mapping, threat modeling, controls, testing, evidence, dashboarding, and governance.
- Runtime security-readiness integration documentation for retrieval and tool authorization paths.
- Evidence collection and validation scripts.
- Launch-gate logic that evaluates evidence artifacts.
- A portfolio-oriented proof package for external review.

## 6) Architecture overview
At a high level:
- **Application layer:** Onyx codebase and retrieval/tool pathways.
- **Control layer:** retrieval authorization, tool authorization, fail-closed rules, and policy decision logging requirements.
- **Testing layer:** boundary tests (RAG, citation leakage, prompt injection, tool authorization) and control verification checks.
- **Evidence layer:** structured artifacts (logs, test output, summaries, validation output).
- **Decision layer:** launch-gate scripts and residual-risk decision artifacts.
- **Presentation layer:** dashboard and final proof package.

## 7) Security risks addressed
- Unauthorized retrieval and identity boundary bypass.
- Sensitive citation leakage.
- Prompt injection influencing unsafe behavior.
- Unsafe or over-privileged tool execution.
- Missing policy/audit traces required for review.

## 8) Controls implemented
- Retrieval authorization control definitions and integration evidence.
- Tool authorization governance with runtime integration review.
- Fail-closed decision posture when required evidence or policy state is missing.
- Policy decision logging requirements and traceability artifacts.

## 9) Tests performed
Evidence in the repository includes:
- Retrieval boundary testing (multiple artifact runs).
- Citation leakage boundary testing.
- Prompt-injection boundary testing.
- Tool authorization test artifacts.
- Evidence completeness and launch-evidence validation checks.

## 10) Evidence generated
The project includes:
- `audit-events.jsonl` artifacts.
- `runtime-trace.jsonl` artifacts.
- Evidence manifests, summaries, and validation outputs.
- Final integration and claim-review documents to reduce overstatement risk.

## 11) Dashboard
A readiness dashboard exists (`security-readiness/dashboard/index.html`) with associated summary data to support control and risk review.

## 12) Launch gate result
Current posture is **NO-GO / PENDING CLOSURE for production claim**, with launch artifacts showing a conditional/not-yet-approved state until remaining gaps are closed.

## 13) Residual risks
Documented residual risks include, at minimum:
- Need for stronger evidence provenance/attestation.
- Incomplete independent secret scanning evidence in the latest pass.
- Inconsistent maturity/status tagging across some artifacts.
- Need for tighter test-failure traceability across all suites.

## 14) What is proven
- A structured, auditable readiness workflow exists and is implemented in-repo.
- Key control and evidence mechanisms are documented and evidenced (including audit and runtime trace artifacts).
- The launch decision process can remain fail-closed when evidence is insufficient.

## 15) What is not proven
- This is **not** a certification result.
- This is **not** a production deployment attestation.
- This does not prove zero residual risk.
- This does not prove complete independent assurance of every artifact’s authenticity.

## 16) How this maps to my professional identity
### Layer Retrofit
Retrofits trust/security readiness controls onto an existing AI platform instead of requiring a full rebuild.

### Secure Starter Kits
Provides reusable readiness scaffolding: control docs, testing templates, evidence scripts, and launch-gate artifacts.

### Launch Gates
Demonstrates evidence-driven go/no-go criteria with explicit fail-closed behavior for unresolved gaps.

### RAG Security
Prioritizes retrieval authorization boundaries, citation-leakage risk controls, and prompt-injection evaluations.

### Agent/Tool Governance
Covers tool-risk classification, authorization boundaries, and high-risk action governance patterns.

### Auditability
Links claims to artifacts, logs, test outputs, and status labels (Verified / Partially Confirmed / Unknown).

## 17) How a real client would use this
1. Use the phase structure to scope a readiness engagement.
2. Map their actual identity, data, and tool boundaries into the provided templates.
3. Execute targeted control tests and collect evidence via scripts.
4. Review dashboard and residual risk register with governance stakeholders.
5. Make a bounded launch decision based on evidence quality, not assumptions.

## 18) Limitations
- Evidence quality varies by phase; some areas are still Partially Confirmed.
- Not all artifacts have uniform maturity labeling yet.
- Current package demonstrates readiness engineering depth, not operational production sign-off.

## 19) Next roadmap
- Normalize a single canonical runtime wiring status source.
- Expand independent secret scanning and integrity attestation evidence.
- Improve cross-suite failure ledger traceability.
- Add stronger CI execution proof artifacts (not only design docs).
- Re-run launch gate after closure evidence is attached.

---

## Supporting references
- `security-readiness/final-proof-package/executive-summary.md`
- `security-readiness/final-integration-audit-v2.md`
- `security-readiness/final-claim-review.md`
- `security-readiness/dashboard/index.html`
