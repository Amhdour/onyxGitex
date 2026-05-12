# Internal Company Knowledge Assistant Case Study (Public Portfolio)

## 1) Project title
**Onyx Internal Company Knowledge Assistant: AI Trust & Security Readiness Case Study**

## 2) One-sentence value proposition
An evidence-first readiness program that helps organizations evaluate whether an internal RAG assistant should launch, using explicit controls, tests, and auditable decision criteria.

## 3) Problem
Enterprises adopting internal AI assistants face a recurring issue: useful retrieval and automation features can outpace security governance. Without explicit controls and verifiable evidence, launch decisions may rely on assumptions rather than proof.

## 4) Scenario: fictional Atlas Advisory Group
This case uses **Atlas Advisory Group** (fictional) as a realistic internal deployment scenario. The objective was to assess whether an Onyx-based assistant could meet launch-readiness expectations in a “Morgan Stanley style” control rigor pattern (reference only; no affiliation or client relationship claimed).

## 5) What was built
- A phase-based readiness workspace under `security-readiness/`.
- Threat, abuse-case, and boundary-control documentation.
- Retrieval and tool governance readiness artifacts.
- Evidence collection/validation automation scripts.
- Dashboard and launch-gate support artifacts.
- Final proof package and claim-review documentation.

## 6) Architecture overview
The case study implements a five-part readiness model:
1. **System & Risk Mapping:** scope, data flow, trust boundaries, and threat models.
2. **Control Definition:** retrieval authorization, tool authorization, fail-closed rules, policy logging requirements.
3. **Verification:** control-oriented and abuse-case testing with artifact capture.
4. **Evidence Operations:** standardized evidence generation and validation scripts.
5. **Decision & Governance:** dashboard views, residual risk handling, and launch-gate outcome tracking.

## 7) Security risks addressed
- Cross-boundary document retrieval.
- Unsupported answers and citation leakage risk.
- Prompt-injection driven policy bypass risk.
- Over-privileged or unsafe tool/action execution.
- Missing audit events and runtime trace coverage.

## 8) Controls implemented
- Retrieval authorization guard integration artifacts.
- Tool authorization and high-risk tool governance artifacts.
- Fail-closed launch/decision patterns.
- Policy decision logging requirements and traceability expectations.

## 9) Tests performed
Repository evidence includes:
- RAG boundary tests with artifact sets.
- Citation boundary/leakage tests.
- Prompt injection boundary tests.
- Tool authorization evidence runs.
- Launch evidence and completeness validation scripts/checks.

## 10) Evidence generated
- Runtime artifacts: `audit-events.jsonl`, `runtime-trace.jsonl`.
- Evidence manifests and summary artifacts.
- Final integration review and overclaim review documents.
- Launch-gate evidence artifacts.

## 11) Dashboard
A web dashboard in `security-readiness/dashboard/` provides a portfolio-level view of readiness status and supporting summaries.

## 12) Launch gate result
As of **2026-05-12 (UTC)**, the documented production-claim posture is **NO-GO / PENDING CLOSURE** pending closure of specified residual gaps.

## 13) Residual risks
Examples documented in final audit artifacts:
- Evidence authenticity/provenance attestation is incomplete.
- Independent secret-scanning evidence depth remains partial in latest pass.
- Some status normalization work remains across final artifacts.
- Cross-suite failed-test traceability requires consolidation.

## 14) What is proven
- A reproducible readiness framework and workflow exist in the repository.
- Multiple control areas have concrete evidence artifacts.
- The program demonstrates a conservative, fail-closed launch posture when evidence is incomplete.

## 15) What is not proven
- No certification is claimed.
- No production deployment claim is made.
- No guarantee of zero risk is claimed.
- Full independent assurance completeness is not claimed.

## 16) Professional identity mapping
- **Layer Retrofit:** demonstrates security-readiness retrofit on an existing AI platform.
- **Secure Starter Kits:** provides reusable templates, scripts, and artifacts for repeatable engagements.
- **Launch Gates:** operationalizes evidence-based launch decisions.
- **RAG Security:** centers retrieval authorization and leakage risk handling.
- **Agent/Tool Governance:** frames autonomy and tool-risk boundaries.
- **Auditability:** ties assertions to evidence artifacts and explicit confidence labels.

## 17) How a real client would use this
- Start with the scope and mapping structure.
- Tailor controls and risk classifications to their environment.
- Execute bounded tests and collect evidence artifacts.
- Review dashboard plus residual risks with governance stakeholders.
- Decide launch posture using documented evidence thresholds.

## 18) Limitations
- This is a readiness case study, not an operational security certification.
- Some evidence areas are intentionally marked Partially Confirmed/Unknown.
- Final operational assurance requires client-specific environment execution and governance approvals.

## 19) Next roadmap
- Unify canonical status references for key runtime control wiring.
- Add stronger evidence integrity attestation procedures.
- Expand independent security scanning records.
- Increase CI/runtime linkage evidence for control enforcement.
- Reassess launch gate after closure of priority gaps.
