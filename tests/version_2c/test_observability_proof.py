import json
import subprocess
from pathlib import Path

E = Path("security-readiness/evidence-artifacts/version-2c-observability-proof")

def test_observability_proof_end_to_end():
    run = subprocess.run(["python", "scripts/run-observability-proof.py"], capture_output=True, text=True)
    assert run.returncode == 0, run.stdout + run.stderr
    req=["version-2c-observability-status.json","observability-evidence-summary.md","trace-events.json","audit-correlation.json","policy-correlation.json","retrieval-correlation.json","citation-correlation.json","launch-gate-correlation.json","incident-timeline.json","dashboard-query-view.json","observability-evidence-manifest.json","validation-result.txt","blockers.md"]
    for n in req:
        assert (E/n).exists(), n

    val = subprocess.run(["python", "scripts/validate-observability-proof.py"], capture_output=True, text=True)
    assert val.returncode == 0, val.stdout + val.stderr

    traces = json.loads((E/"trace-events.json").read_text())["traces"]
    assert len(traces) == 8
    assert len({t["trace_id"] for t in traces}) == 8

    audits={r["audit_event_id"] for r in json.loads((E/"audit-correlation.json").read_text())["records"]}
    policies={r["policy_decision_id"] for r in json.loads((E/"policy-correlation.json").read_text())["records"]}
    retrievals={r["retrieval_event_id"] for r in json.loads((E/"retrieval-correlation.json").read_text())["records"]}
    citations={r["citation_check_id"] for r in json.loads((E/"citation-correlation.json").read_text())["records"]}

    for t in traces:
        assert t["policy_decision_id"] in policies
        assert t["retrieval_event_id"] in retrievals
        assert t["citation_check_id"] in citations
        assert all(a in audits for a in t["audit_event_ids"])
        assert t["production_ready"] is False
        assert t["go_decision"] is False

    incident = json.loads((E/"incident-timeline.json").read_text())
    assert incident["reconstructable"] is True
