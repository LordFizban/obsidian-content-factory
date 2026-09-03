---
type: rule
created: 2026-04-04
updated: 2026-08-30
source_count: 5
related:
  - "[[volume_trap]]"
  - "[[stories_vs_frameworks]]"
  - "[[authority_borrowing]]"
  - "[[turkish_content_strategy]]"
  - "[[360_brew]]"
tags: [strategy, rules, operations]
---

# Decision Rules

> These rules are empirically derived from H1 2026 data (47 published items, 26 weeks of analytics). Each rule cites its evidence source. Rules should be reviewed and updated each quarter via the `/lint` operation.
>
> **Rule Maturity:** ✅ Confirmed (backed by data) | 🧪 Proposed (hypothesis, needs testing) | ❌ Rejected (contradicted by data)

---

## Publishing Cadence

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 1 | **Post once per week. Thursday, 09:00 TRT.** English-only protocol active (Turkish paused per Rule 42). Quality over volume — a single strong post outperforms two mediocre ones, and post-viral throttling makes high-frequency posting counterproductive. | ✅ | H1: 2x/week led to burnout (W26 zero-post week) and post-viral suppression (W24–W25 crash to sub-500 after W22–W23 viral). 1x/week preserves energy for higher-quality output. | User feedback (Jul 2026), Q2 Review §9 |
| 2 | **Posting day: Thursday, 09:00–09:30 Istanbul (GMT+3).** Thursday adds ~30% impressions vs Tuesday. With 1x/week cadence, always choose Thursday. | ✅ | Validated since Feb 15, 2026. Thursday = strongest single day. | Jan Review §1, Jul 2026 revision |
| 3 | **Allow 21 days before judging a post.** 360 Brew resurfaces content for up to 3 weeks. | ✅ | W12 Friday long-tail: 177 views, 5 engagements days after publish. | [[360_brew]], April Plan |

## Content Quality

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 4 | **Every post needs a concrete sprint moment.** Stories > Frameworks. | ✅ | W11 "Respect Is Not Being Nice" (653 imps) vs W12 "Done With People" (198 imps). 3.3x difference. | [[stories_vs_frameworks]], April Plan §Q1 Lessons |
| 5 | **Articles outperform text posts on reach.** Use article format ≥1x/month. | ✅ | W9: Manager's Manual (article) = 357 imps vs Business Owner Story (text) = 225 imps. | Feb Review §3.5 |
| 6 | **Minimum Brand Voice Score: 22/30.** 6-dimension Editor-in-Chief rubric (incorporating anti-AI and aesthetics). | ✅ | Editor-in-Chief SKILL.md, updated to 6-dimension rubric. | Editor-in-Chief SKILL.md |
| 23 | **No staccato fragments or em dash chains.** Short dramatic sentences ("Two people. Two complaints.") and em dashes (—) are AI tells. Use commas, conjunctions, and natural compound sentences instead. Max 1 em dash per post. | ✅ | Reader feedback (May 2026). Perception Is Strong draft revised from 5 em dashes + 4 staccato patterns to 0. | User feedback, avoid-ai-writing audit |

## LinkedIn / 360 Brew

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 7 | **Zero hashtags in post body.** 2-3 niche tags in first comment only. | ✅ | 360 Brew uses NLP for topic classification, not hashtags. Broad tags add zero value. | [[360_brew]], Content Strategist SKILL.md |
| 8 | **First 2 sentences are critical.** Algorithm weighs opening lines for relevance scoring. | ✅ | Content Strategist SKILL.md, 360 Brew documentation. | [[360_brew]] |
| 9 | **Optimize for Saves, not Likes.** Saves = 4-6x a like under 360 Brew. End with frameworks/insights worth bookmarking. | ✅ | 360 Brew signal weights. Kaizen Bridge: highest engagement rate at 4.5% correlated with save-worthy frameworks. | [[360_brew]] |
| 18 | **Authority Borrowing posts generate ~2.4x velocity vs. own-voice posts.** | ✅ | n=3 (Dependency 612, Perception 660, Org Chart 434). AB avg 569 vs own-voice avg ~240. | [[authority_borrowing]], May 2026 Retro |
| 22 | **Hyperlinks in post body cause algorithmic suppression (~4.7x penalty).** | ✅ | Shadow Backlog Sequel (79 imps final with link) vs Calm Mind (369 imps final, no link, same week). | [[cta_experiments]], Q2 Analytics W19 |

