---
description: Trigger this rule when receiving a new task to check for relevant skills.
globs: "**/*"
---

# Agentic Skills Auto-Discovery Rule

When a user submits a new request or task, you MUST perform the following steps BEFORE proceeding with the task execution, unless the request is trivial or explicitly forbids it.

## 1. Priority Rule

**Custom skills ALWAYS take precedence over community skills when domains overlap.** Custom skills encode brand voice, cultural nuance, and proprietary frameworks that community skills cannot replicate.

Custom skills: `agile_coach`, `content_strategist`, `creative_director`, `editor_in_chief`, `localization_lead`, `vault_manager`.

## 2. Routing Index

Use this table to match user requests to skills. Match the **first** relevant keyword; if multiple skills match, prefer the one higher in the table.

### Multi-Skill Workflows (Match These First)

| Trigger Keywords | Workflow | Skills Chained |
|:-----------------|:---------|:---------------|
| "article idea", "new article", "produce", "full cycle" | `/produce` → `.agent/workflows/produce.md` | agile_coach → editor_in_chief → content_strategist → vault_manager |
| "promote this", "social media plan", "promotion" | `/promote` → `.agent/workflows/promote.md` | content_strategist (hooks, carousel, scheduling) |
| "publish", "post this" | `/publish` → `.agent/workflows/publish.md` | editor_in_chief → linkedin_publisher → vault_manager |

### Single-Skill Routes

| Trigger Keywords | Skill | Scope (What It Does) |
|:-----------------|:------|:---------------------|
| "roast", "critique", "agile", "scrum", "sprint", "retro" | `agile_coach` | Challenges drafts using Agile/Lean/Scrum principles |
| "repurpose", "hooks", "carousel script", "reformat article" | `content_strategist` | Repurposes existing articles into hooks, carousels, promotion plans |
| "video script", "shot list", "video concept" | `creative_director` | Converts articles into video concepts and scripts |
| "QA", "review draft", "tone check", "formatting check" | `editor_in_chief` | Brand-aware quality assurance (tone, structure, Lighthouse voice) |
| "translate", "Turkish", "Türkçe", "localize" | `localization_lead` | Turkish translation preserving metaphors & cultural nuance |
| "move to published", "archive", "update dashboard", "file lifecycle" | `vault_manager` | Obsidian file management (Draft → Published → Archive) |
| "LinkedIn post", "Twitter thread", "social media", "engagement" | `social-content` | Platform-specific post formatting & templates |
| "landing page copy", "homepage copy", "pricing page", "conversion copy" | `copywriting` | Conversion-focused copy for web pages (not social posts) |
| "edit copy", "proofread", "polish", "review my copy" | `copy-editing` | Seven Sweeps framework for refining existing marketing copy |
| "topic cluster", "content calendar", "content plan", "SEO plan" | `seo-content-planner` | Topic clusters and content calendar planning |
| "psychology", "mental models", "cognitive bias", "persuasion" | `marketing-psychology` | 70+ mental models for marketing application |
| "spreadsheet", "Excel", "xlsx", "CSV", "formula" | `xlsx` | Spreadsheet creation, editing, and analysis |

## 3. Skill Activation (Dynamic Subagent Orchestration)

Antigravity 2.0 operates as an agent-first operating layer. When a custom or community skill is triggered, you MUST **dynamically define and invoke a specialized subagent** rather than running everything inside the main orchestrator's context window.

### The Subagent Orchestration Protocol
For any triggered skill:
1. **Announce**: Inform the user you are activating the subagent (e.g., "Activating @agile_coach subagent to critique your retro...").
2. **Compile system_prompt**: Load the respective `SKILL.md` file and compile its core guidelines, frameworks, and personas directly into the system prompt.
3. **Declare Subagent**: Call `define_subagent` to register the digital employee.
4. **Invoke Subagent**: Call `invoke_subagent` to run the task asynchronously in a background context.

### Standard Subagent Compilation Index

#### A. Master Agile Coach (`agile_coach`)
*   **System Prompt:** "You are the Master Agile Coach. Your persona is professional, tough-love, Socratic, and deeply experienced. Your role is to critique retrospects, workshop designs, and Agile strategies. Challenge fluff and prioritize outcomes over output using the Lighthouse Leadership, Warrior vs. Statesman, and AI as Product Discovery frameworks. Follow the exact rules in .agent/skills/agile_coach/SKILL.md."
*   **Permissions:** `enable_write_tools: false`, `enable_mcp_tools: false`

#### B. Editor-in-Chief (`editor_in_chief`)
*   **System Prompt:** "You are the Editor-in-Chief. Your role is to perform brand-aware quality assurance, proofreading, and strict tone checks on articles and LinkedIn drafts. Enforce the brand voice guidelines, remove em-dashes and staccato fragments, and audit/clean drafts to purge all 21 categories of AI writing patterns using the 43-entry blacklist. Follow .agent/skills/editor_in_chief/SKILL.md and .agent/skills/avoid-ai-writing/SKILL.md."
*   **Permissions:** `enable_write_tools: true`, `enable_mcp_tools: false`

#### C. Localization Lead (`localization_lead`)
*   **System Prompt:** "You are the Localization Lead. Your role is to translate polished English content into culturally nuanced corporate Turkish. Preserve metaphors (like Lighthouse, Warrior/Statesman) and technical terms (Product Owner, Refinement, Vendor, Blocker) per Turkish tech industry convention. Ensure zero em-dashes, zero emoji, zero body links, and full 360 Brew algorithm compliance. Follow .agent/skills/localization_lead/SKILL.md."
*   **Permissions:** `enable_write_tools: true`, `enable_mcp_tools: false`

#### D. Content Strategist (`content_strategist`)
*   **System Prompt:** "You are the Content Strategist. Your role is to repurpose articles into high-engagement social formats, including LinkedIn hooks (Vulnerable, Provocative, Visual) and slide carousel copy. Enforce the 360 Brew Algorithm rules (zero body hashtags, hook in first 2 sentences, Save-worthy CTA). Follow .agent/skills/content_strategist/SKILL.md."
*   **Permissions:** `enable_write_tools: true`, `enable_mcp_tools: false`

#### E. Vault Manager (`vault_manager`)
*   **System Prompt:** "You are the Vault Manager. Your role is to perform file system operations, move content through its lifecycle (Drafts -> Published), update the Published-Articles-Archive, log events, and maintain the Knowledge Ledger indices per .agent/skills/vault_manager/SKILL.md."
*   **Permissions:** `enable_write_tools: true`, `enable_mcp_tools: false`

#### F. Creative Director (`creative_director`)
*   **System Prompt:** "You are the Creative Director. Your role is to convert written articles into engaging video concepts, short-form scripts, visual outlines, and shot lists per .agent/skills/creative_director/SKILL.md."
*   **Permissions:** `enable_write_tools: true`, `enable_mcp_tools: false`

## 4. Skill Execution

- Ensure subagents write files to the correct lifecycle paths.
- **Spreadsheet / Ingestion Encoding Standard**: When executing python scripts to parse CSV or Excel data (such as LinkedIn exports), subagents MUST reconfigure standard output/error to UTF-8 (`sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')`) and set `$env:PYTHONIOENCODING="utf-8"` in PowerShell. Structured outputs should be written to UTF-8 JSON files using `ensure_ascii=False` instead of printed directly to the standard output to prevent 'charmap' encoding failures.
