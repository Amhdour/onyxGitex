# User Harm Analysis

**Priority:** 18 — Business & Use-Case Risk  
**Use Case:** Internal Company Knowledge Assistant  
**Date:** 2026-05-11

## 1) User Groups

- Employees seeking policy/procedure guidance.
- Operators and responders under time pressure.
- New hires with limited domain context.
- Administrative users configuring access and tools.

## 2) Harm Types

Potential harms to users include:

- **Informational harm:** Incorrect or unsupported answers causing bad decisions.
- **Privacy/confidentiality harm:** Users exposed to data outside their authorization boundary.
- **Workload harm:** Extra remediation effort caused by misleading assistant output.
- **Psychological/trust harm:** Confusion or reduced trust from inconsistent behavior.
- **Career/organizational harm:** Performance or accountability impact from following wrong guidance.

## 3) High-Risk Scenarios

- User follows incorrect incident steps, extending outage scope.
- User receives over-broad retrieval results containing sensitive content.
- User mistakes generated text for approved policy despite uncertainty.
- User relies on stale runbook guidance during critical events.

## 4) Misuse-Amplified Harm

- Prompt manipulation to elicit hidden or restricted content.
- Social engineering via authoritative-seeming generated answers.
- Tool invocation abuse that creates downstream user impact.

## 5) Mitigation Expectations

- Clear provenance/citation and confidence indicators.
- Hard refusals for unauthorized or high-risk requests.
- Human review requirement for critical decisions.
- Rapid feedback/report path for harmful outputs.
- Training guidance on assistant limitations.

## 6) Launch Conditions

- Harm reporting workflow is operational and owned.
- Safety guardrails for known harmful scenarios are verified.
- User-facing messaging clearly states decision-support limitations.

## 7) No-Go Conditions

- Known harmful output classes remain unmitigated.
- Users cannot distinguish grounded content from generated inference.
- No reliable process exists to quarantine risky behaviors quickly.

## 8) Residual Risk

Residual user-harm risk is **Medium** and **Partially Confirmed** due to uncertainty in long-tail prompt behavior and evolving misuse patterns.
