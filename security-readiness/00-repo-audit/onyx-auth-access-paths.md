# Onyx Authentication & Access Paths

## Authentication modules

- `backend/onyx/auth/users.py`
  - Appears to control current user resolution (`current_user`, chat-accessible variants, ws token validation).
  - Evidence reference: symbols like `current_chat_accessible_user`, token retrieval and access denied branches.
  - Confidence: **Partially Confirmed** (large file; key paths sampled).

- `backend/onyx/auth/jwt.py`
  - Appears to control JWT/public key retrieval and validation helpers.
  - Confidence: **Partially Confirmed**.

- `backend/onyx/auth/api_key.py`, `backend/onyx/auth/pat.py`
  - Appears to control API key/PAT extraction & auth mode handling.
  - Confidence: **Partially Confirmed**.

## Authorization modules

- `backend/onyx/auth/permissions.py`
  - `resolve_effective_permissions`, `get_effective_permissions`, `require_permission` dependency.
  - Appears to enforce permission checks via FastAPI dependency injection.
  - Confidence: **Confirmed**.

- `backend/onyx/db/document_access.py`
  - `apply_document_access_filter`, `get_accessible_documents_by_ids`.
  - Appears to enforce document visibility via public/doc-level/group/email ACL logic.
  - Confidence: **Confirmed**.

## User/group model surfaces

- `backend/onyx/db/models.py`
  - Classes: `User`, `UserGroup` and related fields (including effective permissions/group relationships).
  - Confidence: **Confirmed**.

## Key risk flags for Phase 2

- `auth/users.py` size/complexity suggests multiple auth variants that require scenario-driven tests (API key, PAT, OAuth, WS token). Confidence: **Partially Confirmed**.
- Group-based permission recomputation persistence behavior (DB-side recomputation) must be runtime tested for stale grants. Confidence: **Needs Verification**.
