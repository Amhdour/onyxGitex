#!/usr/bin/env python3
import json
from pathlib import Path

p = Path("security-readiness/evidence-artifacts/version-2c-observability-proof/version-2c-observability-status.json")
s = json.loads(p.read_text())
for k in ["version","gate","status","production_ready","go_decision","observability_verified","external_observability_connected","trace_count","trace_correlation_verified","audit_correlation_verified","policy_correlation_verified","retrieval_correlation_verified","citation_correlation_verified","launch_gate_correlation_verified","incident_timeline_reconstructable","dashboard_query_view_defined","next_required_action"]:
    print(f"{k}: {s.get(k)}")
