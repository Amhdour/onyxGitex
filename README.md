<a name="readme-top"></a>

<h2 align="center">
    <a href="https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme"> <img width="50%" src="https://github.com/onyx-dot-app/onyx/blob/logo/OnyxLogoCropped.jpg?raw=true" /></a>
</h2>

<p align="center">
    <a href="https://discord.gg/TDJ59cGV2X" target="_blank">
        <img src="https://img.shields.io/badge/discord-join-blue.svg?logo=discord&logoColor=white" alt="Discord" />
    </a>
    <a href="https://docs.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme" target="_blank">
        <img src="https://img.shields.io/badge/docs-view-blue" alt="Documentation" />
    </a>
    <a href="https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme" target="_blank">
        <img src="https://img.shields.io/website?url=https://www.onyx.app&up_message=visit&up_color=blue" alt="Documentation" />
    </a>
    <a href="https://github.com/onyx-dot-app/onyx/blob/main/LICENSE" target="_blank">
        <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=blue" alt="License" />
    </a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/12516" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/12516" alt="onyx-dot-app/onyx | Trendshift" style="width: 250px; height: 55px;" />
  </a>
</p>

# Onyx - The Open Source AI Platform

## Project Version Status

onyxGitex is currently Version 1.5:

- Version 1 — Portfolio Lab: strong / mostly achieved
- Version 2 — Production-Track Starter Kit: started / incomplete
- Version 3 — Staging Demo: not yet achieved
- Version 4 — Client-Specific Production: template only / not achieved

Current production decision:
NOT_PRODUCTION_READY

Current launch status:
NOT_ENOUGH_EVIDENCE / NO_GO for production


Version 2A RAG Runtime Evidence:
- Status: PARTIAL_RUNTIME_EVIDENCE based on generated evidence
- Canonical evidence directory:
  security-readiness/evidence-artifacts/version-2a-rag-runtime/
- Canonical local harness:
  tests/version_2a/test_rag_runtime_evidence_gate.py
- Production claim remains blocked.


Version 2B CI Artifact Proof:
- Status: CI_ARTIFACT_VERIFIED
- Workflow run ID: 25858591333
- Artifact ID: 6993717057
- Artifact download and required file-list verification completed.
- Production claim remains blocked.

For details, see:
- VERSION_STATUS.md
- portfolio-lab/
- production-readiness/
- staging-demo/
- client-production-template/

This repository must not be described as production-ready. It is a portfolio lab and production-track readiness project. Production readiness requires verified runtime evidence, CI artifacts, observability proof, staging validation, and client-specific approval.


## Evidence Workflows

