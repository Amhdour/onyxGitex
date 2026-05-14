# 04 Version-by-Version Walkthrough

## Version 1
- **Purpose:** Establish portfolio-lab baseline and readiness methodology framing.
- **Artifacts:** Foundational readiness documentation and structure.
- **Value:** Creates shared language for risk, evidence, and decision gates.
- **Limitation:** No runtime production claim.

## Version 2A
- RAG runtime evidence
- Allowed retrieval
- Blocked unauthorized retrieval
- Prompt injection boundary
- Citation boundary
- Fail-closed behavior
- **Limitation:** local/partial runtime evidence, not production

## Version 2B
- GitHub Actions run
- Artifact proof
- Artifact download verification
- File-list verification
- **Limitation:** proves artifact preservation, not production safety

## Version 2C
- Trace IDs
- Audit correlation
- Policy correlation
- Retrieval correlation
- Citation correlation
- Incident timeline
- **Limitation:** local observability evidence, not external observability integration

## Version 2D
- Agent identity
- Tool authorization
- Human approval
- Unknown tool fail-closed
- Missing identity fail-closed
- Prompt-injection escalation blocked
- Sandbox/no-side-effect
- **Limitation:** local agent runtime harness, not real LangGraph production proof

## Version 3
- Staging architecture
- Service map
- Identity/policy/secrets/RAG/agent/observability paths
- **Limitation:** local staging-demo model, not real container runtime

## Version 4
- Client-specific template
- Required client evidence
- Launch-gate model
- **Limitation:** template only, not client evidence
