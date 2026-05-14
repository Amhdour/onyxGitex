# Security Readiness Scripts

## Validator scope
`validate_readiness_evidence.py` checks canonical metadata and referenced artifact consistency, including P0 proof-pack structure and claim-boundary logic.

## Not checked
It does not execute runtime tests and does not prove production, client, or staging security outcomes.

## Run
`python3 security-readiness/scripts/validate_readiness_evidence.py`

PASS means the repository’s readiness metadata and referenced artifacts are internally consistent. It does not mean the system is production-ready, client-ready, staging-verified, or safe to launch.

`allow_go` may remain `false` on PASS because runtime controls can still be `NOT_EXECUTED`.

Add future P0 evidence by replacing placeholders with real test commands, logs, pytest output, and updated `evidence-result.json` files.

Interpret `canonical-validation-result.json` as metadata/artifact integrity output only.
