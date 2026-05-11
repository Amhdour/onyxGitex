# Blocker Summary

## Attempted test
`uv run pytest backend/tests/unit/onyx/security_readiness/test_control_layer.py -q`

## Outcome
- Test did not start; dependency resolution failed before pytest collection completed.

## Blocking issue (Verified)
- Runtime is Python 3.14.4, but locked dependency `onnxruntime==1.20.1` has no cp314 wheel.

## Impact
- Backend test environment is not currently stabilized on this host without changing Python runtime to a supported version for lockfile dependencies.

## Safe remediation (no app behavior change)
1. Use Python 3.11 (matches `backend/Dockerfile` and expected baseline), then run:
   - `uv sync`
   - `uv run pytest backend/tests/unit/onyx/security_readiness/test_control_layer.py -q`
2. Alternative: Python 3.12/3.13 may work for onnxruntime, but 3.11 is the project’s container baseline.

## Readiness/launch decision status
- Unchanged. This artifact only documents environment setup and blocker evidence.
