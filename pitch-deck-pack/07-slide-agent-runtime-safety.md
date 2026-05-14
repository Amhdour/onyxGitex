# Agent Runtime Safety: Identity, Tools, Approval, and Fail-Closed Behavior

## Slide title
Agent Runtime Safety: Identity, Tools, Approval, and Fail-Closed Behavior

## Slide purpose
Explain this stage of the readiness story with clear claim boundaries.

## Main message
Autonomous agents need runtime evidence that tool use is authorized, auditable, approval-aware, and safe from prompt-injection escalation.

## Visual idea
Use a simple consulting-style diagram with neutral palette and minimal iconography.

## Talk track
Focus on evidence boundaries, launch-gate logic, and what is still blocked without real client evidence.

## Key bullets
- Authorized safe tool allowed.
- Restricted tool requires approval.
- Restricted tool denied without approval.
- Unknown tool fails closed.
- Missing identity fails closed.
- Prompt injection cannot escalate tool access.
- Sandboxed tool has no real side effects.
- Agent incident timeline reconstructable.
- Agent launch gate reads evidence.
- Boundary: local deterministic evidence, not real LangGraph production proof.

## Evidence references
- client-facing-walkthrough-pack/
- client-production-template/
- staging-demo/
- production-readiness/
- security-readiness/evidence-artifacts/version-2a-rag-runtime/
- security-readiness/evidence-artifacts/version-2b-ci-artifact-proof/
- security-readiness/evidence-artifacts/version-2c-observability-proof/
- security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence/
- security-readiness/evidence-artifacts/version-3-staging-demo/
- security-readiness/evidence-artifacts/version-4-client-production-template/

## What not to say
- This is production-ready.
- This is fully secure.
- This is a real production GO.

## Client takeaway
Use evidence to decide readiness; do not treat demo success as production authorization.
