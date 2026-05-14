import json, subprocess
from pathlib import Path

def test_v2d():
 subprocess.run(['python','scripts/run-agent-runtime-evidence.py'],check=True)
 e=Path('security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence')
 for n in ['version-2d-agent-runtime-status.json','agent-scenario-results.json','agent-trace-events.json','tool-authorization-decisions.json','sandbox-side-effect-checks.json','agent-incident-timeline.json','agent-launch-gate-result.json']:
  assert (e/n).exists()
 subprocess.run(['python','scripts/validate-agent-runtime-evidence.py'],check=True)
 sc=json.loads((e/'agent-scenario-results.json').read_text())['scenarios']
 tr=json.loads((e/'agent-trace-events.json').read_text())['traces']
 td={x['scenario_id']:x for x in json.loads((e/'tool-authorization-decisions.json').read_text())['records']}
 sb={x['scenario_id']:x for x in json.loads((e/'sandbox-side-effect-checks.json').read_text())['records']}
 tl=json.loads((e/'agent-incident-timeline.json').read_text())
 st=json.loads((e/'version-2d-agent-runtime-status.json').read_text())
 assert len(sc)==9 and len({x['trace_id'] for x in tr})==9
 assert all(x['actual_result']=='PASS' for x in sc)
 assert td['AGENT-2D-004']['fail_closed'] and td['AGENT-2D-004']['decision']=='DENY'
 assert td['AGENT-2D-005']['fail_closed'] and td['AGENT-2D-005']['decision']=='DENY'
 assert td['AGENT-2D-006']['tool_executed'] is False
 assert td['AGENT-2D-003']['tool_executed'] is False
 assert sb['AGENT-2D-007']['external_side_effect'] is False and sb['AGENT-2D-007']['side_effect_scope']=='sandbox_only'
 assert tl['reconstructable'] is True
 assert st['production_ready'] is False and st['go_decision'] is False
