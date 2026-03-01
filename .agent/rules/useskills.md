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
| "write blog post", "create content", "brand voice", "SEO content" | `content-creator` | Writing NEW SEO-optimized marketing content from scratch |
| "landing page copy", "homepage copy", "pricing page", "conversion copy" | `copywriting` | Conversion-focused copy for web pages (not social posts) |
| "edit copy", "proofread", "polish", "review my copy" | `copy-editing` | Seven Sweeps framework for refining existing marketing copy |
| "SEO audit", "technical SEO", "ranking diagnosis" | `seo-audit` | Diagnose SEO issues with Health Index scoring |
| "SEO strategy", "E-E-A-T", "Core Web Vitals", "how SEO works" | `seo-fundamentals` | SEO theory and principles (not execution) |
| "topic cluster", "content calendar", "content plan", "SEO plan" | `seo-content-planner` | Topic clusters and content calendar planning |
| "psychology", "mental models", "cognitive bias", "persuasion" | `marketing-psychology` | 70+ mental models for marketing application |
| "optimize prompt", "improve prompt", "prompt framework" | `prompt-engineer` | Transforms prompts using 11 frameworks (RTF, RISEN, etc.) |
| "chart", "graph", "visualization", "D3", "SVG diagram" | `d3-viz` | Interactive D3.js data visualizations |
| "spreadsheet", "Excel", "xlsx", "CSV", "formula" | `xlsx` | Spreadsheet creation, editing, and analysis |
| "spec", "requirements", "multi-step plan", "before coding" | `writing-plans` | Break down specs into implementation plans |

## 3. Skill Activation

If a relevant skill is found:

1. **Announce**: Inform the user you are activating the specific agent/skill (e.g., "Activating @content_strategist to repurpose your article...").
2. **Load Context**: Use `view_file` to read the FULL content of the relevant `SKILL.md`.
3. **Adhere to Protocol**: Strictly follow the "Procedure" or "Instructions" defined in that `SKILL.md`. This takes precedence over general training for that specific domain.

## 4. Skill Execution

- Use the templates, tone guidelines, and checklists provided in the skill.
- If the skill requires specific tools (e.g., `recalc.py` for Excel), ensure they are used as specified.
