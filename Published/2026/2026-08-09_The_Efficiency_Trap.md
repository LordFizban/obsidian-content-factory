---
tags: [agile, continuous-improvement, theory-of-constraints, leadership]
status: draft
date: 2026-08-03
pillar: Continuous Improvement
type: Article
week: W32
language: EN
ab_source: "[[eliyahu_goldratt]]"
concepts: ["[[theory_of_constraints]]", "[[subordination_vs_activation]]", "[[five_focusing_steps]]", "[[hero_bottleneck]]"]
---

# The Efficiency Trap

## Post Body

The sprint was an official success: every item in the backlog was marked done, and the sprint goal was met.

So why did a tester message a developer late at night, asking for help on something the developer thought was already finished?

---

It started in the second week of a three-week sprint. The team was moving. Everyone had their items, everyone was heads-down. From the outside, it looked healthy. Developers working on their stories, progress visible on the board, items shifting from left to right.

But they were each moving at their own speed. Not the system's speed.

By mid-sprint, the first crack appeared. A tester needed clarification on an item to finish testing it. She sent a message late at night. The developer had already marked his work as done and moved on to the next story. His response the next morning was five words long:

"But I finished my work."

That sentence is the efficiency trap.

At the daily the next day, a few team members brought up the late messages. The back and forth was tense. Some felt it was unreasonable to be contacted that late. Others felt they had no choice because the sprint was slipping.

I stepped in. Not to assign blame, but to set a ground rule: if something is truly urgent, call. If it can wait, send a message and the receiver reads it the next day. The team agreed. It felt like the right move. Systemic, no finger-pointing.

It wasn't enough.

The final week became a death march. The ground rule made the late nights more civil, but it didn't stop them. Work kept piling up at testing. Developers kept finishing their own items and pulling new ones from the backlog, while testers scrambled to keep up with a growing queue of unreviewed work. The pile-up was quiet and steady until the last few days, when everything converged at once.

The team went above and beyond to deliver. They stayed late. They pushed through. And on paper, the sprint was a success.

Then came the retrospective.

I opened with a simple question: "How did the sprint go?"

Silence filled the call before emojis started popping up in our retro tool: a tired face, a person holding a help sign, and someone working on a beach as waves crashed over them.

The team was creative in their exhaustion. Every emoji told the same story: we delivered, but it nearly broke us.

I had set the ground rule mid-sprint. I thought I'd addressed the problem. But looking at those emojis, I realized I had fixed how people communicated about the pile-up. I hadn't fixed the pile-up itself.

---

In 1984, Eliyahu Goldratt published *The Goal*, a business novel that introduced one of the most uncomfortable principles in operations management: keeping every resource busy does not improve output. It destroys it.

Goldratt's argument is straightforward. Every system has a constraint, a single point that limits the throughput of the whole. Optimizing anything other than that constraint is an illusion. When non-bottleneck resources produce faster than the constraint can absorb, they don't create value. They create inventory. Work-in-progress that sits in a queue, waiting and aging.

In our sprint, every developer was busy. That was the problem. Each one was optimizing their own throughput, pulling new items as soon as they finished the last one. But testing couldn't absorb the output at that pace. So the work piled up. Not because testers were slow, but because multiple developers feeding one testing process is a system with a built-in flood.

Goldratt called this subordination: the principle that non-bottleneck resources must match their pace to the constraint's capacity, not exceed it. The fastest parts of your system need to slow down to protect the throughput of the whole. Individual speed and system speed are not the same thing, and confusing them is where teams get hurt.

Goldratt illustrated this with a Boy Scout named Herbie, the slowest hiker who sets the pace for the entire troop. Gene Kim later adapted the idea as "Brent" in *The Phoenix Project*, the hero engineer who becomes the bottleneck because everything routes through him. We keep re-learning this lesson in software because being busy feels productive.

---

After the retrospective, we changed one thing: we introduced WIP limits.

The rule was simple. Before you pull new work from the sprint backlog, look around. Is anyone blocked? Does a tester need help verifying something? Is a code review sitting untouched? You help first. You pull new work second.

This is subordination in practice. Developers weren't idle. They were aligned. Instead of optimizing their individual speed, they were protecting the system's speed. The queue at testing shrank, the end-of-sprint panic vanished, and nobody had to send late-night messages in the final week.

---

The most dangerous thing about that death march sprint was that it worked.

We delivered everything. The sprint review went fine. The metrics looked healthy. Nobody outside the team would ever know what it cost to get there. What happens in a retro stays in a retro, and that's the trap. When success hides the cost from the outside, the system never gets questioned.

Because the next time it delivers, your senior tester starts declining overtime. Because the time after that, the developer who stayed late to help stops volunteering for complex items. The sprint absorbs the damage silently until the team can't absorb anymore.

---

If you're a Scrum Master or an Agile Coach, you've probably been in this conversation. A manager looks at the board, sees a developer without an active item, and asks: "Why is this person idle?"

Here's what I've learned to say:

"They're not idle. They're waiting — because if they pull new work now, they'll flood the testing queue and guarantee a death march in the final week. Their 'idleness' is what's protecting your deadline."

That reframe is not easy to deliver. But it's the truth Goldratt proved in manufacturing forty years ago, and your sprint data will confirm it if you start measuring cycle time instead of individual output.

---

Think about your last sprint. Where did work pile up? That pile-up is your constraint. Everything else is noise.

And if the sprint succeeded anyway, that's not proof the system works. That's proof your team absorbed the damage.

## First Comment

Eliyahu Goldratt's *The Goal* is one of the most important books on flow and throughput ever written. If you manage teams and haven't read it, start there.

#TheoryOfConstraints #AgileLeadership #ContinuousImprovement
