# Misuse Impact Assessment

**Priority:** 18 — Business & Use-Case Risk  
**Use Case:** Internal Company Knowledge Assistant  
**Date:** 2026-05-11

## 1) Misuse Paths

Representative misuse paths:

1. **Prompt-based exfiltration attempts** against retrieval boundaries.
2. **Role/identity confusion exploits** to access higher-privilege context.
3. **Tool misuse attempts** to trigger unauthorized operational actions.
4. **Instruction laundering** through uploaded/internal content.
5. **Confidence spoofing** where users are persuaded by fluent but unsupported output.

## 2) Business and User Impact

- Exposure of sensitive internal information.
- Incorrect operational actions from manipulated outputs.
- Increased incident response burden and trust degradation.
- Potential cascading impact when misuse is automated at scale.

## 3) Likelihood and Severity (Qualitative)

- Exfiltration probing: Likelihood Medium-High, Severity High.
- Tool abuse attempts: Likelihood Medium, Severity High.
- Instruction laundering: Likelihood Medium, Severity Medium-High.
- Confidence spoofing: Likelihood High, Severity Medium-High.

## 4) Control Expectations

- Strong retrieval authorization checks and deny-by-default behavior.
- Role-bound context assembly with strict identity verification.
- Tool policy layer with explicit allowlists and runtime checks.
- Abuse telemetry, anomaly detection, and rapid response playbooks.

## 5) Launch Conditions

- Abuse-case tests show effective block/contain outcomes for priority misuse paths.
- Tool actions are attributable, reversible where feasible, and audited.
- Incident runbooks include misuse-specific triage and containment.

## 6) No-Go Conditions

- Demonstrated bypass of core authorization controls.
- Ability to invoke sensitive tools through prompt-only manipulation.
- Missing telemetry for high-risk misuse detection.

## 7) Residual Risk

Residual misuse risk is **Medium-High** and **Partially Confirmed**, with uncertainty concentrated in novel prompt strategies and dependency-level weaknesses.
