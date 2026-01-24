# Obsidian Content Factory: Setup Guide

This guide will help you set up an automated content factory in Obsidian, migrating from manual workflows (like Notion) to a dynamic, template-driven system.

## ✅ What You'll Have When Done

- **5-Part Post Scaffold** template (Pattern → Mini-case → Diagram → Try this week → Tradeoff question)
- **Bilingual workflow** (EN + collapsible 🇹🇷 sections)
- **Content Dashboard** showing pillar distribution, publishing calendar, and metrics
- **Frameworks Library** cataloging your signature concepts
- **Proof Points Library** for quick metric insertion
- **Article Archive** with repurposing tracker

---

## Step 1: Create Folder Structure

In your Obsidian vault, create these folders:

```
LinkedIn-Content/
├── _templates/
├── Drafts/
├── Published/
│   ├── 2026/
│   └── Archive/
├── Content-Strategy/
└── Assets/
    └── Diagrams/
```

**How to do it:**

1. Right-click in Obsidian file explorer → New folder
2. Create each folder listed above

---

## Step 2: Install Required Plugins

Go to `Settings` → `Community Plugins` → `Browse` and install:

1. **Templater** (essential for dynamic templates)
2. **Dataview** (for content dashboard)
3. **Tasks** (for workflow tracking)
4. **Kanban** (optional - visual content pipeline)
5. **Calendar** (optional - visual posting schedule)

**Enable each plugin** after installation in `Settings` → `Community Plugins`.

---

## Step 3: Configure Templater

1. Go to `Settings` → `Templater`
2. Set **Template folder location** to: `LinkedIn-Content/_templates`
3. Enable **Trigger Templater on new file creation**
4. Click **Save**

---

## Step 4: Create Core Templates

### Template 1: Post Scaffold Template

Create: `LinkedIn-Content/_templates/Post-Scaffold.md`

```markdown
---
pillar: 
kind: 
status: Draft
created: <% tp.date.now("YYYY-MM-DD") %>
linkedin_url: 
---

# <% tp.file.title %>

## 1️⃣ The Pattern
[Describe the recurring problem or observation]

## 2️⃣ Mini-Case with Numbers
**Before:** 
**After:** 
**Timeframe:** 

## 3️⃣ One Diagram
![[diagram-name.png]]
*[Create diagram in Assets/Diagrams/]*

## 4️⃣ Try This Week
- [ ] [Specific actionable ritual]

## 5️⃣ Tradeoff Question
*[Pointed question that reveals priorities]*

---

> [!info]- 🇹🇷 Türkçe Özet
> [Turkish summary goes here]
> 
> **Dene:** [Try this week in Turkish]

---

## Metadata
**Pillar:** `=this.pillar`
**Status:** `=this.status`
**Created:** `=this.created`
```

### Template 2: Article Template

Create: `LinkedIn-Content/_templates/Article-Template.md`

```markdown
---
pillar: 
kind: 
status: Draft
created: <% tp.date.now("YYYY-MM-DD") %>
linkedin_url: 
frameworks_used: []
metrics_used: []
---

# <% tp.file.title %>

## Hook
[Opening story or observation - 2-3 sentences]

## The Pattern
[What you noticed, the broader principle]

## Mini-Case: [Title]
**Context:** 
**Challenge:** 
**Approach:** 
**Results:** 
- Metric 1: [before → after]
- Metric 2: [before → after]

## The Framework
[Your signature framework explanation]

![[framework-diagram.png]]

## Try This
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Tradeoff Question
*[Question that reveals priorities]*

---

> [!info]- 🇹🇷 Türkçe Özet
> ### [Article Title in Turkish]
> 
> [Full Turkish summary - 3-4 paragraphs]
> 
> **Dene:**
> 1. [Step 1 in Turkish]
> 2. [Step 2 in Turkish]

---

## Metadata
**Frameworks:** `=this.frameworks_used`
**Metrics:** `=this.metrics_used`
**Status:** `=this.status`
```

