# Service Account Review

## Relevant code paths
- `backend/onyx/auth/users.py` (`optional_user` API-key/PAT paths, `current_user` limited-user block).
- `backend/onyx/db/users.py` (`is_limited_user` semantics).
- `backend/onyx/db/api_key.py` and `backend/onyx/db/pat.py` (identity lookup for key-based auth).

## Current observed behavior
- Service/API identities can authenticate via PAT or API key.
- `current_user` denies limited users, including permissionless service accounts.

## Unknowns
- Rotation/expiry governance for all deployed service credentials.
- Least-privilege review coverage across existing service accounts.

## Expected control
- Service accounts must be least-privilege and non-interactive.
- Service accounts with no explicit permissions must fail closed on privileged routes.

## Test cases
- Permissionless service account denied protected user route.
- Key-based identity cannot execute admin-only operations without required permission.

## Evidence needed
- Unit tests for limited-service denial.
- Credential inventory and permission review evidence.

## Launch gate impact
- **High**: over-privileged or weakly-governed service identities materially increase blast radius.
