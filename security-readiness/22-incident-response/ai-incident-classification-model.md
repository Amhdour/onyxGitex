# AI Incident Classification Model (Priority 14)

Date: 2026-05-11
Status: Operational Draft
Owner: AI Trust & Security Readiness

## Purpose
Provide a shared severity model for AI incidents in the Onyx internal knowledge assistant so Security, Engineering, Legal, and Client Success can classify, escalate, and respond consistently.

## Incident categories
- Retrieval Leak Incident: unauthorized disclosure or cross-boundary retrieval of private content.
- Prompt Injection Incident: malicious prompt/content manipulates model behavior, policy decisions, or tool usage.
- Tool Misuse Incident: unsafe or unauthorized tool invocation, parameter abuse, or excessive privilege use.
- Model Abuse Incident: jailbreak, harmful output generation, abusive automation, or policy bypass attempts.

## Severity levels

### Sev-1 Critical
**Definition:** Confirmed exposure of restricted client/internal data, high-confidence identity boundary failure, or active exploitation causing ongoing harm.

**Operational triggers:**
- Confirmed retrieval of restricted docs by unauthorized principal.
- Prompt injection resulting in protected data exfiltration or privileged tool execution.
- Tool event stream shows unauthorized destructive action.

**Target response:**
- Incident commander assigned within 15 minutes.
- Containment started immediately (fail-closed mode).
- Executive and client communications started within 60 minutes.

### Sev-2 High
**Definition:** Strong evidence of attempted or partial compromise with meaningful business/security risk but limited confirmed impact.

**Operational triggers:**
- Repeated policy denials + anomalous trace patterns indicating exploitation attempts.
- Tool misuse attempt blocked, but privilege model gaps detected.
- Potential leak indicators pending confirmation.

**Target response:**
- Incident commander assigned within 30 minutes.
- Containment within 60 minutes.
- Stakeholder notification within 2 hours.

### Sev-3 Medium
**Definition:** Contained or low-impact incident with no confirmed sensitive-data exposure; control weakness requires remediation.

**Operational triggers:**
- Single-session prompt injection attempt blocked by controls.
- Misconfigured retrieval filters detected pre-exposure.
- Abusive query pattern rate-limited with no spillover.

**Target response:**
- Triage within 4 hours.
- Remediation plan within 1 business day.

### Sev-4 Low
**Definition:** Suspicious or policy-violating activity with negligible risk and no evidence of control failure.

**Operational triggers:**
- Low-confidence alert with no corroborating evidence.
- User behavior violating acceptable use without security impact.

**Target response:**
- Queue for routine review.
- Track trend for abuse analytics.

## Required telemetry for classification
- Audit logs: auth events, access denials, policy decisions, admin changes.
- Runtime traces: request trace IDs, orchestration decisions, model/tool routing.
- Retrieval events: query, document IDs, ACL decision, connector source, snippet hashes.
- Tool events: tool name, caller identity, arguments (redacted), allow/deny result, execution status.

## Escalation path by severity
- Sev-1: On-call Security Engineer -> Incident Commander -> CISO delegate -> Legal/Privacy -> Client Executive Sponsor.
- Sev-2: On-call Security Engineer -> Incident Commander -> Product Security Lead -> Client Success Lead.
- Sev-3: Security Operations -> Feature Owner -> Risk/Compliance tracker.
- Sev-4: Security Operations queue; monthly governance review.

## Evidence classification outcome tags
Every incident record must include one of:
- **Verified**: supported by code/config/log evidence.
- **Partially Confirmed**: some indicators present, incomplete proof.
- **Unknown**: insufficient evidence; assumptions documented.
