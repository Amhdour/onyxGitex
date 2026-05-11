# Independent Control Review Checklist

## Purpose
Provide an independent, evidence-based control review workflow before launch-gate decisions.

## Use Criteria
Use this checklist only after control owners publish their latest evidence set for the target release candidate.

## Review Rules
1. Reviewers must be independent of first-line control implementation.
2. Every checklist result must cite evidence artifacts (code/config/test output/assumption).
3. Any control without sufficient evidence is marked `Unknown` or `Partially Confirmed`.
4. No `Ready` recommendation is allowed while unresolved high-severity gaps remain.

## Checklist

| ID | Control Review Item | Evidence Required | Status (`Verified` / `Partially Confirmed` / `Unknown` / `Not Effective`) | Reviewer Notes | Follow-up Owner | Due Date |
|---|---|---|---|---|---|---|
| ICR-01 | Control objective is clearly defined. | Control description, scope statement. |  |  |  |  |
| ICR-02 | Control implementation exists in system artifacts. | Code/config reference links and commit SHA. |  |  |  |  |
| ICR-03 | Control test coverage exists and is relevant. | Test cases, commands, outputs, timestamps. |  |  |  |  |
| ICR-04 | Control behavior is fail-closed when enforcement is uncertain. | Runtime/policy behavior evidence. |  |  |  |  |
| ICR-05 | Control is mapped to trust boundary and data classification risk. | Threat model and data-flow references. |  |  |  |  |
| ICR-06 | Policy decisions are logged and auditable. | Audit event schema/log samples. |  |  |  |  |
| ICR-07 | Known limitations and assumptions are documented. | Assumption log with confidence labels. |  |  |  |  |
| ICR-08 | Residual risk and owner acceptance are documented. | Risk register entry and owner acceptance note. |  |  |  |  |

## Reviewer Attestation
- Reviewer Name:
- Reviewer Function (Second Line / Internal Audit / External):
- Date (YYYY-MM-DD):
- Recommendation: `Ready` / `Blocked` / `Ready with Conditions`
- Blocking Findings:
- Signature:
