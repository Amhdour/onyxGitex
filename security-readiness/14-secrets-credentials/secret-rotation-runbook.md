# Secret Rotation Runbook (Priority 6)

Date: 2026-05-11
Status: Draft

## Rotation SLOs (target)
- Critical (auth/encryption root): every 30 days or emergency rotate within 4 hours of incident.
- High (DB/admin/provider/connector): every 60 days.
- Medium (test/service integration keys): every 90 days.

## Trigger conditions
- Scheduled rotation window reached.
- Personnel change with privileged access.
- Suspicious access or confirmed exposure.
- Third-party breach notification.

## Standard rotation procedure
1. Create new secret version in vault as `[REDACTED_NEW_VERSION]`.
2. Validate dependent service compatibility in staging.
3. Deploy config pointer update to consume latest version.
4. Perform health checks and auth-path smoke tests.
5. Revoke prior version after confirmation window.
6. Record evidence (who/what/when/result) in readiness evidence log.

## Emergency rotation procedure
1. Freeze impacted integrations where possible.
2. Rotate compromised secret immediately.
3. Invalidate active sessions/tokens tied to compromised material.
4. Review logs for abnormal use between suspected exposure and containment.
5. Complete post-incident control review.

## Required evidence artifact fields
- Secret class, secret id/path (not value), old version id, new version id, operator, timestamp, verification command, rollback status.

## Rollback
- Maintain one prior version for bounded rollback window.
- Rollback only with incident commander approval.
- Any rollback event triggers new expedited rotation window.
