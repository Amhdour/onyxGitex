# Data Minimization Review
Date: 2026-05-11 (UTC)
Scope: Minimize data stored/exposed in retrieval workflows
Status: Control requirements defined; implementation confirmation incomplete

## Minimization Principles for Retrieval Corpus
- Ingest only fields needed for retrieval relevance and authorization.
- Exclude unnecessary sensitive attributes at connector stage where possible.
- Store operational metadata separately from raw content when feasible.
- Enforce least-privilege retrieval and deny-by-default on missing ACL metadata.

## Review Findings
- Repository readiness artifacts already call for fail-closed retrieval authorization behavior.
- Existing retention policy artifact records unresolved TTL/deletion assumptions, indicating minimization controls are not yet fully evidence-backed.

## Required Actions
1. Define allowed metadata schema per connector source.
2. Add explicit disallowed fields list (PII/secrets categories) for indexing pipeline.
3. Prove deletion and retention execution with test evidence.
4. Add periodic minimization audit (sampled documents/chunks).

## Verification Labels
- **Partially Confirmed:** Policy intent.
- **Unknown:** Measured minimization effectiveness and enforcement coverage.
