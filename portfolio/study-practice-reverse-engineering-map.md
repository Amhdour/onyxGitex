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

## Current Evidence Levels
| Track | Evidence Level | What Exists | What Remains |
|---|---|---|---|
| RAG Readiness | NOT_ENOUGH_EVIDENCE | Existing RAG package and plans | Primary CI run + artifact proof |
| LangGraph Compatibility Agent Lab | PARTIAL_EVIDENCE | Local compatibility runtime artifacts | CI artifact verification |
| Real LangGraph Runtime | NOT_AVAILABLE | Optional path documented | Install and execute real runtime |
| Memory Boundary | PARTIAL | Local seed + boundary logs | Production memory integration proof |
| Sandboxed Tools | PARTIAL | Local mock tools + logs | CI artifact verification |
| Incident Trace | PARTIAL | Local timeline artifact | Production-grade telemetry correlation |
| CI Artifact Verification | NOT_VERIFIED | Plan and instructions | Direct download/inspection proof |

## Next 30-Day Practice Plan
Week 1: Trigger LangGraph CI workflow; download artifacts; compare local vs CI final-run-status.
Week 2: Install optional langgraph; attempt real runtime pass; preserve compatibility fallback.
Week 3: Strengthen memory-boundary tests; add prompt-injection memory-poisoning cases.
Week 4: Return to RAG primary CI evidence; obtain direct workflow/artifact proof.
