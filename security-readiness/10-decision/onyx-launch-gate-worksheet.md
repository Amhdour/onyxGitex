# Onyx Launch Gate Worksheet

**Generated:** 2026-05-12 (UTC)  
**Decision Engine:** `security-readiness/scripts/run-launch-gate.py`  
**Decision:** **NOT_ENOUGH_EVIDENCE**

## Evidence-Driven Inputs
- Evidence registry: `security-readiness/47-evidence-automation/evidence-artifact-registry.json`
- Evidence completeness validation: `security-readiness/evidence-artifacts/evidence-validation/validation-result.json`
- Control test results: `security-readiness/evidence-artifacts/control-layer-unit-tests/control-layer-summary.md`
- Red-team results: `security-readiness/09-evidence/onyx-red-team-results.md`
- Residual risk register: `security-readiness/10-decision/onyx-residual-risk-register.md`
- Critical findings: `security-readiness/01-assessment/onyx-initial-risk-register.md`
- Evidence pack: `security-readiness/evidence-artifacts/evidence-pack.json`

## Rule Evaluation
1. Any critical retrieval leak = NO_GO → **Not triggered**.
2. Missing identity fail-closed test = NOT_ENOUGH_EVIDENCE or NO_GO → **Triggered**.
3. Missing evidence pack = NOT_ENOUGH_EVIDENCE → **Not triggered**.
4. Critical open risk without remediation = NO_GO → **Not triggered by current parsing evidence**.
5. Passing core tests but medium residual risks = CONDITIONAL_GO → **Not eligible**.
6. All required evidence present and no critical open risk = GO → **Not eligible** (`validation status = INCOMPLETE`).
7. Unknown runtime integration = NOT_ENOUGH_EVIDENCE → **Not directly triggered in this run**, but overall completeness remains incomplete.

## Decision Rationale
- Decision set to **NOT_ENOUGH_EVIDENCE** because required fail-closed identity/retrieval authorization evidence is missing in validator output (`retrieval_authorization_tests`).
- Evidence completeness validator status is **INCOMPLETE** and `allow_go=false`, preventing GO.
- Uncertainty is intentionally preserved; no launch approval is inferred from assumptions.

## Evidence Artifacts Produced
- `security-readiness/evidence-artifacts/launch-gate/decision-inputs.json`
- `security-readiness/evidence-artifacts/launch-gate/launch-gate-result.json`
- `security-readiness/evidence-artifacts/launch-gate/launch-gate-summary.md`
- `security-readiness/evidence-artifacts/launch-gate/timestamp.txt`
- `security-readiness/evidence-artifacts/launch-gate/git-commit.txt`
