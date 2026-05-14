# The Problem: AI Systems Move Faster Than Their Evidence

## Slide title
The Problem: AI Systems Move Faster Than Their Evidence

## Slide purpose
Explain this stage of the readiness story with clear claim boundaries.

## Main message
Many RAG and agent systems are launched after functional testing, but without enough proof of access control, tool authorization, observability, or launch readiness.

## Visual idea
Use a simple consulting-style diagram with neutral palette and minimal iconography.

## Talk track
Focus on evidence boundaries, launch-gate logic, and what is still blocked without real client evidence.

## Key bullets
- RAG may expose restricted documents.
- Citations may leak unauthorized material.
- Prompt injection may try to override policy.
- Agents may call tools without proper approval.
- Unknown tools may not fail closed.
- Incidents may be hard to reconstruct.
- Launch decisions may be based on assumptions instead of evidence.

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
