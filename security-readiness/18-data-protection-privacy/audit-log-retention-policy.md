# Audit Log Retention Policy (Build Priority 10.114)
Date: 2026-05-11 (UTC)
Status: Readiness policy draft

## Audit/Log Surfaces
- Application logger emits contextual request/tenant metadata.
- Optional rotating file logs persisted to `/var/log/onyx/` (container) or `./log/` (dev).
- Trace instrumentation exists and may capture workflow/span metadata.

## Privacy Risks in Audit Logs
- Over-collection: message/tool payloads accidentally logged.
- Correlation risk: tenant + request IDs linked with user actions.
- Long-term retention in downstream collectors without minimization.

## Retention and Minimization Rules
1. Keep audit signals necessary for accountability, not full content payloads.
2. Redact/highlight sensitive values before sink ingestion.
3. Define bounded retention windows per sink (app logs, SIEM, traces).
4. Apply role-restricted access for audit viewers.
5. Enforce deletion/aging procedure aligned with legal and internal policy.

## Evidence Required
- Logging field inventory and redaction policy.
- Trace payload schema and capture rules.
- Retention job evidence from each sink.

## Launch Gate Effect
If audit logging cannot prove privacy-preserving minimization and bounded retention, launch decision should be downgraded to **Conditional** or **No-Go**.
