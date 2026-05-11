# Security Reviewer Training Guide

## Purpose
Prepare security reviewers to assess whether the internal knowledge assistant meets trust, control, and evidence standards for launch decisions.

## Audience
- Security engineers
- AI risk and governance reviewers
- Internal audit or assurance contributors

## Learning Outcomes
Reviewers will be able to:
1. Evaluate system behavior against security objectives.
2. Validate that controls are enforced and not merely documented.
3. Determine evidence quality and confidence levels.
4. Challenge weak assumptions and unsupported claims.
5. Guide incident-response readiness reviews.
6. Drive defensible GO / CONDITIONAL GO / NO-GO recommendations.

---

## 1) How the Assistant Works (Reviewer Lens)

### 1.1 Security-critical flow checkpoints
- Identity establishment
- Retrieval authorization
- Context assembly controls
- Model/tool guardrails
- Decision and audit logging

### 1.2 Key failure modes to look for
- Cross-boundary data exposure
- Prompt or tool abuse bypassing intended controls
- Unsupported claims without source evidence
- Missing or non-attributable audit events

---

## 2) Control Verification Framework

### 2.1 Required control families
- Identity and access management
- Retrieval authorization controls
- Fail-closed policy behavior
- Logging, monitoring, and traceability
- Incident response and rollback readiness

### 2.2 Verification depth model
- Design review: control intent and threat coverage
- Implementation review: code/config enforcement points
- Runtime review: observed behavior in test/log outputs

### 2.3 Confidence labels
- **Verified**: direct objective evidence across design + runtime.
- **Partially Confirmed**: some evidence, incomplete runtime validation.
- **Unknown**: no reliable evidence or unresolved contradictions.

---

## 3) Evidence Review Method

### 3.1 Evidence quality criteria
- Reproducible commands
- Traceable output artifacts
- Time-stamped and scoped findings
- Clear mapping from claim → proof

### 3.2 Red flags
- Narrative claims with no test outputs
- Unclear ownership for unresolved risks
- Overbroad “passed” statements lacking negative tests

### 3.3 Reviewer decision log template
- Claim under review
- Evidence provided
- Confidence label
- Residual risk
- Required remediation

---

## 4) How to Run / Validate Security Tests

### 4.1 Reviewer-led tests
- Authorization boundary tests (allow + deny)
- Abuse-case validation (prompt/tool misuse attempts)
- Fail-closed behavior under control-plane degradation
- Audit completeness checks

### 4.2 Required output capture
- Test command/procedure
- Expected vs actual behavior
- Screenshots/log snippets (redacted where required)
- Final confidence determination

---

## 5) Incident Response Review Duties

### 5.1 What reviewers verify
- Containment speed and scope correctness
- Evidence preservation quality
- Root-cause rigor and reproducibility
- Control improvements tied to incident lessons

### 5.2 Post-incident acceptance criteria
- Regression tests exist and pass
- Runbooks updated
- Residual risk acknowledged and owned

---

## 6) Launch Gate Interpretation

### GO
Critical controls are demonstrably effective, evidence is complete, and risk acceptance is documented.

### CONDITIONAL GO
Limited gaps exist with compensating controls and tightly bounded remediation commitments.

### NO-GO
Critical evidence is missing/contradictory, or unacceptable residual risk remains.

### Reviewer recommendation practice
- State exact blocker controls for NO-GO.
- Define objective exit criteria for moving to CONDITIONAL GO or GO.
