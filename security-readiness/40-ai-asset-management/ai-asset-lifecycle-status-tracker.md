# AI Asset Lifecycle Status Tracker

_Date: 2026-05-11_
_Status: Draft for Security Readiness (Build Priority 32)_

## Lifecycle Definitions
- **Planned**: Approved but not implemented.
- **Active**: In active use and supported.
- **Maintenance**: Supported with limited feature changes.
- **Deprecated**: Scheduled for retirement; replacement identified.
- **Retired**: Removed from active runtime.

## Lifecycle Tracker

| Asset Name | Type | Owner | Dependency | Data Touched | Risk Level | Lifecycle Status | Target Transition | Evidence | Review Cadence |
|---|---|---|---|---|---|---|---|---|---|
| Onyx Web App | Application UI | Frontend Engineering | Backend APIs, SSO | User prompts, UX metadata | Medium | Active | N/A | `web/` codebase present and maintained | Monthly |
| Onyx Backend Server | AI Orchestration Service | Platform Engineering | LLM APIs, vector DB, authN/Z | Prompt/context handling | High | Active | N/A | `backend/onyx/server/` codebase present and maintained | Bi-weekly |
| Legacy/Alternate Model Endpoint Configurations | Integration Config | AI Platform Engineering | External model providers | Prompt and output payloads | High | Maintenance | Review for deprecation candidate | Runtime config references and deployment settings | Monthly |
| Legacy Connector Definitions (unused or low-value) | Ingestion Integration | Integrations Engineering | External content APIs | Synced docs and metadata | Medium | Maintenance | Candidate for Deprecated status after usage review | Connector inventory and sync ownership review | Quarterly |
| Experimental AI Features (non-default paths) | Feature Flags/Experiments | Product + AI Engineering | Backend feature flags | Limited prompts and response paths | Medium | Planned/Active (varies) | Promote to Active or retire | Feature flag configurations and roadmap references | Monthly |

## Lifecycle Governance Notes
- Deprecated candidates require explicit risk review before retirement.
- Retired status must include evidence of disabled execution path and removed credentials.
