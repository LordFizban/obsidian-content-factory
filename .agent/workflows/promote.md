---
description: Generate a social media promotion plan for a draft article using the Content Strategist skill.
---

# Workflow: Social Media Sprint

1. **Input:** Identify the target draft file (User will provide path or content).
2. **Action:** Invoke `content_strategist` skill.
    * Pass the content of the draft.
    * Request 3 Hook Options (Vulnerable, Provocative, Visual).
    * Request a Carousel Script.
3. **Output:** Create a new file `LinkedIn-Content/Drafts/{Draft_Name}_Promotion.md` with the results.
