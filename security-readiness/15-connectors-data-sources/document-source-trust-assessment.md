# Build Priority 7 - Document Source Trust Assessment

Date: 2026-05-11

## Trust tiers
- **Tier 1 (Higher trust, managed internal systems)**: enterprise SaaS with scoped service principals and auditable APIs.
- **Tier 2 (Moderate trust)**: collaborative systems with variable ACL hygiene.
- **Tier 3 (Lower trust)**: open web, user-uploaded files, externally supplied API-ingested content.

## Assessment factors
- Source identity assurance
- Upstream ACL reliability
- Metadata integrity and provenance
- Update cadence / stale-data likelihood
- Poisoning resistance

## Assessment summary
| Source class | Poisoning risk | Stale data risk | Misconfiguration risk | Notes |
|---|---|---|---|---|
| Managed enterprise SaaS connectors (Drive, Jira, Confluence, Notion, etc.) | Medium | Medium | Medium | Depends on upstream ACL fidelity + connector scope correctness |
| Messaging/email (Slack, Gmail, Teams) | Medium-High | Medium | High | Channel/mailbox sprawl and broad token scopes can overexpose data |
| Web connector | High | High | High | URL scope errors and untrusted content injection risk |
| File uploads | High | Medium | Medium | User-provided content provenance uncertain; requires strong validation |
| Ingestion API | High | Medium | High | Caller trust and payload validation are critical |

## Evidence anchors
- Connector source catalog is centrally declared (`DocumentSource`).
- Runtime connector loading is controlled (`CONNECTOR_CLASS_MAP` + factory).
- Metadata parsing accepts string/list fields but connector-level metadata definitions vary.

## Required controls mapping
- Retrieval authorization controls: enforce permission sync where available and verify `AccessType` boundaries.
- Fail-closed rules: invalid credentials and permission validation failures must block connector activation.
- Audit events: index attempt status and connector health telemetry must support forensics.
