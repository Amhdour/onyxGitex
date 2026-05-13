#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import platform
import sys
from pathlib import Path

LAB_DIR = Path(__file__).resolve().parent
OUT = LAB_DIR / "runtime-artifacts" / "langgraph-dependency-check.json"


def available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    lg = available("langgraph")
    te = available("typing_extensions")
    pd = available("pydantic")
    mode = "REAL_LANGGRAPH_AVAILABLE" if lg else "DETERMINISTIC_GRAPH_COMPATIBILITY_MODE"
    data = {
        "python_version": platform.python_version(),
        "python_executable": sys.executable,
        "langgraph_available": lg,
        "typing_extensions_available": te,
        "pydantic_available": pd,
        "dependency_status": "READY_FOR_REAL_LANGGRAPH_RUNTIME" if lg else "READY_FOR_COMPATIBILITY_RUNTIME",
        "selected_runtime_mode": mode,
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
