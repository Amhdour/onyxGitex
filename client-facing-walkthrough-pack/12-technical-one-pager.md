# 12 Technical One-Pager

Audience: CTO / security engineer / AI engineer.

- Architecture flow: identity -> policy -> retrieval/tooling -> observability -> decision gate
- Evidence artifacts: runtime evidence, CI artifacts, trace/audit links, decision records
- RAG controls: retrieval authorization, citation boundary, fail-closed handling
- Agent controls: agent identity, tool authorization, human approval checks
- Observability controls: trace correlation, audit timelines, incident reconstruction support
- Launch-gate controls: NO-GO/CONDITIONAL-GO/GO criteria tied to evidence
- Validation scripts: repository validators for consistency and claim boundaries
- CI artifacts: transport and preservation checks
- Limitations: local/demo/template evidence is not client production evidence
