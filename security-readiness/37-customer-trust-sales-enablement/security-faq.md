# Security FAQ

_Last updated: 2026-05-11_

## 1) Is the AI assistant "secure"?
We describe the program as **evidence-backed readiness**, not guaranteed safety. Security is treated as an ongoing control-and-verification process with known residual risks.

## 2) Do you guarantee zero data leakage?
No. We do not claim zero risk. We design for prevention, detection, and response, including authorization boundaries, fail-closed behaviors, and audit evidence.

## 3) How do you prevent users from seeing unauthorized documents?
Primary approach: retrieval authorization controls aligned to identity and entitlements, plus verification testing and logging. Any unverified control area is explicitly labeled as Partially Confirmed or Unknown.

## 4) Do model responses always reflect source truth?
Not always. The system is designed to improve grounding to source data, but unsupported outputs remain a known model risk category. We monitor and test for this failure mode.

## 5) What happens if a required policy component is unavailable?
Target behavior is fail-closed (deny or degrade safely), with policy decision logging for investigation and audit.

## 6) Do you use customer data to train foundation models?
This FAQ does not assert training terms by default. Client-specific data handling terms must be confirmed in applicable platform contracts, deployment configuration, and data-processing documentation.

## 7) Can administrators audit what happened during a sensitive query?
That is a core objective. Audit evidence should include request context, policy decisions, retrieval actions, and outcome metadata as available in the deployed environment.

## 8) Are you certified against a specific framework?
No certification claim is made here. Where framework mappings exist, they are control mappings for readiness and governance support, not certification statements.

## 9) Is this safe for regulated or high-risk use cases?
Suitability depends on the client context, data sensitivity, integration posture, and accepted residual risk. Additional controls and validation are often required.

## 10) What evidence can you share during procurement?
Typically:
- Control summaries,
- Test approach and selected outputs,
- Residual risk register excerpts,
- Governance and incident response process summaries,
- Environment-specific assumptions and limitations.

## 11) What should a buyer ask to validate claims?
- Which controls are Verified vs Partially Confirmed vs Unknown?
- What tests were executed, when, and with what outcomes?
- What are current top residual risks and owners?
- What is the fail-closed design for authorization and policy outages?

## 12) How often is readiness reviewed?
Readiness should be reviewed continuously with formal checkpoints tied to release governance and material system changes.
