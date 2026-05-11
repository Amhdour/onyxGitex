# Access Review Workflow

## Relevant code paths
- `backend/onyx/auth/permissions.py` and dependency usage across route modules.
- `backend/onyx/db/models.py` user/group/permission-bearing entities.
- Existing tests under `backend/tests/` validating authorization behavior.

## Current observed behavior
- Permission evaluation is code-centralized, making periodic review scriptable.
- Some authorization tests exist, and additional identity/access negative tests were added in this phase.

## Unknowns
- Formal cadence/owners for recurring access recertification are not codified in code.
- Completeness of role-permission recertification evidence in current runbooks is unknown.

## Expected control
- Quarterly (or stricter) access reviews with named owners.
- Evidence pack per cycle: user-role export, privileged account review, exception approvals, remediation tracking.
- Launch gate requires latest completed review with no unresolved critical exceptions.

## Test cases
- Validate protected routes reject unauthorized/under-privileged identities.
- Validate tenant/department isolation negative paths.

## Evidence needed
- Review runbook and signed review artifacts.
- Automated test outputs and endpoint guard inventory.

## Launch gate impact
- **Medium-High**: absent recertification process weakens ongoing control assurance post-launch.
