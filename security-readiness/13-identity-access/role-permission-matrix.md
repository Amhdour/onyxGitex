# Role & Permission Matrix

## Relevant code paths
- `backend/onyx/auth/permissions.py` (`resolve_effective_permissions`, `get_effective_permissions`, `require_permission`).
- `backend/onyx/auth/users.py` (`is_user_admin`, `current_curator_or_admin_user`).
- `backend/onyx/db/enums.py` (`Permission` enum).

## Current observed behavior
- Permission checks are centralized in `require_permission` and enforced as FastAPI dependencies.
- `FULL_ADMIN_PANEL_ACCESS` implies all permissions.
- Additional implied permissions are expanded by rule map (e.g., manage implies read/add in several domains).

## Unknowns
- Complete endpoint-to-permission mapping coverage is not yet enumerated here.
- Any EE-only overrides/hooks that add authorization behavior are not fully validated in this phase.

## Expected control
- Admin-only operations must require either explicit admin role gate or `FULL_ADMIN_PANEL_ACCESS` path.
- Permission implication logic must remain deterministic and auditable.

## Test cases
- Non-admin/non-granted user denied on admin/manage action.
- Admin-permission user allowed on the same action.

## Evidence needed
- Tests for dependency behavior (`require_permission`).
- Endpoint inventory mapping required permissions to handlers.

## Launch gate impact
- **High**: incorrect permission expansion or missing checks creates horizontal/vertical privilege escalation risk.
