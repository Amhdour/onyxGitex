# Buyer Objection Handling Sheet

_Last updated: 2026-05-11_

## Guidance
Use factual, conservative responses. Do not over-claim. Route deep technical objections to security and engineering reviewers with evidence artifacts.

## Objection 1: “AI can’t be trusted with internal documents.”
**Response:**
That risk is valid and recognized. Our approach is evidence-backed readiness: authorization controls, abuse-case testing, auditability, and explicit residual risk tracking. We do not claim zero risk.

## Objection 2: “How do I know users won’t retrieve data they shouldn’t?”
**Response:**
We evaluate retrieval authorization boundaries and document results as Verified, Partially Confirmed, or Unknown. We can provide environment-specific evidence and gaps.

## Objection 3: “Your chatbot might hallucinate policies or numbers.”
**Response:**
Unsupported outputs are a known model risk. We mitigate through source grounding patterns, control testing, and user guidance; we also track failure modes and escalation paths.

## Objection 4: “If policy checks fail, does the system still answer?”
**Response:**
Target posture is fail-closed or safe degradation with policy-decision logging. We provide evidence of observed behavior where available.

## Objection 5: “Show me proof, not promises.”
**Response:**
Agreed. We provide control evidence, test commands and outputs, assumptions, and residual risks. Claims are tied to dated artifacts.

## Objection 6: “Are you certified?”
**Response:**
We do not make certification claims in these materials. We can share control mappings and governance artifacts to support your review process.

## Objection 7: “Can this satisfy our procurement security review?”
**Response:**
Often yes, with the right evidence package and scope alignment. Final determination depends on your requirements, data classification, and accepted residual risk.

## Red Flags (Do Not Say)
- “Guaranteed safe.”
- “No chance of data exposure.”
- “Fully compliant out of the box.”
- “Certified” (unless separately and formally validated).

## Escalation Triggers
Escalate to security/engineering when buyer requests:
- Detailed threat model artifacts,
- Pen-test or red-team evidence,
- Control-by-control verification status,
- Data residency or legal commitments.
