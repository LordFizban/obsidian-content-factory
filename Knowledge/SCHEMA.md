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
├── synthesis/          # Cross-concept analyses filed back from /produce or ad-hoc queries.
├── views/              # Dataview dashboards for Obsidian (read-only for LLM).
└── raw/                # Immutable source material (clipped articles, notes).
```

---

## Page Conventions

### Frontmatter (all pages)

Every page MUST have YAML frontmatter with these fields:

```yaml
---
type: entity | concept | synthesis | source_summary | rule
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

## Counter-Arguments & Data Gaps
Active challenges to this concept's validity. The LLM MUST populate this
section with at least 2 items during every ingest or produce-compound that
touches this page. This section exists to prevent confirmation bias.

1. **Against:** [strongest argument against the current rule]
2. **Data Gap:** [what data would we need to confirm or reject this concept?]
3. **Bias Check:** [are we only ingesting sources that reinforce this view?]

## Open Questions
What's still uncertain or untested.
```

> **Why Counter-Arguments?** Without this section, the Knowledge Ledger becomes
> an echo chamber that only reinforces existing beliefs. Every concept page must
> actively challenge itself. (Inspired by community feedback on Karpathy's gist.)

### Synthesis Page Template

Use for valuable cross-concept analyses that emerged during `/produce` or ad-hoc queries. This is the "Query → File Back" mechanism.

```markdown
---
type: synthesis
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: N
related:
  - "[[concept_1]]"
  - "[[concept_2]]"
tags: [synthesis]
---

# [Synthesis Title]

## Question / Context
The original question, production context, or explore that generated this synthesis.

## Synthesis
The LLM-generated analysis connecting multiple concept/entity pages.

## Pages Touched
- [[concept_1]] — how it was connected
- [[concept_2]] — how it was connected

## Filed From
Source workflow and date (e.g., `/produce` cycle for "Meeting Before the Meeting", 2026-04-08).
```

**When to file a synthesis:**
- During `/produce` Phase 5 (Draft Compound), if the production process generated a novel connection between two or more existing concept pages.
- During ad-hoc exploration, if you ask a question and the answer is valuable enough to preserve.
- The key test: *"Would losing this insight force re-derivation in a future conversation?"* If yes, file it.

---

## Rule Maturity States

Rules in `rules.md` have a maturity lifecycle:

| State | Symbol | Meaning | Graduation Criteria |
|:---|:---:|:---|:---|
| Proposed | 🧪 | Hypothesis generated during `/produce`. No performance data yet. | Needs evidence from at least 1 published post. |
| Confirmed | ✅ | Supported by empirical performance data from `/archive` compound. | At least 2 data points in the same direction. |
| Rejected | ❌ | Contradicted by performance data. | Evidence shows opposite effect or no effect. |

Rules are filed as `🧪 Proposed` during `/produce` Phase 5 (Draft Compound). They graduate to `✅ Confirmed` or `❌ Rejected` during `/archive` Phase 5 (Archive Compound) when real analytics data arrives.

---

## Operations

### Ingest (`/ingest`)

1. Read the raw source from `Knowledge/raw/`.
2. Discuss key takeaways with the user.
3. Create or update entity pages for any referenced persons/tools/orgs.
4. Create or update concept pages for any patterns or insights.
5. **Populate Counter-Arguments & Data Gaps** for every concept page touched.
6. Update `index.md` with new/modified pages.
7. Append entry to `log.md` with format: `## [YYYY-MM-DD] ingest | Source Title`.

### Query (during `/produce` Phase -1)

1. Read `Knowledge/index.md` to find relevant pages.
2. Read relevant entity/concept pages.
3. Synthesize context for the current content task.
4. If the query produces a valuable new synthesis, **file it back** as a new page in `Knowledge/synthesis/`. This is the compounding mechanism.

### Draft Compound (`/produce` Phase 5)

1. File any new rule candidates into `rules.md` with status `🧪 Proposed`.
2. If a new entity was referenced, create a stub entity page.
3. Update relevant concept pages with cross-references to the new draft.
4. **Update Counter-Arguments & Data Gaps** for every concept page touched.
5. If a valuable cross-concept synthesis emerged, file it in `Knowledge/synthesis/`.
6. Append entry to `log.md` with format: `## [YYYY-MM-DD] produce-compound | Draft Title`.

### Lint (`/lint`)

1. Scan all concept pages — flag any where `updated` is >60 days old.
2. Cross-reference `rules.md` against active SKILL.md files — flag divergences.
3. Check for orphan pages (no inbound links from other pages).
4. Check for mentioned concepts that lack their own page.
5. **Check for empty Counter-Arguments sections** — flag as bias risk.
6. Compare Content Strategist pillar targets against Content Pillars.md.
7. Generate a Lint Report with suggested actions.
8. Append entry to `log.md` with format: `## [YYYY-MM-DD] lint | Scope`.

### Archive Compound (`/archive` Phase 5)

1. Identify top and bottom performing posts of the period.
2. Update relevant concept pages with performance data in Evidence tables.
3. Confirm or reject `🧪 Proposed` rules based on observed analytics data.
4. If a new rule emerges, add it to `rules.md` and flag skills for update.
5. Update entity cooling statuses based on actual usage.
6. Append entry to `log.md` with format: `## [YYYY-MM-DD] archive-compound | Period`.

---

## Rules for LLM Maintainers

1. **Never modify files in `raw/`.** They are immutable source material.
2. **Always update `index.md`** when creating or significantly modifying a page.
3. **Always append to `log.md`** after any operation.
4. **Use `[[wiki links]]`** in page bodies to connect related pages.
5. **Keep pages focused.** One entity or concept per page. Max ~200 lines.
6. **Date everything.** Every Evidence table row needs a date.
7. **Flag, don't fix.** When Lint finds a skill divergence, flag it. Do not auto-update skills.
8. **File back, don't discard.** When a `/produce` cycle or query generates a valuable cross-concept synthesis, file it as a synthesis page. Knowledge should compound, not evaporate into chat history.
9. **Rules have maturity.** New rules from `/produce` are always `🧪 Proposed`. Only `/archive` with real data can promote them to `✅ Confirmed`.
10. **Challenge everything.** Every concept page must have a populated Counter-Arguments & Data Gaps section. If you can't find a counter-argument, that itself is a data gap worth noting.
11. **Don't touch `views/`.** Dataview dashboards are for Obsidian rendering only. The LLM should not modify them.
