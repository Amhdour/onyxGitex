# Version 2A — RAG Runtime Evidence Gate

Current status:
NOT_VERIFIED or PARTIAL_RUNTIME_EVIDENCE depending on generated evidence.

Purpose:
Prove locally that RAG retrieval respects authorization boundaries.

This is not production proof.
This is not CI proof.
This is not staging proof.
This is not client-specific proof.

Canonical generated evidence:
security-readiness/evidence-artifacts/version-2a-rag-runtime/

Required proof:
- Authorized user can retrieve allowed documents.
- Unauthorized user cannot retrieve restricted documents.
- Cross-department retrieval is blocked.
- Prompt-injected document cannot override access policy.
- Source citations only use authorized material.
- Unauthorized attempts are logged.
- Fail-closed behavior works.
- Launch gate reads the evidence.

Allowed claim after successful local run:
Version 2A local RAG runtime evidence harness executed and produced reviewable artifacts.

Blocked claims:
- Production ready
- GO launch decision
- CI verified
- Staging verified
- Client verified
- Full production RAG security proven

How to run:
python scripts/run-rag-runtime-evidence.py
python scripts/validate-rag-runtime-evidence.py
python scripts/print-rag-runtime-status.py
