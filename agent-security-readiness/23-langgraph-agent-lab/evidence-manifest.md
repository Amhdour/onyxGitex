| Artifact | Present | Scope | Status | Notes |
|---|---|---|---|---|
| langgraph-runtime-dependency-check.py | Yes | GRAPH_RUNTIME | Present | Dependency detection entrypoint. |
| runtime-artifacts/langgraph-dependency-check.json | Yes | COMPATIBILITY_RUNTIME | Generated | Captures LangGraph availability/mode. |
| run-real-langgraph-or-compat-harness.py | Yes | GRAPH_RUNTIME | Present | Graph-orchestrated harness. |
| graph-runtime-artifacts/graph-runtime-summary.json | Yes | GRAPH_RUNTIME | Generated | 12/12 pass in compatibility mode. |
| graph-runtime-artifacts/graph-runtime-trace.json | Yes | GRAPH_RUNTIME | Generated | Per-scenario trace with required fields. |
| graph-runtime-artifacts/graph-policy-decision-log.json | Yes | TOOL_AUTHORIZATION | Generated | Policy decisions. |
| graph-runtime-artifacts/graph-audit-events.json | Yes | AUDIT | Generated | Per-node audit events. |
| graph-runtime-artifacts/graph-allowed-tool-call-log.json | Yes | TOOL_AUTHORIZATION | Generated | Allowed actions. |
| graph-runtime-artifacts/graph-denied-tool-call-log.json | Yes | FAIL_CLOSED | Generated | Denied actions. |
| graph-runtime-artifacts/graph-human-approval-required-log.json | Yes | HUMAN_APPROVAL | Generated | Approval-required decisions. |
| graph-runtime-artifacts/graph-fail-closed-log.json | Yes | FAIL_CLOSED | Generated | Fail-closed decisions. |
| graph-runtime-artifacts/graph-memory-boundary-log.json | Yes | MEMORY_BOUNDARY | Generated | Memory scenarios. |
| graph-runtime-artifacts/graph-prompt-injection-log.json | Yes | PROMPT_INJECTION | Generated | Injection scenario evidence. |
| graph-runtime-artifacts/graph-incident-timeline.json | Yes | INCIDENT_TRACE | Generated | Reconstructed timelines. |
| graph-runtime-artifacts/graph-harness-output.txt | Yes | GRAPH_RUNTIME | Generated | Human-readable output. |
| graph-runtime-artifacts/graph-runtime-mode.txt | Yes | COMPATIBILITY_RUNTIME | Generated | Runtime mode marker. |
| graph-runtime-artifacts/timestamp.txt | Yes | GRAPH_RUNTIME | Generated | UTC timestamp. |
| graph-runtime-artifacts/git-commit.txt | Yes | GRAPH_RUNTIME | Generated | Git commit used by run. |
| memory-boundary-test-plan.md | Yes | MEMORY_BOUNDARY | Present | Boundary plan. |
| sandboxed-tool-model.md | Yes | TOOL_AUTHORIZATION | Present | Sandbox model constraints. |
| incident-trace-reconstruction.md | Yes | INCIDENT_TRACE | Present | IR reconstruction guide. |
| final-run-status.json | Yes | LAUNCH_GATE | Updated | PARTIAL_EVIDENCE / NO_GO. |
| claims_not_allowed entries | Yes | NON_CLAIM | Enforced | No production-safe launch claim. |
