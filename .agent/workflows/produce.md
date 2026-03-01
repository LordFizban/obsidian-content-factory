---
description: End-to-end workflow to take a raw idea and turn it into a polished, promoted article.
---

# Workflow: The Full Production Cycle

1. **Phase 1: Spark & Roast (Agile Coach)**
    * **Input:** User provides a raw idea or problem.
    * **Action:** Invoke `agile_coach`. Ask for a "Roast" and "Framework Match."
    * **Output:** Refined Outline.

2. **Phase 2: Draft & Polish (Editor-in-Chief)**
    * **Input:** User writes the draft based on Phase 1.
    * **Action:** Invoke `editor_in_chief`.
    * **Output:** Editor's Report + Formatted Draft.

3. **Phase 3: Promotion Strategy (Content Strategist)**
    * **Input:** The final draft.
    * **Action:** Invoke `content_strategist`.
    * **Output:** `Social_Promotion_Plan.md` — 3 Hook Options, Carousel Script, Posting Schedule.
    * **Optional:** Invoke `creative_director` for a video script.

4. **Phase 4: LinkedIn Formatting (Social Content)**
    * **Input:** The promotion plan + final draft.
    * **Action:** Invoke `social-content`.
    * **Output:** LinkedIn-ready post — character limits applied, hashtag strategy, CTA placement, post structure optimized for the platform.

5. **Phase 5: Launch (Vault Manager)**
    * **Action:** Move file to `Published`. Update Archive and Content Dashboard.
