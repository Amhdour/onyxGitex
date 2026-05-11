# User Identity Model

## Relevant code paths
- `backend/onyx/auth/users.py` (`optional_user`, `double_check_user`, `current_user`, `current_chat_accessible_user`).
- `backend/onyx/db/models.py` (`User` model fields such as `role`, `account_type`, `oidc_expiry`, `effective_permissions`).

## Current observed behavior
- Identity can be resolved from session auth, JWT bearer (if configured), PAT, or API key in `optional_user`.
- `double_check_user` denies unauthenticated users, denies unverified users (when configured), and denies expired OIDC identities unless explicitly allowed.
- `current_user` additionally blocks limited users.

## Unknowns
- Whether every production deployment consistently enables email verification and OIDC expiry tracking.
- Whether all API surfaces call the strict dependency (`current_user`) vs optional/auth-relaxed variants.

## Expected control
- Every non-public route should require a strong user dependency (`current_user` or stricter).
- Expired identities and unverified identities should fail closed.
- Limited/service identities must not escalate into standard-user routes.

## Test cases
- Unauthenticated request is denied.
- Missing session/cookie is denied.
- Expired OIDC identity is denied.
- Limited service account is denied in `current_user` routes.

## Evidence needed
- Unit/integration test output for the above denial paths.
- Route-level dependency review confirming protected endpoints use enforced dependencies.

## Launch gate impact
- **High**: if identity resolution or fail-closed checks are bypassable, launch should be blocked.
