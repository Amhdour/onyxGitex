# Tool Access Removal Checklist (Scope 298)

## Shutdown Trigger Reference
- Trigger/change record ID: `TBD`
- Effective shutdown date (UTC): `TBD`
- Owner: Security Engineering Owner

## Checklist
- [ ] Enumerate tool registry entries and policy bindings used by the AI system.
- [ ] Disable autonomous tool-calling feature flags for decommissioned scope.
- [ ] Remove service account permissions for tool execution.
- [ ] Remove allowlist entries for sensitive tool actions.
- [ ] Revoke OAuth/client grants and machine identities linked to tools.
- [ ] Verify tool invocation attempts are denied and logged.
- [ ] Review audit logs for denied post-decommission tool calls.

## Evidence to Archive
- Access control policy before/after snapshots.
- IAM role/policy revocation records.
- Denied invocation log evidence.

## Residual Risk
- **Status:** Unknown until denied-invocation test evidence is complete.
- **Risk owner:** Security Engineering Owner.

## Final Sign-Off
- Security Engineering Owner: `TBD`
- AI Service Owner: `TBD`
- Date (UTC): `TBD`
