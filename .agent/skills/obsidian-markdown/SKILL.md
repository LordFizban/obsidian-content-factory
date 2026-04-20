---
name: obsidian-markdown
description: Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax.
risk: unknown
source: "https://github.com/kepano/obsidian-skills"
date_added: "2026-04-20"
---

# Obsidian Flavored Markdown Skill

Use this skill to ensure all generated content uses Obsidian's local-first syntax.

## Internal Links (Wikilinks)
- Use [[Note Name]] instead of standard markdown links for internal vault connections.

## Callouts
- Use [!type] syntax for highlights (note, tip, warning, importance).

## Properties (Frontmatter)
Standard frontmatter for Content Factory:
`yaml
---
title: Note Title
date: YYYY-MM-DD
tags:
  - pillar/subpillar
  - status/draft
aliases:
  - Alt Name
---
`
"@

 = @"
---
name: obsidian-bases
description: Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries.
risk: unknown
source: "https://github.com/kepano/obsidian-skills"
date_added: "2026-04-20"
---

# Obsidian Bases Skill

Use .base files for structured views of content.

## Workflow
1. Create a .base file.
2. Define filters to select notes.
3. Configure views (table, cards, list).
