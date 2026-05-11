# Admin Access Review

## Relevant code paths
- `backend/onyx/auth/permissions.py` (admin-as-all-permissions logic).
- `backend/onyx/auth/users.py` (`current_curator_or_admin_user`, role checks).
- Admin API route modules that apply `require_permission`/admin dependencies.

## Current observed behavior
- Admin effective permission (`FULL_ADMIN_PANEL_ACCESS`) bypasses granular checks.
- Curator/admin role-based dependency exists for role-gated paths.

## Unknowns
- Complete validation that all admin routes consistently bind one of the required dependencies.
- Existence of any legacy/admin path not covered by dependency guards.

## Expected control
- Every admin operation must have explicit dependency guard.
- Admin actions should produce auditable event logs (verify separately in observability phase).

## Test cases
- Non-admin denied admin operation.
- Admin allowed for same operation.

## Evidence needed
- Route dependency audit and tests.
- Audit log verification for admin operations.

## Launch gate impact
- **High**: unguarded admin endpoints are a direct launch blocker.
