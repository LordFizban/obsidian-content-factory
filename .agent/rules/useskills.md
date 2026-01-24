---
description: Trigger this rule when receiving a new task to check for relevant skills.
globs: **/*
---

# Agentic Skills Auto-Discovery Rule

When a user submits a new request or task, you MUST perform the following steps BEFORE proceeding with the task execution, unless the request is trivial or explicitly forbids it.

## 1. Skill Assessment Phase

1.  **Stop and Think**: "Does this request align with any of my registered Agentic Skills?"
2.  **Scan Operations**:
    *   List the contents of `.agent/skills/` to identify available skills.
    *   Read the `description` field in the frontmatter of `SKILL.md` for each skill (or infer from the directory content if necessary).
    *   Match keywords in the user request to the skill descriptions (e.g., "LinkedIn" -> `@social-content`, "SEO" -> `@seo-fundamentals`, "spreadsheet" -> `@xlsx`).

## 2. Skill Activation

If a relevant skill is found:

1.  **Announce**: Inform the user you are activating the specific agent/skill (e.g., "Activating @social-content to handle your LinkedIn post...").
2.  **Load Context**: Use `view_file` to read the FULL content of the relevant `SKILL.md`.
3.  **Adhere to Protocol**: Strictly follow the "Procedure" or "Instructions" defined in that `SKILL.md`. This takes precedence over general training for that specific domain.

## 3. Skill Execution

*   Use the templates, tone guidelines, and checklists provided in the skill.
*   If the skill requires specific tools (e.g., `recalc.py` for Excel), ensure they are used as specified.

## Example

> **User:** "Write a thread about AI."
> **Agent:**
> 1. Scans `.agent/skills/`.
> 2. Finds `social-content` skill matching "thread".
> 3. Reads `.agent/skills/social-content/SKILL.md`.
> 4. Says: "Activating @social-content..."
> 5. Drafts thread using the "Twitter Thread Templates" from the skill.
