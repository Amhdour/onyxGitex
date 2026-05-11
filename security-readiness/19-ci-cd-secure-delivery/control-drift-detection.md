# Control Drift Detection

Date: 2026-05-11  
Status: **Plan (Partially Confirmed)**

## Objective
Detect drift between documented controls, implemented checks, and CI verification expectations.

## Drift Signals
- Required control documents missing.
- Required sections removed from control docs.
- CI launch-gate script and readiness checklist out of sync.

## Minimal Drift Mechanism
- Maintain single required-file manifest in `.github/scripts/readiness_launch_gate_check.sh`.
- Generate run output in `artifacts/launch-gate-summary.md`.
- Compare output across runs during readiness review.

## Future Drift Hardening
- Add checksum baseline for selected readiness control documents.
- Add owner-review requirement for control-file changes.
- Introduce blocking mode after stable baseline is accepted.
