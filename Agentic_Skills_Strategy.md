# Agentic Skills Strategy: Content Factory

This document tracks the deployment and lifecycle of agentic skills (digital employees) within the Content Factory. It outlines our 7-Phase strategy for expanding from a core team to a fully automated multi-platform production engine.

## 🏛️ Architecture: The 3-Layer Model

Our skills are organized into three functional layers:

1. Strategic Layer (Intelligence) — Goal setting, pillar development, and high-level design.
2. Production Layer (Execution) — Writing, localizing, and formatting content.
3. Operations Layer (Automation) — File management, publishing, and analytics.

---

## 🌌 Community Repository Source

All community-sourced skills originate from:

> **[Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills)** - 882+ universal agentic skills for Claude Code, Gemini CLI, Cursor, Copilot & more.

| Attribute | Value |
|-----------|-------|
| **Repo** | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) |
| **Current Version** | v5.9.0 (Feb 20, 2026) |
| **Total Skills** | 882+ |
| **License** | MIT |
| **Install Path** | `.agent/skills/` |

**Skill Categories available upstream:**

| Category | Focus | Examples |
|----------|-------|----------|
| Architecture | System design, ADRs, C4 | `architecture`, `senior-architect` |
| Business | Growth, pricing, CRO, SEO | `copywriting`, `seo-audit` |
| Data & AI | LLM apps, RAG, agents | `rag-engineer`, `prompt-engineer` |
| Development | Language mastery, frameworks | `typescript-expert`, `react-patterns` |
| General | Planning, docs, writing | `brainstorming`, `writing-plans` |
| Infrastructure | DevOps, cloud, CI/CD | `docker-expert`, `aws-serverless` |
| Security | AppSec, pentesting | `api-security-best-practices` |
| Testing | TDD, test design, QA | `test-driven-development` |
| Workflow | Automation, orchestration | `workflow-automation` |

**Quick Update:** `npx antigravity-awesome-skills`

> **Note:** Custom skills (Phase 1 core team) are NOT sourced from this repo and should never be overwritten during updates.

---

## 📈 Expansion Roadmap

### Phase 1: Core Lifecycle Excellence (COMPLETED)

**Objective:** Restore missing capabilities and ensure a working foundation.

| Agent | Status | Layer | Source | Notes |
|-------|--------|-------|--------|-------|
| Content Strategist | ✅ Active | Strategic | Custom |
| Master Agile Coach | ✅ Active | Strategic | Custom |
| Localization Lead | ✅ Active | Strategic | Custom |
| Creative Director | ✅ Active | Strategic | Custom |
| Editor-in-Chief | ✅ Active | Production | Custom |
| Vault Manager | ✅ Active | Operations | Custom |
| **Social Content** | ✅ Restored | Production | Community |
| **Writing Plans** | ✅ Installed | Strategic | Community |
| **D3 Visualization** | ✅ Installed | Production | Community |
| ~~Document Processing~~ | ❌ Removed (2026-02-20) | Production | Community | Zero usage, not found upstream |

### Phase 2: Core Capability Sync (COMPLETED)

**Objective:** Update existing SEO and marketing skills to the latest community standards.

| Agent | Status | Layer | Source | Notes |
|-------|--------|-------|--------|-------|
| **Marketing Psychology** | ✅ Current | Strategic | Community | Matches latest repo version (21KB) |
| **XLSX Analyst** | ✅ Active | Operations | Community | Installed with recalc scripts |
| **SEO Fundamentals** | ✅ Synced | Strategic | Community | Updated to latest version (5.8KB+) |
| **SEO Audit** | ✅ Synced | Strategic | Community | Updated to latest version (12KB+) |

### Phase 3: Content Mastery (COMPLETED)

**Objective:** Advanced copywriting, prompt engineering, and SEO content planning.

| Agent | Status | Layer | Source | Notes |
|-------|--------|-------|--------|-------|
| **Content Creator** | ✅ Installed | Production | Community | SEO-optimized marketing content (7.3KB) |
| **Copywriting** | ✅ Installed | Production | Community | Conversion-focused marketing copy (5.2KB) |
| **Copy-editing** | ✅ Installed | Production | Community | Seven Sweeps review framework (12.9KB) |
| **Prompt Engineer** | ✅ Installed | Strategic | Community | 11 prompting frameworks (11KB) |
| **SEO Content Planner** | ✅ Installed | Strategic | Community | Topic clusters & content calendars (2.6KB) |

### Phase 4: LinkedIn Automation (In Planning)

**Objective:** Publish content directly to LinkedIn from the Content Factory via API.

| Capability | Approach | Status |
|:-----------|:---------|:------:|
| **Post Publishing** | Composio MCP (LinkedIn) or direct LinkedIn Posts API | ⬜ Research |
| **Scheduling** | Time-delayed publish via agent workflow | ⬜ Design |
| **Analytics Ingest** | Automate .xlsx export → Data Bridge pipeline | ⬜ Design |
| **Authority Borrowing** | Automated repost/comment workflows | ⬜ Future |

> **Dependencies:** Composio MCP server setup, LinkedIn OAuth 2.0 (`w_member_social` scope), LinkedIn Company Page association.

### Phase 5: Visual Asset Automation (Future)

**Objective:** Programmatic carousel and visual asset generation.

- **Canva Automation** (Composio MCP)
- **Diagram generation** (D3 → image pipeline)

### Phase 6: Content Repurposing (Future)

**Objective:** Extract insights from external media for content fuel.

- **YouTube Summarizer** (transcript parsing → article seeds)
- **Podcast-to-Post** pipeline

### Phase 7: Multi-Platform Scale (Future)

**Objective:** Reach beyond LinkedIn.

- **Email Sequence** (newsletter / drip campaigns)
- **Instagram Automation**
- **Twitter/X Automation**

---

## 🛠️ Skill Maintenance & Governance

- **Community Sync:** Every quarter, compare local versions against [antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills).
- **Customization:** Core Team skills (1-6) are customized for brand voice and should only be updated manually.
- **Verification:** All new skill deployments must be verified with ls -R .agent/skills and confirmed valid metadata.

---

*Last Updated: 2026-03-01*
*Community Repo Version at Last Check: v5.9.0*
