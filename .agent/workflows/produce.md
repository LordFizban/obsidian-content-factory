---
description: End-to-end workflow to take a raw idea and turn it into a polished, promoted article using model-tiered subagents and quality gates.
---

# Workflow: The Full Production Cycle (Produce)

## 🧠 Model Routing

This workflow uses a hybrid model strategy to balance creative rigor and token efficiency. Each phase dispatches its subagent on the model specified below. The orchestrating agent MUST respect these assignments when invoking subagents.

| Phase | Subagent | Model | Task Type |
|:---|:---|:---|:---|
| **-1 & 0** | `@content_strategist` | `flash` | Full knowledge scan & context brief (output ≤500 tokens) |
| **1** | `@agile_coach` | `inherit` (Opus) | Deep framework reasoning & Roast |
| **2** | `@editor_in_chief` | `inherit` (Opus) | Prose crafting, Seven Sweeps, 21-cat AI audit, 18/25 Brand Voice |
| **3** | `@content_strategist` | `flash` | 360 Brew algorithm audit & 2 hook options |
| **5** | `@vault_manager` | `flash` | Structured file operations & Knowledge Ledger updates |

At the end of the workflow, output a **Model Routing Report** confirming which model each subagent was dispatched on (see Phase 6).

---

## Production Steps & Quality Gates

0. **Phase -1: Knowledge Scan** `[Model: flash]`
    * **Model:** Invoke on **flash**.
    * **Input:** `Knowledge/index.md` + all active concept/entity pages + `Knowledge/rules.md`.
    * **Action:** Read `Knowledge/index.md` first, then scan active concept/entity pages and `Knowledge/rules.md`. Use obsidian-cli to check for backlinks and unresolved links related to the topic to surface hidden context. Identify applicable rules, related prior posts, evolving concepts, and entity cooling statuses.
    * **Output Constraint:** Contextual brief for Phase 0 (**strict max ≤500 tokens**). Prioritize non-obvious cross-concept connections, rule constraints, and counter-arguments over generic concept summaries.

1. **Phase 0: Context Check (Strategist + SEO Content Planner Subagents)** `[Model: flash]`
    * **Model:** Invoke on **flash**.
    * **Input:** Phase -1 brief + latest `[Month]_Content_Plan.md` and `Content Dashboard.md`.
    * **Action:** Review pillar balance and recent cadence. Use the `@content_strategist` subagent to ensure topic cluster authority and schedule alignment.
    * **Output:** Confirmation of strategic and SEO alignment.

2. **Phase 1: Spark & Roast (Agile Coach Subagent)** `[Model: inherit]`
    * **Model:** Invoke on **inherit** (Opus 4.6) — the Roast requires deep framework reasoning (TOC, Warrior/Statesman, Systems Archetypes) to surface genuine structural tensions.
    * **Input:** User provides a raw idea or problem + Phase -1 brief.
    * **Action:** If multiple topic candidates exist, score them across the 6 Idea Darwin dimensions (Novelty, Feasibility, Value, Logic, Cross Potential, Verifiability) to select the strongest concept. Then, define and invoke the `@agile_coach` subagent asynchronously in the background to execute a rigorous "Roast" using the Frameworks Library.
    * **Output:** Scored Idea Card + Psychologically-primed 6-beat Outline.
    * **🚦 GATE 1 — STOP and present output to user.**
      * Display: Idea Darwin Score breakdown + Roast findings + Narrative Beat Sheet.
      * **Decision:**
        * If user approves → proceed to Phase 2.
        * If user rejects → abort workflow to save tokens. Do NOT draft.
        * If user requests angle adjustments → iterate Phase 1.

3. **Phase 2: Draft & Polish (Editor-in-Chief Subagent)** `[Model: inherit]`
    * **Model:** Invoke on **inherit** (Opus 4.6) — prose crafting, sentence-level cadence, 21-category AI pattern audit, and authentic trench voice.
    * **Input:** Approved Phase 1 outline + `Author_Profile.md`.
    * **Action:** Define and launch the `@editor_in_chief` subagent in the background. The subagent drafts the copy, executes the "Seven Sweeps" copy-editing review, audits and filters out the 21 categories of AI writing patterns, verifies character length (Feed Post: 1,300–1,950 chars / max 2,500 vs Article: >3,000 chars), enforces Rule 42 Deep Conversational Decoupling, verifies Rule 26 explicit book/publication title attribution, and performs the brand voice QA check.
    * **Output:** Editor's Report + AI-Audit Clean Draft + Copy Score (X/25).
    * **🚦 GATE 2 — STOP and present output to user.**
      * Display: Brand Voice Score (Target: ≥ 18/25) + Editor's Report summary + Full Clean Draft.
      * **Decision:**
        * If score ≥ 18/25 and user approves → proceed to Phase 3.
        * If score < 18/25 → perform an additional editorial sweep.
        * If user requests revisions → adjust draft before moving to promotion.

