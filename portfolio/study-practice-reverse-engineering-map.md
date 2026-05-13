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


## Current Next Milestones

| Track | Current Evidence | Next Evidence Target | Why It Matters |
|---|---|---|---|
| RAG readiness | NOT_ENOUGH_EVIDENCE | Primary CI artifact proof | Launch dependency |
| LangGraph compatibility agent lab | COMPATIBILITY_GRAPH_PASS | CI artifact verification | Reproducibility |
| Real LangGraph runtime | NOT_AVAILABLE | REAL_LANGGRAPH_RUNTIME_PASS | Runtime parity |
| CI artifact verification | NOT_VERIFIED | CI_ARTIFACT_VERIFIED | Auditability |
| Memory boundary | PARTIAL | Integrated memory proof | Data isolation |
| Sandboxed tools | PARTIAL | Real tool guard evidence | Side-effect safety |
| Telemetry/incident readiness | Local mapping | Production integration | Incident response |
| Launch gate | NO_GO | Evidence-backed decision | Governance |

## Reverse Engineering Exercises

RAG exercises:
1. Trace identity to retrieval filter.
2. Trace document permission to answer source.
3. Trace CI artifact to launch-gate decision.
4. Trace dependency blocker to NOT_ENOUGH_EVIDENCE.

Agent exercises:
1. Trace request to node sequence.
2. Trace node sequence to policy decision.
3. Trace policy decision to sandboxed tool action.
4. Trace memory decision to denial.
5. Trace prompt injection to escalation denial.
6. Trace audit events to incident timeline.
7. Trace final-run-status.json to launch-gate status.

## Evidence Verification Milestones

| Milestone | Current status | Next action | What it teaches |
|---|---|---|---|
| LangGraph local compatibility evidence | Verified (21/21 compatibility) | Preserve deterministic reruns | How to build fallback evidence when optional deps fail |
| LangGraph real runtime attempt | Install failed / runtime unverified | Retry in network-enabled env | Honest separation of attempted vs verified runtime |
| LangGraph CI artifact verification | Not verified (artifact not available) | Trigger workflow + download artifact + run verifier | Direct-artifact proof discipline |
| RAG primary CI artifact verification | Not verified (artifact not available) | Download primary artifact and run RAG verifier | Primary-vs-external signal integrity |
| Telemetry mapping | Local schema mapped, not integrated | Implement production telemetry wiring evidence | Difference between schema planning and runtime integration |
| Production telemetry integration | Unverified | Integrate and validate in runtime logs | Auditability requirements for launch evidence |
| Launch-gate decision | NO_GO | Close blockers with direct evidence only | Strict evidence-first launch governance |
