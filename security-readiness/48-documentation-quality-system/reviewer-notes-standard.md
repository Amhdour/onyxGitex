# Reviewer Notes Standard

## Purpose
Create a consistent format for reviewer feedback that improves traceability and closure tracking.

## Required Fields
Each reviewer note must include:
- Note ID
- Reviewer
- Timestamp (UTC)
- Artifact Path
- Section/Line Reference
- Severity (`Critical` | `High` | `Medium` | `Low`)
- Comment
- Requested Action
- Owner
- Due Date (UTC)
- Resolution Status (`Open` | `In Progress` | `Resolved` | `Rejected`)
- Resolution Evidence Reference (if resolved)

## Review Principles
- Comments must be specific and actionable.
- Security-critical gaps require explicit severity and closure evidence.
- Rejected notes must include rationale.
