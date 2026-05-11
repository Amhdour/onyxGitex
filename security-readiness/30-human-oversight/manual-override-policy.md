# Build Priority 22 — Manual Override Policy

Date: 2026-05-11
Status: Proposed

## Purpose
Define narrowly-scoped emergency override conditions while preserving auditability and fail-closed defaults.

## Permitted Override Scenarios
1. Active incident containment requiring immediate block/disable action.
2. Safety-preserving rollback when automated path is unavailable.
3. Temporary denial of risky tool execution to prevent suspected misuse.

## Prohibited Override Scenarios
- Bypassing required approvals for convenience or delivery speed.
- Authorizing high-risk data access without evidence.
- Clearing launch gate blockers without logged risk acceptance.

## Authorization Requirements
- Minimum approvers: Incident Commander + Security Reviewer.
- For launch-impacting overrides: add Launch Gate Approver.
- Overrides must include expiry time and rollback plan.

## Mandatory Override Record
- Override ID and timestamp (UTC)
- Initiator and approvers
- Justification and impacted scope
- Controls bypassed/added
- Expiration and restoration confirmation
- Linked evidence artifacts

## Post-Override Review
Within 2 business days:
- verify all temporary changes were reverted or formally approved,
- document residual risk,
- update evidence pack.
