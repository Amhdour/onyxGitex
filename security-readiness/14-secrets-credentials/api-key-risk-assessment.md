# API Key Risk Assessment (Priority 6)

Date: 2026-05-11
Status: Partially Confirmed

## Risk model
Likelihood/Impact scoring: Low / Medium / High / Critical.

## Key risk findings

| Secret Class | Example (Redacted) | Primary Risk | Likelihood | Impact | Launch Gate Impact |
|---|---|---|---|---|---|
| Auth signing keys | `USER_AUTH_SECRET=[REDACTED]` | Token forgery, privilege escalation | Medium | Critical | **Blocker** if unmanaged |
| Encryption root key | `ENCRYPTION_KEY_SECRET=[REDACTED]` | Decrypt stored secrets, long-term compromise | Medium | Critical | **Blocker** if unmanaged |
| DB/admin credentials | `POSTGRES_PASSWORD=[REDACTED]` | Data exfiltration, tampering | Medium | High | **Blocker** if static/shared |
| Search/storage admin credentials | `OPENSEARCH_ADMIN_PASSWORD=[REDACTED]`, `S3_AWS_SECRET_ACCESS_KEY=[REDACTED]` | Index/object access takeover | Medium | High | **Blocker** if long-lived |
| LLM/provider API keys | `OPENAI_API_KEY=[REDACTED]` | Billing abuse, prompt/data leakage via provider | High | High | **Major** |
| Connector API tokens | `CONFLUENCE_ACCESS_TOKEN=[REDACTED]` | Unauthorized enterprise data extraction | High | High | **Blocker** for broad scopes |
| Test-only API keys in mock env | `MCP_API_KEY=[REDACTED]` | Misuse if promoted to prod by mistake | Low | Medium | **Minor** with environment isolation |

## Additional risk observations
- Compose templates include default password fallbacks; if reused in production manifests, risk is immediate credential predictability.
- Some scripts include placeholder constants for API keys; operational guidance must ensure these are never committed with real values.

## Readiness decision mapping
- **Launch Gate: Fail** if any Critical/High secret class remains static, shared, unrotated, or stored outside approved vault controls.
- **Launch Gate: Conditional Pass** only when secret manager integration + rotation evidence + exposure playbook tests are all Verified.

## Evidence status
- Verified: secret variable names, code consumption paths.
- Partially Confirmed: production operational controls.
- Unknown: historical rotation execution evidence.
