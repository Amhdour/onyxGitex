# Secrets Access Policy (Priority 6)

Date: 2026-05-11
Status: Draft for implementation

## Policy objectives
1. Enforce least privilege for all secret reads.
2. Eliminate static/shared credentials where short-lived alternatives exist.
3. Make all secret access auditable.
4. Fail closed on secret retrieval failures.

## Access rules
- Secrets **must** be stored in an approved secret manager (Vault/OpenBao or cloud-native equivalent).
- Direct `.env` usage is limited to local development and non-production test scenarios.
- Production workloads must receive secrets via runtime injection (sidecar/CSI/env-from-secret reference), not hardcoded config.
- Access is bound to workload identity (service account/role), never shared team credentials.
- Human read access to production secrets requires break-glass approval and time-bound session.

## Enforcement controls
- Deny deployment if required secret references are missing.
- Deny startup when required secrets resolve to empty values.
- Deny use of known insecure defaults (e.g., template fallback passwords) outside dev.
- Deny logging of raw secret values; allow only key names and hash-safe fingerprints.

## Audit requirements
- Log: principal, secret path/name, action (read/list/rotate), decision (allow/deny), timestamp, request-id.
- Retain audit logs per compliance policy; minimum 1 year recommended (assumption).

## Verification requirements before launch gate
- Verified policy-as-code checks for secret references in deployment manifests.
- Verified runtime failure behavior when secret manager is unavailable.
- Verified deny events for unauthorized secret path access.

## Exceptions
- Any exception must have: owner, expiry date, compensating controls, and explicit risk acceptance.
