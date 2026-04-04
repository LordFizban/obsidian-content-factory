---
description: Health-check the Knowledge Ledger and detect drift between skills and accumulated evidence.
---

# Workflow: Knowledge Lint

Triggered monthly or quarterly. Scans the Knowledge Ledger for staleness, inconsistencies, and drift against active skills.

## Prerequisites

- Read `Knowledge/SCHEMA.md` for conventions.
- Read `Knowledge/index.md` for the full page catalog.

## Steps

1. **Staleness Check**
    * **Action:** Scan all entity and concept pages. Flag any where `updated` in frontmatter is >60 days old.
    * **Output:** List of stale pages with last update dates.

2. **Skill Drift Detection**
    * **Action:** Read `Knowledge/rules.md` (especially the Divergence Alerts section).
    * **Action:** Compare rules against the following active SKILL.md files:
      - `.agent/skills/content_strategist/SKILL.md` — pillar targets, 360 Brew rules, platform rules
      - `.agent/skills/editor_in_chief/SKILL.md` — scoring rubric, AI-speak blacklist
      - `.agent/skills/vault_manager/SKILL.md` — lifecycle paths
    * **Output:** List of divergences with specific line references.

3. **Cross-Reference Check**
    * **Action:** For each concept/entity page:
      - Check that all `[[wiki links]]` point to existing pages.
      - Check for concepts or entities *mentioned* in page text that don't have their own page.
      - Identify orphan pages (pages with no inbound links from other pages).
    * **Output:** List of broken links, missing pages, and orphans.

4. **Pillar Alignment**
    * **Action:** Compare the pillar targets in `Knowledge/rules.md` against:
      - `Content Pillars.md` in the Obsidian vault
      - `Content Strategist` SKILL.md
      - `Author_Profile.md`
    * **Output:** Any mismatches flagged.

5. **Evidence Gap Analysis**
    * **Action:** For each concept page, check the Evidence table:
      - Are there concepts with <2 evidence rows? (Weak support.)
      - Are there concepts where recent data contradicts the Current Rule? (Rule may need revision.)
      - Are there Open Questions that could be answered with available data?
    * **Output:** List of under-evidenced concepts and answerable questions.

6. **Generate Lint Report**
    * **Action:** Compile findings into a structured report:
      ```markdown
      # Knowledge Lint Report — [Date]

      ## 🔴 Stale Pages (>60 days)
      - [list]

      ## ⚠️ Skill Divergences
      | Skill | Skill Value | Ledger Value | Suggested Action |
      |:---|:---|:---|:---|

      ## 🔗 Link Health
      - Broken links: [list]
      - Missing pages: [list]
      - Orphan pages: [list]

      ## 📊 Evidence Gaps
      - Under-evidenced concepts: [list]
      - Answerable open questions: [list]

      ## ✅ Suggested Actions
      1. [prioritized action items]
      ```
    * **Output:** Present report to user for review.

7. **Log**
    * **Action:** Append to `Knowledge/log.md`:
      ```
      ## [YYYY-MM-DD] lint | Full scan
      **Stale pages:** [count]
      **Skill divergences:** [count]
      **Broken links:** [count]
      **Actions taken:** [list or "pending user review"]
      ```