## Growth & Audience

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 10 | **Authority Borrowing is the only proven follower conversion mechanism.** | ✅ | Followers only grew in weeks with external voice tagging. Pure own-voice weeks = 0 growth. | [[authority_borrowing]], Feb Review §3.2 |
| 11 | **Cooling policy: max 2 references per person per quarter.** | ✅ | Prevents dependency on single voices. Danish, Fred, Graban all cooled after Q1. | [[authority_borrowing]], April Plan |
| 12 | **Turkish content = reach lever, not conversation target.** Zero comments is acceptable. | ✅ | W12 Turkish Kaizen Bridge: 549 imps, 0 comments. 67% audience is Turkish-speaking. | [[turkish_content_strategy]], April Plan §Turkish Strategy |
| 24 | **Turkish translations of story-driven posts generate disproportionate reach — up to 50x English originals.** | ✅ | TR Facilitator's Silence finalized at 22,983 vs EN original 419 (54.8x). | [[turkish_content_strategy]], Jun 2026 Archive |
| 26 | **Book & Publication-Source AB with Explicit Attribution:** Cite the exact landmark book, HBR study, or publication title in the body and First Comment (e.g. *In his classic Harvard Business Review study "Teaching Smart People How to Learn"...*). Book/publication AB outperforms generic person tagging by 2.9x in reach and saves. | ✅ | Phoenix Project 4,430 imps + 7 saves. Explicit naming builds instant practitioner credibility and answers reader provenance questions. | [[authority_borrowing]], Q2 Review §7, User Feedback (Aug 31, 2026) |

## Pillar Balance (H2 2026 Targets — 1x/week cadence)

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 13 | **AI in Scrum: 15–20%. WIP limit = 1 post/quarter.** Introduce one new book source in Q3 (not Musashi). At ~4 posts/month, AI gets ~1 slot every 2 months. | ✅ | Q1 over-indexed at 33%, Q2 corrected to 0%. | Content Pillars.md, Q2 Review §2 |
| 14 | **Manager Partnership: 35%. Cap at 2 new EN MP posts/month.** Turkish translations tracked separately. | ✅ | MP was 55% of Q2 output (target 35%). At 1x/week, tighter caps essential. | Content Pillars.md, Q2 Review §2 |
| 15 | **Psychological Safety: 25%. Must include a concrete sprint moment.** Musashi on ice until Q4. ~1 PS post/month. | ✅ | Abstract PS underperforms story-driven PS. Musashi fatigued (3 consecutive declines). | Content Pillars.md, Q2 Review §9.7 |
| 16 | **Continuous Improvement: 25%. Raised priority.** Sprint That Ate Itself proves CI is a breakout pillar. ~1 CI post/month. Phoenix Project as priority AB source. | ✅ | CI was -3pp below target in H1. Sprint That Ate Itself (4,430 imps) = CI breakout proof. | Content Pillars.md, Q2 Review §3 |
| T | **Turkish Localization (PAUSED):** Paused per Rule 42. Originally: Every other Thursday. Translate top-performers or create originals.** Tracked as a separate meta-dimension. Does not count toward pillar balance. | ✅ | 73% of Q2 impressions from 25% of output. Up to 55× EN originals. | [[turkish_content_strategy]], Q2 Review §6 |

