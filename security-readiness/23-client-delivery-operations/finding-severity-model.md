# Finding Severity Model

## Purpose
Provide consistent severity ratings for readiness findings across diverse client sectors.

## Severity Levels

### Critical
A control failure with immediate, high-likelihood impact (e.g., unauthorized access to highly sensitive records across trust boundaries).
- Typical expectation: immediate containment and executive escalation.

### High
A significant weakness that can materially affect confidentiality, integrity, or availability if exploited.
- Typical expectation: remediation plan before launch or explicit executive risk acceptance.

### Medium
A control gap that increases risk but is less likely to cause severe near-term harm alone.
- Typical expectation: scheduled remediation with tracked owner and due date.

### Low
A minor control or process weakness with limited standalone impact.
- Typical expectation: remediation in normal improvement cycle.

### Informational
Observation that improves clarity, consistency, or auditability without representing an immediate control failure.

## Rating Factors
Score each finding using:
- Business impact (service, legal, safety, financial, reputational)
- Data sensitivity affected
- Exploitability and required attacker capability
- Existing compensating controls
- Detection likelihood and response readiness

## Sector Examples
- Legal: matter-level access leakage -> High/Critical depending on exposed content.
- School: student data overexposure to unauthorized staff -> High/Critical.
- Clinic: patient record boundary failure -> Critical.
- Agency/Consulting: cross-client document retrieval -> High/Critical.
- Engineering Office: restricted design/IP leak -> High.

## Evidence Limitation Language (Client-Facing)
Severity is assigned from evidence available at assessment time. If evidence is incomplete, severity may be provisional and updated when additional artifacts or test results are obtained.

## Launch Gate Decision Language (Client-Facing)
Open Critical findings generally indicate **No-Go**. Open High findings require documented mitigation or explicit risk acceptance by designated decision owners before any **Go with Risk Acceptance** outcome.
