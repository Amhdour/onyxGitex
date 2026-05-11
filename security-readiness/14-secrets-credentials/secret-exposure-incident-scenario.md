# Secret Exposure Incident Scenario (Priority 6)

Date: 2026-05-11
Status: Tabletop Scenario Draft

## Scenario
A connector API token is accidentally committed to a feature branch and mirrored into CI logs before detection.

## Assumptions
- Secret scanning exists but may not block all pushes (**Partially Confirmed**).
- Token has read access to sensitive enterprise content.

## Timeline exercise
- T0: Commit introduced with secret value `[REDACTED]`.
- T0 + 10m: CI executes and logs request failures containing token-adjacent metadata.
- T0 + 45m: Security scanner or reviewer flags exposure.
- T0 + 60m: Incident declared; secret revocation initiated.

## Response playbook
1. Contain
   - Revoke exposed token.
   - Disable affected connector sync jobs.
2. Eradicate
   - Purge secret from git history where feasible.
   - Remove leaked log artifacts per retention policy.
3. Recover
   - Issue new scoped token.
   - Re-enable sync with monitoring.
4. Lessons learned
   - Add/strengthen pre-commit and CI secret detection rules.
   - Validate fail-closed behavior when token revoked.

## Required evidence for this scenario
- Revocation timestamp and actor.
- Proof of failed access for old token after revocation.
- New token issuance record.
- Post-incident review with root cause and control improvements.

## Launch-gate impact mapping
- If revocation + detection MTTD/MTTR targets are unmet, readiness is **No-Go**.
- If incident process executes with complete evidence and bounded blast radius, mark **Conditionally Ready** pending control hardening completion.
