---
description: Generate a social media promotion plan for a draft article using the Content Strategist skill.
---

# Workflow: Social Media Sprint

> [!NOTE]
> **Context Check:** Use this `/promote` workflow only when generating hooks or carousels for an already completed or published post. For new drafts, use `/produce` which runs promotional planning inline during Phase 3.

1. **Input:** Identify the target draft file (User will provide path or content).
2. **Action (Asynchronous Subagent):** Define and invoke the `@content_strategist` subagent asynchronously in the background.
    * Set prompt parameters using `.agent/skills/content_strategist/SKILL.md`.
    * Generate 3 Hook Options (Vulnerable, Provocative, Visual) compliant with 360 Brew algorithm rules.
    * Generate a high-impact Carousel Script.
3. **Output:** The subagent writes the results directly to `LinkedIn-Content/Drafts/{Draft_Name}_Promotion.md`.
