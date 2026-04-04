---
description: End-to-end workflow to take a raw idea and turn it into a polished, promoted article.
---

# Workflow: The Full Production Cycle (Produce)

0. **Phase -1: Knowledge Scan**
    * **Input:** `Knowledge/index.md` + relevant entity/concept pages.
    * **Action:** Read the Knowledge Ledger. Identify applicable rules from `Knowledge/rules.md`, related prior posts, evolving concepts relevant to the topic, and any entity cooling statuses.
    * **Output:** Contextual brief for Phase 0. Include: applicable rules, related prior posts, concept pages to reference, any divergence alerts.

1. **Phase 0: Context Check (Strategist + SEO Content Planner)**
    * **Input:** Phase -1 brief + latest [Month]_Content_Plan.md and Content Dashboard.md.
    * **Action:** Review pillar balance and recent cadence. Use `seo-content-planner` to ensure topic cluster authority. 
    * **Output:** Confirmation of strategic and SEO alignment.

2. **Phase 1: Spark & Roast (Agile Coach + Marketing Psychology)**
    * **Input:** User provides a raw idea or problem.
    * **Action:** Invoke `agile_coach` for a "Roast". Stack with `marketing-psychology` to identify 70+ mental models (e.g., IKEA Effect, Contrast Principle).
    * **Output:** Psychologically-primed Outline.

3. **Phase 2: Draft & Polish (Editor-in-Chief + Copywriting + Copy-editing)**
    * **Input:** User writes the draft based on Phase 1.
    * **Action:** Invoke `copywriting` for high-conversion hooks. Use `copy-editing` for the "Seven Sweeps" review. Final audit by `editor_in_chief`.
    * **Output:** Editor's Report + Formatted Draft + Copy Score.

4. **Phase 3: Promotion & Optimization (Content Strategist + Social Content)**
    * **Input:** The final draft.
    * **Action:** Invoke `content_strategist` for algorithm compliance. Use `social-content` for platform-specific engagement hacks.
    * **Constraint:** **360 Brew Algorithm Compliance** (zero hashtags in body, hook in first 2 sentences, Save-worthy CTA). Verify against `Knowledge/entities/360_brew.md`.
    * **Output:** Social_Promotion_Plan.md.

5. **Phase 4: Localization Branch (Localization Lead)**
    * **Input:** Polished English draft.
    * **Action:** If slot is marked 🇹🇷 in the plan, invoke `localization_lead`. Consult `Knowledge/concepts/turkish_content_strategy.md` for current rules.
    * **Output:** Culturally nuanced Turkish version.

6. **Phase 5: Knowledge Compound**
    * **Input:** Published post + Editor's Report + any new insights generated during production.
    * **Action:** Update relevant Knowledge Ledger concept/entity pages. If a new rule emerged during production, add to `Knowledge/rules.md`. If a thought leader was referenced, update their entity page. Append to `Knowledge/log.md`.
    * **Output:** Updated Knowledge Ledger.

---
**Next Steps (Manual/Operations):**
*   Refer to `/archive` workflow after scheduling/publishing.
