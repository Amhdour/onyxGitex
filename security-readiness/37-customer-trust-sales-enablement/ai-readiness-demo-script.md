# AI Readiness Demo Script

_Last updated: 2026-05-11_

## Objective
Provide a structured, honest demonstration of trust and security readiness posture without overstating guarantees.

## Audience
- Security reviewers
- Procurement stakeholders
- Technical evaluators
- Executive sponsors

## Demo Guardrails (Say Up Front)
1. This demo shows **illustrative evidence** in a controlled environment.
2. It is not a substitute for client-specific validation.
3. We do not claim guaranteed safety or zero risk.
4. Production acceptance requires environment-specific evidence.

## Demo Flow

### 1) Opening (2–3 minutes)
- Introduce the readiness framework and lifecycle.
- State the evidence model: Verified / Partially Confirmed / Unknown.
- Explain residual risk handling and governance cadence.

### 2) Access Boundary Scenario (5 minutes)
- Show two users with different entitlements.
- Attempt retrieval from restricted content.
- Explain expected behavior and observed outcome.
- Highlight logging or trace artifacts captured.

### 3) Grounding / Unsupported Answer Scenario (5 minutes)
- Ask a question with weak or missing source support.
- Show how the assistant responds under current controls.
- Explain what mitigation exists and what risk remains.

### 4) Fail-Closed Scenario (5 minutes)
- Simulate unavailable policy dependency (demo-safe simulation).
- Show deny/degrade behavior.
- Show policy-decision event artifacts if available.

### 5) Evidence Walkthrough (5 minutes)
- Walk through where evidence is stored.
- Distinguish clearly:
  - Demo artifacts (illustrative), vs
  - Client artifacts (decision-grade, environment-specific).

### 6) Residual Risk Discussion (3 minutes)
- Present top current residual risks.
- Show owners and mitigation direction.
- Confirm what remains Unknown or Partially Confirmed.

### 7) Close (2 minutes)
- Reiterate conservative posture and next-step validation plan.
- Offer client-specific evidence review session.

## Suggested Presenter Language
“We aim for evidence-backed readiness, not absolute guarantees. Today’s demo illustrates controls and failure handling. Your production decision should rely on environment-specific evidence and residual-risk acceptance.”

## Demo-to-Client Transition Checklist
Before using this demo in live deals, confirm:
- Demo statements align with latest dated evidence.
- No certification or absolute safety claims appear.
- Unknowns are visible and not re-labeled as verified.
- Client-specific follow-up path is defined.
