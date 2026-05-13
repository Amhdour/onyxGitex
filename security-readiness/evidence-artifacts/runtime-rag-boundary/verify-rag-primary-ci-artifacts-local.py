#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
ART = BASE / "ci-downloaded-artifact"
OUT = BASE / "rag-ci-artifact-verification-output.json"
REQ = ["final-run-status.json","pytest-output.txt","test-command.txt","git-commit.txt","timestamp.txt","runtime-status.txt"]

def now(): return datetime.now(timezone.utc).isoformat()
exists = ART.exists() and ART.is_dir()
present=[];missing=[];json_check={}
status="RAG_CI_ARTIFACT_NOT_AVAILABLE"
if exists:
    for r in REQ:
        p=ART/r
        (present if p.exists() else missing).append(r)
    j=ART/"final-run-status.json"
    if j.exists():
        try: json.loads(j.read_text()); json_check["final-run-status.json"]="VALID"
        except Exception as e: json_check["final-run-status.json"]=f"INVALID: {e}"
    if missing or json_check.get("final-run-status.json")!="VALID":
        status="RAG_CI_ARTIFACT_INCOMPLETE"
    else:
        status="RAG_CI_ARTIFACT_VERIFIED"
out={"artifact_dir":str(ART),"artifact_dir_exists":exists,"required_files_present":present,"required_files_missing":missing,"json_validation":json_check,"verification_status":status,"checked_at_utc":now()}
OUT.write_text(json.dumps(out,indent=2)+"\n")
print(status)
raise SystemExit(1 if status=="RAG_CI_ARTIFACT_INCOMPLETE" else 0)
