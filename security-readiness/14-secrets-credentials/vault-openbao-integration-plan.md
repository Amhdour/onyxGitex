# Vault / OpenBao Integration Plan (Priority 6)

Date: 2026-05-11
Status: Planned

## Goal
Move from environment-file-centric secret delivery to centralized secret management with auditable, identity-bound access.

## Phased plan

### Phase 1: Inventory and namespace design
- Define secret paths by environment and service:
  - `kv/[env]/onyx/backend/[secret-name]`
  - `kv/[env]/onyx/workers/[secret-name]`
- Map current env var names to vault keys one-to-one.

### Phase 2: AuthN/AuthZ setup
- Use workload identity auth method (Kubernetes auth / cloud IAM auth).
- Define per-service policies permitting read on minimum paths only.
- Explicitly deny list/read on non-owned paths.

### Phase 3: Runtime injection
- Integrate via Vault Agent Injector or CSI driver.
- Replace direct plaintext env fallback patterns in production manifests with secret references.
- Add startup validation that required secret files/vars exist, else fail closed.

### Phase 4: Rotation automation
- Enable versioned secrets and rotation pipelines.
- Schedule rotation by class (critical/high/medium) from runbook.
- Add post-rotation smoke tests and automatic rollback guardrails.

### Phase 5: Audit and detection
- Ship vault audit logs to SIEM.
- Alert on denied access, anomalous read rates, and after-hours break-glass usage.
- Correlate secret reads with deployment and runtime trace ids.

## Compatibility constraints
- Existing compose templates are development-oriented and may include defaults; production overlays must override with vault-backed references.
- Some scripts expect env vars directly; migration may require wrappers that source from injected secret files.

## Success criteria
- 100% production secrets sourced from Vault/OpenBao.
- 0 high-risk static secrets in deployment manifests.
- Verified audit trail for all secret reads and rotations.
