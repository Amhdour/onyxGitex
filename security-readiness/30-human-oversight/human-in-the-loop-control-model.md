# Build Priority 22 — Human-in-the-Loop Control Model

Date: 2026-05-11
Status: Proposed

## Objective
Define how human reviewers must approve, reject, or escalate high-risk AI assistant actions before launch and during operations.

## Control Principles
1. **No implied review**: A decision is valid only when recorded in the reviewer decision log.
2. **Fail-closed**: If required reviewer evidence is missing, the action is blocked.
3. **Least privilege**: Reviewers can approve only within their delegated authority.
4. **Dual-control for critical risk**: Critical-risk actions require two distinct human approvers.
5. **Traceable evidence**: Every decision must include artifact links and timestamps.

## Reviewer Roles
- **Requestor**: Proposes action and submits evidence package.
- **Primary Reviewer**: Validates risk, scope, and evidence sufficiency.
- **Security Reviewer**: Validates policy, abuse-case risk, and control adherence.
- **Launch Gate Approver**: Final go/no-go authority for release-affecting decisions.
- **Incident Commander (Escalation)**: Resolves urgent or ambiguous risk events.

## Decision States
- **Approved**: Evidence complete and risk accepted within policy.
- **Approved with Conditions**: Temporary controls required with expiration date.
- **Rejected**: Evidence insufficient or policy conflict.
- **Escalated**: Requires higher authority or cross-functional arbitration.
- **Deferred**: Awaiting missing evidence.

## Required Evidence Inputs
- Linked control/test evidence from `security-readiness/`.
- Risk statement (including data sensitivity and blast radius).
- Affected systems/tools and trust boundaries.
- Reviewer rationale and policy references.
- Expiration/revalidation date for conditional approvals.

## Launch Gate Use
Human oversight is mandatory at launch gate when any of the following apply:
- unresolved critical findings,
- unresolved high-risk evidence gaps,
- planned use of high-risk tool actions,
- sensitive-data workflows with partial controls.
