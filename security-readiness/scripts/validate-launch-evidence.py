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
PRE_LAUNCH_PHASE = "pre_launch_evidence_validation"
POST_LAUNCH_PHASE = "post_launch_output_validation"
LAUNCH_MODE_CONFIG_DEFAULT = "security-readiness/evidence-artifacts/launch-mode/launch-mode-config.json"
VALID_LAUNCH_MODES = {"RAG_ONLY", "RAG_PLUS_TOOLS"}


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
    parser.add_argument(
        "--launch-mode-config",
        default=LAUNCH_MODE_CONFIG_DEFAULT,
        help="Path to launch mode config JSON",
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


def resolve_launch_mode(rules: dict[str, Any], launch_mode_config_path: Path) -> str:
    mode = str(rules.get("launch_mode", "RAG_ONLY")).upper()
    if launch_mode_config_path.exists():
        try:
            payload = read_json_file(launch_mode_config_path)
            mode = str(payload.get("active_launch_mode", mode)).upper()
        except Exception:
            pass
    if mode not in VALID_LAUNCH_MODES:
        mode = "RAG_ONLY"
    return mode


def read_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_evidence_payload(path: Path) -> Any:
    if path.suffix.lower() == ".json":
        return read_json_file(path)
    return {"generated": path.exists() and path.stat().st_size > 0}


def get_nested_value(obj: Any, dotted_field: str) -> Any:
    current = obj
    for key in dotted_field.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current



def get_control_check_status(checked: list[dict[str, Any]], failed: list[dict[str, Any]], missing: list[dict[str, Any]], item_id: str) -> str:
    if any(item.get("id") == item_id for item in checked):
        return "PASS"
    if any(item.get("id") == item_id for item in failed):
        return "FAILED"
    if any(item.get("id") == item_id for item in missing):
        return "MISSING"
    return "UNKNOWN"

def main() -> int:
    args = parse_args()
    repo_root = Path.cwd()
    rules_path = repo_root / args.rules
    rules = load_yaml(rules_path)

    default_status = rules.get("default_status_when_unsure", "INCOMPLETE")
    if default_status not in VALID_STATUSES:
        default_status = "INCOMPLETE"

    tools_enabled = resolve_tools_enabled(args.tools_enabled, rules)
    launch_mode = resolve_launch_mode(rules, repo_root / args.launch_mode_config)
    phase_rules = rules.get("phases") or {}
    pre_launch_required = phase_rules.get(PRE_LAUNCH_PHASE) or []
    post_launch_required = phase_rules.get(POST_LAUNCH_PHASE) or []
    required = [*pre_launch_required, *post_launch_required]

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    checked, missing, failed, skipped = [], [], [], []

    for item in required:
        when = item.get("when", "always")
        phase = item.get("phase", PRE_LAUNCH_PHASE)
        if when == "tools_enabled" and not tools_enabled:
            skipped.append({
                "id": item.get("id"),
                "phase": phase,
                "reason": "Skipped because tools are disabled",
            })
            continue
        if when == "rag_plus_tools" and launch_mode != "RAG_PLUS_TOOLS":
            skipped.append({
                "id": item.get("id"),
                "phase": phase,
                "reason": "Skipped because launch mode is RAG_ONLY",
            })
            continue

        evidence_file = item.get("evidence_file")
        evidence_path = repo_root / evidence_file
        pass_field = item.get("pass_field")
        pass_values = item.get("pass_values", [])

        if not evidence_path.exists():
            missing.append({
                "id": item.get("id"),
                "phase": phase,
                "description": item.get("description"),
                "critical": bool(item.get("critical", True)),
                "expected_file": evidence_file,
                "status": "INCOMPLETE",
                "reason": "Required evidence artifact is missing",
            })
            continue

        try:
            payload = read_evidence_payload(evidence_path)
        except Exception as exc:
            failed.append({
                "id": item.get("id"),
                "phase": phase,
                "description": item.get("description"),
                "critical": bool(item.get("critical", True)),
                "expected_file": evidence_file,
                "status": "FAILED",
                "reason": f"Unable to parse evidence artifact: {exc}",
            })
            continue

        observed = get_nested_value(payload, pass_field)
        passes = (observed in pass_values) if pass_values else observed is not None
        if passes:
            checked.append({
                "id": item.get("id"),
                "phase": phase,
                "status": "COMPLETE",
                "observed": observed,
                "expected": pass_values,
                "file": evidence_file,
            })
        else:
            failed.append({
                "id": item.get("id"),
                "phase": phase,
                "description": item.get("description"),
                "critical": bool(item.get("critical", True)),
                "expected_file": evidence_file,
                "status": "FAILED",
                "reason": "Evidence artifact does not meet pass criteria",
                "observed": observed,
                "expected": pass_values,
            })

    def phase_items(items: list[dict[str, Any]], phase: str) -> list[dict[str, Any]]:
        return [i for i in items if i.get("phase") == phase]

    pre_missing = phase_items(missing, PRE_LAUNCH_PHASE)
    pre_failed = [f for f in phase_items(failed, PRE_LAUNCH_PHASE) if f.get("critical", True)]
    pre_blocking_issues = [*pre_missing, *pre_failed]
    pre_launch_status = "COMPLETE" if not pre_blocking_issues else ("FAILED" if pre_failed else default_status)

    post_missing = phase_items(missing, POST_LAUNCH_PHASE)
    post_failed = [f for f in phase_items(failed, POST_LAUNCH_PHASE) if f.get("critical", True)]
    post_blocking_issues = [*post_missing, *post_failed]
    post_launch_status = "COMPLETE" if not post_blocking_issues else ("FAILED" if post_failed else default_status)

    blocking_issues = [*missing, *[f for f in failed if f.get("critical", True)]]
    final_status = "COMPLETE" if pre_launch_status == "COMPLETE" and post_launch_status == "COMPLETE" else (
        "FAILED" if failed else default_status
    )
    allow_go = pre_launch_status == "COMPLETE" and not pre_blocking_issues



    output_dir = repo_root / args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "validator": "launch-evidence-completeness",
        "version": rules.get("version", 1),
        "generated_at": now,
        "rules_file": args.rules,
        "status": final_status,
        "phases": {
            PRE_LAUNCH_PHASE: {
                "status": pre_launch_status,
                "blocking_issues": len(pre_blocking_issues),
            },
            POST_LAUNCH_PHASE: {
                "status": post_launch_status,
                "blocking_issues": len(post_blocking_issues),
            },
        },
        "allow_go": allow_go,
        "draft_decision_only": bool(rules.get("draft_decision_only", True)),
        "default_status_when_unsure": default_status,
        "tools_enabled": tools_enabled,
        "active_launch_mode": launch_mode,
        "counts": {
            "complete": len(checked),
            "missing": len(missing),
            "failed": len(failed),
            "skipped": len(skipped),
            "required_total": len(required),
            "pre_launch_required_total": len(pre_launch_required),
            "post_launch_required_total": len(post_launch_required),
        },
        "checked": checked,
        "missing": missing,
        "failed": failed,
        "skipped": skipped,
        "control_checks": {
            "pure_control_unit_tests": get_control_check_status(checked, failed, missing, "pure_control_unit_tests"),
            "citation_source_leakage_dependency_light": get_control_check_status(checked, failed, missing, "citation_source_leakage_dependency_light"),
            "prompt_injection_boundary_dependency_light": get_control_check_status(checked, failed, missing, "prompt_injection_boundary_dependency_light"),
            "tool_authorization_dependency_light": get_control_check_status(checked, failed, missing, "tool_authorization_dependency_light"),
            "tool_runtime_context_guard_dependency_light": get_control_check_status(checked, failed, missing, "tool_runtime_context_guard_dependency_light"),
            "tool_runtime_wiring_adjacent": get_control_check_status(checked, failed, missing, "tool_runtime_wiring_adjacent"),
            "tool_runtime_wiring_research_agent_adjacent": get_control_check_status(checked, failed, missing, "tool_runtime_wiring_research_agent_adjacent"),
            "mcp_deny_before_dispatch_adjacent": get_control_check_status(checked, failed, missing, "mcp_deny_before_dispatch_adjacent"),
            "tier4_artifact_writer_scaffold": get_control_check_status(checked, failed, missing, "tier4_artifact_writer_scaffold"),
        },
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
            f"- Pre-launch status: **{pre_launch_status}**",
            f"- Post-launch status: **{post_launch_status}**",
            f"- Draft decision only: **{bool(rules.get('draft_decision_only', True))}**",
            f"- Active launch mode: **{launch_mode}**",
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
