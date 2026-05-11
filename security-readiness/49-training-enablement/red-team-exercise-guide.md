# Red-Team Exercise Guide

## Purpose
Provide a practical guide for adversarial testing of the internal knowledge assistant, focused on realistic abuse paths and measurable control effectiveness.

## Goals
- Identify exploitable gaps in retrieval, authorization, and tool pathways.
- Validate defense-in-depth controls under adversarial pressure.
- Produce evidence suitable for launch-gate and governance review.

---

## 1) Rules of Engagement
- Test only approved environments and scopes.
- Use sanitized/redacted data.
- Document all prompts, tool actions, and observed outcomes.
- Stop testing and escalate immediately if real sensitive exposure is detected.

---

## 2) Threat Themes to Exercise
1. Cross-tenant or cross-group data access attempts
2. Prompt manipulation to override policy intent
3. Tool misuse for unauthorized actions
4. Citation laundering or unsupported-answer generation
5. Control degradation scenarios (missing context/policy signals)

---

## 3) Exercise Design

### 3.1 Pre-brief checklist
- Defined success/failure criteria
- Approved test identities and role profiles
- Logging and tracing enabled
- Incident escalation channel confirmed

### 3.2 Attack execution model
For each attack path:
- Hypothesis
- Test steps
- Expected control behavior (allow/deny)
- Observed behavior
- Evidence references
- Severity and exploitability

### 3.3 Evidence classification
- **Verified control**: attack blocked with traceable logs.
- **Partially Confirmed**: mixed results or incomplete telemetry.
- **Unknown**: no trustworthy evidence of behavior.

---

## 4) Example Exercise Cases
- Attempt to retrieve documents from unauthorized business unit.
- Attempt to induce model to ignore role boundaries.
- Attempt high-risk tool action without entitlement.
- Attempt repeated probing with varied phrasing to evade detection.

---

## 5) Post-Exercise Reporting
Include:
- Executive summary of top risks
- Detailed findings by control family
- Reproduction steps and artifacts
- Recommended remediation and target dates
- Proposed launch-gate impact (GO / CONDITIONAL GO / NO-GO)

---

## 6) Mapping Results to Launch Gate
- GO: no critical exploitable paths and strong evidence coverage.
- CONDITIONAL GO: medium-risk findings with compensating controls and deadlines.
- NO-GO: critical exploitable paths or unacceptable unknowns.
