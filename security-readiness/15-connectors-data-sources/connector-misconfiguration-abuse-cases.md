# Build Priority 7 - Connector Misconfiguration Abuse Cases

Date: 2026-05-11

## Abuse cases

### AC-01: Over-broad OAuth/API token scope
- **Path**: Admin configures connector with privileged token -> connector ingests unauthorized corpus.
- **Impact**: Confidentiality breach.
- **Controls**: Connector permission review checklist; `validate_connector_settings`; enforce `AccessType` boundary checks.
- **Evidence needed**: Token scope checklist + negative retrieval tests.

### AC-02: Public cc-pair assigned to sensitive source
- **Path**: Sensitive connector set to `AccessType.PUBLIC`.
- **Impact**: Unauthorized data exposure including anonymous access.
- **Controls**: Admin change review; automated detector for sensitive-source/public mismatch.
- **Evidence needed**: Policy rule + alert output + remediation logs.

### AC-03: Permission sync disabled or failing silently
- **Path**: Connector requires ACL sync, but runs without effective permission updates.
- **Impact**: Stale or incorrect document authorization.
- **Controls**: `AccessType.SYNC` validation path; perm-sync metrics and error monitoring.
- **Evidence needed**: perm-sync success/error dashboards and incident drill.

### AC-04: Web/File/Ingestion source poisoning
- **Path**: Untrusted content injected, then retrieved as authoritative answer context.
- **Impact**: Integrity compromise / model manipulation.
- **Controls**: Source trust tagging; moderation/validation gates; retrieval provenance requirements.
- **Evidence needed**: Poisoning test cases with blocked/flagged outcomes.

### AC-05: Connector not quarantined after compromise
- **Path**: Compromised credential/source remains active during incident.
- **Impact**: Ongoing ingestion of hostile or overexposed data.
- **Controls**: Fast disable path (`PAUSED`) and deletion/quarantine flow (`DELETING`), plus reindex/revocation.
- **Evidence needed**: Time-to-disable exercise with timestamped logs.
