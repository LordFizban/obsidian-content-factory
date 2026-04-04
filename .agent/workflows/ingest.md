---
description: Ingest raw source material (articles, books, podcasts) into the Knowledge Ledger.
---

# Workflow: Source Ingest

Triggered when the user encounters valuable source material (an article, book chapter, podcast, conference talk) and wants to capture it in the Knowledge Ledger.

## Prerequisites

- Read `Knowledge/SCHEMA.md` for page conventions and frontmatter requirements.
- Read `Knowledge/index.md` to understand existing pages and avoid duplication.

## Steps

1. **Receive Source**
    * **Input:** User provides a file path (dropped in `Knowledge/raw/`), a URL, or pastes content directly.
    * **Action:** If URL, use web clipper or `read_url_content` to extract text. Save to `Knowledge/raw/` as markdown.
    * **Rule:** Raw source files are **immutable** — never modify them after saving.

2. **Discuss Takeaways**
    * **Action:** Read the source material. Present 3-5 key takeaways to the user.
    * **Action:** Ask the user: "Which of these are most relevant to your content strategy? Any connections to existing concepts?"
    * **Output:** User-directed focus areas.

3. **Create/Update Entity Pages**
    * **Action:** For any persons, tools, or organizations mentioned that are relevant to content strategy:
      - If the entity already has a page in `Knowledge/entities/`, update it with new references and connections.
      - If the entity is new and relevant, create a page using the Entity Page Template from SCHEMA.md.
    * **Rule:** Not every person mentioned deserves a page. Only create entity pages for people/things that are likely to be referenced in future content or have strategic relevance.

4. **Create/Update Concept Pages**
    * **Action:** For any patterns, insights, or strategies discovered:
      - If the concept already has a page in `Knowledge/concepts/`, add the new evidence to its Evidence table and update the Evolution section.
      - If the concept is new, create a page using the Concept Page Template from SCHEMA.md.
    * **Rule:** A single source ingest might touch 3-10 wiki pages. This is expected.

5. **Update Index**
    * **Action:** Update `Knowledge/index.md` with any new pages created. Add one-line summaries.

6. **Log**
    * **Action:** Append to `Knowledge/log.md`:
      ```
      ## [YYYY-MM-DD] ingest | Source Title
      **Source:** [filename or URL]
      **Pages created:** [list]
      **Pages updated:** [list]
      **Notes:** [brief summary of key insights]
      ```
