# Build Priority 12.126 — Deployment Risk Assessment

Date: 2026-05-11  
Status: Partially Confirmed

## Risk Register

1. **Risk:** Default credential carry-over to production  
   **Impact:** Unauthorized access / data compromise  
   **Likelihood:** Medium  
   **Evidence:** env templates and compose defaults include development-style values.  
   **Status:** Partially Confirmed

2. **Risk:** Excessive port exposure in non-dev environments  
   **Impact:** Enlarged attack surface  
   **Likelihood:** Medium  
   **Evidence:** `docker-compose.dev.yml` exposes internal service ports.  
   **Status:** Verified (artifact-level)

3. **Risk:** Incomplete environment segmentation (no explicit staging standard)  
   **Impact:** Pre-prod/prod control bypass and drift  
   **Likelihood:** Medium  
   **Evidence:** No dedicated staging manifest found in reviewed scope.  
   **Status:** Partially Confirmed

4. **Risk:** Configuration drift between compose and helm paths  
   **Impact:** Inconsistent controls and runtime surprises  
   **Likelihood:** Medium  
   **Evidence:** Distinct deployment systems with different defaults and patterns.  
   **Status:** Partially Confirmed

5. **Risk:** Rollback uncertainty without tested runbook evidence  
   **Impact:** Prolonged outage / unsafe recovery actions  
   **Likelihood:** Medium  
   **Status:** Unknown

## Priority Mitigations
- Enforce production credential policy (no defaults, no plaintext in repo-managed files).
- Add deployment boundary policy checks in CI.
- Introduce environment parity and drift checks across compose/helm.
- Validate rollback procedure in staging before production approval.
