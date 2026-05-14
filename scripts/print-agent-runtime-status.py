#!/usr/bin/env python3
import json
from pathlib import Path
p=Path('security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence/version-2d-agent-runtime-status.json')
if not p.exists():
 print('status file not found'); raise SystemExit(1)
s=json.loads(p.read_text())
for k in ['version','gate','status','harness_type','production_ready','go_decision','agent_runtime_verified','real_langgraph_runtime_verified','external_tool_execution_enabled','scenario_count','scenarios_passed','scenarios_failed','tool_authorization_verified','human_approval_verified','unknown_tool_fail_closed_verified','missing_identity_fail_closed_verified','prompt_injection_tool_escalation_blocked','sandbox_no_side_effect_verified','agent_incident_timeline_reconstructable','agent_launch_gate_verified','next_required_action']:
 print(f"{k}: {s.get(k)}")
