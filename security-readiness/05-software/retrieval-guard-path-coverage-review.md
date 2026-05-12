# Retrieval Guard Path Coverage Review
Date: 2026-05-12
Launch Gate: NOT_ENOUGH_EVIDENCE
Full Runtime Retrieval Status: NOT_PASS / BLOCKED

Scope reviewed:
- `backend/onyx/context/search/pipeline.py`
- `backend/onyx/context/search/models.py`
- `backend/onyx/context/search/retrieval/search_runner.py`
- `backend/onyx/context/search/preprocessing/access_filters.py`
- `backend/onyx/db/document_set.py`
- `backend/onyx/security_readiness/retrieval_guard_adapter.py`
- federated retrieval flow in `backend/onyx/federated_connectors/federated_retrieval.py`

## Path-by-path coverage

1) **base_filters.document_set**
- Code location: `_build_index_filters` in `pipeline.py`; `enforce_retrieval_authorization` in `retrieval_guard_adapter.py`.
- Current authorization control: explicit `enforce_retrieval_authorization(...)` call when `base_filters.document_set is not None and not bypass_acl` plus DB ownership re-check (`filter_document_set_names_by_user_access`).
- RetrievalAuthorizationGuard applies: **Yes**.
- Existing ACL filters apply: **Yes** (through access filters and explicit document set access check).
- Audit/trace coverage: emits `retrieval.allow` / `retrieval.deny` + `retrieval.authorization` trace.
- Bypass risk: low if `bypass_acl=False`; medium if upstream caller can force bypass.
- Status: **Covered** (runtime-adjacent).
- Risk severity: **Medium**.
- Recommended next test: integration-level test through `search_pipeline(...)` and mixed document sets against real DB fixtures.

2) **persona_document_sets**
- Code location: `_build_index_filters` in `pipeline.py`, assignment `document_set_filter = base_filters.document_set if ... else persona_document_sets`.
- Current authorization control: no guard invocation when only persona sets are used (guard path currently keyed on `base_filters.document_set` presence).
- RetrievalAuthorizationGuard applies: **No (directly)** when user does not provide `base_filters.document_set`.
- Existing ACL filters apply: **Partially** (query-level ACL list exists but no explicit guard/audit for persona set names).
- Audit/trace coverage: **No explicit retrieval guard audit for persona-only path**.
- Bypass risk: **High** until proven by runtime path tests.
- Status: **Partially Covered**.
- Risk severity: **High**.
- Recommended next test: adapter/integration-adjacent test where `persona_document_sets` includes unauthorized set and `user_selected_filters.document_set` is `None`.

3) **attached_document_ids**
- Code location: `AssistantKnowledgeFilters` in `models.py`; passed through in `search_pipeline` and `_build_index_filters` into `IndexFilters`.
- Current authorization control: no explicit `enforce_retrieval_authorization` for attached doc IDs in reviewed path.
- RetrievalAuthorizationGuard applies: **No**.
- Existing ACL filters apply: **Unknown/Indirect** (depends on downstream index enforcement + ACL filter conjunction).
- Audit/trace coverage: **No dedicated allow/deny event observed**.
- Bypass risk: **High**.
- Status: **Unknown**.
- Risk severity: **High**.
- Recommended next test: runtime-adjacent test that injects attached IDs outside allowed set and verifies deny/fail-closed behavior.

4) **hierarchy_node_ids**
- Code location: `AssistantKnowledgeFilters` in `models.py`; populated in `search_pipeline`; forwarded in `_build_index_filters`.
- Current authorization control: no explicit retrieval guard for hierarchy node IDs in reviewed files.
- RetrievalAuthorizationGuard applies: **No**.
- Existing ACL filters apply: **Unknown/Indirect**.
- Audit/trace coverage: **No dedicated authorization event path found**.
- Bypass risk: **High**.
- Status: **Unknown**.
- Risk severity: **High**.
- Recommended next test: runtime-adjacent adapter test for unauthorized hierarchy nodes combined with user ACL filters.

