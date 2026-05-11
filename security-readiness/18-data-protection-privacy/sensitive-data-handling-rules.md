# Sensitive Data Handling Rules (Build Priority 10.110)
Date: 2026-05-11 (UTC)
Status: Readiness policy draft

## Purpose
Define handling constraints for sensitive data in RAG and autonomous agent operations.

## Rules
1. Data minimization: only collect/store fields required for product behavior.
2. No secret replay: API keys/tokens/password-like strings must never be echoed back in model responses.
3. Least exposure in logs/traces: prohibit raw sensitive payload logging where practical.
4. Tenant boundary preservation: sensitive artifacts remain tenant-scoped.
5. Redaction-first UX: display redacted placeholders (`[REDACTED]`) when sensitive content is detected.
6. No real personal data in readiness tests; fictional examples only.

## Operational Handling Matrix
- Prompts/responses: allowed with detection + retention + deletion controls.
- Tool arguments/responses: allowed with redaction and auditability controls.
- Attachments/derived metadata: allowed only when access controls and deletion path are verified.
- Secrets in any channel: blocked/quarantined.

## Evidence Required
- Logging review showing no intentional raw-secret logging patterns in critical paths.
- Trace configuration evidence documenting what payload fields are captured.
- Test outputs proving sensitive-content redaction/block behavior.

## Current Status
- **Partially Confirmed**: Logging and tracing entry points identified.
- **Unknown**: Exhaustive redaction controls for every tool and connector path.

## Launch Gate Effect
If secret-handling controls are not proven (block/redact + audit), launch readiness remains **Conditional / No-Go**.
