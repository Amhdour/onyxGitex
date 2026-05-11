# Build Priority 22 — Escalation Rules

Date: 2026-05-11
Status: Proposed

## Escalation Triggers
1. **Sensitive-data response risk** where policy alignment is uncertain.
2. **High/Critical tool action** lacking required evidence or reviewer consensus.
3. **Unresolved evidence gaps** at launch gate decision time.
4. **Critical findings** from testing, red teaming, or runtime incidents.
5. **Conflicting reviewer decisions** with material security impact.

## Escalation Path
1. Primary Reviewer marks decision as **Escalated**.
2. Notify Security Reviewer + Launch Gate Approver.
3. For production-affecting urgency, notify Incident Commander.
4. Freeze relevant release/action until disposition is logged.
5. Record final adjudication, owner, and due dates.

## Required Escalation Artifacts
- Summary of disputed/unknown evidence.
- Impact statement (confidentiality, integrity, availability, compliance).
- Proposed containment action.
- Final adjudicator identity and rationale.

## SLA Targets (Policy)
- Critical: acknowledge within 1 hour, disposition within 24 hours.
- High: acknowledge within 4 hours, disposition within 2 business days.
- Moderate: disposition within 5 business days.

## Fail-Closed Rule
If escalation is open and impacts launch criteria, launch is blocked until explicit recorded override or risk acceptance decision.
