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
