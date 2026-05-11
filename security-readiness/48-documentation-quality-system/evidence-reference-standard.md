# Evidence Reference Standard

## Purpose
Define mandatory evidence reference fields to support auditability and reproducibility.

## Mandatory Evidence Fields
Every evidence reference must include:
1. **Artifact Path** (repo-relative path)
2. **Command** (exact command executed)
3. **Timestamp (UTC)** (ISO 8601 preferred)
4. **Git Commit** (full or short hash tied to observation)
5. **Status** (`Verified` | `Partially Confirmed` | `Unknown`)

## Required Evidence Entry Format
Use a structured block for each evidence item:

- **Evidence ID:**
- **Artifact Path:**
- **Command:**
- **Timestamp (UTC):**
- **Git Commit:**
- **Status:**
- **Observed Result Summary:**
- **Assumptions / Gaps:**

## Status Definitions
- **Verified**: directly observed and reproducible from artifact/command output.
- **Partially Confirmed**: some evidence exists but coverage is incomplete.
- **Unknown**: no reliable evidence currently available.

## Redaction Rules
- Replace sensitive values with `[REDACTED]`.
- Do not remove structural context required for audit interpretation.