5) **acl_filters**
- Code location: `_build_index_filters` in `pipeline.py`; `build_access_filters_for_user` in `access_filters.py`.
- Current authorization control: ACL list is either caller-supplied (`acl_filters`) or built from user via `get_acl_for_user`.
- RetrievalAuthorizationGuard applies: **Not directly** (guard is document-set specific).
- Existing ACL filters apply: **Yes** for retrieval query filters.
- Audit/trace coverage: **No dedicated audit events for ACL filter construction in reviewed path**.
- Bypass risk: medium if insecure caller injects permissive prefetched `acl_filters`.
- Status: **Partially Covered**.
- Risk severity: **Medium**.
- Recommended next test: validate that prefetched ACLs cannot broaden access beyond user DB ACLs.

6) **bypass_acl=True**
- Code location: `_build_index_filters` in `pipeline.py`.
- Current authorization control: guard call and ACL filter building are skipped; `access_control_list` becomes `None`.
- RetrievalAuthorizationGuard applies: **No (explicit bypass)**.
- Existing ACL filters apply: **No**.
- Audit/trace coverage: **No retrieval authorization audit in this branch**.
- Bypass risk: **High**.
- Status: **Not Covered** (from guard perspective).
- Risk severity: **High**.
- Recommended next test: restricted system-caller contract test requiring explicit trusted context + deny by default otherwise.

7) **federated retrieval**
- Code location: `search_runner.py` (`get_federated_retrieval_functions` call); `federated_retrieval.py`.
- Current authorization control: federated connector selection constrained by `document_set_names` mapping and user/slack context, but no direct retrieval guard adapter call in federated module.
- RetrievalAuthorizationGuard applies: **Indirect only** if document sets were guarded earlier.
- Existing ACL filters apply: **Partially/connector-specific**.
- Audit/trace coverage: **No retrieval.allow/deny audit from guard in federated module path itself**.
- Bypass risk: **Medium-High**.
- Status: **Partially Covered**.
- Risk severity: **High**.
- Recommended next test: federated path test with mixed authorized/unauthorized document sets and source filters.

8) **citation/source construction**
- Code location: `SearchDoc.from_chunks_or_sections` and `SearchDocsResponse.citation_mapping` in `models.py`.
- Current authorization control: relies on prior retrieval filtering; citation/source objects are constructed from returned chunks.
- RetrievalAuthorizationGuard applies: **No (post-retrieval transform)**.
- Existing ACL filters apply: **Only upstream**.
- Audit/trace coverage: **No explicit citation-leak audit in reviewed path**.
- Bypass risk: **High** until end-to-end no-leak assertions are proven.
- Status: **Unknown**.
- Risk severity: **High**.
- Recommended next test: ensure denied docs never appear in `search_docs` or `citation_mapping` during mixed-access scenarios.

9) **post-query censoring**
- Code location: `search_pipeline` post-processing call to `_post_query_chunk_censoring` via `fetch_ee_implementation_or_noop`.
- Current authorization control: optional EE censoring hook after retrieval.
- RetrievalAuthorizationGuard applies: **No** (separate control stage).
- Existing ACL filters apply: **Upstream only**.
- Audit/trace coverage: **Unknown** in OSS path; hook may be no-op.
- Bypass risk: medium-high when connector field-level ACLs depend on this stage.
- Status: **Unknown**.
- Risk severity: **High**.
- Recommended next test: verify censor hook invocation and denied-field removal evidence (or explicit blocker if EE module unavailable).

## Net finding
- Adapter-level evidence strengthens `base_filters.document_set` coverage.
- High-risk paths (`bypass_acl`, `attached_document_ids`, citation/source path) remain **Not Covered/Unknown** for runtime proof.
- Launch gate remains **NOT_ENOUGH_EVIDENCE**.
