# Model/API Key Revocation Checklist (Scope 299)

## Shutdown Trigger Reference
- Trigger/change record ID: `TBD`
- Effective shutdown date (UTC): `TBD`
- Owner: Security Operations Owner

## Checklist
- [ ] Inventory all model provider credentials (API keys, org tokens, cloud roles).
- [ ] Disable key usage in application configuration before revocation.
- [ ] Revoke active model/API keys at provider side.
- [ ] Rotate and disable fallback keys in secret stores.
- [ ] Confirm calls with revoked credentials fail authentication.
- [ ] Confirm no alternate untracked credentials remain in CI/CD or runtime envs.
- [ ] Record revocation timestamps and approvers.

## Evidence to Archive
- Provider revocation receipts/log entries.
- Secret manager version history showing disablement/rotation.
- Authentication failure test output after revocation.

## Residual Risk
- **Status:** Partially Confirmed until all non-production environments are checked.
- **Risk owner:** Security Operations Owner.

## Final Sign-Off
- Security Operations Owner: `TBD`
- Platform Engineering Owner: `TBD`
- Date (UTC): `TBD`
