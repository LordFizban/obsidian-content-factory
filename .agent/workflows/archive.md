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
    * **Action:** Identify top and bottom performing posts of the period.
    * **Action:** For each: update relevant concept pages in `Knowledge/concepts/` with performance data in Evidence tables (e.g., update `stories_vs_frameworks.md`, `cta_experiments.md`, `authority_borrowing.md`).
    * **Action:** If a new empirical rule emerges (e.g., a new format outperforms expectations), add it to `Knowledge/rules.md` and flag any skills that should be updated in the Divergence Alerts section.
    * **Action:** Update entity pages if a thought leader was referenced (update refs table, adjust cooling status).
    * **Action:** Append entry to `Knowledge/log.md` with format: `## [YYYY-MM-DD] archive-compound | Period`.
    * **Output:** Updated Knowledge Ledger ready for next `/produce` Phase -1.
