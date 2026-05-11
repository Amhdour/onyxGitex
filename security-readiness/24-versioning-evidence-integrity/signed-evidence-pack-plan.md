# Signed Evidence Pack Plan

## Objective
Plan phased introduction of cryptographic signing for evidence packs used in readiness reviews.

Date: 2026-05-11
Status: Planned (not yet fully enforced)

## Target Outcome
Each evidence pack is:
- Hashed (file-level + pack-level)
- Signed by authorized signer identity
- Verifiable by reviewers/auditors
- Traceable to Git commit and release tag

## Proposed Phases
1. **Phase 1 (Baseline)**
   - Generate unsigned SHA-256 manifest.
   - Store manifest with evidence artifacts.
2. **Phase 2 (Signer Introduction)**
   - Introduce signing key custody and rotation policy.
   - Sign manifest and/or package digest.
3. **Phase 3 (Verification Gate)**
   - Add CI verification step: reject unsigned/invalid manifests.
4. **Phase 4 (Audit Automation)**
   - Emit verification logs and attach to evidence pack.

## Signing Control Requirements
- Authorized signer allowlist
- Key rotation schedule
- Revocation handling
- Expired-signature rejection
- Verification evidence retention

## Current Confidence (2026-05-11)
- Manifest hashing workflow: **Verified** (local script implementation present).
- Signature enforcement workflow: **Unknown** (no CI policy evidence in this task scope).
