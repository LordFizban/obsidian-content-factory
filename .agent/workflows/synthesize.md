---
description: Synthesize cross-book concepts and frameworks into reusable mental models outside of production runs.
---

# Workflow: Concept Synthesis (`/synthesize`)

Triggered on-demand or after ingesting new sources/books to cross-pollinate concepts across different authors, paradigms, and content pillars.

## Prerequisites

- Read `Knowledge/SCHEMA.md` for page conventions and frontmatter requirements.
- Read `Knowledge/index.md` to review available concepts and existing synthesis pages.

## Steps

1. **Select Target Concepts / Theme**
    * **Input:** User specifies 2–4 concepts across different books/sources, OR asks the LLM to identify high-leverage cross-concept clusters.
    * **Action:** Inspect the selected concept files in `Knowledge/concepts/`.
    * **Focus Question:** *"What non-obvious systemic insight emerges when these distinct concepts are combined?"*

2. **Cross-Concept Mapping & Structural Analysis**
    * **Action:** Analyze commonalities, structural feedback loops, tensions, and complementary mechanisms.
    * **Action:** Ground the synthesis in concrete leadership / Agile coaching scenarios (e.g., Sprint Reviews, Retrospectives, Manager Partnerships, Capacity planning).

3. **Generate Synthesis Page**
    * **Action:** Create a new page in `Knowledge/synthesis/[synthesis_title].md` using the Synthesis Page Template from `SCHEMA.md`.
    * **Requirements:**
      - YAML frontmatter (`type: synthesis`, `created`, `updated`, `source_count`, `related: ["[[concept_1]]", "[[concept_2]]"]`, `tags: [synthesis]`).
      - `# [Synthesis Title]`
      - `## Question / Context` (The strategic theme or prompt that initiated this synthesis).
      - `## Synthesis` (The deep cross-concept analysis).
      - `## Pages Touched` (List of connected concepts/entities with brief context).
      - `## Actionable Rules / Takeaways` (Proposed rules or operational insights).
      - `## Filed From` (e.g., `/synthesize` cycle, YYYY-MM-DD).

4. **Update Index Catalog**
    * **Action:** Update `Knowledge/index.md` under the **Synthesis** table with the new page name and a 1-line summary.

5. **Log Operation**
    * **Action:** Append entry to `Knowledge/log.md`:
      ```markdown
      ## [YYYY-MM-DD] synthesize | [Synthesis Title]
      **Concepts merged:** [list of concepts]
      **Page created:** `synthesis/[synthesis_title].md`
      **Notes:** [brief summary of core insight]
      ```