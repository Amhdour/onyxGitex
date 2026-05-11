# Build Priority 7 - Connector Permission Review

Date: 2026-05-11

## Scope
Review connector permission dependencies and authorization controls for ingestion + retrieval.

## Permission model observations
- CC-pair visibility and editability are filtered by user role, group membership, creator relationship, and `AccessType` (public/private/sync).
- Connector creation validation enforces connector settings and optionally permission-sync validation when `AccessType.SYNC` is used.
- Anonymous users are restricted to public connector-credential pairs.

## Permission review matrix
| Control point | Expected behavior | Evidence | Status |
|---|---|---|---|
| CC-pair access filtering | Non-admin users only see/edit allowed connectors via group ownership and role constraints | `_add_user_filters`, `get_connector_credential_pairs_for_user` | **Verified** |
| Anonymous access restriction | Anonymous users limited to `AccessType.PUBLIC` | `_add_user_filters` anonymous branch | **Verified** |
| Sync permission validation | For `AccessType.SYNC`, connector permission-sync validation is invoked | `validate_ccpair_for_user` -> `validate_perm_sync` | **Verified** |
| Credential handling | Credentials loaded from DB-backed providers / credential JSON, not hardcoded in orchestrator | `instantiate_connector` | **Verified** |

## Gaps / unknowns
- Per-connector minimum upstream OAuth/API scopes are not centrally enforced in a single policy file. **Unknown**.
- Per-connector least-privilege templates for source systems are not present in this folder yet. **Unknown**.

## Evidence required before launch gate
1. Connector-by-connector scope matrix (actual OAuth scopes and API roles).
2. Test evidence for permission sync correctness for representative connectors (Slack, Google Drive, Jira).
3. Negative tests for unauthorized retrieval attempts across private connectors.
