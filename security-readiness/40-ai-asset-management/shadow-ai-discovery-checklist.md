# Shadow AI Discovery Checklist (Client-Ready)

_Date: 2026-05-11_
_Status: Client-Ready Draft for Security Readiness (Build Priority 32)_

## How to Use
Use this checklist during stakeholder interviews, architecture reviews, and telemetry sampling to discover unregistered AI usage.

## Shadow AI Discovery Checklist

| Check Item | Asset Name | Type | Owner | Dependency | Data Touched | Risk Level | Lifecycle Status | Evidence | Review Cadence |
|---|---|---|---|---|---|---|---|---|---|
| Confirm all AI-enabled SaaS tools used by teams are listed in approved inventory. | [To be captured] | External AI SaaS | Business + IT Owner | Vendor APIs/plugins | Potential internal docs, prompts | High (if unknown) | Unknown until validated | Procurement records, SSO app catalog, DLP reports | Quarterly |
| Identify browser extensions or desktop apps sending prompts to external AI services. | [To be captured] | Endpoint AI Tool | Endpoint Security Owner | Browser stores, desktop software | User-entered corporate content | High (if unsanctioned) | Unknown until validated | EDR telemetry, endpoint inventory, policy scan output | Monthly |
| Validate whether personal API keys are used in internal scripts/notebooks. | [To be captured] | Unmanaged API Integration | Team Lead + Security | External model providers | Internal source/data excerpts | High | Unknown until validated | Secret scanning, repo review, CI checks | Monthly |
| Check collaboration platforms for AI bots added without security review. | [To be captured] | Chat/Collab AI Bot | Collaboration Platform Owner | Slack/Teams app ecosystem | Chat content, files, metadata | High | Unknown until validated | Workspace app inventory, admin audit logs | Monthly |
| Verify model-assisted coding tools are approved and policy-conformant. | [To be captured] | AI Dev Tooling | Engineering Productivity Owner | IDE plugins, cloud inference | Source code and comments | Medium to High | Unknown until validated | IDE policy baselines, plugin inventory, DLP findings | Quarterly |
| Review network egress/DNS logs for traffic to unapproved model endpoints. | [To be captured] | Network-detected AI Usage | Network Security Owner | Firewall, proxy, DNS | Potential prompts/metadata in transit | High | Unknown until validated | Egress logs, DNS analytics, CASB reports | Monthly |
| Confirm data classification controls are applied before any external AI call. | [To be captured] | Data Governance Control | Data Governance Owner | Classification service, gateway | Sensitive/regulated data | High | Partially Confirmed or Unknown | Data classification policy mapping and gateway tests | Monthly |

## Escalation and Disposition
- **Immediate escalation**: Any unapproved AI tool touching confidential, regulated, or client data.
- **Containment action**: Disable access, rotate exposed credentials, and trigger incident review if exfiltration risk exists.
- **Registration requirement**: Newly discovered assets must be entered into the AI Asset Register before continued use.

## Completion Criteria
- All business units interviewed.
- All discovered AI usage mapped to owner and risk level.
- Unknown items tracked with due dates and accountable owners.
- Evidence artifacts linked for every high-risk finding.
