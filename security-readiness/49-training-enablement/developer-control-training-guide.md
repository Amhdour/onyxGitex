# Developer Control Training Guide

## Purpose
Train developers to implement and maintain secure, auditable controls for the internal knowledge assistant without introducing unsupported or unverified behavior.

## Audience
- Application developers
- Platform engineers
- Security-focused software engineers

## Learning Outcomes
Developers will be able to:
1. Explain the assistant’s control path from request to response.
2. Implement and preserve fail-closed security decisions.
3. Produce evidence-ready code and tests.
4. Execute targeted control tests and interpret failures.
5. Support incident triage with high-quality technical evidence.
6. Explain launch-gate outcomes to technical and non-technical stakeholders.

---

## 1) System Behavior Developers Must Understand

### 1.1 Request lifecycle
- Input request received with identity/session context.
- Retrieval executes against authorized corpora.
- Policy checks gate what context can reach generation.
- Response emitted with observability metadata.

### 1.2 Trust boundaries
- User interface to API boundary
- API to retrieval boundary
- Retrieval to model boundary
- Runtime to audit/logging boundary

### 1.3 Developer responsibility
- Never bypass policy checks for convenience.
- Keep enforcement paths explicit and testable.
- Ensure denial behavior is deterministic under ambiguity.

---

## 2) Core Controls and Expected Behavior

### 2.1 Authentication and authorization
- Require authenticated identity for protected operations.
- Enforce least privilege via role/group-scoped controls.

### 2.2 Retrieval authorization
- Apply auth filtering before model context assembly.
- Block context inclusion when policy decision is missing.
- Preserve denial reasons for audit (without sensitive leakage).

### 2.3 Prompt and tool safety
- Restrict tool invocation pathways to approved intents.
- Validate arguments and scope for tool actions.
- Deny risky actions lacking explicit entitlement.

### 2.4 Logging and evidence hooks
- Emit structured events for allow/deny decisions.
- Capture testable identifiers (request ID, policy ID, actor scope).
- Ensure events are queryable by reviewers.

---

## 3) Evidence-First Development Workflow

### 3.1 Build with evidence in mind
For each control change, include:
- Control intent
- Expected allow/deny behavior
- Test plan (positive + negative)
- Observability points

### 3.2 Evidence status model
- **Verified**: tests and logs confirm intended behavior.
- **Partially Confirmed**: some paths tested, others pending.
- **Unknown**: control exists conceptually but lacks proof.

### 3.3 Common anti-patterns
- Feature flags that can disable controls without guardrails
- Silent fallback from deny to allow
- Tests that only cover successful access paths

---

## 4) How to Run Developer Control Tests

### 4.1 Minimum required test set
1. Positive authorization path (allowed access)
2. Negative authorization path (denied access)
3. Missing context path (fail-closed deny)
4. Audit event generation path

### 4.2 Test execution discipline
- Start narrow (component/unit-level).
- Expand only when control dependencies require integration coverage.
- Record exact commands and outputs for evidence packaging.

### 4.3 What failures mean
- Allow when deny expected: critical control regression.
- Deny when allow expected: policy/config mismatch or logic bug.
- Missing logs: observability/audit gap, launch risk.

---

## 5) Incident Response Expectations for Developers

### 5.1 During active incident
- Assist with precise impact scoping.
- Reproduce behavior in controlled environment.
- Propose containment that is safe and reversible.

### 5.2 Post-incident corrective actions
- Add regression tests for discovered failure mode.
- Improve policy decision transparency.
- Update runbooks and evidence trail.

---

## 6) Launch Gate Interpretation (Developer View)

### GO
All critical control paths are **Verified** with reproducible tests and audit events.

### CONDITIONAL GO
Non-critical gaps remain **Partially Confirmed**, mitigation is documented, and owners/dates are assigned.

### NO-GO
Critical control behavior is failing, **Unknown**, or not evidenced.

### Developer commitments by outcome
- GO: monitor and rapidly address post-launch findings.
- CONDITIONAL GO: complete mitigation backlog within committed timeline.
- NO-GO: stop release and remediate with retest evidence.
