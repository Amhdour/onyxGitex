# Suspicious Tool-Use Pattern List

Date: 2026-05-11  
Status: Draft (Detection Content)

All examples are fictional and safe.

| Signal category | Example | Severity | Detection source | Response | Evidence | Owner | Trend metric |
|---|---|---|---|---|---|---|---|
| Privileged tool escalation | User asks assistant to run admin-only connector action | Critical | Tool invocation authorization logs | Deny invocation, trigger pager alert, open incident | Tool deny event, alert ID, incident ID | Platform Security | Privileged-tool deny rate |
| Destructive operation request | "Delete all records in index X" | Critical | Tool action classifier + allowlist policy engine | Hard block; require break-glass workflow outside assistant | Policy deny record, workflow reference | Platform Owner + SRE | Destructive-action block count |
| Hidden side-effect chaining | "Summarize docs then quietly email exports externally" | High | Multi-step plan audit + egress control logs | Refuse hidden egress, terminate chain, alert | Plan trace ID, egress deny event | Security Engineering | Side-effect chain alerts/week |
| Off-hours abnormal tool use | Elevated tool requests at unusual times for user baseline | Medium | Behavioral analytics + tool logs | Step-up verification, temporary lock | Behavior score, auth challenge logs | Security Operations | Off-hours anomaly rate |
| Policy mismatch execution | Tool called with parameters outside approved policy bounds | High | Runtime policy decision logs | Fail closed, mark case for review board | Policy mismatch ID, case queue ID | Tooling Owner | Parameter-mismatch trend |
