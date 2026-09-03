---
description: Health-check the Knowledge Ledger and detect drift between skills and accumulated evidence.
---

# Workflow: Knowledge Lint

Triggered monthly or quarterly. Scans the Knowledge Ledger for staleness, inconsistencies, and drift against active skills.

## Prerequisites

- Read `Knowledge/SCHEMA.md` for conventions.
- Read `Knowledge/index.md` for the full page catalog.

## Steps

1. **Staleness & Bias Check**
    * **Action:** Scan all active concept and entity pages. Flag any active page where `updated` in frontmatter is >60 days old.
    * **Action:** Check all concept pages for a populated `Counter-Arguments & Data Gaps` section. Flag any that are missing or empty as a bias risk.
    * **Output:** List of stale active pages and bias alerts.

2. **Skill Drift Detection**
    * **Action:** Read `Knowledge/rules.md` (especially the Divergence Alerts section).
    * **Action:** Compare rules against the following active SKILL.md files:
      - `.agent/skills/content_strategist/SKILL.md` — pillar targets, 360 Brew rules, platform rules
      - `.agent/skills/editor_in_chief/SKILL.md` — scoring rubric, AI-speak blacklist
      - `.agent/skills/vault_manager/SKILL.md` — lifecycle paths
      - `.agent/skills/agile_coach/SKILL.md` - roast, simulation, frameworks
      - `.agent/skills/localization_lead/SKILL.md` - Turkish, translation, glossary
    * **Output:** List of divergences with specific line references.

3. **Cross-Reference Check (Obsidian CLI)**
    * **Action:** For each concept/entity page:
      - Check that all `[[wiki links]]` point to existing pages.
      - Use obsidian-cli to detect unresolved links (mentions without pages).
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

      ## âš ï¸ Skill Divergences
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