4. **Phase 3: Promotion & Optimization (Content Strategist Subagent)** `[Model: flash]`
    * **Model:** Invoke on **flash** — 360 Brew audit is a mechanical checklist; hooks are alternative presentation cards on a finalized Opus draft.
    * **Input:** Approved final draft from Phase 2.
    * **Action:** Define and invoke the `@content_strategist` subagent asynchronously to generate **2 distinct hook options** (down from 3 for token efficiency), visual/carousel scripts, and verify 360 Brew algorithm compliance.
    * **Constraint:** **360 Brew Algorithm Compliance** (zero hashtags in body, hook in first 2 sentences, Save-worthy CTA). Verify against `Knowledge/entities/360_brew.md`.
    * **Output:** `Social_Promotion_Plan.md` (Hook options + Visual layout + First comment payload).

> ℹ️ **Turkish Localization:** Turkish translations/adaptations are handled by the standalone `/localize` workflow (`.agent/workflows/localize.md`). Run it separately whenever you want to produce a Turkish version of this post.

5. **Phase 5: Draft Compound (Vault Manager Subagent)** `[Model: flash]`
    * **Model:** Invoke on **flash** — structured file manipulation and ledger updates.
    * **Trigger:** Fires immediately after the draft passes Gate 2.
    * **Condition (Lazy Compound):** If the draft introduces **no new concepts, entities, or rules** (i.e. it only references existing Knowledge Ledger pages with no novel connections), skip the full compound checklist and execute only the file save, `index.md` check, and `log.md` append.
    * **Action:** Define and invoke the `@vault_manager` subagent to execute the **Compound Checklist**:
      - [ ] Identify all concept pages touched by this draft.
      - [ ] For each touched concept: add a row to its `Evidence` table with date + draft title + "Supports/Contradicts" status.
      - [ ] For each touched concept: update its `Evolution` section describing how it was applied.
      - [ ] Update `updated: YYYY-MM-DD` and increment `source_count` in YAML frontmatter for all modified concepts.
      - [ ] If the draft connects 2+ concepts in a novel way → file a synthesis page in `Knowledge/synthesis/` (Target: 1 synthesis page per month).
      - [ ] If a new entity was referenced (e.g. Esther Derby) → create a stub page in `Knowledge/entities/`.
      - [ ] If a new rule candidate emerged → file into `Knowledge/rules.md` as `🧪 Proposed`.
      - [ ] Update `Knowledge/index.md` catalog references.
      - [ ] Save finalized draft into `Drafts/[Title].md` with complete YAML frontmatter.
      - [ ] Append to `Knowledge/log.md` with format: `## [YYYY-MM-DD] produce-compound | Draft Title`.
    * **Output:** Updated Knowledge Ledger and saved draft in `Drafts/`.

6. **Phase 6: Model Routing Report**
    * **Action:** Output a summary table confirming which model was dispatched for each phase. This serves as a verification audit.
    * **Format:**
      ```markdown
      ## 📋 Model Routing Report
      | Phase | Subagent | Target Model | Dispatched Model | Status |
      |:---|:---|:---|:---|:---|
      | -1 & 0 | @content_strategist | flash | flash | ✅ Verified |
      | 1 | @agile_coach | inherit (Opus) | inherit (Opus) | ✅ Verified |
      | 2 | @editor_in_chief | inherit (Opus) | inherit (Opus) | ✅ Verified |
      | 3 | @content_strategist | flash | flash | ✅ Verified |
      | 5 | @vault_manager | flash | flash | ✅ Verified |
      ```
    * **Audit Log:** Append a model routing summary tag to the `Knowledge/log.md` entry.

---
**Next Steps (Post-Launch Operations):**
*   If creating a Turkish version, run `/localize Drafts/[Title].md`.
*   Refer to `/archive` workflow after scheduling/publishing to ingest analytics and confirm `🧪 Proposed` rules.
