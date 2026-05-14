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
