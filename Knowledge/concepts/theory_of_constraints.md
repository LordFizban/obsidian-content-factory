---
type: concept
status: active
created: 2026-08-02
updated: 2026-08-30
source_count: 2
related:
  - "[[eliyahu_goldratt]]"
  - "[[hero_bottleneck]]"
  - "[[volume_trap]]"
  - "[[outcomes_over_outputs]]"
tags: [concept, flow, theory_of_constraints, continuous_improvement]
---

# Theory of Constraints (TOC)

## Definition
A management philosophy introduced by Eliyahu Goldratt asserting that any manageable system is limited in achieving more of its goals by a very small number of constraints (often only one). Optimization anywhere except at the primary constraint is a local optimum and does not increase system throughput.

## Evidence
| Post | Date | Result | Supports/Contradicts |
|:---|:---|:---|:---|
| Ingested from *The Goal* | 2026-08-02 | Ingested baseline | Supports (Book-source AB) |

| The Efficiency Trap | 2026-08-09 | 398 imps (FINAL, 21d, 281 reach, 8 article views) | Supports (Book-source AB: Goldratt TOC subordination) |

## Current Rule
**Rule 35 (Proposed):** Identify the team's single active constraint (e.g. PO approval, QA testing, deployment) before introducing new tooling or practices. Any optimization away from the constraint is waste.

## Evolution
- **2026-08-02:** Ingested from *The Goal*. Established as the foundational framework underpinning Continuous Improvement and WIP management.

## Counter-Arguments & Data Gaps
1. **Against:** In complex, highly dynamic software environments, constraints shift rapidly across sprints; rigidly treating one area as the constraint can cause teams to miss emerging risks elsewhere.
2. **Data Gap:** Need performance data on whether posts using TOC terminology (bottleneck, throughput vs utilization) resonate better with engineering managers or senior directors.
3. **Bias Check:** We must avoid applying manufacturing floor metaphors blindly to software engineering where work items are non-homogeneous and creative discovery is non-linear.

## Open Questions
- How can Scrum Masters use the 5 Focusing Steps during sprint planning to prevent flooding non-bottleneck developers?
