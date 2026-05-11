# AI Trust One-Pager

## Purpose
This one-pager supports customer trust conversations for the internal knowledge assistant readiness program. It summarizes current **evidence-backed readiness** and known limits as of **2026-05-11**.

## What This Assistant Is
- An internal retrieval-augmented generation (RAG) assistant built on Onyx patterns.
- Designed to answer enterprise knowledge questions with controlled access boundaries and auditable operations.
- Evaluated through a structured security-readiness lifecycle in `security-readiness/`.

## Trust Positioning (Conservative)
- We do **not** claim guaranteed safety.
- We do **not** claim zero risk.
- We do **not** claim certification in this document.
- We provide **evidence-backed readiness** based on documented controls, tests, assumptions, and residual risks.

## Core Control Themes
1. **Identity and Access Boundaries**
   - Goal: users can only retrieve content they are authorized to access.
   - Status language for clients: Verified / Partially Confirmed / Unknown by control area.

2. **Grounded Responses**
   - Goal: reduce unsupported or fabricated answers by anchoring outputs to retrievable sources.
   - Evidence expectation: test cases showing citation behavior and failure modes.

3. **Policy Enforcement and Fail-Closed Behavior**
   - Goal: deny or degrade safely when required controls are unavailable or uncertain.
   - Evidence expectation: explicit policy decision logs and negative-path tests.

4. **Observability and Auditability**
   - Goal: provide traceable events for retrieval decisions, tool usage, and incidents.
   - Evidence expectation: retained logs/traces and review procedures.

## Evidence Model Used
All readiness statements should map to one or more of:
- Code/config references,
- Executed test commands and outputs,
- Explicit assumptions and confidence levels,
- Residual risk statements with owners.

## What Customers Should Expect
- Transparent discussion of confirmed controls and open gaps.
- A distinction between:
  - **Demo evidence** (illustrative, controlled environment), and
  - **Client evidence** (customer-relevant control proofs and outputs).
- Ongoing readiness updates rather than one-time assurances.

## Current Risk Posture (Client-Safe Summary)
- Certain risks can be reduced but not eliminated (e.g., retrieval leakage attempts, prompt abuse, operational drift).
- Residual risk is tracked and managed with owners and review cadence.
- Launch decisions should be tied to evidence acceptance criteria, not marketing claims.

## Customer Conversation Close
If needed, we can provide:
- Security FAQ,
- Client Evidence Summary,
- Buyer Objection Handling Sheet,
- Trust Center content draft,
- Demo walkthrough script,
- Client-facing risk summary.
