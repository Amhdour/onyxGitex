# Discovery Call Script

## Purpose
Guide the first structured conversation with client stakeholders to establish scope, constraints, risks, and delivery expectations.

## Opening (5 minutes)
"Thank you for joining. Today we will confirm your goals, systems in scope, data risks, timeline, and decision process for readiness and launch gate outcomes."

## Agenda
1. Business goals and use cases
2. Data and user access boundaries
3. Current controls and known gaps
4. Evidence availability and testing logistics
5. Timeline and launch gate process

## Core Questions
- What business decisions depend on this assistant (advisory only vs. operational action)?
- Which users will access it first (internal staff, students, clinicians, counsel, project teams)?
- What data must never be exposed across users or departments?
- What are the highest-impact failure scenarios for your organization?
- Which controls are already implemented versus planned?
- What evidence can you provide now (logs, configs, policies, tickets)?

## Sector-Specific Probes
- Legal: matter-level confidentiality boundaries and ethical wall requirements.
- School: student privacy controls, role separation, and parent/guardian access constraints.
- Clinic: care-team minimum access, PHI handling, and escalation duty model.
- Agency/Consulting: client-to-client separation and project partitioning.
- Engineering Office: design/IP segregation and vendor collaboration boundaries.

## Close-Out Prompts
- "Which unresolved risks would block launch for your leadership?"
- "Who has authority to accept residual risk at launch gate?"
- "What evidence is missing today that we must gather before recommendation?"

## Evidence Limitation Language (Client-Facing)
Discussion outputs are planning inputs and do not, by themselves, validate technical control effectiveness. Validation requires review of configurations, logs, tests, and operating records.

## Launch Gate Decision Language (Client-Facing)
This call does not determine launch readiness. Launch gate recommendations are made later using verified evidence, open findings, and documented risk acceptance decisions.
