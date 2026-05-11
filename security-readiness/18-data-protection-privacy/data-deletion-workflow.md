# Data Deletion Workflow (Build Priority 10.112)
Date: 2026-05-11 (UTC)
Status: Readiness workflow draft

## Deletion Scope
- User-requested deletion (privacy request).
- Admin-initiated deletion (offboarding / incident response).
- Scheduled retention-based deletion.

## Candidate Technical Paths (From Schema Behavior)
- Cascade deletion is configured for several user/chat linked entities.
- Chat sessions may be soft-deleted in some modes (`deleted` flag), requiring follow-up hard-delete workflows.
- Tool calls and linked retrieval artifacts can be removed by foreign-key cascade where configured.

## Workflow
1. Intake deletion request (ticket ID + requester identity proof).
2. Determine tenant + user scope.
3. Execute deletion plan:
   - sessions/messages/tool calls/search-doc links,
   - related feedback objects,
   - applicable logs/traces in downstream systems (if supported).
4. Verify deletion via post-action queries and audit event.
5. Return completion status as `Verified`, `Partially Confirmed`, or `Unknown`.

## Evidence Required
- Runbook with exact commands/API calls.
- Before/after record counts for fictional test accounts.
- Audit event proving who approved/executed deletion.

## Risks / Gaps
- Soft-delete without hard-delete timer can create over-retention risk.
- External sinks (SIEM/tracing backends) may retain copied data beyond DB deletion.

## Launch Gate Effect
If end-to-end deletion verification (DB + logs/traces) is missing, launch remains **No-Go** for privacy-sensitive deployment profiles.
