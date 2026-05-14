# Version 2.1 — Artifact-Aware Evidence Validator + P0 Runtime Proof Pack

## 1. Purpose
Define a conservative, artifact-aware readiness milestone that raises evidence quality without overclaiming runtime/security outcomes.

## 2. Why V2.1 exists
V1.5 normalized metadata consistency; V2.1 adds artifact checks and explicit P0 runtime-proof structure.

## 3. Relationship to V1, V1.5, V2, V3, V4
- V1: portfolio methodology strength.
- V1.5: evidence-consistency layer.
- V2-alpha: starter-kit implementation in progress.
- V2.1: artifact-aware validator + P0 proof-pack structure.
- V3/V4: still blocked pending real staging/client/production evidence.

## 4. What V2.1 is allowed to claim
- Artifact-aware evidence validation requirements are defined.
- P0 runtime proof-pack structure and acceptance criteria exist.
- Launch-gate blockers are explicitly tracked.

## 5. What V2.1 is not allowed to claim
Not production-ready, client-ready, staging-verified, certified, safe-to-launch, or risk-elimination proof.

## 6. Required P0 controls
Retrieval authorization, citation leakage boundary, prompt-injection retrieval boundary, tool authorization, fail-closed behavior, audit logging, telemetry tracing.

## 7. Required evidence artifacts
Per-control runbook files, acceptance criteria, evidence-result schema, placeholder logs marked not executed, plus manifest and final-status files.

## 8. Required validation logic
Validator must confirm required files exist, required evidence-result fields exist, and claims are not upgraded without runtime artifacts.

## 9. Acceptance criteria
- Evidence references are artifact-aware.
- Missing artifacts/invalid statuses are detected.
- Runtime claims require runtime files.
- NO_GO blockers remain enforced.
- P0 structure exists with schema/runbook per control.

## 10. Remaining NO_GO conditions
Any P0 control not PASSED, or missing staging/production/client runtime evidence.

## 11. Next version after V2.1
V2.2 — Execute P0 Runtime Boundary Proof.
