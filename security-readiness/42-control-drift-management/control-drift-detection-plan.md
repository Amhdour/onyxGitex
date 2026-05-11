# Control Drift Detection Plan

Date: 2026-05-11  
Status: **Plan (Partially Confirmed)**

## Scope
Define how control drift is detected across policy, retrieval boundaries, tool permissions, evidence artifacts, dashboard signals, and governance approvals.

## Drift Categories
1. **Policy Drift**: required policy constraints differ from approved baseline.
2. **Retrieval Boundary Drift**: authorization or source-boundary controls diverge from expected behavior.
3. **Tool Permission Drift**: agent/tool permission scope expands or bypasses approved least privilege.
4. **Evidence Drift**: required evidence files are missing, stale, or no longer traceable to controls.
5. **Dashboard Drift**: launch-gate dashboards no longer reflect approved control definitions.
6. **Governance Drift**: ownership, approvals, or review cadences fall out of policy.

## Detection Method
- Run a deterministic file/config drift check (`drift_check.py`) against expected artifacts.
- Record findings with timestamp and repository-relative path.
- Classify each result as **No Drift**, **Drift Detected**, or **Unknown**.

## Launch Gate Impact Rules
- **Blocker**: drift in policy, retrieval boundary, or tool permission controls.
- **Conditional Hold**: drift in evidence, dashboard, or governance controls until remediation owner and due date are assigned.
- **Escalation**: repeated drift in same category across two review cycles triggers governance escalation.

## Evidence Requirements
- Drift check command and output captured in evidence notes.
- Changed file diffs attached to change review.
- Exception approvals documented with owner and expiry date.
