#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, subprocess, os
from datetime import datetime, timezone
from pathlib import Path

LAB = Path(__file__).resolve().parent
OUT = LAB / "real-langgraph-attempt-output.json"
SUMMARY = LAB / "graph-runtime-artifacts" / "graph-runtime-summary.json"
HARNESS = LAB / "run-real-langgraph-or-compat-harness.py"

def now(): return datetime.now(timezone.utc).isoformat()

def write(payload): OUT.write_text(json.dumps(payload, indent=2)+"\n")

def main() -> int:
    lg = importlib.util.find_spec("langgraph") is not None
    payload = {
        "langgraph_available": lg,
        "attempted_real_runtime": False,
        "real_runtime_status": "REAL_LANGGRAPH_NOT_AVAILABLE" if not lg else "REAL_LANGGRAPH_ATTEMPT_FAILED",
        "runtime_mode_observed": "DETERMINISTIC_GRAPH_COMPATIBILITY_MODE",
        "graph_summary_path": str(SUMMARY),
        "evidence_implication": "Real runtime not available; compatibility evidence remains applicable." if not lg else "Real runtime attempt executed; inspect summary and status.",
        "launch_gate_implication": "NO_GO",
        "checked_at_utc": now(),
    }
    if not lg:
        write(payload)
        return 0
    payload["attempted_real_runtime"] = True
    env = os.environ.copy()
    env["FORCE_REAL_LANGGRAPH_RUNTIME"] = "1"
    rc = subprocess.run(["python", str(HARNESS)], env=env).returncode
    if SUMMARY.exists():
        s = json.loads(SUMMARY.read_text())
        payload["runtime_mode_observed"] = s.get("runtime_mode", "UNKNOWN")
        real_used = bool(s.get("real_langgraph_used")) or s.get("runtime_mode") == "REAL_LANGGRAPH_RUNTIME"
        if rc == 0 and real_used:
            payload["real_runtime_status"] = "REAL_LANGGRAPH_RUNTIME_PASS"
            write(payload)
            return 0
    payload["real_runtime_status"] = "REAL_LANGGRAPH_ATTEMPT_FAILED"
    write(payload)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
