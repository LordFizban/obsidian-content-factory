---
type: entity
created: 2026-04-04
updated: 2026-04-04
source_count: 2
related:
  - "[[authority_borrowing]]"
  - "[[stories_vs_frameworks]]"
  - "[[cta_experiments]]"
tags: [linkedin, algorithm, platform-mechanics]
---

# 360 Brew (LinkedIn Algorithm)

## Summary

LinkedIn's AI-powered content ranking model that replaced legacy ranking systems. Deployed in 2025-2026. Uses NLP for topic classification instead of hashtags. Weighs engagement signals asymmetrically — Saves are 4-6x a Like, meaningful comments ~12x a Like.

## Signal Weights

| Signal | Weight | Action |
|:---|:---|:---|
| **Saves** | 4-6x a like | End posts with frameworks/insights worth bookmarking |
| **Meaningful comments** | ~12x a like | Ask specific, answerable questions |
| **Shares/Reposts** | High | Make insights quotable and shareable |
| **Likes** | Baseline (1x) | Don't optimize for likes alone |
| **Hashtags** | Supportive only | NLP handles topic classification |
| **First 2 sentences** | Critical | Algorithm weighs opening lines for relevance scoring |
| **Profile alignment** | High | Post topics should match headline/About expertise |
| **Content lifespan** | 21 days | Posts resurface for up to 3 weeks |

## Operational Rules Derived

1. Zero hashtags in post body. 2-3 niche tags in first comment only.
2. First 2 sentences must hook AND classify the topic for NLP.
3. Optimize for Saves over Likes — end with bookmarkable frameworks.
4. Allow 21-day evaluation window before judging post performance.
5. Profile alignment matters — posts should match LinkedIn headline expertise.

## Relevance

Every content decision in the Content Factory is shaped by 360 Brew mechanics. The algorithm dictates hook structure, CTA design, hashtag policy, and evaluation timelines. Changes to 360 Brew require immediate propagation to Content Strategist SKILL.md and rules.md.

## Evolution

- **Pre-2025:** Legacy LinkedIn algorithm (hashtag-driven discovery).
- **2025-2026:** 360 Brew rollout. NLP-based topic classification. Heavy save/comment weighting.
- **Mar 2026:** Content Strategist SKILL.md updated with 360 Brew rules table.

## Open Questions

1. Does 360 Brew treat article-format posts differently from text posts in distribution? (Q1 data suggests articles get higher reach, but correlation ≠ causation.)
2. How does 360 Brew handle bilingual content (Turkish posts)? Does NLP classify Turkish text differently?
3. Does the 21-day resurfacing window apply equally to all content types (text, article, carousel, video)?

## Cross-References

- [[authority_borrowing]] — Cross-network distribution via tagged person's engagement graph
- [[cta_experiments]] — CTA design directly affects save/comment signals
- [[stories_vs_frameworks]] — Story-driven content may trigger different NLP classification

## Status

**✅ Active** — Core platform mechanic. Monitor for algorithm updates.
