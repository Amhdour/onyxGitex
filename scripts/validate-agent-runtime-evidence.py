#!/usr/bin/env python3
import json,sys
from pathlib import Path
E=Path('security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence')
req=["version-2d-agent-runtime-status.json","agent-runtime-evidence-summary.md","agent-scenario-results.json","agent-trace-events.json","agent-identity-events.json","tool-authorization-decisions.json","human-approval-events.json","unknown-tool-events.json","prompt-injection-tool-escalation-results.json","sandbox-side-effect-checks.json","agent-audit-events.json","agent-incident-timeline.json","agent-launch-gate-result.json","agent-runtime-evidence-manifest.json","validation-result.txt","blockers.md"]
errs=[]
for n in req:
 if not (E/n).exists(): errs.append(f"missing {n}")

def j(n):
 try:return json.loads((E/n).read_text())
 except Exception as ex: errs.append(f"invalid json {n}: {ex}"); return {}
if not errs:
 s=j('version-2d-agent-runtime-status.json'); sc=j('agent-scenario-results.json'); tr=j('agent-trace-events.json'); td=j('tool-authorization-decisions.json'); ti=j('agent-incident-timeline.json'); lg=j('agent-launch-gate-result.json'); mf=j('agent-runtime-evidence-manifest.json')
 if s.get('version')!='2D' or s.get('gate')!='AGENT_RUNTIME_EVIDENCE_GATE': errs.append('bad status version/gate')
 if s.get('production_ready') or s.get('go_decision'): errs.append('status production/go must be false')
 allowed={"AGENT_RUNTIME_EVIDENCE_VERIFIED","AGENT_RUNTIME_EVIDENCE_GENERATED","LANGGRAPH_RUNTIME_VERIFIED","NOT_ENOUGH_EVIDENCE","NO_GO"}
 if s.get('status') not in allowed: errs.append('invalid status')
 if s.get('status')=='AGENT_RUNTIME_EVIDENCE_VERIFIED':
  for k,v in {'agent_runtime_verified':True,'harness_type':'LOCAL_AGENT_RUNTIME_HARNESS','scenario_count':9,'scenarios_passed':9,'scenarios_failed':0,'tool_authorization_verified':True,'human_approval_verified':True,'unknown_tool_fail_closed_verified':True,'missing_identity_fail_closed_verified':True,'prompt_injection_tool_escalation_blocked':True,'sandbox_no_side_effect_verified':True,'agent_incident_timeline_reconstructable':True,'agent_launch_gate_verified':True}.items():
   if s.get(k)!=v: errs.append(f'status {k} mismatch')
 scenarios=sc.get('scenarios',[])
 if len(scenarios)!=9: errs.append('need 9 scenarios')
 if any(x.get('actual_result')!='PASS' for x in scenarios): errs.append('all scenarios must PASS')
 traces=tr.get('traces',[])
 if len(traces)!=9 or len({x.get('trace_id') for x in traces})!=9: errs.append('need 9 unique traces')
 for t in traces:
  if not all([t.get('identity_event_id'),t.get('tool_decision_id'),t.get('sandbox_check_id'),t.get('audit_event_ids')]): errs.append(f"trace links missing {t.get('trace_id')}")
 tmap={x['scenario_id']:x for x in td.get('records',[])}
 if not (tmap.get('AGENT-2D-004',{}).get('fail_closed') and tmap.get('AGENT-2D-004',{}).get('decision')=='DENY'): errs.append('unknown tool fail_closed invalid')
 if not (tmap.get('AGENT-2D-005',{}).get('fail_closed') and tmap.get('AGENT-2D-005',{}).get('decision')=='DENY'): errs.append('missing identity fail_closed invalid')
 if tmap.get('AGENT-2D-006',{}).get('tool_executed') is not False: errs.append('prompt escalation executed')
 if ti.get('reconstructable') is not True: errs.append('timeline not reconstructable')
 if lg.get('production_ready') or lg.get('go_decision'): errs.append('launch gate production/go must be false')
 if s.get('real_langgraph_runtime_verified') is True: errs.append('langgraph claim must be false')
 rset={Path(x.get('path','')).name for x in mf.get('required_artifacts',[])}
 for n in [x for x in req if x!='agent-runtime-evidence-manifest.json']:
  if n not in rset: errs.append(f'manifest missing {n}')
 text='\n'.join((E/n).read_text() for n in ['version-2d-agent-runtime-status.json','agent-scenario-results.json','agent-trace-events.json','agent-incident-timeline.json','agent-launch-gate-result.json'])
 if '"production_ready": true' in text or '"go_decision": true' in text or '"agent_launch_status": "GO"' in text: errs.append('forbidden true/go claim')
if errs:
 print('FAIL: ' + '; '.join(errs)); sys.exit(1)
print('PASS: agent-runtime-evidence')
