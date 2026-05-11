# Evidence Limitation Statement

> **Non-Legal Draft Notice (Required Lawyer Review):**
> This text is a draft for operational use and is **not legal advice**. Obtain legal review before external use.

## Purpose
Clarify what readiness evidence proves, what it does not prove, and how evidence confidence should be interpreted.

## Template Language
"Readiness evidence reflects observed system behavior, control configuration, and test outcomes at specific points in time, under specific conditions and assumptions.

Evidence limitations include:
1. Time-bound validity: Results may change as software, models, data, dependencies, or infrastructure change.
2. Environment dependency: Test outcomes in one environment may not fully predict outcomes in another environment.
3. Coverage constraints: Not all abuse cases, attack paths, or failure modes can be exhaustively tested.
4. Third-party opacity: Certain risks depend on upstream vendors where full internal assurance is not available.
5. Non-determinism: AI behavior variability can affect repeatability of output-level findings.

Accordingly, evidence should be interpreted as risk-informed assurance, not absolute proof of security, compliance, or operational fitness." 

## Confidence Labeling Guidance
- **Verified:** Directly observed in code, configuration, logs, or reproducible tests.
- **Partially Confirmed:** Some supporting evidence exists, but material gaps remain.
- **Unknown:** No reliable evidence currently available.

## Operational Notes
- Attach evidence dates and component versions.
- Revalidate after material changes.
- Preserve raw test output references where possible.
