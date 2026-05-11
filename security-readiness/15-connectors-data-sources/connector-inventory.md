# Build Priority 7 - Connector Inventory

Date: 2026-05-11
Status labels: **Verified**, **Partially Confirmed**, **Unknown**

## Method
- Enumerated supported connector source types from `DocumentSource` enum.
- Mapped runtime loader wiring via `CONNECTOR_CLASS_MAP` and connector factory.
- Confirmed connector lifecycle modes (load / poll / slim / event) from interfaces.

## Inventory (code/config referenced)

| Connector name | Source system | Permissions required | Ingestion path | Document metadata captured | Access-control dependency | Evidence status |
|---|---|---|---|---|---|---|
| Slack | Slack workspace channels/DMs | Bot/user token scopes configured in connector credentials; permission-sync capability exists in connector framework | `backend/onyx/connectors/slack/connector.py` via `CONNECTOR_CLASS_MAP` -> factory instantiate/load | Connector `Document.metadata` structure is connector-defined, parsed by base metadata parser when string/list values | Depends on `AccessType` + optional permission sync validation (`validate_perm_sync`) | **Partially Confirmed** |
| Google Drive | Google Workspace Drive | OAuth/service account credentials; permission sync path supported | `backend/onyx/connectors/google_drive/connector.py` mapped in registry and loaded through factory | Connector-defined metadata in `Document.metadata` | Depends on connector permission sync + `AccessType.SYNC` flows | **Partially Confirmed** |
| Gmail | Google Workspace mailboxes | OAuth/service account + admin delegation (connector-specific) | `backend/onyx/connectors/gmail/connector.py` | Connector-defined metadata in `Document.metadata` | Permission sync capable (`retrieve_all_slim_docs_perm_sync`) + `AccessType.SYNC` | **Partially Confirmed** |
| Confluence/Jira/Notion/etc. | SaaS APIs | API token / OAuth credentials per connector | Mapped by `CONNECTOR_CLASS_MAP` and instantiated by factory | Connector-defined metadata in `Document.metadata` | Access model gates via CC-pair access type and optional perm sync validation | **Partially Confirmed** |
| File | Onyx-managed uploaded files | No external SaaS credentials required; local file references in connector config | `backend/onyx/connectors/file/connector.py` mapping and admin connector APIs | Metadata from file parsing pipeline and connector metadata conventions | Access governed via CC pair access/group membership and document permission propagation | **Partially Confirmed** |
| Web | Public/internal web URLs | URL-only connector configuration (plus optional auth depending on endpoint) | `backend/onyx/connectors/web/connector.py` mapping and indexing pipeline | URL/title/body-derived metadata set by connector | Access primarily via connector visibility + retrieval controls | **Partially Confirmed** |
| Ingestion API | API-driven source uploads | API key / auth to ingestion endpoint (no connector secret in this review) | `backend/onyx/server/onyx_api/ingestion.py` and `DocumentSource.INGESTION_API` special-case | Metadata supplied by API payload + processing pipeline | Access type and tenant controls at API + storage layers | **Partially Confirmed** |

## Baseline findings
1. Connector source inventory is defined centrally in `DocumentSource` and wiring in `CONNECTOR_CLASS_MAP`; runtime creation is centralized in `instantiate_connector`.
2. Credential use is abstracted through DB-backed credential providers, reducing direct secret handling in orchestration code.
3. Connector metadata schema is not globally normalized; each connector controls `Document.metadata` content, increasing source-by-source validation needs.

## Evidence references
- `backend/onyx/configs/constants.py`
- `backend/onyx/connectors/registry.py`
- `backend/onyx/connectors/factory.py`
- `backend/onyx/connectors/interfaces.py`
- `backend/onyx/server/onyx_api/ingestion.py`
