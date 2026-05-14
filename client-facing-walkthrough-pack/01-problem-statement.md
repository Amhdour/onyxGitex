# 01 Problem Statement

Companies are deploying RAG assistants and autonomous agents quickly, often validating only response quality while skipping authorization, policy, and incident reconstruction readiness checks.

- Teams often test “does it answer?” but not “should it be allowed?”
- RAG workflows can leak restricted data when retrieval boundaries are weak.
- Agent workflows can call tools incorrectly, overreach scope, or bypass intended approval logic.
- Prompt injection can attempt to override policy and trigger unsafe behavior.
- Observability gaps make incidents hard to reconstruct and audit.
- Launch decisions are frequently made without structured evidence.

onyxGitex addresses this gap by modeling an evidence-first readiness approach for RAG and agent systems, emphasizing boundaries, traceability, and conservative launch gating.
