#!/usr/bin/env python3
"""Validate launch-gate evidence completeness.

Outputs (under security-readiness/evidence-artifacts/evidence-validation/):
- validation-result.json
- validation-summary.md
- missing-evidence.json
- failed-evidence.json
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


VALID_STATUSES = {"COMPLETE", "INCOMPLETE", "FAILED", "STALE"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate launch evidence completeness")
    parser.add_argument(
        "--rules",
        default="security-readiness/47-evidence-automation/evidence-completeness-rules.yaml",
        help="Path to evidence completeness rules YAML",
    )
    parser.add_argument(
        "--output-dir",
        default="security-readiness/evidence-artifacts/evidence-validation",
        help="Directory for validator output artifacts",
    )
    parser.add_argument(
        "--tools-enabled",
        choices=["true", "false", "auto"],
        default="auto",
        help="Whether tools are enabled. auto uses rules.tools.enabled",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        try:
            import yaml  # type: ignore
        except Exception as exc:  # fail-closed
            raise RuntimeError("Rules file is not JSON and PyYAML is unavailable") from exc
        data = yaml.safe_load(raw)

    if not isinstance(data, dict):
        raise ValueError("Rules file must decode to an object")
    return data


def resolve_tools_enabled(cli_value: str, rules: dict[str, Any]) -> bool:
    if cli_value in {"true", "false"}:
        return cli_value == "true"

    rules_value = ((rules.get("tools") or {}).get("enabled"))
    return bool(rules_value)


def read_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_nested_value(obj: Any, dotted_field: str) -> Any:
    current = obj
    for key in dotted_field.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def main() -> int:
    args = parse_args()
    repo_root = Path.cwd()
    rules_path = repo_root / args.rules
    rules = load_yaml(rules_path)

    default_status = rules.get("default_status_when_unsure", "INCOMPLETE")
    if default_status not in VALID_STATUSES:
        default_status = "INCOMPLETE"

    tools_enabled = resolve_tools_enabled(args.tools_enabled, rules)
    required = rules.get("required_evidence") or []

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    checked, missing, failed, skipped = [], [], [], []

    for item in required:
        when = item.get("when", "always")
        if when == "tools_enabled" and not tools_enabled:
            skipped.append({
                "id": item.get("id"),
                "reason": "Skipped because tools are disabled",
            })
            continue

        evidence_file = item.get("evidence_file")
        evidence_path = repo_root / evidence_file
        pass_field = item.get("pass_field")
        pass_values = item.get("pass_values", [])

        if not evidence_path.exists():
            missing.append({
                "id": item.get("id"),
                "description": item.get("description"),
                "critical": bool(item.get("critical", True)),
                "expected_file": evidence_file,
                "status": "INCOMPLETE",
                "reason": "Required evidence artifact is missing",
            })
            continue

        try:
            payload = read_json_file(evidence_path)
        except Exception as exc:
            failed.append({
                "id": item.get("id"),
                "description": item.get("description"),
                "critical": bool(item.get("critical", True)),
                "expected_file": evidence_file,
                "status": "FAILED",
                "reason": f"Unable to parse evidence artifact: {exc}",
            })
            continue

        observed = get_nested_value(payload, pass_field)
        if observed in pass_values:
            checked.append({
                "id": item.get("id"),
                "status": "COMPLETE",
                "observed": observed,
                "expected": pass_values,
                "file": evidence_file,
            })
        else:
            failed.append({
                "id": item.get("id"),
                "description": item.get("description"),
                "critical": bool(item.get("critical", True)),
                "expected_file": evidence_file,
                "status": "FAILED",
                "reason": "Evidence artifact does not meet pass criteria",
                "observed": observed,
                "expected": pass_values,
            })

    blocking_issues = [*missing, *[f for f in failed if f.get("critical", True)]]
    final_status = "COMPLETE" if not blocking_issues else default_status

    if failed:
        final_status = "FAILED"

    allow_go = final_status == "COMPLETE" and not blocking_issues

    output_dir = repo_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "validator": "launch-evidence-completeness",
        "version": rules.get("version", 1),
        "generated_at": now,
        "rules_file": args.rules,
        "status": final_status,
        "allow_go": allow_go,
        "draft_decision_only": bool(rules.get("draft_decision_only", True)),
        "default_status_when_unsure": default_status,
        "tools_enabled": tools_enabled,
        "counts": {
            "complete": len(checked),
            "missing": len(missing),
            "failed": len(failed),
            "skipped": len(skipped),
            "required_total": len(required),
        },
        "checked": checked,
        "missing": missing,
        "failed": failed,
        "skipped": skipped,
    }

    (output_dir / "validation-result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (output_dir / "missing-evidence.json").write_text(json.dumps(missing, indent=2) + "\n", encoding="utf-8")
    (output_dir / "failed-evidence.json").write_text(json.dumps(failed, indent=2) + "\n", encoding="utf-8")

    summary_md = "\n".join(
        [
            "# Launch Evidence Validation Summary",
            "",
            f"- Generated at: `{now}`",
            f"- Overall status: **{final_status}**",
            f"- Allow GO: **{allow_go}**",
            f"- Draft decision only: **{bool(rules.get('draft_decision_only', True))}**",
            f"- Tools enabled: **{tools_enabled}**",
            "",
            "## Counts",
            f"- Complete: {len(checked)}",
            f"- Missing: {len(missing)}",
            f"- Failed: {len(failed)}",
            f"- Skipped: {len(skipped)}",
            "",
        ]
    )

    if missing:
        summary_md += "## Missing Evidence\n"
        for item in missing:
            summary_md += f"- `{item['id']}`: {item['reason']} (`{item['expected_file']}`)\n"
        summary_md += "\n"

    if failed:
        summary_md += "## Failed Evidence\n"
        for item in failed:
            summary_md += f"- `{item['id']}`: {item['reason']} (`{item['expected_file']}`)\n"
        summary_md += "\n"

    if skipped:
        summary_md += "## Skipped Evidence\n"
        for item in skipped:
            summary_md += f"- `{item['id']}`: {item['reason']}\n"

    (output_dir / "validation-summary.md").write_text(summary_md, encoding="utf-8")

    print(json.dumps({"status": final_status, "allow_go": allow_go, "output_dir": str(output_dir)}, indent=2))
    return 0 if final_status == "COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
