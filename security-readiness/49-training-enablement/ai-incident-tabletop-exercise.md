# AI Incident Tabletop Exercise

## Purpose
Run a structured tabletop exercise to train teams on coordinated response to internal knowledge assistant security incidents.

## Scenario
A user reports receiving an answer that appears to summarize a restricted document from another business unit.

## Objectives
- Validate detection, escalation, and containment speed.
- Test role clarity across admin, developer, and security functions.
- Verify evidence preservation and decision logging quality.
- Assess readiness to make GO / CONDITIONAL GO / NO-GO updates post-incident.

---

## 1) Participants and Roles
- Incident Commander: owns timeline and decisions.
- Client Admin Lead: access controls and connector containment.
- Developer Lead: technical triage and reproducibility.
- Security Reviewer: control assurance and risk determination.
- Communications Lead: stakeholder and leadership updates.

---

## 2) Exercise Timeline (90 minutes)

### Phase A: Detection (0-20 min)
Inject: Reported cross-boundary content exposure.

Expected actions:
- Open incident record.
- Preserve relevant logs and request identifiers.
- Classify initial severity.

### Phase B: Containment (20-45 min)
Inject: Additional suspicious responses appear.

Expected actions:
- Apply temporary restrictive controls (source disable, stricter policy).
- Verify fail-closed behavior for ambiguous requests.
- Notify impacted governance stakeholders.

### Phase C: Investigation (45-70 min)
Inject: Preliminary evidence suggests auth filter inconsistency.

Expected actions:
- Reproduce issue with controlled test identities.
- Determine blast radius and affected sources.
- Document verified vs unknown findings.

### Phase D: Decision & Recovery (70-90 min)
Inject: Team must recommend launch-gate status.

Expected actions:
- Present evidence summary.
- Propose GO / CONDITIONAL GO / NO-GO with rationale.
- Define remediation, owners, and due dates.

---

## 3) Evaluation Criteria
- Time to containment
- Quality of evidence captured
- Accuracy of confidence labeling (Verified/Partially Confirmed/Unknown)
- Clarity of launch-gate recommendation
- Completeness of follow-up tasks

---

## 4) Facilitator Debrief Questions
1. Which controls worked as intended?
2. Where did process or ownership ambiguity slow response?
3. What evidence was missing at key decisions?
4. What would force a NO-GO outcome?
5. What changes are required before next exercise?

---

## 5) Deliverables
- Incident timeline with key decision points
- Evidence register (commands, logs, artifacts)
- Residual risk list with owners
- Updated launch-gate recommendation and acceptance criteria
