# Client-Facing Risk Summary

_Last updated: 2026-05-11_

## Purpose
Summarize key AI assistant risks in customer-friendly language with conservative, evidence-aligned positioning.

## Risk Rating Language
- **Inherent Risk**: Baseline risk before controls.
- **Control Effect**: Expected reduction when controls operate as designed.
- **Residual Risk**: Remaining risk after controls; never assumed to be zero.

## Key Risk Areas

### 1) Unauthorized Retrieval Exposure
- **Inherent Risk:** High for sensitive internal knowledge contexts.
- **Control Effect:** Access controls and authorization-aware retrieval can materially reduce exposure.
- **Residual Risk:** Medium/variable depending on identity integration quality, policy coverage, and testing depth.

### 2) Unsupported or Fabricated Responses
- **Inherent Risk:** Medium to high in generative systems.
- **Control Effect:** Grounding patterns, response constraints, and testing reduce but do not eliminate this risk.
- **Residual Risk:** Medium; requires operational monitoring and user guidance.

### 3) Prompt Abuse / Policy Evasion Attempts
- **Inherent Risk:** Medium.
- **Control Effect:** Input/output controls, policy enforcement, and abuse-case testing improve resistance.
- **Residual Risk:** Medium; adversarial evolution is continuous.

### 4) Tool Misuse or Over-Permissioning
- **Inherent Risk:** Medium to high where agentic actions exist.
- **Control Effect:** Scope limits, least privilege, and policy gates reduce misuse likelihood.
- **Residual Risk:** Medium; depends on connector/tool governance maturity.

### 5) Logging and Forensic Gaps
- **Inherent Risk:** Medium.
- **Control Effect:** Structured audit events and tracing increase detectability and investigation quality.
- **Residual Risk:** Low to medium depending on retention, coverage, and alerting.

## Client Interpretation Notes
- These ratings are directional and must be validated for each client deployment.
- Evidence recency matters; stale evidence lowers confidence.
- Unknowns and partially confirmed controls should be reviewed before launch decisions.

## Plain-Language Close
Risk can be reduced through controls and verification, but not eliminated. Production decisions should be based on current, environment-specific evidence and explicit residual-risk acceptance.
