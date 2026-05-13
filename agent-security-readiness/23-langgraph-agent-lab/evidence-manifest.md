# Evidence Manifest

| Artifact | Present | Scope | Status | Notes |
|---|---|---|---|---|
| ci-real-runtime-followup-precheck.md | Yes | LOCAL_EVIDENCE | PARTIAL_EVIDENCE | Follow-up readiness snapshot. |
| ci-downloaded-artifact/README.md | Yes | CI_ARTIFACT | VERIFIED_DOC | Manual artifact handling instructions. |
| fetch-langgraph-ci-artifact.sh | Yes | CI_ARTIFACT | VERIFIED_DOC | Optional gh helper; does not assert verification. |
| ci-fetch-output.txt | No | CI_ARTIFACT | NOT_AVAILABLE | Generated only when helper runs. |
| verify-ci-artifacts-local.py | Yes | CI_ARTIFACT | VERIFIED_LOCAL_TOOL | Local verifier implemented. |
| ci-artifact-verification-output.json | Yes | CI_ARTIFACT | CI_ARTIFACT_NOT_AVAILABLE | No downloaded artifact validated yet. |
| attempt-real-langgraph-runtime.py | Yes | REAL_LANGGRAPH_RUNTIME | PARTIAL_EVIDENCE | Attempt path maintained. |
| real-langgraph-attempt-output.json | Yes | REAL_LANGGRAPH_RUNTIME | REAL_LANGGRAPH_NOT_AVAILABLE | No importable langgraph runtime. |
| real-langgraph-install-attempt.md | Yes | REAL_LANGGRAPH_RUNTIME | INSTALL_FAILED | Install evidence captured. |
| real-langgraph-install-output.txt | Yes | REAL_LANGGRAPH_RUNTIME | INSTALL_FAILED | Pip/network error evidence. |
| final-run-status.json | Yes | LAUNCH_GATE | PARTIAL_EVIDENCE | Maintains NO_GO discipline. |
| ci-result-summary.md | Yes | CI_ARTIFACT | PARTIAL_EVIDENCE | Explicit non-claims preserved. |
| runtime-execution-report.md | Yes | COMPATIBILITY_RUNTIME | PARTIAL_EVIDENCE | Follow-up section added. |
| graph-runtime-artifacts/graph-runtime-summary.json | Yes | COMPATIBILITY_RUNTIME | COMPATIBILITY_GRAPH_PASS | 21/21 compatibility pass. |
| graph-runtime-artifacts/graph-runtime-trace.json | Yes | COMPATIBILITY_RUNTIME | PRESENT | Deterministic trace artifact. |
| graph-runtime-artifacts/graph-policy-decision-log.json | Yes | COMPATIBILITY_RUNTIME | PRESENT | Policy decisions captured. |
| graph-runtime-artifacts/graph-audit-events.json | Yes | COMPATIBILITY_RUNTIME | PRESENT | Audit events captured. |
| graph-runtime-artifacts/graph-memory-boundary-log.json | Yes | COMPATIBILITY_RUNTIME | COMPATIBILITY_RUNTIME_PARTIAL | Boundary checks in compatibility mode. |
| graph-runtime-artifacts/graph-sandboxed-tool-results.json | Yes | COMPATIBILITY_RUNTIME | COMPATIBILITY_RUNTIME_PARTIAL | No external side effects observed. |
| graph-runtime-artifacts/graph-incident-timeline.json | Yes | COMPATIBILITY_RUNTIME | PRESENT | Incident timeline present. |
