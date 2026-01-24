---
description: An end-to-end workflow to take a raw idea and turn it into a polished, promoted article.
---

# Task: The Full Production Cycle

1. **Phase 1: Spark & Roast (Agile Coach)**
    * **Input:** User provides a raw idea or problem.
    * **Action:** Invoke `agile_coach`. Ask for a "Roast" and "Framework Match."
    * **Output:** Refined Outline.

2. **Phase 2: Draft & Polish (Editor-in-Chief)**
    * **Input:** User writes the draft based on Phase 1.
    * **Action:** Invoke `editor_in_chief`.
    * **Output:** Editor's Report + Formatted Draft.

3. **Phase 3: Promotion (Content Strategist)**
    * **Input:** The final draft.
    * **Action:** Invoke `content_strategist`.
    * **Output:** `Social_Promotion_Plan.md`.
    * **Optional:** Invoke `creative_director` for a video script.

4. **Phase 4: Launch (Vault Manager)**
    * **Action:** Move file to `Published`. Update Archive.
