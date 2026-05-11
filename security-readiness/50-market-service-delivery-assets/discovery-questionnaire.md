# Discovery Questionnaire (Client-Facing)

## Purpose
Collect the minimum required information to scope AI Trust & Security Readiness for RAG and autonomous agents.

## Instructions
- Provide concise and current answers.
- Mark unknown answers explicitly as "Unknown".
- Redact sensitive content and mark `[REDACTED]`.

## Section A: Business Context
1. What business outcomes must this AI assistant support?
2. What is the intended launch date and critical dependency timeline?
3. Who owns final launch-governance decisions?

## Section B: System Scope
4. What AI use cases are in scope for this engagement?
5. Which user populations will access the assistant?
6. Which environments are in scope (dev/stage/prod)?

## Section C: Data & Knowledge Sources
7. What repositories/data sources are retrieved by the assistant?
8. How is data classified (public/internal/confidential/restricted)?
9. What sensitive data types may be present (PII, finance, legal, IP)?

## Section D: Identity & Access
10. How are users authenticated and authorized?
11. How are retrieval permissions enforced at query time?
12. Are service accounts or elevated agent identities used?

## Section E: Agent Tooling & Runtime
13. What tools/actions can agents execute?
14. What guardrails exist for high-impact actions?
15. What fail-closed behavior occurs when control checks fail?

## Section F: Security Controls
16. Which controls are currently implemented and tested?
17. Are policy decisions logged with actor, action, resource, and outcome?
18. Which controls are planned but not yet validated?

## Section G: Third-Party & Supply Chain
19. Which external vendors or models are in the critical path?
20. How are third-party updates and vulnerabilities tracked?
21. What contractual/security obligations apply to providers?

## Section H: Observability & Evidence
22. What logs, traces, and audit events are available today?
23. Can evidence be mapped to code/config/test artifacts?
24. What evidence gaps are already known?

## Section I: Launch Gate Readiness
25. What criteria define Go / Conditional Go / No-Go?
26. Who accepts residual risk and by what process?
27. What remediation deadline is required for open high-severity findings?
