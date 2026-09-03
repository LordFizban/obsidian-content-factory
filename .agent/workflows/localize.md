---
description: Standalone workflow to translate/adapt a finished English draft into culturally nuanced Turkish for LinkedIn.
---

# Workflow: Turkish Localization (Localize)

> **Model choice is per-invocation:**
> - Run on **Opus (`inherit`)** for high-stakes originals, complex cultural adaptations, or viral candidate pieces.
> - Run on **Flash** for routine translations and straightforward technical posts.

## Steps

1. **Phase 1: Source & Context Load**
    * **Input:** Target English file path in `Drafts/` or `Published/`.
    * **Action:** Read the source text. Confirm that the target is a valid English article or post. Read `Author_Profile.md` for voice/tone reference. Read 1–2 relevant Knowledge concept pages for cultural context (e.g. `warrior_vs_statesman.md` for Savaşçı/Devlet Adamı terminology).
    * **Output:** Source text + cultural context brief.

2. **Phase 2: Translation & Cultural Bridge (Localization Lead Subagent)**
    * **Action:** Define and invoke the `@localization_lead` subagent in the background.
    * **Instructions:**
      * Translate/adapt the text into White-collar corporate Turkish ("Kurumsal Türkçe").
      * Use active voice. Avoid excessive "Plaza Turkish" mix.
      * Strictly adhere to the terminology glossary:
        * *Lighthouse Leadership* ➔ **Deniz Feneri Liderliği**
        * *Warrior* ➔ **Savaşçı**
        * *Statesman* ➔ **Devlet Adamı**
        * *Psychological Safety* ➔ **Psikolojik Güvenlik**
        * *Facilitator Restraint* ➔ **Kolaylaştırıcı Otokontrol**
        * *Scrum Master* / *Product Owner* / *Sprint* ➔ Keep English terms.
      * Generate 3 Turkish Title Options:
        1. **Direct:** Plain translation.
        2. **Emotional:** Focus on feelings/resonance.
        3. **Professional:** LinkedIn professional ("Kurumsal") tone.

3. **Phase 3: Turkish 360 Brew Audit**
    * **Action:** Verify the Turkish draft against 360 Brew constraints:
      - [ ] Zero hashtags in body (2-3 niche tags in first comment only).
      - [ ] First 2 sentences classify topic for Turkish NLP models.
      - [ ] Save-worthy CTA adapted for Turkish professional audience.
      - [ ] No external links in body.
    * **Output:** Audit-clean Turkish draft.

4. **Phase 4: Package Draft & Save**
    * **Action:** Save the output as a new note in the drafts folder:
      * Path: `LinkedIn-Content/Drafts/TR_[Name].md`
    * **Metadata Block:** Include the following frontmatter in the new file:
      ```yaml
      pillar: [Copy from English Original]
      format: TR Translation
      status: draft
      date: [Suggested Thursday slot]
      framework: [Copy from English Original]
      ```

5. **Phase 5: Concept Backlink Updates**
    * **Action:** Execute the standard Draft Compound check (from `/produce` Phase 5 checklist) to update the `Evidence` tables in the `Knowledge/concepts/` files matching the content's pillars and frameworks.

---
**Next Steps:**
*   Schedule via Content Plan.
*   After publishing, run `/archive` to track Turkish performance separately in `Analytics/`.
