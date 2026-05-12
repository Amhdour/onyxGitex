# Control Test Plan

**Organization:** Atlas Advisory Group (Fictional)  
**Program:** Internal Company Knowledge Assistant ("Morgan Stanley style")  
**Artifact Owner:** AI Trust & Security Readiness Engineer  
**Draft Date:** 2026-05-11  
**Document Status:** Draft (Readiness Documentation Phase)

## Primary Launch Question
Can Atlas Advisory Group safely launch an internal knowledge assistant without leaking private documents or giving unsupported answers?

## Evidence Status
- **Not Collected:** Runtime production telemetry, red-team execution logs, and live policy decision logs.
- **Pending:** Control test execution in staging, dashboard wiring, and launch-gate sign-offs.
- **Collected:** Repository audit artifacts under `security-readiness/00-repo-audit/` and scoped planning documentation.
- **Verified:** Only items explicitly traceable to repository files and static architecture assumptions.

## Current Assurance View
- **Verified:** Documentation scope and repository audit references are present.
- **Partially Confirmed:** Design-time controls are defined but not execution-verified.
- **Unknown:** Runtime effectiveness, false positive/negative rates, and incident response timing.

## Key Inputs
- `security-readiness/00-repo-audit/phase-1-findings.md`
- `security-readiness/00-repo-audit/onyx-auth-access-paths.md`
- `security-readiness/00-repo-audit/onyx-retrieval-paths.md`
- `security-readiness/00-repo-audit/onyx-observability-paths.md`
- `security-readiness/00-repo-audit/onyx-tool-mcp-paths.md`

## Content
- Draft deliverable populated for Priority 1 with Atlas-specific readiness context.
- Includes explicit statuses (Not Collected/Pending/Collected/Verified), assumptions, and unresolved unknowns.
- References repository-audit artifacts for available evidence; avoids unsupported implementation claims.
- Maintains launch posture as **Draft / Not Yet Approved** until runtime evidence is attached.

## Open Unknowns
1. Unknown: Whether department-level authorization is fail-closed for all retrieval paths in runtime.
2. Unknown: Whether unsupported-answer suppression consistently triggers under adversarial prompts.
3. Unknown: Whether audit evidence can be generated on-demand for launch-gate review.

## Next Evidence Step
Run scoped control and abuse-case tests defined in `security-readiness/08-testing/` and attach command output before any launch approval.

## Control Test Addendum — Citation Boundary 001 (2026-05-12)

- **Control Objective:** Verify unauthorized documents are never exposed through citation structures (title, URL/path, snippet, metadata, source IDs/references) and that authorized citations remain available.
- **Test Implementation:** `test_citation_leakage_boundary_controls` in `backend/tests/unit/onyx/security_readiness/test_control_layer.py`.
- **Evidence Artifact Folder:** `security-readiness/evidence-artifacts/citation-boundary-001/`.
- **Requested Cases Covered:**
  1. Unauthorized document title not shown.
  2. Unauthorized document URL/path not shown.
  3. Unauthorized snippet not shown.
  4. Unauthorized metadata not shown.
  5. Unauthorized document not cited as source.
  6. Authorized document cited normally.
  7. Prompt injection cannot force hidden sources.
  8. Refusal text does not reveal restricted document names.
- **Dataset/Sensitivity Handling:** Uses fictional documents and redacted restricted values only.
- **Current Verification State:** **Partially Confirmed** (test exists; runtime execution blocked by missing dependency `fastapi_users` in this environment).
