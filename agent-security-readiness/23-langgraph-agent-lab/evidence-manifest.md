# Evidence Manifest — LangGraph Agent Lab

| Artifact | Present | Scope | Status | Notes |
|---|---|---|---|---|
| README.md | Yes | FOUNDATION | Present | Baseline lab purpose and non-claims. |
| tool-registry.json | Yes | POLICY_DECISION | Present | Tool policy inventory used by harness. |
| langgraph-agent-runtime-skeleton.py | Yes | FOUNDATION | Present | Skeleton control-point reference implementation. |
| run-langgraph-agent-harness.py | Yes | MOCK_RUNTIME | Present | Deterministic executable runtime harness. |
| runtime-precheck.md | Yes | STATUS | Present | Environment and dependency precheck recorded. |
| final-run-status.json | Yes | LAUNCH_GATE | Updated | Updated from executed mock-runtime evidence. |
| launch-gate-notes.md | Yes | LAUNCH_GATE | Updated | Includes latest runtime result and NO_GO rationale. |
| runtime-artifacts/allowed-tool-call-log.json | Yes | MOCK_RUNTIME | Generated | Allowed tool decisions only. |
| runtime-artifacts/denied-tool-call-log.json | Yes | POLICY_DECISION | Generated | DENY and DENY_FAIL_CLOSED decisions. |
| runtime-artifacts/human-approval-required-log.json | Yes | APPROVAL_GATE | Generated | REQUIRE_APPROVAL decisions. |
| runtime-artifacts/fail-closed-log.json | Yes | FAIL_CLOSED | Generated | DENY_FAIL_CLOSED decisions only. |
| runtime-artifacts/runtime-trace.json | Yes | MOCK_RUNTIME | Generated | Full scenario-by-scenario execution trace. |
| runtime-artifacts/policy-decision-log.json | Yes | POLICY_DECISION | Generated | Per-case policy decision record. |
| runtime-artifacts/audit-events.json | Yes | AUDIT | Generated | Audit event stream for all decisions. |
| runtime-artifacts/harness-summary.json | Yes | STATUS | Generated | Mock-runtime summary and aggregate status. |
| runtime-artifacts/harness-output.txt | Yes | MOCK_RUNTIME | Generated | Human-readable harness execution output. |
| runtime-artifacts/timestamp.txt | Yes | STATUS | Generated | UTC runtime timestamp. |
| runtime-artifacts/git-commit.txt | Yes | STATUS | Generated | Commit hash at runtime execution. |
