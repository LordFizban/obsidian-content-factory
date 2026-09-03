---
version: 15.7.0
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
