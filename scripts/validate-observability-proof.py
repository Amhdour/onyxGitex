#!/usr/bin/env python3
import json
from pathlib import Path
import sys

E = Path("security-readiness/evidence-artifacts/version-2c-observability-proof")
REQ = ["version-2c-observability-status.json","observability-evidence-summary.md","trace-events.json","audit-correlation.json","policy-correlation.json","retrieval-correlation.json","citation-correlation.json","launch-gate-correlation.json","incident-timeline.json","dashboard-query-view.json","observability-evidence-manifest.json","validation-result.txt","blockers.md"]
errs=[]

for n in REQ:
    if not (E/n).exists(): errs.append(f"missing required artifact: {n}")

def j(name):
    try:return json.loads((E/name).read_text())
    except Exception as ex:
        errs.append(f"invalid json {name}: {ex}")
        return {}

if not errs:
    s=j("version-2c-observability-status.json")
    t=j("trace-events.json")
    a=j("audit-correlation.json")
    p=j("policy-correlation.json")
    r=j("retrieval-correlation.json")
    c=j("citation-correlation.json")
    l=j("launch-gate-correlation.json")
    i=j("incident-timeline.json")
    d=j("dashboard-query-view.json")
    m=j("observability-evidence-manifest.json")

    if s.get("version")!="2C" or s.get("gate")!="OBSERVABILITY_PROOF": errs.append("status version/gate mismatch")
    if s.get("production_ready") is not False or s.get("go_decision") is not False: errs.append("status must keep production_ready/go_decision false")
    if s.get("status") not in {"OBSERVABILITY_EVIDENCE_VERIFIED","OBSERVABILITY_EVIDENCE_GENERATED","NOT_ENOUGH_EVIDENCE","NO_GO"}: errs.append("invalid status")
    if s.get("status")=="OBSERVABILITY_EVIDENCE_VERIFIED":
        for k,v in {"observability_verified":True,"trace_count":8,"trace_correlation_verified":True,"audit_correlation_verified":True,"policy_correlation_verified":True,"retrieval_correlation_verified":True,"citation_correlation_verified":True,"launch_gate_correlation_verified":True,"incident_timeline_reconstructable":True,"dashboard_query_view_defined":True}.items():
            if s.get(k)!=v: errs.append(f"status field {k} expected {v}")

    traces=t.get("traces",[])
    if len(traces)!=8: errs.append("trace-events must contain exactly 8 traces")
    tids=[x.get("trace_id") for x in traces]
    if len(set(tids))!=len(tids): errs.append("trace IDs must be unique")
    pids={x.get("policy_decision_id") for x in p.get("records",[])}
    rids={x.get("retrieval_event_id") for x in r.get("records",[])}
    cids={x.get("citation_check_id") for x in c.get("records",[])}
    aids={x.get("audit_event_id") for x in a.get("records",[])}
    for tr in traces:
        if not tr.get("scenario_id"): errs.append("trace missing scenario_id")
        for f in ["policy_decision_id","retrieval_event_id","citation_check_id"]:
            if not tr.get(f): errs.append(f"trace missing {f}")
        if not tr.get("audit_event_ids"): errs.append("trace missing audit_event_ids")
        if tr.get("policy_decision_id") not in pids: errs.append(f"unresolved policy id {tr.get('policy_decision_id')}")
        if tr.get("retrieval_event_id") not in rids: errs.append(f"unresolved retrieval id {tr.get('retrieval_event_id')}")
        if tr.get("citation_check_id") not in cids: errs.append(f"unresolved citation id {tr.get('citation_check_id')}")
        for aid in tr.get("audit_event_ids",[]):
            if aid not in aids: errs.append(f"unresolved audit id {aid}")

    for name,obj in [("audit",a),("policy",p),("retrieval",r),("citation",c),("launch",l)]:
        if obj.get("correlation_status")!="PASS": errs.append(f"{name} correlation status must be PASS")
    if i.get("reconstructable") is not True: errs.append("incident timeline must be reconstructable")
    if d.get("external_dashboard_connected") is not False: errs.append("external_dashboard_connected must be false")

    for path in ["trace-events.json","launch-gate-correlation.json","version-2c-observability-status.json","incident-timeline.json","dashboard-query-view.json"]:
        txt=(E/path).read_text()
        if '"production_ready": true' in txt: errs.append(f"{path} claims production_ready true")
        if '"go_decision": true' in txt: errs.append(f"{path} claims go_decision true")
        if '"launch_status": "GO"' in txt: errs.append(f"{path} claims launch_status GO")

    mp={Path(x.get("path","")) .name:x for x in m.get("required_artifacts",[])}
    for n in [x for x in REQ if x!="observability-evidence-manifest.json"]:
        ent=mp.get(n)
        if not ent: errs.append(f"manifest missing {n}")
        else:
            if ent.get("exists") is not True: errs.append(f"manifest exists false for {n}")
            if not ent.get("sha256"): errs.append(f"manifest sha256 missing for {n}")

if errs:
    print("FAIL: " + "; ".join(errs))
    sys.exit(1)
print("PASS: observability-proof")
