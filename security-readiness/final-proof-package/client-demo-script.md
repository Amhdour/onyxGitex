# Client Demo Script

**Audience:** Client stakeholders (security, risk, platform, product)  
**Duration:** 30–40 minutes

## 1. Executive Framing
- This is a readiness engagement for an internal company knowledge assistant.
- Pattern inspiration: **Morgan Stanley-style** internal RAG assistant approach.
- No affiliation is claimed; this is a reusable security-readiness pattern.

## 2. Business-Risk Framing
We focus on preventing:
- unauthorized document retrieval,
- identity boundary bypass,
- unsupported or ungrounded answers,
- unsafe tool execution,
- weak audit posture at launch.

## 3. What We Built for You
- Control layer around retrieval/input/output/tooling boundaries.
- Evidence lifecycle with validator and launch gate.
- Review artifacts usable by security, audit, and delivery teams.

## 4. Launch Mode Options
### Mode A: `RAG_ONLY`
- Lower risk profile.
- Appropriate while tool authorization evidence is still maturing.

### Mode B: `RAG_PLUS_TOOLS`
- Higher capability, higher risk.
- Requires explicit tool authorization and identity propagation proof.

## 5. Controls Demonstrated
- `RetrievalAuthorizationGuard`
- `RetrievalGuardAdapter`
- `BypassACLContract`
- `TrustedSystemContextInputBoundary`
- `CitationSourceLeakageFilter`
- `PromptInjectionBoundary`
- `AuditLogger`
- `RuntimeTracer`
- `LaunchGateEngine`

## 6. Evidence Maturity and Current Status
- Evidence tiers are tracked from design intent through launch-grade evidence.
- Some important categories passed (dependency-light, runtime-adjacent, validator/dashboard generation).
- Critical launch categories remain incomplete; therefore launch stays blocked.

## 7. Launch Decision
- Current gate output: `NOT_ENOUGH_EVIDENCE`.
- This is expected and correct under a fail-closed policy.
- We do **not** recommend a GO decision yet.

## 8. Next Actions Before GO Can Be Considered
1. Complete backend runtime retrieval authorization evidence.
2. Complete runtime citation leakage and prompt-injection/red-team evidence.
3. Complete `RAG_PLUS_TOOLS` tool authorization wiring and evidence.
4. Close evidence-pack gaps and rerun launch gate.

## 9. Why This Matters
- Prevents premature launch risk.
- Gives leadership auditable decision quality.
- Establishes repeatable AI governance practice for future assistants.
