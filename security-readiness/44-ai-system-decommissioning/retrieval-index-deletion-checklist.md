# Retrieval Index Deletion Checklist (Scope 296)

## Shutdown Trigger Reference
- Trigger/change record ID: `TBD`
- Effective shutdown date (UTC): `TBD`
- Owner: Data Governance Owner

## Checklist
- [ ] Confirm ingestion freeze is active for all index sources.
- [ ] Enumerate all retrieval indexes, namespaces, and embedding stores in scope.
- [ ] Capture pre-deletion inventory artifact (index IDs, sizes, last update time).
- [ ] Delete primary retrieval indexes.
- [ ] Delete derived embedding caches and temporary vector artifacts.
- [ ] Delete backup copies not required by legal hold.
- [ ] Verify delete operations succeeded (API/job status evidence attached).
- [ ] Run retrieval probes confirming deleted content is non-retrievable.
- [ ] Document exceptions, legal holds, and approved retention constraints.

## Evidence to Archive
- Commands/API calls used for deletion.
- Deletion job outputs and timestamps.
- Negative retrieval test results.

## Residual Risk
- **Status:** Unknown until probes and retention exceptions are documented.
- **Risk owner:** Data Governance Owner.

## Final Sign-Off
- Data Governance Owner: `TBD`
- Security Readiness Lead: `TBD`
- Date (UTC): `TBD`
