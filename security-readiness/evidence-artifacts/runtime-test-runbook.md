# Runtime Test Runbook

| Test name | Path | Command | Required environment | Expected artifact output | Evidence classification | Claim allowed if pass | Still blocked if pass |
|---|---|---|---|---|---|---|---|
| Retrieval boundary local test | security-readiness/evidence-artifacts/rag-boundary-001 | See `test-command.txt` | Local python test deps | `control-result.json`, logs | LOCAL_RUNTIME | Local retrieval boundary evidence exists | Production/staging claim |
| Citation leakage local test | security-readiness/evidence-artifacts/citation-source-leakage | See `test-command.txt` | Local python test deps | `test-output.txt` | LOCAL_RUNTIME | Local leakage check evidence exists | Leakage elimination claim |
| Tool authorization local test | security-readiness/evidence-artifacts/tool-authorization | See `test-command.txt` | Local python test deps | `test-output.txt` | LOCAL_RUNTIME | Local tool auth checks exist | Full agent tool risk claim |
| Prompt injection boundary | security-readiness/evidence-artifacts/prompt-injection-boundary-001 | See `test-command.txt` | Local python test deps | `prompt-injection-results.json` | LOCAL_RUNTIME | Local prompt-injection boundary evidence exists | Staging/production robustness claim |
| Launch-gate validation | security-readiness/scripts | `python3 security-readiness/scripts/validate_readiness_evidence.py` | Python 3 | canonical-validation-result.json | STATIC_REVIEW | Metadata consistency claim | Runtime security claim |

Missing tests for real staging and production runtime are blocking claims.
