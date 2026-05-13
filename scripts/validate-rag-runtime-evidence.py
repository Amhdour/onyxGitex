#!/usr/bin/env python3
import json
import sys
from pathlib import Path

E = Path("security-readiness/evidence-artifacts/version-2a-rag-runtime")
REQ = ["rag-runtime-final-status.json","rag-pytest-output.txt","rag-audit-events.json","rag-policy-decisions.json","rag-retrieval-log.json","rag-citation-check.json","rag-launch-gate-result.json","evidence-manifest.json","evidence-summary.md","blockers.md"]
errs = []
for name in REQ:
    if not (E / name).exists():
        errs.append(f"missing required artifact: {name}")

def load_json(name: str):
    try:
        return json.loads((E / name).read_text())
    except Exception as ex:
        errs.append(f"invalid json {name}: {ex}")
        return {}

status = load_json("rag-runtime-final-status.json") if (E / "rag-runtime-final-status.json").exists() else {}
for k, v in {"version":"2A","gate":"RAG_RUNTIME_EVIDENCE_GATE","harness_type":"LOCAL_RUNTIME_HARNESS","production_ready":False,"go_decision":False,"ci_verified":False,"staging_verified":False,"client_verified":False}.items():
    if status.get(k) != v: errs.append(f"status field {k} expected {v}, got {status.get(k)}")
ls = status.get("launch_status")
if ls not in {"PARTIAL_RUNTIME_EVIDENCE","NO_GO","NOT_ENOUGH_EVIDENCE"}: errs.append("invalid launch_status")
if ls == "GO": errs.append("launch_status must never be GO")

if ls == "PARTIAL_RUNTIME_EVIDENCE":
    if status.get("tests_total") != 8 or status.get("tests_passed") != 8 or status.get("tests_failed") != 0:
        errs.append("PARTIAL_RUNTIME_EVIDENCE must have 8/8 passing")
    if status.get("required_artifacts_present") is not True:
        errs.append("required_artifacts_present must be true for PARTIAL_RUNTIME_EVIDENCE")
    if any(v != "PASS" for v in status.get("required_proof", {}).values()):
        errs.append("all required_proof fields must be PASS for PARTIAL_RUNTIME_EVIDENCE")
if ls == "NOT_ENOUGH_EVIDENCE" and "block" not in (E / "blockers.md").read_text().lower():
    errs.append("blockers must be documented for NOT_ENOUGH_EVIDENCE")
if ls == "NO_GO" and all(v != "FAIL" for v in status.get("required_proof", {}).values()):
    errs.append("NO_GO must include failed proof fields")

print("PASS" if not errs else "FAIL")
for e in errs:
    print(f"- {e}")
sys.exit(0 if not errs else 1)
