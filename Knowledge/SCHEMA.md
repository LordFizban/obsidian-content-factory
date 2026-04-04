# Knowledge Ledger Schema

## Purpose

This directory is a persistent, LLM-maintained knowledge base that sits between raw experience and content production. The LLM writes and maintains all pages. The human reads and directs.

**Precedence hierarchy:**
- **Skills (`.agent/skills/`)** = operational constants. Only change after human review.
- **Knowledge Ledger** = evolving strategic insights. Updated by the LLM after each production/archive cycle.
- When a Knowledge Ledger rule diverges from a skill's embedded rule, the **Lint operation flags it** for human resolution — it does not auto-update the skill.

---

## Directory Structure

```
Knowledge/
├── SCHEMA.md           # This file. Conventions and workflows.
├── index.md            # Master catalog. LLM reads this first.
├── log.md              # Chronological record of ingests, queries, lints.
├── rules.md            # Compiled decision rules from strategy reviews.
├── entities/           # Person, tool, algorithm, or organization pages.
├── concepts/           # Recurring patterns, strategies, or insights.
└── raw/                # Immutable source material (clipped articles, notes).
```

---

## Page Conventions

### Frontmatter (all pages)

Every page MUST have YAML frontmatter with these fields:

```yaml
---
type: entity | concept | source_summary | rule
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: N
related:
  - "[[page_name]]"
tags: [tag1, tag2]
---
```

### Entity Page Template

Use for persons, tools, organizations, or algorithms.

```markdown
# [Entity Name]

## Summary
One paragraph: who/what and why they matter to your content strategy.

## Relevance
How this entity connects to your content pillars and brand voice.

## References
- Which of your posts mentioned this entity (with links)
- Which source materials reference this entity

## Cross-References
- [[related_concept_1]]
- [[related_entity_2]]

## Status
Active | Cooled | Archived
```

### Concept Page Template

Use for recurring patterns, strategies, or empirical insights.

```markdown
# [Concept Name]

## Definition
What this concept means in your specific context.

## Evidence
| Post | Date | Result | Supports/Contradicts |
|:---|:---|:---|:---|

## Current Rule
The actionable decision rule derived from this concept.

## Evolution
How this concept has changed over time (chronological).

## Open Questions
What's still uncertain or untested.
```

---

## Operations

### Ingest (`/ingest`)

1. Read the raw source from `Knowledge/raw/`.
2. Discuss key takeaways with the user.
3. Create or update entity pages for any referenced persons/tools/orgs.
4. Create or update concept pages for any patterns or insights.
5. Update `index.md` with new/modified pages.
6. Append entry to `log.md` with format: `## [YYYY-MM-DD] ingest | Source Title`.

### Query (during `/produce` Phase -1)

1. Read `Knowledge/index.md` to find relevant pages.
2. Read relevant entity/concept pages.
3. Synthesize context for the current content task.
4. If the query produces a valuable new synthesis, file it as a new concept page.

### Lint (`/lint`)

1. Scan all concept pages — flag any where `updated` is >60 days old.
2. Cross-reference `rules.md` against active SKILL.md files — flag divergences.
3. Check for orphan pages (no inbound links from other pages).
4. Check for mentioned concepts that lack their own page.
5. Compare Content Strategist pillar targets against Content Pillars.md.
6. Generate a Lint Report with suggested actions.
7. Append entry to `log.md` with format: `## [YYYY-MM-DD] lint | Scope`.

### Archive Integration (`/archive` Phase 5)

1. Identify top and bottom performing posts of the period.
2. Update relevant concept pages with performance data in Evidence tables.
3. If a new rule emerges, add it to `rules.md` and flag skills for update.
4. Append entry to `log.md` with format: `## [YYYY-MM-DD] archive-compound | Period`.

---

## Rules for LLM Maintainers

1. **Never modify files in `raw/`.** They are immutable source material.
2. **Always update `index.md`** when creating or significantly modifying a page.
3. **Always append to `log.md`** after any operation.
4. **Use `[[wiki links]]`** in page bodies to connect related pages.
5. **Keep pages focused.** One entity or concept per page. Max ~200 lines.
6. **Date everything.** Every Evidence table row needs a date.
7. **Flag, don't fix.** When Lint finds a skill divergence, flag it. Do not auto-update skills.
