# Build Priority 22 — Human Approval Workflow

Date: 2026-05-11
Status: Proposed

## Workflow Steps
1. **Submission**
   - Requestor submits action request with evidence links and risk classification.
2. **Completeness Check**
   - Primary Reviewer verifies mandatory fields and artifacts.
   - Missing evidence => **Deferred** (fail-closed).
3. **Risk Tier Validation**
   - Confirm risk tier (Low/Moderate/High/Critical) using approval matrix.
4. **Security Review**
   - Required for High/Critical actions and sensitive-data responses.
5. **Decision**
   - Approve, Approve with Conditions, Reject, or Escalate.
6. **Logging**
   - Record decision in `reviewer-decision-log.md` with timestamp and reviewer identity.
7. **Execution Gate**
   - Action proceeds only when recorded decision satisfies role and risk requirements.
8. **Post-Decision Verification**
   - Validate that conditions (if any) are implemented before closure.

## Minimum Record for Approval
- Request ID
- Action summary
- Risk tier
- Evidence links
- Reviewer names/roles
- Decision + rationale
- Timestamp (UTC)
- Revalidation date (if conditional)

## Prohibition
No workflow step may assert that human review occurred unless the decision record exists and is complete.
