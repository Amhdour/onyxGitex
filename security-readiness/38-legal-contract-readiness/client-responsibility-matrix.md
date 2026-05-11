# Client Responsibility Matrix

> **Non-Legal Draft Notice (Required Lawyer Review):**
> This matrix is an operational draft and **not legal advice**. Legal counsel should convert this into binding contractual language.

## Purpose
Define clear allocation of responsibilities between Provider and Client to reduce ambiguity in AI risk ownership.

## Responsibility Matrix (Draft)

| Domain | Provider Responsibility (Draft) | Client Responsibility (Draft) | Shared / Notes |
|---|---|---|---|
| Identity & Access | Provide configurable access controls and enforcement hooks. | Configure role mappings, least privilege, and user lifecycle controls. | Shared review of privileged access exceptions. |
| Data Classification | Support metadata and policy integration where available. | Classify data sources and assign handling requirements. | Client authoritative for classification accuracy. |
| Connector Scope | Document supported integrations and control behavior. | Approve and maintain allowed connector list and scope. | New connectors require change review. |
| Retrieval Authorization | Provide policy decision points and deny-path behavior where implemented. | Define authorization policies and approve policy changes. | Fail-closed behavior preferred on policy uncertainty. |
| Prompt / Tool Governance | Provide configurable guardrails and audit hooks. | Approve tool access, business rules, and prohibited use cases. | Periodic governance review required. |
| Output Validation | Provide system warnings and confidence/limitation messaging where supported. | Validate outputs before legal, regulatory, financial, or safety-critical use. | Human review required for high-impact decisions. |
| Incident Response | Notify according to agreed incident process for provider-managed components. | Maintain internal escalation and response workflows. | Joint tabletop exercises recommended. |
| Logging & Audit Retention | Provide audit event generation for platform-controlled events. | Set retention policies, legal hold, and downstream SIEM controls. | Verify timestamp and integrity controls. |
| Third-Party Risk | Disclose known material dependencies and update cadence. | Perform vendor risk acceptance and contractual review. | Shared review of high-risk dependency changes. |
| Change Management | Publish release/change notices for managed components. | Test and approve environment-specific rollout decisions. | Reassessment triggered by material change. |
| End-User Training | Provide usage guidance documentation. | Train users on safe use, boundaries, and escalation paths. | Track completion for regulated teams. |

## Operational Notes
- Mark each row as **Agreed / Pending / Rejected** during contract review.
- Record named owners and review dates.
- Add jurisdiction-specific obligations as directed by counsel.
