---
description: Lifecycle workflow for post-launch operations, analytics ingestion, and archiving.
---

# Workflow: Post-Launch Operations (Archive)

1. **Phase 1: Launch & Archive (Vault Manager)**
    * **Action:** Move the scheduled/published file from `Drafts/` to the year/month folder in `Published/`.
    * **Action:** Update `Published Articles Archive.md` with the live LinkedIn URL and framework data.

2. **Phase 2: Analytics Ingest (XLSX Analyst)**
    * **Input:** User-supplied LinkedIn Analytics `.xlsx` file.
    * **Action:** Use `xlsx` skill to extract `Impressions`, `Engagements`, and `Kaydetmeler` (Saves).
    * **Action:** Match data to the specific activity ID or title.

3. **Phase 3: Registry Update (Vault Manager / XLSX Analyst)**
    * **Action:** Update `2026_Q1_Analytics_Log.md` with the extracted metrics.
    * **Action:** Update `Content Dashboard.md` pillar counts and the 360 Brew signal tracker.

4. **Phase 4: 360 Brew Harvest (Vault Manager)**
    * **Action:** Calculate "Save Rate" and set 21-day resurfacing check reminders in the task list.
    * **Output:** Updated Strategy state for next Phase 0.

5. **Phase 5: Knowledge Compound (Knowledge Ledger)**
    * **Input:** Analytics data from Phases 2-3 + post metadata.
    * **Action:** Execute the **Archive Compound Checklist**:
      - [ ] Identify top and bottom performing posts of the period.
      - [ ] For top 3 posts: update their referenced concepts' `Evidence` tables with final impressions, saves, and date.
      - [ ] For bottom 3 posts: update their referenced concepts' `Evidence` tables and add analytical notes explaining the underperformance.
      - [ ] Confirm or reject any `🧪 Proposed` rules in `Knowledge/rules.md` based on observed metrics.
      - [ ] Update `updated: YYYY-MM-DD` and increment `source_count` in YAML frontmatter for all updated concepts.
      - [ ] Update entity pages if an external thought leader was tagged (update references table, adjust cooling status).
      - [ ] If analytics reveal a wider, cross-concept trend → file a synthesis page in `Knowledge/synthesis/` (Target: 1 synthesis page per month).
      - [ ] Append to `Knowledge/log.md` with format: `## [YYYY-MM-DD] archive-compound | Period`.
    * **Output:** Updated and validated Knowledge Ledger, ready for the next `/produce` Phase -1 scan.
