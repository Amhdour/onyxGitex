# Version 2A RAG Runtime Evidence Gate Contract

Inputs:
- rag-runtime-final-status.json
- rag-pytest-output.txt
- rag-audit-events.json
- rag-policy-decisions.json
- rag-retrieval-log.json
- rag-citation-check.json
- rag-launch-gate-result.json

Outputs:
- PARTIAL_RUNTIME_EVIDENCE if all local scenarios pass and all artifacts exist
- NO_GO if any scenario fails
- NOT_ENOUGH_EVIDENCE if artifacts are missing or execution is blocked

Hard rules:
- production_ready must remain false
- go_decision must remain false
- CI proof is required before any stronger claim
- GO is forbidden in Version 2A

# Version 2B CI Artifact Proof Contract

Inputs:
- version-2b-ci-artifact-status.json
- workflow-contract.json
- artifact-contract.json
- expected-artifact-file-list.txt
- workflow-run-evidence.json if available
- artifact-download-evidence.json if available
- artifact-file-list.txt if available
- verified-artifact-manifest.json if available

Outputs:
- CI_WORKFLOW_CONFIGURED_NOT_VERIFIED when workflow and contracts exist but no real CI artifact download is verified.
- CI_ARTIFACT_GENERATED_UNVERIFIED when a CI run exists but artifact download/file-list verification is incomplete.
- CI_ARTIFACT_VERIFIED when real CI artifact download and required file verification are complete.
- NO_GO when CI evidence shows failed tests or invalid evidence.
- NOT_ENOUGH_EVIDENCE when required CI proof is missing.

Hard rules:
- production_ready must remain false.
- go_decision must remain false.
- Version 2B cannot produce GO.
- Version 2B cannot claim staging or client verification.
- Version 2B only verifies CI artifact proof for Version 2A evidence.

# Version 2C Observability Proof Contract

Inputs:
- version-2c-observability-status.json
- trace-events.json
- audit-correlation.json
- policy-correlation.json
- retrieval-correlation.json
- citation-correlation.json
- launch-gate-correlation.json
- incident-timeline.json
- dashboard-query-view.json
- observability-evidence-manifest.json

Outputs:
- OBSERVABILITY_EVIDENCE_VERIFIED when all local trace/correlation artifacts validate.
- OBSERVABILITY_EVIDENCE_GENERATED when artifacts exist but validation is incomplete.
- NOT_ENOUGH_EVIDENCE when required artifacts are missing.
- NO_GO when correlation, trace reconstruction, or claim-safety validation fails.

Hard rules:
- production_ready must remain false.
- go_decision must remain false.
- Version 2C cannot produce GO.
- Version 2C cannot claim external observability integration unless real external evidence exists.
- Version 2C cannot claim staging or client-specific readiness.
- Version 2C only proves local observability evidence and correlation for Version 2A/2B evidence.


# Version 2D Agent Runtime Evidence Gate Contract

Inputs:
- version-2d-agent-runtime-status.json
- agent-scenario-results.json
- agent-trace-events.json
- agent-identity-events.json
- tool-authorization-decisions.json
- human-approval-events.json
- unknown-tool-events.json
- prompt-injection-tool-escalation-results.json
- sandbox-side-effect-checks.json
- agent-audit-events.json
- agent-incident-timeline.json
- agent-launch-gate-result.json
- agent-runtime-evidence-manifest.json

Outputs:
- AGENT_RUNTIME_EVIDENCE_VERIFIED when all local agent runtime artifacts validate.
- AGENT_RUNTIME_EVIDENCE_GENERATED when artifacts exist but validation is incomplete.
- LANGGRAPH_RUNTIME_VERIFIED only when real LangGraph runtime proof exists.
- NOT_ENOUGH_EVIDENCE when required artifacts are missing.
- NO_GO when agent runtime scenarios, fail-closed behavior, timeline reconstruction, or claim-safety validation fails.

Hard rules:
- production_ready must remain false.
- go_decision must remain false.
- Version 2D cannot produce GO.
- Version 2D cannot claim real LangGraph runtime unless LangGraph proof exists.
- Version 2D cannot claim MCP hardening unless MCP proof exists.
- Version 2D cannot claim staging or client-specific readiness.
- Version 2D only proves local deterministic agent runtime evidence unless stronger runtime proof is actually present.
