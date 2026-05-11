# Artifact Versioning Standard

## Purpose
Establish a consistent versioning process for readiness artifacts and templates.

## Versioning Model
Use semantic-style versioning for documentation artifacts:
- **Major**: incompatible structural or governance change.
- **Minor**: additive content updates with backward compatibility.
- **Patch**: typo fixes, formatting cleanup, non-substantive edits.

Format: `v<major>.<minor>.<patch>` (example: `v1.3.2`).

## Where to Record Version
Record version in:
1. In-document metadata header.
2. Change log section inside the document.
3. Git history (commit message should mention impacted artifact).

## Minimum Change Log Entry
Each version change should record:
- Date (UTC)
- Author
- Version
- Change summary
- Evidence impact (None | Updated | Deprecated)

## Supersession Rules
If an artifact is replaced:
1. Mark prior artifact `Superseded`.
2. Link to the replacement artifact path.
3. Preserve previous file in git history (no destructive deletion unless required).
