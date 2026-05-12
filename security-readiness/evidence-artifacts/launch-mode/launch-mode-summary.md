# Launch Mode Summary

- Date (UTC): 2026-05-12
- Active launch mode: **RAG_ONLY**
- Default launch mode: **RAG_ONLY**

## RAG_ONLY

- Tool authorization evidence may be skipped.
- Skips must be explicit and explained in validator outputs.
- RAG runtime evidence is still required for GO.

## RAG_PLUS_TOOLS

- Tool authorization tests are required.
- Tool runtime wiring evidence is required.
- MCP/tool hardening evidence is required when MCP/tools are enabled.

## Current gate effect

- Current launch decision remains **NOT_ENOUGH_EVIDENCE**.
- RAG_ONLY does not bypass missing runtime evidence for retrieval/citation/prompt-injection controls.
