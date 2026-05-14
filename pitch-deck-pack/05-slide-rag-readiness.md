# RAG Readiness: Retrieval Boundaries and Citation Safety

## Slide title
RAG Readiness: Retrieval Boundaries and Citation Safety

## Slide purpose
Explain this stage of the readiness story with clear claim boundaries.

## Main message
RAG systems need proof that users retrieve only what they are allowed to see, and that citations do not leak restricted material.

## Visual idea
Use a simple consulting-style diagram with neutral palette and minimal iconography.

## Talk track
Focus on evidence boundaries, launch-gate logic, and what is still blocked without real client evidence.

## Key bullets
- Authorized user can retrieve allowed documents.
- Unauthorized user cannot retrieve restricted documents.
- Cross-department retrieval blocked.
- Prompt-injected document cannot override policy.
- Citations only use authorized material.
- Unauthorized attempts are logged.
- Fail-closed behavior works.
- Launch gate reads evidence.
- Version 2B preserves RAG evidence chain in CI artifacts.

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
