# LinkedIn Article Draft: AI as Product Discovery

**Scheduled:** Tuesday, February 3, 2026 @ 09:30 TRT ✅ PUBLISHED
**Pillar:** AI in Scrum
**Format:** Long-form Article
**Visual:** [[ai_discovery_visual.png]]
**Status:** 🟢 Published

---

## 📝 Full Article Draft

**Title:** We Stopped Using AI to Code. We Started Using It to Think.

---

My team looked at me crazy when I said: "Put *Argue with AI* in the Sprint Backlog."

In late 2025, I wrote about AI as Product Discovery. This sprint, we actually did it.

We moved AI from the *Solution Space* (writing code) to the *Problem Space* (figuring out what to build).

The results were uncomfortable. And exactly what we needed.

---

### The Problem We Were Solving

Most teams use AI to type faster. But if I'm being honest, **typing speed isn't our bottleneck**. *Clarifying our thinking* is.

We weren't slow because our fingers couldn't keep up. We were slow because we didn't know what we were building until we built the wrong thing.

So for this sprint, we made a rule:

> **No AI for code generation. Only for Product Discovery.**

---

### The Experiment: Three "Non-Technical" Backlog Items

We pulled three experiments into our Sprint Backlog. None of them involved generating code. All of them forced us to think harder.

**1. The Slicer (Story Splitting)**

We stopped asking "Is this story too big?" and started asking: *"Propose 3 ways to split this story to deliver value in 2 days."*

AI naturally thinks in patterns. It suggested vertical slicing options—"Split by Workflow" vs. "Split by Data Type"—that we missed when we were stuck in the weeds.

**But here's the honest part: this one failed.**

The AI gave us suggestions that looked reasonable on paper. But it lacked our *domain knowledge*. It didn't understand the hidden dependencies, the technical debt, the "we tried that two years ago" history. The splits weren't impactful.

So we're carrying it to the next sprint with a different approach: instead of asking AI to split stories *after* they're written, we're asking it to challenge our assumptions *before* we write.

**2. The Skeptic (Gap Analysis)**

This was the strongest "Thinking Partner" use case. We turned the AI into a "Red Team" member.

Instead of asking generic questions, we prompted it to play a persona: *"Act as a confused compliance officer. What gaps do you see?"*

It found documentation gaps and logic errors that we would have shipped. Our "Blindspot Rate" metric (YZ kaç eksik yer / mantık hatası bulundu) tracked every gap found. One sprint example: the email template alone had 1 critical question and 3 unanswered edge cases.

Here's the insight that made it click: **finding gaps in the analysis phase is cheaper than finding them during testing.** By the time QA finds a logic error, you've already written the code, the tests, and the documentation. AI helped us shift left—not in code, but in *thinking*.

**3. The QA Lead (Edge Cases)**

AI is great at generating the "Happy Path." We already know the happy path. We made it find the weird stuff.

We focused on *unhappy paths*—the edge cases that only appear at 2 AM when a user does something you never expected.

---

### The Shift: Demoing Learnings, Not Code

We didn't demo code at the Sprint Review. We demoed the *arguments* we had with the AI.

But here's the part I'm most proud of: **I didn't present it myself.**

In the previous sprint review, I had demonstrated how we use AI. This time, I asked a team member to take the lead. She explained the experiments while I helped from the side.

Why? Because the Scrum Master shouldn't be the star of the Sprint Review. The team should. And if our AI experiments were really working, the team should be able to explain them without me.

She did it brilliantly.

And then came the surprise I didn't plan.

One of the developers stood up to present his technical improvement. But instead of showing code, he used **Gemini's Dynamic View** to explain it visually—in non-technical language that even the stakeholders could follow.

I hadn't asked him to do that. He just... did it.

That's when I realized: the AI experiments weren't just changing how we *work*. They were changing how we *communicate*.

---

### The Uncomfortable Insight

The result? We didn't just ship features. We shipped *understanding*.

And here's the part no one talks about:

**AI isn't there to replace the junior dev. It's there to challenge the senior architect.**

When the senior architect can't answer the AI's question, that's when you know the AI is being used correctly. It's not a typer. It's a sparring partner.

---

### How We Measured It

We created a simple "Discovery Log" to track the experiments (all metrics are team self-reported):

**📊 Story Splitting**
→ Metric: Risk Items Prevented
→ Result: 1 blocked item avoided (experiment needs iteration)

**📊 Gap Analysis**
→ Metric: Blindspot Rate
→ Result: 60-70% speed increase; 1 critical + 3 vague points identified

**📊 AI Code Review**
→ Metric: PR Merge Time
→ Result: Fewer back-and-forth cycles; 1-2 critical bugs caught per review

**📊 Unit Test Assistant**
→ Metric: Time for Tests
→ Result: Team finally had time for unit tests (admitted they couldn't before)

**📊 Test Scenarios**
→ Metric: Scenario Creation Time
→ Result: 75% decrease; saved time used to increase WIP limit

During the Sprint Review, we walked through these results.

An IT Manager in the audience was intrigued. He gave feedback and asked for a separate meeting to discuss our AI experiments.

His comment stuck with me: *"Everyone says AI is going to replace people. But you're using it to maximize their benefits instead."*

That's when the Product Owner jumped in: "Even I use AI now—to improve the quality of acceptance criteria before the team even sees them."

That's when I knew: we weren't just experimenting anymore. We were leading.

---

### The Lighthouse Takeaway

Are you using AI to speed up your hands, or to sharpen your mind?

Most teams treat AI like a faster keyboard. We're treating it like a stakeholder—one that asks the questions we forgot to ask ourselves.

If you want to try this in your next sprint, start with one experiment: **The Skeptic.** Prompt the AI to poke holes in your next user story.

Then watch what happens when your senior developer can't answer.

---

*What's the hardest question AI has ever asked you about your own product?*

---

## 🏷️ Tags

# ScrumMaster #Agile #AI #ProductDiscovery #Leadership #Retrospectives

---

> [!NOTE] Editor's Report
> **Status:** 🟢 Ready to Publish
>
> **Tone Check:**
>
> - ✅ Human: Uses real dialogue and team dynamics
> - ✅ Vulnerable: Admits Story Splitting failed; shares iteration plan
> - ✅ Respectful: Highlights team member's presentation, PO contribution
> - ✅ No AI-speak detected
>
> **Agile Coach Review:**
>
> - ✅ Demonstrates "AI as Product Discovery" framework correctly
> - ✅ Shows empiricism (inspect & adapt with Story Splitting failure)
> - ✅ Scrum Master stepping back for team visibility = mature practice
>
> **Content Strategist Review:**
>
> - ✅ Transformation Story angle maintained
> - ✅ IT Manager quote = social proof
> - ✅ PO intervention = unexpected depth
> - ✅ Strong CTA with "The Skeptic" experiment
>
> **Writing Plans Review:**
>
> - ✅ Hook → Problem → Experiments → Shift → Insight → Measurement → Takeaway
> - ✅ Clean narrative flow

---

## ✅ Status

- [x] Expand key points into full narrative
- [x] Add personal anecdotes
- [x] Incorporate user feedback (14 comments)
- [x] Generate accompanying visual
- [x] Final review before publish

**✅ READY TO PUBLISH: February 3, 2026 @ 09:30 TRT**
