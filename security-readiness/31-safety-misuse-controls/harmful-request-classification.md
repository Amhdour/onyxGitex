# Harmful Request Classification

## Purpose
Classify misuse-oriented request patterns for an internal enterprise assistant and map them to required controls.

## Classification Taxonomy

| Class ID | Harmful Request Class | Description | Default Action | Severity |
|---|---|---|---|---|
| HRC-01 | Private Document Extraction | Requests to reveal confidential docs, bulk export, or hidden repositories. | Refuse + log + monitor | High |
| HRC-02 | Employee Data Misuse | Requests for payroll, health, disciplinary, identity, or contact data without purpose/authority. | Refuse or safe-complete with minimization | High |
| HRC-03 | Legal/Financial Overreliance | Requests for definitive legal/financial advice or binding interpretation. | Safe-complete + disclaimer + escalate when needed | Medium |
| HRC-04 | Prompt Injection | Requests or retrieved instructions attempting to override policy/system instructions. | Strip/ignore tainted instructions; continue with trusted context or refuse | High |
| HRC-05 | Policy Bypass | Attempts to disable safeguards, role-play bypass, or coercive re-prompts. | Refuse + flag abuse signal | High |
| HRC-06 | Tool Misuse | Commands to run unauthorized tools/actions, especially data exfiltration or privilege misuse. | Block tool path + refuse + alert | High |
| HRC-07 | Sensitive Operational Exposure | Requests for secrets, infrastructure internals, security response tactics. | Refuse + redacted high-level guidance only | High |

## Classifier Inputs
- User identity and role claims.
- Query intent and entities.
- Requested action verb (extract/export/reveal/ignore/override/run).
- Data sensitivity tags from retrieval layer.
- Prompt injection indicators in retrieved chunks.
- Tool invocation target and parameters.

## Confidence Bands
- **High confidence harmful**: immediate refuse/block path.
- **Medium confidence**: safe-complete with strict minimization; raise monitoring event.
- **Low confidence**: require additional context and maintain fail-closed for sensitive requests.

## Required Logging Fields
- `request_id`, `user_id`, `session_id`
- `harm_class_id`, `confidence_score`
- `decision` (allow/safe-complete/refuse/escalate)
- `control_ids_triggered`
- `retrieval_doc_ids` (redacted where required)

## Verification Status
- **Verified**: Taxonomy documented.
- **Partially Confirmed**: Real classifier labels and thresholds not yet validated in runtime.
