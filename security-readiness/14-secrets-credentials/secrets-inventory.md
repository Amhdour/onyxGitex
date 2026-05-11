# Secrets Inventory (Priority 6)

Date: 2026-05-11
Status: Partially Confirmed

## Scope and method
- Inspected configuration templates, compose files, Helm values, and secret-loading codepaths only.
- Did **not** read `.env` files, runtime secret values, or external secret stores.
- All examples below are redacted (`[REDACTED]`).

## Secret variable inventory (name-only, redacted)

| Secret Variable | Primary Usage Area | Evidence | Classification |
|---|---|---|---|
| `POSTGRES_PASSWORD` | DB auth for backend/services | compose + Helm + scripts | High |
| `DB_READONLY_PASSWORD` | KG readonly DB user provisioning | compose + migrations | High |
| `REDIS_PASSWORD` | Redis auth | Helm + debugging script | Medium |
| `OPENSEARCH_ADMIN_PASSWORD` / `OPENSEARCH_INITIAL_ADMIN_PASSWORD` | OpenSearch admin auth | compose + Helm | High |
| `S3_AWS_SECRET_ACCESS_KEY` / `AWS_SECRET_ACCESS_KEY` | Object storage auth | compose + Helm | High |
| `MINIO_ROOT_PASSWORD` | MinIO root auth | compose | High |
| `USER_AUTH_SECRET` | JWT signing/verification | backend auth path | Critical |
| `ENCRYPTION_KEY_SECRET` | At-rest secret encryption | encryption utility + compose | Critical |
| `OAUTH_CLIENT_SECRET`, `GOOGLE_OAUTH_CLIENT_SECRET` | OAuth client credential | compose / app config import path | High |
| `OPENAI_API_KEY`, `OPENAI_DEFAULT_API_KEY`, `GEN_AI_API_KEY` | LLM provider auth | tests + compose | High |
| `MCP_API_KEY`, `MCP_OAUTH_CLIENT_SECRET`, `MCP_OAUTH_PASSWORD` | MCP auth testing paths | MCP test compose | Medium |
| Connector tokens (e.g., `DISCORD_BOT_TOKEN`, `CONFLUENCE_ACCESS_TOKEN`) | Third-party connector auth | connector tests/config | High |

## Secret handling observations
- Current deployment examples include insecure fallback defaults for some credentials in compose templates; these are acceptable for local examples but launch-gate risk for production if not overridden.
- `USER_AUTH_SECRET` is directly used for JWT encode/decode, making key compromise a direct auth-boundary risk.
- `ENCRYPTION_KEY_SECRET` has explicit length validation and is used in encryption/decryption helpers.

## Known gaps
- Unknown whether production environments enforce external secret manager usage.
- Unknown rotation cadence currently enforced by operations.
- Unknown whether short-lived credentials are used for cloud data-plane access.
