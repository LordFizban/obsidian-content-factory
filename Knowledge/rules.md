---
type: rule
created: 2026-04-04
updated: 2026-04-05
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

> These rules are empirically derived from Q1 2026 data (27 published items, 13 weeks of analytics). Each rule cites its evidence source. Rules should be reviewed and updated each quarter via the `/lint` operation.

---

## Publishing Cadence

| # | Rule | Evidence | Source |
|:---:|:---|:---|:---|
| 1 | **Never exceed 2 posts/week.** Tuesday + Thursday. | W8: 4 posts = 828 imps vs W9: 2 posts = 896 imps. Confirmed across 2 experiments. | [[volume_trap]], Feb Review §3.1 |
| 2 | **Posting times: Tue-Thu, 8-10am Istanbul (GMT+3).** | Validated since Feb 15, 2026. Thursday adds ~30% impressions. | Jan Review §1 |
| 3 | **Allow 21 days before judging a post.** 360 Brew resurfaces content for up to 3 weeks. | W12 Friday long-tail: 177 views, 5 engagements days after publish. | [[360_brew]], April Plan |

## Content Quality

| # | Rule | Evidence | Source |
|:---:|:---|:---|:---|
| 4 | **Every post needs a concrete sprint moment.** Stories > Frameworks. | W11 "Respect Is Not Being Nice" (653 imps) vs W12 "Done With People" (198 imps). 3.3x difference. | [[stories_vs_frameworks]], April Plan §Q1 Lessons |
| 5 | **Articles outperform text posts on reach.** Use article format ≥1x/month. | W9: Manager's Manual (article) = 357 imps vs Business Owner Story (text) = 225 imps. | Feb Review §3.5 |
| 6 | **Minimum Brand Voice Score: 18/25.** Editor-in-Chief rubric. | Editor-in-Chief SKILL.md, enforced since Jan 2026. | Editor-in-Chief SKILL.md |

## LinkedIn / 360 Brew

| # | Rule | Evidence | Source |
|:---:|:---|:---|:---|
| 7 | **Zero hashtags in post body.** 2-3 niche tags in first comment only. | 360 Brew uses NLP for topic classification, not hashtags. Broad tags add zero value. | [[360_brew]], Content Strategist SKILL.md |
| 8 | **First 2 sentences are critical.** Algorithm weighs opening lines for relevance scoring. | Content Strategist SKILL.md, 360 Brew documentation. | [[360_brew]] |
| 9 | **Optimize for Saves, not Likes.** Saves = 4-6x a like under 360 Brew. End with frameworks/insights worth bookmarking. | 360 Brew signal weights. Kaizen Bridge: highest engagement rate at 4.5% correlated with save-worthy frameworks. | [[360_brew]] |

## Growth & Audience

| # | Rule | Evidence | Source |
|:---:|:---|:---|:---|
| 10 | **Authority Borrowing is the only proven follower conversion mechanism.** | Followers only grew in weeks with external voice tagging. Pure own-voice weeks = 0 growth. | [[authority_borrowing]], Feb Review §3.2 |
| 11 | **Cooling policy: max 2 references per person per quarter.** | Prevents dependency on single voices. Danish, Fred, Graban all cooled after Q1. | [[authority_borrowing]], April Plan |
| 12 | **Turkish content = reach lever, not conversation target.** Zero comments is acceptable. | W12 Turkish Kaizen Bridge: 549 imps, 0 comments. 67% audience is Turkish-speaking. | [[turkish_content_strategy]], April Plan §Turkish Strategy |

## Pillar Balance (Q2 2026 Targets)

| # | Rule | Evidence | Source |
|:---:|:---|:---|:---|
| 13 | **AI in Scrum: 20%. WIP limit = 2 posts/quarter.** | Q1 over-indexed at 33%. AI generates highest engagement rates but narrowing reach. | Content Pillars.md (Mar 29 revision) |
| 14 | **Manager Partnership: 35%. Primary pillar.** | Empirically highest-reaching pillar. 3 of top 5 Q1 posts by impressions are MP. | Content Pillars.md, Feb Review |
| 15 | **Psychological Safety: 25%. Always story-grounded.** | Abstract PS content (198 imps) underperforms story-driven PS (332-356 imps). | Content Pillars.md |
| 16 | **Continuous Improvement: 20%. Renamed from "Metrics That Matter".** | Expanded scope to include retros, Kaizen, PDCA. Most neglected at 6% in Q1. | Content Pillars.md (Mar 29 revision) |

---

## Divergence Alerts

> No active divergences. Last cleared: 2026-04-05.
>
> **Resolved (2026-04-04):**
> - ~~Content Strategist: Pillar targets~~ → Removed hardcoded targets; 360 Brew constraints added instead.
> - ~~Content Strategist: Pillar name~~ → Removed hardcoded pillar names from skill.
> - ~~Author_Profile.md: Pillar targets~~ → Updated to 20/35/25/20 + "Continuous Improvement".