---

## Step 5: Create Content Strategy Documents

### Document 1: Frameworks Library

Create: `LinkedIn-Content/Content-Strategy/Frameworks-Library.md`

```markdown
# Frameworks Library

Your signature intellectual property - reference these in posts.

## Framework Example: The Triangular Process
**Definition:** A framework for balancing Speed, Quality, and Cost.
**When to use:** Project kick-offs, stakeholder negotiations
**Related articles:** [[My Article on Triangles]]

---

## Framework Example: The Feedback Loop
**Definition:** Shortening the distance between action and result.
**When to use:** Agile transformation, team coaching
```

### Document 2: Proof Points Library

Create: `LinkedIn-Content/Content-Strategy/Proof-Points-Library.md`

```markdown
# Proof Points Library

Quick-insert metric callouts for your posts.

## Cycle Time Improvement
**Metric:** 12 → 7 days in 3 sprints
**Context:** After clarifying operating rules
**Use in:** Efficiency posts

---

## Customer Retention
**Metric:** +15% YoY
**Context:** Implemented new support workflow
```

### Document 3: Content Pillars

Create: `LinkedIn-Content/Content-Strategy/Content-Pillars.md`

```markdown
# Content Pillars

## Distribution Target
- **Pillar A (TOFU):** 30%
- **Pillar B (MOFU):** 30%
- **Pillar C (MOFU):** 25%
- **Pillar D (BOFU):** 15%

## Pillar 1: Education (TOFU)
**Focus:** Teaching basic concepts to a broad audience
**Sub-topics:**
- Topic 1
- Topic 2
**Post scaffold:** Pattern → Mini-case → Diagram → Try this week → Tradeoff question

---

## Pillar 2: Case Studies (MOFU)
**Focus:** Showing expertise through real examples
**Sub-topics:**
- Client X
- Project Y
```

---

## Step 6: Create Content Dashboard

Create: `LinkedIn-Content/LinkedIn-Dashboard.md`

```markdown
# 📊 LinkedIn Content Dashboard

## 📅 Publishing Calendar (Next 4 Weeks)

```dataview
TABLE status as Status, pillar as Pillar, created as Created
FROM "LinkedIn-Content/Drafts"
WHERE status = "Scheduled" OR status = "Ready"
SORT created ASC
LIMIT 10
\```

---

## 🎯 Pillar Distribution

```dataview
TABLE pillar as Pillar, length(rows) as Count
FROM "LinkedIn-Content/Published"
GROUP BY pillar
\```

---

## 🇹🇷 Bilingual Tracker

**Posts needing full Turkish version** (every 3-4 posts):

```dataview
TABLE created as Date, pillar as Pillar
FROM "LinkedIn-Content/Published/2026"
WHERE !contains(file.content, "🇹🇷 Türkçe Özet")
SORT created DESC
LIMIT 5
\```

---

## 📈 Recent Published

```dataview
TABLE pillar as Pillar, created as Published, linkedin_url as "LinkedIn"
FROM "LinkedIn-Content/Published/2026"
SORT created DESC
LIMIT 10
\```

---

## ✍️ Current Drafts

```dataview
TABLE status as Status, pillar as Pillar, created as Started
FROM "LinkedIn-Content/Drafts"
WHERE status = "Draft" OR status = "In Progress"
SORT created DESC
\```
```

---

## Step 7: Test Your Setup

1. **Create a test post:**
   - Press `Ctrl+N` (new note)
   - Save it in `LinkedIn-Content/Drafts/`
   - Use Templater: `Ctrl+P` → "Templater: Insert Template" → Select "Post-Scaffold"

2. **Fill in the template:**
   - Add a pillar (e.g., "Education")
   - Fill in the 5 sections

3. **Check the dashboard:**
   - Open `LinkedIn-Dashboard.md`
   - Verify your draft appears in "Current Drafts"

---

## 🎉 You're Ready

You now have a fully functional content factory!
