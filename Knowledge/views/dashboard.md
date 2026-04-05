---
tags: [dataview, dashboard, knowledge-ledger]
---

# Knowledge Ledger Dashboard

> Powered by [Dataview](https://blacksmithgu.github.io/obsidian-dataview/). These views update automatically — no manual maintenance needed.

---

## All Concepts by Category

```dataview
TABLE tags as "Tags", updated as "Last Updated", source_count as "Sources"
FROM "LinkedIn-Content/Knowledge/concepts"
SORT updated DESC
```

---

## All Entities

```dataview
TABLE type as "Type", tags as "Tags", updated as "Last Updated"
FROM "LinkedIn-Content/Knowledge/entities"
SORT updated DESC
```

---

## Stale Pages (>60 days since update)

```dataview
LIST
FROM "LinkedIn-Content/Knowledge"
WHERE updated AND date(updated) < date(today) - dur(60 days)
SORT updated ASC
```

---

## Recently Updated

```dataview
TABLE type as "Type", updated as "Last Updated"
FROM "LinkedIn-Content/Knowledge"
WHERE type
SORT updated DESC
LIMIT 10
```

---

## Rule Maturity Overview

> Manual summary — updated during `/lint` passes.

| Status | Count | Description |
|:---:|:---:|:---|
| ✅ Confirmed | 16 | Backed by Q1 2026 analytics data |
| 🧪 Proposed | 1 | Pending validation from upcoming posts |
| ❌ Rejected | 0 | None yet |

---

## Raw Sources

```dataview
LIST
FROM "LinkedIn-Content/Knowledge/raw"
SORT file.name ASC
```

---

## Synthesis Pages

```dataview
TABLE related as "Concepts Connected", updated as "Filed"
FROM "LinkedIn-Content/Knowledge/synthesis"
SORT updated DESC
```

---

## Orphan Check (pages with zero inbound links)

> Use Obsidian's Graph View filtered to `path:LinkedIn-Content/Knowledge` to visually spot orphaned pages. Dataview cannot natively count inbound links.

---

*This file is read-only for LLM operations. Maintained by the Obsidian Dataview plugin.*
