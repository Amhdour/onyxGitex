# Client Admin Training Guide

## Purpose
This guide trains client administrators to safely operate the internal knowledge assistant in an enterprise setting. It focuses on practical operations, security controls, and evidence-aware decision making.

## Audience
- Platform or workspace administrators
- Knowledge base owners
- Support leads with user and access responsibilities

## Learning Outcomes
By the end of this guide, a client admin should be able to:
1. Explain how the assistant processes user questions and retrieves data.
2. Configure and validate identity-aware access controls.
3. Recognize approved evidence for readiness and launch decisions.
4. Execute core verification checks and document outcomes.
5. Follow incident response pathways and escalation rules.
6. Interpret launch-gate decisions: **GO**, **CONDITIONAL GO**, and **NO-GO**.

---

## 1) How the Internal Knowledge Assistant Works

### 1.1 High-level flow
1. A user asks a question through approved interfaces.
2. Identity and session context are attached to the request.
3. Retrieval fetches candidate documents from connected sources.
4. Authorization filters ensure the user only sees permitted content.
5. The model composes a response based on retrieved context and policy.
6. Logging and telemetry capture auditable events for review.

### 1.2 What admins must monitor
- Data source sync health and freshness
- User/group mapping integrity
- Retrieval authorization enforcement outcomes
- Error rates and blocked-action events
- Audit log completeness and retention

---

## 2) Controls Every Client Admin Must Understand

### 2.1 Access and identity controls
- SSO/MFA integration for trusted identity
- Role-based and group-based access boundaries
- Joiner/mover/leaver procedures for access lifecycle

### 2.2 Retrieval authorization controls
- Per-document or source-level permission checks
- Deny-by-default for unknown identity context
- Fail-closed behavior when policy or identity signals are missing

### 2.3 Data protection controls
- Source-level inclusion/exclusion policies
- Sensitive content handling and redaction rules
- Restricted connector setup and approval steps

### 2.4 Auditability controls
- Request-level policy decision logging
- User action traceability (who asked what, when, outcome)
- Evidence artifacts for launch-gate review

---

## 3) Reviewing Evidence as an Admin

Use this three-state evidence rubric:
- **Verified**: Directly observed in logs, test output, config, or code references.
- **Partially Confirmed**: Some evidence exists, but coverage is incomplete.
- **Unknown**: No reliable evidence is currently available.

### 3.1 Evidence checklist
- Latest test run commands and results
- Control coverage map (access, retrieval, audit, incident)
- Known gaps and ownership assignments
- Timestamped artifacts and reviewer sign-off

### 3.2 Common evidence mistakes to avoid
- Treating assumptions as test outcomes
- Accepting screenshots without reproducible commands
- Ignoring failed negative tests (denials must be tested)

---

## 4) How to Run Core Admin Tests

### 4.1 Access boundary validation
- Test with two users from different permission groups.
- Ask for protected content with each user.
- Confirm allowed user receives scoped answers and denied user is blocked.

### 4.2 Fail-closed validation
- Temporarily remove or invalidate policy signal in a test environment.
- Confirm request is denied, not silently allowed.

### 4.3 Audit log validation
- Perform representative user actions.
- Confirm logs capture actor, action, resource scope, and policy outcome.

### 4.4 Recording results
For each test record:
- Command or procedure
- Expected result
- Actual result
- Evidence location
- Status (Verified / Partially Confirmed / Unknown)

---

## 5) Incident Response for Client Admins

### 5.1 Trigger conditions
- Possible unauthorized document exposure
- Unexpected policy bypass behavior
- Suspicious spikes in denied/allowed patterns

### 5.2 Initial response (first 30 minutes)
1. Contain: disable impacted connector, workflow, or tenant scope as needed.
2. Preserve evidence: retain logs, event IDs, and timeline.
3. Notify: security, platform owner, and incident commander.
4. Classify: data sensitivity and affected populations.

### 5.3 Stabilization
- Apply temporary restrictive controls.
- Verify compensating controls.
- Begin scoped retest before reopening access.

---

## 6) Interpreting Launch Gate Results

### GO
Use when critical controls are **Verified**, residual risk is acceptable, and evidence is complete.

### CONDITIONAL GO
Use when no critical blockers exist, but specific gaps are **Partially Confirmed** with time-bound remediation owners.

### NO-GO
Use when critical controls are **Unknown**, failing, or evidence is insufficient for safe operation.

### Admin action by outcome
- GO: proceed with monitored rollout.
- CONDITIONAL GO: proceed only with documented restrictions and deadlines.
- NO-GO: halt launch and escalate remediation plan.

---

## 7) Quick Start Checklist
- [ ] Confirm admin account and role scope.
- [ ] Validate identity provider and group mappings.
- [ ] Run access boundary tests.
- [ ] Validate fail-closed behavior.
- [ ] Check audit evidence completeness.
- [ ] Review launch-gate status and required actions.