## Rejected Rules

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 17 | **Explicit save prompts in first comment increase save rate.** | ❌ | Tested on Meeting Before the Meeting + Dependency Dynamic (W15). Zero saves on both. 0 saves across 9 tracked posts total. | [[cta_experiments]], Q2 Analytics W15 |
| 20 | **AI-generated images boost post reach.** | ❌ | Same Problem (264/19d with image) vs PO Private Strength (460/24d text-only). Image actively suppressed reach. | Q2 Analytics W17 |
| 21 | **Fill-in-the-blank CTAs drive comments.** | ❌ | Same Problem (0 comments at 19 days). Generic format invites zero engagement. | Q2 Analytics W17 |
| 25 | **Saves correlate with massive reach, not with content format.** | ❌ | Rejected. Sprint That Ate Itself got 7 saves at 4,430 imps. Save-worthy CTA works at sub-viral reach. | [[360_brew]], Jun 2026 Archive |

## Proposed Rules (Pending Validation)

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 19 | **Meta-content (content about content) is penalized by the algorithm.** | 🧪 | Q1 Retro (158 imps FINAL) is the weakest post of 2026. Low curiosity gap for non-followers. | Q2 Analytics W14 |
| 32 | **Systems Thinking over Local Fixes:** Structure drives behavior. Fix the system boundary, feedback loop, or incentive structure before coaching individuals on behavior. | 🧪 | Ingested from Peter Senge (*The Fifth Discipline*). | [[systems_thinking]], Aug 2026 Ingest |
| 33 | **Systems Archetypes Diagnostic:** Identify the active archetype (Fixes that Fail, Shifting the Burden, Limits to Growth) before prescribing an intervention. | 🧪 | Ingested from Peter Senge (*The Fifth Discipline*). | [[systems_archetypes]], Aug 2026 Ingest |
| 34 | **Team Learning as Alignment:** A team of brilliant individuals produces systemic failure without shared mental models and master-level dialogue. | 🧪 | User-confirmed focus area from Senge ingest. | [[team_learning]], Aug 2026 Ingest |
| 35 | **Theory of Constraints (TOC) Primacy:** Identify the single active constraint before optimizing tooling or ceremonies. Any optimization away from the constraint is waste. | 🧪 | Ingested from Eliyahu Goldratt (*The Goal*). Validated in The Efficiency Trap (384 imps/17d). | [[theory_of_constraints]], Aug 2026 Ingest |
| 36 | **The Herbie/Brent Lineage:** The constraint must be subordinated to, isolated from unplanned work, and protected from upstream flooding. | 🧪 | Ingested from Goldratt (*The Goal*) & Gene Kim (*The Phoenix Project*). Validated in TR Hero Trap (554 imps). | [[hero_bottleneck]], Aug 2026 Ingest |
| 37 | **Subordination over 100% Activation:** Resist demands for 100% developer utilization. Non-bottlenecks must maintain slack capacity to prevent flooding the bottleneck. | 🧪 | Validated in The Efficiency Trap (384 imps/17d). | [[subordination_vs_activation]], Aug 2026 Ingest |
| 38 | **Intent-Based Leadership:** Shift from leader-follower ("tell me what to do") to leader-leader ("I intend to..."). Psychological safety requires competence and clarity. | 🧪 | Ingested from David Marquet (*Turn the Ship Around!*). Core AB source for H2. | [[intent_based_leadership]], Aug 2026 Ingest |
| 39 | **Leader-Leader Model:** Do not build leadership around the Scrum Master or Team Lead. Distribute ownership across the entire team through clear intent protocols. | 🧪 | Ingested from David Marquet (*Turn the Ship Around!*). | [[leader_leader_model]], Aug 2026 Ingest |
| 40 | **Competence & Clarity Dual Pillars:** Autonomy without technical competence causes chaos; autonomy without organizational clarity creates friction. Both must accompany delegated authority. | 🧪 | Ingested from David Marquet (*Turn the Ship Around!*). | [[competence_and_clarity]], Aug 2026 Ingest |
| 41 | **Deliberate Action Protocol:** In high-consequence technical or process actions, mandate a deliberate pause ("point and call" / deliberate action) before execution to prevent systemic errors. | 🧪 | Ingested from David Marquet (*Turn the Ship Around!*). | [[deliberate_action]], Aug 2026 Ingest |
| 43 | **Mental Models Diagnostic:** When encountering persistent management resistance to agile change, pause ceremony enforcement. Surface and test underlying mental models using the Ladder of Inference and Inquiry vs. Advocacy. | 🧪 | Ingested from Peter Senge (*The Fifth Discipline* Ch 10). | [[mental_models]], Aug 2026 Ingest |

