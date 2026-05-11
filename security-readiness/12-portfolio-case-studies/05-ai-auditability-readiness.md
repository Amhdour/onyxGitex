# AI Auditability Readiness Case Study

## Scenario
A fictional insurance provider, **Cedarstone Mutual**, needs defensible evidence for how assistant responses are produced, including retrieval sources and policy decisions.

## Business Risk
Insufficient auditability impairs incident response, regulatory examinations, customer dispute handling, and internal control assurance.

## System Components Involved
- Request/response orchestration layer
- Retrieval provenance capture
- Policy decision logging service
- Tool execution event stream
- Central log storage + SIEM/dashboard
- Retention and access governance controls

## Threat Model Summary
- **Primary asset:** integrity and completeness of runtime evidence.
- **Adversary profile:** malicious insider, compromised component, or accidental log loss.
- **Trust boundary:** distributed runtime events aggregating into central evidence store.
- **Failure mode:** missing, tampered, or uncorrelated logs prevent reconstruction.

## Abuse Case
A sensitive response is challenged, but no traceable linkage exists between user prompt, retrieved documents, and final answer, preventing root-cause analysis.

## Control Design
- Emit immutable correlation IDs across prompt, retrieval, policy, tool, and output events.
- Capture redacted provenance metadata for retrieved sources used in final response.
- Enforce append-only or tamper-evident log storage controls.
- Define retention, access, and review workflows aligned to governance needs.

## Test Design
- End-to-end traceability test verifying full event chain by correlation ID.
- Negative test validating missing event detection/alerting.
- Integrity test for tamper-evidence controls.
- Role-based access test for audit log viewers.

## Evidence Required
**Planned Evidence**
- Log schema references and correlation field definitions.
- Traceability test outputs demonstrating complete event linkage.
- Alert evidence for missing-event simulation.
- Retention/access policy documentation with control owner mapping.

## Expected Dashboard Signal
- Trace completeness metric at or near target threshold.
- Alert visibility for dropped or malformed events.
- Audit query latency and coverage KPIs within defined bounds.

## Residual Risk
Over-redaction may reduce investigative usefulness; under-redaction may expose sensitive data in logs.

## Launch Gate Impact
Launch for regulated workflows should be deferred until traceability coverage and audit evidence quality are validated.

## Client-Facing Explanation
"Auditability means being able to prove how each answer was produced. We gate launch on reliable, reviewable, and policy-aligned evidence trails."

## Portfolio Summary
This case study demonstrates how to evaluate AI systems for forensic-grade operational transparency and compliance support.
