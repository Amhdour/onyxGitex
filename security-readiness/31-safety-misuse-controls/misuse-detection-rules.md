# Misuse Detection Rules

## Purpose
Provide concrete, auditable rule logic for identifying enterprise assistant misuse attempts.

## Rule Set

| Rule ID | Pattern | Logic (High-Level) | Action | Signal |
|---|---|---|---|---|
| MDR-01 | Bulk confidential extraction | Detect requests for "all", "full dump", "entire folder", tied to restricted corpus. | Refuse + block retrieval | AMS-01 |
| MDR-02 | Employee PII targeting | Detect combinations of employee identifiers + sensitive fields (SSN, salary, health, discipline). | Refuse or redact | AMS-02 |
| MDR-03 | Unauthorized legal/financial directive | Detect imperative advice language ("what should we do legally", "guarantee compliance"). | Safe-complete + disclaimer + escalate option | AMS-03 |
| MDR-04 | Prompt injection instructions | Detect meta-instructions to ignore policy/system messages from user or retrieved text. | Ignore tainted content + continue guarded | AMS-04 |
| MDR-05 | Guardrail bypass phrasing | Detect role-play jailbreaks, policy override requests, encoded bypass attempts. | Refuse + abuse flag | AMS-05 |
| MDR-06 | Tool exfiltration path | Detect tool requests that export/download/transmit restricted content externally. | Deny tool call + alert | AMS-06 |
| MDR-07 | Secret/ops detail request | Detect queries for credentials, keys, incident playbook internals, privileged topology. | Refuse + high-level substitute | AMS-07 |
| MDR-08 | Missing policy audit metadata | Detect response decisions without required control IDs/decision fields. | Raise observability incident | AMS-08 |

## Tuning Guidance
- Start conservative for high-severity classes (prefer false positives over false negatives).
- Require periodic precision/recall review using labeled internal misuse samples.
- Maintain exception list with expiry and security owner approval.

## Rule Governance
- Each rule must have owner, version, last review date, and rollback path.
- Any weakening change requires risk sign-off and documented rationale.

## Verification Status
- **Verified**: Rule definitions documented.
- **Unknown**: Runtime detection efficacy metrics pending evaluation run.
