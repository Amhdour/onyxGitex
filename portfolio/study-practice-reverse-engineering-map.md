# Study / Practice / Reverse Engineering Map

## RAG Track

Study:
- Onyx architecture
- retrieval flow
- document permissions
- CI evidence
- final-run-status schema

Practice:
- dependency prechecks
- pytest evidence
- CI artifact capture
- launch-gate updates

Reverse engineering:
- identity to retrieval
- access filtering
- source grounding
- audit/logging path

## Autonomous Agent Track

Study:
- LangGraph node flow
- tool registry
- policy gate
- approval gate
- memory state
- audit events

Practice:
- allowed/denied tool scenarios
- fail-closed behavior
- prompt-injection escalation
- memory leakage denial
- incident trace reconstruction

Reverse engineering:
- agent decision path
- tool authorization path
- approval state transitions
- audit-event correlation
- launch-gate decision logic

## Portfolio Evidence

- what is proven: compatibility-mode graph harness executes deterministic scenarios and emits trace/audit artifacts.
- what is partial evidence: memory boundary and prompt-injection controls in local harness scope.
- what is not proven: production LangGraph deployment, real external tool execution, persistent memory protections.
- what remains NO_GO: launch gate for autonomous agent and RAG remains NO_GO.
