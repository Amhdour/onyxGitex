# LangGraph Autonomous Agent Runtime Lab

## Purpose

This folder adds a LangGraph-oriented autonomous-agent practice lab to the existing AI Trust & Security Readiness project.

The goal is not to claim that an autonomous agent is production-safe. The goal is to create a concrete runtime lab for studying, testing, and collecting evidence around agent identity, tool authorization, human approval, memory boundaries, fail-closed behavior, auditability, and launch-gate decisions.

## Current status

`FOUNDATION_CREATED / NOT_RUNTIME_VERIFIED`

## Why this exists

The existing Onyx-based work is strongest for RAG readiness. Autonomous agents require additional runtime questions:

- Which identity is the agent acting under?
- Which tools can the agent call?
- Which actions require human approval?
- What happens when identity, policy, or tool registry data is missing?
- Can prompt injection cause tool escalation?
- Are tool calls logged in a way that supports audit and incident response?

## Intended architecture

```text
User request
  -> LangGraph agent state
  -> identity context
  -> policy decision
  -> tool registry lookup
  -> human approval gate when required
  -> tool execution or denial
  -> audit event
  -> final response
  -> launch-gate evidence
```

## Initial lab files

| File | Purpose |
|---|---|
| `langgraph-agent-runtime-skeleton.py` | Minimal runnable-style skeleton showing where LangGraph nodes and policy gates belong. |
| `tool-registry.json` | Example tool inventory with risk levels and approval requirements. |
| `policy-inputs/allow-read-docs.json` | Example ALLOW policy input. |
| `policy-inputs/deny-sensitive-without-approval.json` | Example DENY / REQUIRE_APPROVAL policy input. |
| `final-run-status.json` | Machine-readable evidence status for this lab. |
| `launch-gate-notes.md` | Agent launch-gate interpretation and non-claims. |

## What this lab should prove later

Future runtime evidence should prove or disprove:

1. Authorized low-risk tools can execute.
2. Unauthorized tools are denied.
3. Sensitive tools require human approval.
4. Unknown tools fail closed.
5. Missing identity fails closed.
6. Prompt-injection attempts cannot override policy.
7. Tool decisions are logged.
8. Launch-gate status is based on evidence, not intent.

## What this lab does not prove yet

This initial addition does not prove:

- LangGraph runtime execution passed.
- Any production agent is safe to launch.
- Tool authorization is enforced in a deployed runtime.
- Human approval is enforced in a deployed runtime.
- Prompt injection is fully mitigated.

## Next required action

Implement and execute a small LangGraph runtime test harness that emits:

- allowed-tool-call-log.json
- denied-tool-call-log.json
- human-approval-required-log.json
- fail-closed-log.json
- runtime-trace.json
- final-run-status.json
