# Session Security Review

## Relevant code paths
- `backend/onyx/auth/users.py` (`optional_user`, `_check_for_saml_and_jwt`, `double_check_user`, refresh hooks).
- `backend/onyx/auth/jwt.py` (JWT verification helpers).
- Config references in `backend/onyx/configs/app_configs.py` (session expiry/auth backend settings).

## Current observed behavior
- Session user is resolved first, then optional JWT/PAT/API-key fallback paths.
- Expired OIDC identities are denied by default in `double_check_user`.
- OAuth token refresh is best-effort and non-fatal to authentication flow.

## Unknowns
- Cookie/session hardening runtime settings (secure/samesite/domain) for all deployment profiles not fully validated in this artifact.
- Revocation timing behavior for all auth backends under failure/restart conditions.

## Expected control
- Missing or invalid session must fail closed.
- Session/token expiry must be enforced consistently.
- Security attributes for session cookies must meet environment baseline.

## Test cases
- Missing session denied.
- Expired/invalid identity denied when expiry tracking enabled.

## Evidence needed
- Unit tests for denial paths.
- Config snapshots and runtime response headers for cookie/session settings.

## Launch gate impact
- **High**: weak session enforcement increases account takeover and replay risk.
