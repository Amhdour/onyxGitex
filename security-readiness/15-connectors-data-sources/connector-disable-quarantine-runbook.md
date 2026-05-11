# Build Priority 7 - Connector Disable / Quarantine Runbook

Date: 2026-05-11

## Trigger conditions
- Credential compromise suspected.
- Source ACL drift detected.
- Poisoning indicators in indexed documents.
- Repeated permission-sync failures.

## Procedure (fail-closed)
1. **Identify connector-credential pair** by `cc_pair_id`, source, owner group, and last successful indexing attempt.
2. **Immediate containment**:
   - Set connector status to `PAUSED` for short-term quarantine, or
   - Initiate deletion attempt API to mark `DELETING` and cancel scheduled indexing attempts.
3. **Stop active ingestion**:
   - Cancel in-progress/scheduled index attempts for impacted cc-pair.
4. **Credential revocation**:
   - Revoke upstream token/key in source system.
   - Rotate credential stored in Onyx credential store.
5. **Data impact assessment**:
   - Enumerate documents by cc-pair via ingestion API path.
   - Identify time range and sensitivity of potentially tainted documents.
6. **Cleanup**:
   - Reindex or delete affected documents per incident response decision.
7. **Recovery criteria**:
   - Permission review completed.
   - Connector settings validated successfully.
   - Control verification tests pass.

## Evidence required for closure
- API/action logs showing status transition (`PAUSED` or `DELETING`).
- Proof of canceled indexing attempts.
- Credential revocation/rotation evidence ([REDACTED]).
- Document impact report for affected cc-pair.
- Post-remediation verification test output.

## Code references
- CC-pair statuses: `ACTIVE`, `PAUSED`, `DELETING`, `INVALID`.
- Deletion attempt endpoint cancels indexing and marks status `DELETING`.
- Connector-doc listing endpoint supports impact scoping by `cc_pair_id`.