[![Version 2B - RAG Runtime Evidence CI Artifact Proof](https://github.com/Amhdour/onyxGitex/actions/workflows/version-2b-rag-runtime-evidence.yml/badge.svg)](https://github.com/Amhdour/onyxGitex/actions/workflows/version-2b-rag-runtime-evidence.yml)

[![Evidence Artifact Validation](https://github.com/Amhdour/onyxGitex/actions/workflows/evidence-artifact-validation.yml/badge.svg)](https://github.com/Amhdour/onyxGitex/actions/workflows/evidence-artifact-validation.yml)

[![Tier 4 Runtime Collection](https://github.com/Amhdour/onyxGitex/actions/workflows/tier4-runtime-collection.yml/badge.svg)](https://github.com/Amhdour/onyxGitex/actions/workflows/tier4-runtime-collection.yml)

[![Readiness CI](https://github.com/Amhdour/onyxGitex/actions/workflows/readiness-ci.yml/badge.svg)](https://github.com/Amhdour/onyxGitex/actions/workflows/readiness-ci.yml)

Workflow meanings:

- Version 2B CI Artifact Proof: runs the Version 2A RAG runtime evidence command, validates Version 2A evidence, validates the Version 2B CI artifact contract, and uploads evidence artifacts.
- Evidence Artifact Validation: validates evidence artifact structure, JSON parseability, consistency checks, and forbidden-claim safety.
- Tier 4 Runtime Collection: collects backend/runtime collection evidence and dependency/import/pytest collection logs. It does not assert runtime PASS or GO.
- Readiness CI: checks readiness/launch-gate documentation and uploads readiness evidence artifacts.

Important boundary:

Workflow badges show CI workflow status only. They do not by themselves prove production readiness, GO launch status, staging verification, client-specific approval, or full runtime security.

Current Version 2B status:

CI_ARTIFACT_VERIFIED

Version 2B verifies CI artifact transport and evidence preservation for Version 2A only. Production readiness remains blocked.


Version 2C Observability Proof:
- Status: OBSERVABILITY_EVIDENCE_VERIFIED
- Canonical evidence directory:
  security-readiness/evidence-artifacts/version-2c-observability-proof/
- External observability connected: false
- Production claim remains blocked.


Version 2D Agent Runtime Evidence:
- Status: AGENT_RUNTIME_EVIDENCE_VERIFIED
- Harness type: LOCAL_AGENT_RUNTIME_HARNESS
- Canonical evidence directory:
  security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence/
- Real LangGraph runtime verified: false
- External tool execution enabled: false.
- Production claim remains blocked.

---

**[Onyx](https://www.onyx.app/?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)** is the application layer for LLMs - bringing a feature-rich interface that can be easily hosted by anyone.
Onyx enables LLMs through advanced capabilities like RAG, web search, code execution, file creation, deep research and more.

Connect your applications with over 50+ indexing based connectors provided out of the box or via MCP.

> [!TIP]
> Deploy with a single command:
> ```
> curl -fsSL https://onyx.app/install_onyx.sh | bash
> ```

![Onyx Chat Silent Demo](https://github.com/onyx-dot-app/onyx/releases/download/v3.0.0/Onyx.gif)

---

## ⭐ Features

- **🔍 Agentic RAG:** Get best in class search and answer quality based on hybrid index + AI Agents for information retrieval
  - Benchmark to release soon!
- **🔬 Deep Research:** Get in depth reports with a multi-step research flow.
  - Top of [leaderboard](https://github.com/onyx-dot-app/onyx_deep_research_bench) as of Feb 2026.
- **🤖 Custom Agents:** Build AI Agents with unique instructions, knowledge, and actions.
- **🌍 Web Search:** Browse the web to get up to date information.
  - Supports Serper, Google PSE, Brave, SearXNG, and others.
  - Comes with an in house web crawler and support for Firecrawl/Exa.
- **📄 Artifacts:** Generate documents, graphics, and other downloadable artifacts.
- **▶️ Actions & MCP:** Let Onyx agents interact with external applications, comes with flexible Auth options.
- **💻 Code Execution:** Execute code in a sandbox to analyze data, render graphs, or modify files.
- **🎙️ Voice Mode:** Chat with Onyx via text-to-speech and speech-to-text.
- **🎨 Image Generation:** Generate images based on user prompts.

Onyx supports all major LLM providers, both self-hosted (like Ollama, LiteLLM, vLLM, etc.) and proprietary (like Anthropic, OpenAI, Gemini, etc.).

To learn more - check out our [docs](https://docs.onyx.app/welcome?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)!

---

## 🚀 Deployment Modes

> Onyx supports deployments in Docker, Kubernetes, Helm/Terraform and provides guides for major cloud providers.
> Detailed deployment guides found [here](https://docs.onyx.app/deployment/overview).

Onyx supports two separate deployment options: standard and lite.

#### Onyx Lite

The Lite mode can be thought of as a lightweight Chat UI. It requires less resources (under 1GB memory) and runs a less complex stack.
It is great for users who want to test out Onyx quickly or for teams who are only interested in the Chat UI and Agents functionalities.

#### Standard Onyx

The complete feature set of Onyx which is recommended for serious users and larger teams. Additional components not included in Lite mode:
- Vector + Keyword index for RAG.
- Background containers to run job queues and workers for syncing knowledge from connectors.
- AI model inference servers to run deep learning models used during indexing and inference.
- Performance optimizations for large scale use via in memory cache (Redis) and blob store (MinIO).

> [!TIP]  
> **To try Onyx for free without deploying, visit [Onyx Cloud](https://cloud.onyx.app/signup?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme)**.

---

## 🏢 Onyx for Enterprise

Onyx is built for teams of all sizes, from individual users to the largest global enterprises:
- 👥 Collaboration: Share chats and agents with other members of your organization.
- 🔐 Single Sign On: SSO via Google OAuth, OIDC, or SAML. Group syncing and user provisioning via SCIM.
- 🛡️ Role Based Access Control: RBAC for sensitive resources like access to agents, actions, etc.
- 📊 Analytics: Usage graphs broken down by teams, LLMs, or agents.
- 🕵️ Query History: Audit usage to ensure safe adoption of AI in your organization.
- 💻 Custom code: Run custom code to remove PII, reject sensitive queries, or to run custom analysis.
- 🎨 Whitelabeling: Customize the look and feel of Onyx with custom naming, icons, banners, and more.

## 📚 Licensing

There are two editions of Onyx:

- Onyx Community Edition (CE) is available freely under the MIT license and covers all of the core features for Chat, RAG, Agents, and Actions.
- Onyx Enterprise Edition (EE) includes extra features that are primarily useful for larger organizations.

For feature details, check out [our website](https://www.onyx.app/pricing?utm_source=onyx_repo&utm_medium=github&utm_campaign=readme).

## 👪 Community

Join our open source community on **[Discord](https://discord.gg/TDJ59cGV2X)**!

## 💡 Contributing

Looking to contribute? Please check out the [Contribution Guide](CONTRIBUTING.md) for more details.

---

## 🛡️ AI Trust & Security Readiness Portfolio

This repository also includes a portfolio-style readiness package for a fictional internal company knowledge assistant case study built on Onyx.

Start here:
- `docs/case-study-internal-company-knowledge-assistant.md`
- `docs/evidence-gallery.md`
- `docs/client-demo-pack.md`
- `docs/github-repository-structure.md`
- `docs/professional-service-offer.md`

These materials describe scope, controls, evidence, and launch-gate decision framing with explicit boundaries on what is proven versus not proven.

For workflow visibility and evidence-boundary explanations, see the Evidence Workflows section near the top of this README.
