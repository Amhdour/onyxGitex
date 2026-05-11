# Connector Deactivation Checklist (Scope 297)

## Shutdown Trigger Reference
- Trigger/change record ID: `TBD`
- Effective shutdown date (UTC): `TBD`
- Owner: Platform Engineering Owner

## Checklist
- [ ] Identify all active connectors, credentials, and sync schedules.
- [ ] Disable scheduled ingestion jobs (cron/workers/webhooks).
- [ ] Disable connector runtime execution paths in platform configuration.
- [ ] Revoke connector-specific access tokens/secrets from secret manager.
- [ ] Confirm no connector can establish new upstream sessions.
- [ ] Confirm no queued connector jobs remain runnable.
- [ ] Capture post-disablement state (screenshots/logs/config diff references).
- [ ] Validate fail-closed behavior when connector endpoints are requested.

## Evidence to Archive
- Connector inventory before/after deactivation.
- Secret revocation records.
- Scheduler/job queue disablement evidence.

## Residual Risk
- **Status:** Partially Confirmed until queued and retry paths are proven disabled.
- **Risk owner:** Platform Engineering Owner.

## Final Sign-Off
- Platform Engineering Owner: `TBD`
- Security Readiness Lead: `TBD`
- Date (UTC): `TBD`
