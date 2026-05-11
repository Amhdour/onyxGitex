# Policy Test CI Pipeline

Date: 2026-05-11  
Status: **Plan (Partially Confirmed)**

## Objective
Continuously validate AI policy controls (authorization, fail-closed behavior, and policy decision logging expectations) as a CI check.

## Pipeline Design
- Reuse readiness workflow (`.github/workflows/readiness-ci.yml`) as orchestration layer.
- Add policy check stage that validates required policy artifacts are present and internally consistent:
  - `security-readiness/04-controls/onyx-control-matrix.md`
  - `security-readiness/04-controls/onyx-fail-closed-rules.md`
  - `security-readiness/04-controls/onyx-policy-decision-log-requirements.md`
- Emit machine-readable pass/fail summary to `security-readiness/19-ci-cd-secure-delivery/artifacts/policy-check-summary.md`.

## Guardrails
- Do not assert policy enforcement as **Verified** unless backed by test output or runtime logs.
- Mark unmet assertions as **Unknown** or **Partially Confirmed**.
- Fail-closed requirement: missing mandatory policy documents should fail the step.

## Rollout Mode
- Initial mode non-blocking (`continue-on-error: true`) until false-positive rate is measured.
- Promotion criteria to blocking: control owner sign-off + evidence acceptance.
