# Document Naming Standard

## Purpose
Define a reusable naming convention for security-readiness artifacts so documentation is searchable, version-aware, and auditable.

## Naming Pattern
Use lowercase kebab-case file names with an optional semantic version suffix.

`<artifact-name>[-v<major>.<minor>].md`

Examples:
- `trust-boundary-map.md`
- `abuse-case-catalog-v1.0.md`
- `launch-gate-decision-v2.1.md`

## Required Rules
1. Use only lowercase letters, numbers, and hyphens.
2. Use `.md` for narrative/report artifacts unless another extension is explicitly required.
3. Keep names descriptive and phase-aligned.
4. Do not include spaces, underscores, or special characters.
5. When a breaking structure update occurs, increment major version in file name or in-document metadata.

## Optional Prefixing
For folders with many peer artifacts, optional numeric or domain prefixes are allowed:
- `01-...`, `02-...` for workflow order.
- `auth-...`, `retrieval-...`, `audit-...` for domain grouping.

## Metadata Block Requirement
Each document should include these fields near the top:
- `Document Owner`
- `Last Updated (UTC)`
- `Version`
- `Status (Draft | Approved | Superseded | Archived)`
