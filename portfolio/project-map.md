| Project | Repo/folder | System type | Main risks | Controls | Evidence | Launch decision | Status |
|---|---|---|---|---|---|---|---|
| RAG Internal Knowledge Assistant | security-readiness | RAG assistant | Retrieval leakage, prompt injection | Authz + fail-closed | Tiered artifacts | NO_GO | EVIDENCE_DEPENDENT |
| Autonomous Internal Operations Agent | agent-security-readiness | Agentic system | Unauthorized tools, approval bypass | Policy-as-code + approval gate | Foundation + lab artifacts | NO_GO | AGENT_READINESS_FOUNDATION |
| LangGraph Autonomous Agent Runtime Lab | agent-security-readiness/23-langgraph-agent-lab | Agentic runtime lab | Tool escalation, approval bypass, memory leakage, audit gaps | Graph nodes + policy + approval + fail-closed | Compatibility graph harness artifacts | NO_GO | COMPATIBILITY_GRAPH_PASS / PARTIAL_EVIDENCE |
