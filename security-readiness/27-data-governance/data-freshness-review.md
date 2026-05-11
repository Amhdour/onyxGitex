# Data Freshness Review
Date: 2026-05-11 (UTC)
Scope: Retrieval corpus recency and update latency
Status: Unknown SLA values; control requirements documented

## Freshness Expectations by Data Class
- Policy/compliance documents: strict recency requirement (hours to 1 day).
- Knowledge-base/how-to content: moderate recency requirement (1-7 days).
- Archived references: low recency sensitivity (weeks+).

## Current Evidence Position
- Connector source types are enumerated, indicating multi-source ingestion.
- No repository-wide, source-specific freshness SLA registry was confirmed in this task.

## Freshness Risks
- Stale retrieval may return superseded policies or outdated operational instructions.
- Partial connector failures may silently degrade corpus coverage.
- Reindex lag can diverge searchable data from source-of-record.

## Evidence Needed
- Per-source `last_successful_sync` telemetry and alert thresholds.
- Dashboard/report proving ingestion and index lag distributions.
- Negative test showing fail-closed/flag behavior when freshness exceeds threshold.
