# Assessment Interview Questions

## Purpose
Collect auditable, role-based inputs for security readiness assessment.

## Interview Metadata
- Interview date:
- Interviewee name/title:
- Functional area:
- Interviewer:

## Questions by Control Area

### Governance and Ownership
1. Who owns security control decisions for the assistant?
2. Who can approve exceptions or risk acceptance?
3. How are policy updates communicated to operations teams?

### Identity and Access
4. How are user roles mapped to document access?
5. What prevents cross-client or cross-department data leakage?
6. How quickly are terminated users removed from access paths?

### Retrieval and Content Controls
7. How are source repositories classified and approved for ingestion?
8. What checks prevent unsupported answers from untrusted sources?
9. How are sensitive content classes blocked, masked, or restricted?

### Tooling and Agent Behavior
10. Which tools can autonomous or assisted workflows invoke?
11. What approval steps exist for high-impact actions?
12. What fail-closed behavior occurs when policy checks fail?

### Monitoring and Incident Response
13. Which audit events are captured for user queries and tool actions?
14. How are suspicious patterns investigated and escalated?
15. What is the mean time target for triage and containment?

### Readiness and Launch Gate
16. Which criteria must be met before launch recommendation?
17. Which unresolved findings are acceptable only with executive risk acceptance?
18. What evidence is currently missing for a complete readiness decision?

## Evidence Rating for Each Response
- **Verified**: backed by direct artifact (config, log, test, ticket).
- **Partially Confirmed**: plausible but incomplete evidence.
- **Unknown**: no reliable evidence provided.

## Evidence Limitation Language (Client-Facing)
Interview responses are treated as statements until corroborated. Uncorroborated claims are recorded as **Partially Confirmed** or **Unknown** and cannot support a positive readiness conclusion on their own.

## Launch Gate Decision Language (Client-Facing)
Interview evidence contributes to launch gate review but does not replace technical validation. Final launch recommendation depends on verified controls, remaining severity, and formal risk acceptance.
