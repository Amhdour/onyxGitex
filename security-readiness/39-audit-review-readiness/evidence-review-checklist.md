# Evidence Review Checklist

## Purpose
Prevent unsupported launch claims by requiring verifiable, reproducible evidence for each readiness assertion.

## Blocking Rule
If any required evidence item is missing, stale, non-reproducible, or contradictory, readiness status is `Blocked`.

## Evidence Checklist

| ID | Review Criteria | Evidence Required | Reviewer | Status | Finding Severity | Remediation | Sign-off |
|---|---|---|---|---|---|---|---|
| EV-01 | Every security claim maps to source evidence. | Traceability map linking claim -> code/config/test/assumption. | Evidence Reviewer | Not Started | N/A | N/A | Pending |
| EV-02 | Test commands are recorded exactly and rerunnable. | Command history, test scripts, rerun notes. | Evidence Reviewer | Not Started | N/A | N/A | Pending |
| EV-03 | Test outputs include timestamps and result status. | Raw output excerpts or artifacts with execution date. | Evidence Reviewer | Not Started | N/A | N/A | Pending |
| EV-04 | Unknowns and partial confirmations are explicitly labeled. | Assumptions/risk docs with confidence labels. | Evidence Reviewer | Not Started | N/A | N/A | Pending |
| EV-05 | Evidence is current for the release candidate. | Artifact dates, commit SHAs, environment metadata. | Evidence Reviewer | Not Started | N/A | N/A | Pending |
| EV-06 | No secrets or sensitive raw credentials are present. | Redaction check notes, secret scan output (if used). | Evidence Reviewer | Not Started | N/A | N/A | Pending |
| EV-07 | Contradictions across artifacts are resolved or escalated. | Issue log, resolution notes, approver decision. | Evidence Reviewer | Not Started | N/A | N/A | Pending |
| EV-08 | Launch claim is blocked until all critical evidence passes. | Final checklist status with blocker IDs and owners. | Evidence Reviewer | Not Started | N/A | N/A | Pending |

## Evidence Review Sign-off
- Reviewer Name:
- Date (YYYY-MM-DD):
- Recommendation: `Ready` / `Blocked` / `Ready with Conditions`
- Blocking Items (if any):
- Sign-off:
