# Tool Authorization Runtime Evidence Package

- **Purpose:** Collect runtime proof for agent tool authorization controls.
- **Scope:** Allow/deny decisions, sensitive-tool human approval gating, and fail-closed behavior.
- **Agent control area:** Tool authorization and runtime decision enforcement.
- **Evidence status:** STATUS: NOT_ENOUGH_EVIDENCE.
- **Runtime verification status:** RUNTIME_STATUS: NOT_RUN.

## What is verified
- Evidence package structure exists.
- Runtime collection requirements are documented.

## What is not verified
- Unauthorized tool calls blocked at runtime.
- Human confirmation enforced at runtime.
- Fail-closed behavior enforced at runtime.
- Runtime audit completeness.

## Required artifacts
policy-test-output.txt, allowed-tool-call-log.txt, denied-tool-call-log.txt, human-confirmation-log.txt, fail-closed-log.txt, runtime-trace.json, git-commit.txt, test-command.txt, timestamp.txt.

## Reproduction command
`bash agent-security-readiness/17-evidence-artifacts/tool-authorization-runtime/scripts/run-tool-authorization-check.sh`

## Launch-gate implication
Without executed runtime artifacts, decision remains NOT_ENOUGH_EVIDENCE / NO-GO.
