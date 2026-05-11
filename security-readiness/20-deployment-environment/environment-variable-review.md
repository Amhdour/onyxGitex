# Build Priority 12.125 — Environment Variable Review

Date: 2026-05-11  
Status: Partially Confirmed

## Method
Reviewed `env.template`, `env.prod.template`, and compose/helm references for secret-like and safety-critical variables.

## Secret-like Variable Families (Redacted)
- Authentication and signing:
  - `USER_AUTH_SECRET=[REDACTED]`
  - `SECRET=[REDACTED]`
  - OAuth/OIDC/SAML client secrets and metadata fields (`*_SECRET`, `OPENID_CONFIG_URL`, etc.)
- Data plane credentials:
  - `POSTGRES_PASSWORD=[REDACTED]`
  - `DB_READONLY_PASSWORD=[REDACTED]`
  - `S3_AWS_ACCESS_KEY_ID=[REDACTED]`
  - `S3_AWS_SECRET_ACCESS_KEY=[REDACTED]`
  - `MINIO_ROOT_PASSWORD=[REDACTED]`
- External service/API credentials:
  - `AWS_ACCESS_KEY_ID=[REDACTED]`
  - `AWS_SECRET_ACCESS_KEY=[REDACTED]`
  - `DISCORD_BOT_TOKEN=[REDACTED]`
  - `SENTRY_DSN=[REDACTED]`

## Key Findings
1. Templates include known defaults (e.g., local passwords/admin values) that are unsafe if reused outside development.
2. Production template requires operator-provided secrets but does not itself enforce secret manager sourcing.
3. Compose files ingest `.env` directly; accidental commit risk exists if local process controls are weak.

## Control Status
- **Verified:** Secret-handling mechanism exists in Helm (`auth-secrets.yaml`) and can fail when required values are missing.
- **Partially Confirmed:** Runtime secret hygiene in compose-based production.
- **Unknown:** Whether live deployments rotate secrets and prohibit default literals.

## Recommendations
- Prohibit default credential values in non-dev deployments with CI policy checks.
- Move production secrets to external secret manager integrations.
- Add pre-deploy scanner for `.env` and values files to block placeholder/default creds.