## Operational Rules (H2 2026)

| # | Rule | Status | Evidence | Source |
|:---:|:---|:---:|:---|:---|
| 42 | **Corporate Shielding & Conversational Decoupling:** Publish exclusively in English until further notice. Pause all Turkish originals and translations. Deeply decouple anecdotes: do NOT transcribe 1-on-1 conversations, retaliatory arguments, or private quotes. Use gender-neutral leadership archetypes and abstract specific team events into universal systemic dynamics. | ✅ | Turkish posts and specific dialogue patterns triggered internal scrutiny. Deep decoupling prevents conversational fingerprinting while preserving systemic insight. | User Feedback (Aug 26–31, 2026) |

| 27 | **AB source cooling: max 2 references per book/author per quarter. Musashi on ice until Q4 2026.** | ✅ | Musashi: 709 → 290 → 203 → 216. 3 consecutive declines = fatigue signal. | Q2 Review §9.7 |
| 28 | **Manager Partnership: max 2 new EN posts/month.** Turkish translations excluded from this count. | ✅ | MP was 55% of Q2 output (target: 35%). At 1x/week, tighter caps essential. | Q2 Review §2 |
| 29 | **Continuous Improvement: minimum 1 post/month.** Sprint That Ate Itself (4,430 imps) proves CI can break out. | ✅ | CI was -3pp below target in H1. Needs intentional scheduling. | Q2 Review §3 |
| 30 | **Monthly strategy review on the last Friday of each month.** Review pillar balance, rule health, and next month's calendar. | ✅ | Q2 review was 3+ months overdue. System ran without checkpoint from late March to July 4. | Q2 Review §9.6 |
| 31 | **After a viral post (>5,000 imps), expect 2–3 weeks of algorithmic suppression.** Do not panic-post or increase volume. Let the throttle period pass. | ✅ | W22: 16,463 (viral) → W24: 493 → W25: 402 despite quality content. Algorithm redistributes attention after a spike. | Q2 Review §9.1 |


---

## Divergence Alerts

> Last sync: 2026-08-30 (Lint audit). Rule 6 updated (22/30). Rule 42 synchronized across skills.
>
> **Resolved (2026-08-30 — lint):**
> - Content Strategist SKILL.md synchronized with Rule 42 (100% English-only freeze) and Rule 26 (Book-source AB priority).
> - rules.md Rule 6 updated from 18/25 to 22/30 to reflect the 6-dimension Editor-in-Chief rubric.
>
> **Resolved (2026-05-31 — lint):**
> - rules.md Rule 18 & 22 moved to ✅ Confirmed.
> - Added Rule 24 & 25 as 🧪 Proposed.
> - Updated all metrics to May 31, 2026 status.
>
> **Resolved (2026-04-19 — lint):**
> - ~~Content Strategist SKILL.md L59: "Optimize for Saves"~~ → Updated to "Optimize for Comments." (Rule 17 ❌)
> - ~~Content Pillars.md L14: "Q2 Priority: Generate Saves"~~ → Updated to comments + profile views.
> - ~~rules.md Rule 18: "375 imps/3d"~~ → Updated to "538 imps/10d, 2.6x."
>
> **Resolved (2026-04-04):**
> - ~~Content Strategist: Pillar targets~~ → Removed hardcoded targets; 360 Brew constraints added instead.
> - ~~Content Strategist: Pillar name~~ → Removed hardcoded pillar names from skill.
> - ~~Author_Profile.md: Pillar targets~~ → Updated to 20/35/25/20 + "Continuous Improvement".
