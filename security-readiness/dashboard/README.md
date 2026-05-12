# Local Readiness Dashboard

This dashboard provides a local, evidence-driven readiness view for portfolio/client review.

## Run

1. Export dashboard data from current evidence artifacts:
   ```bash
   python3 security-readiness/scripts/export-dashboard-data.py
   ```
2. Serve locally:
   ```bash
   python3 -m http.server 8765 --directory security-readiness/dashboard
   ```
3. Open:
   `http://localhost:8765/index.html`

## Data source behavior

- Reads `security-readiness/dashboard/dashboard-data.json`.
- The exporter populates values from existing evidence artifacts where available.
- Missing evidence is shown as **Missing** (never assumed as Passed).
- No secrets are loaded into the dashboard.

## Current launch posture

This dashboard reflects the latest launch gate decision from evidence artifacts; it does not grant production approval by itself.
