# Runtime Test Runbook

## V2.1 P0 Runtime Boundary Proof

For each control below, expected test path is `TO_BE_IDENTIFIED` unless already known. Commands are `COMMAND_PLACEHOLDER_NOT_EXECUTED` until finalized.

- **P0-RA-001 Retrieval Authorization**: purpose = enforce authorized-only retrieval; outputs = pytest/log/evidence-result; pass = allow authorized + deny unauthorized + audit deny; fail otherwise; local pass still does not unlock staging/production/client claims.
- **P0-CL-001 Citation Leakage Boundary**: purpose = prevent restricted citation leakage; outputs = answer/citation/log/result; pass = only authorized citations; fail if restricted metadata leaks; local pass still blocks staging/production/client claims.
- **P0-PI-001 Prompt-Injection Retrieval Boundary**: purpose = block authorization bypass via injection; outputs = policy decision/log/result; pass = blocked restricted content + fail-closed missing context; local pass still blocks staging/production/client claims.
- **P0-TA-001 Tool Authorization**: purpose = enforce tool auth + identity/session checks; outputs = allow/deny audit + result; pass = unknown/missing identity/high-risk without approval denied; local pass still blocks staging/production/client claims.
- **P0-FC-001 Fail-Closed Behavior**: purpose = deny on missing policy/identity/session/metadata; outputs = deny logs + result; pass = no missing-context allow path; local pass still blocks staging/production/client claims.
- **P0-AL-001 Audit Logging**: purpose = structured allow/deny events; outputs = audit events + result; pass = fields present and no sensitive content leak; local pass still blocks staging/production/client claims.
- **P0-TT-001 Telemetry Tracing**: purpose = request traceability across decision points; outputs = trace + result; pass = trace links policy/retrieval/tool paths; local pass still blocks staging/production/client claims.
