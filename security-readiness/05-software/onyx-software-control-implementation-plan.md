# Software Control Implementation Plan

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
