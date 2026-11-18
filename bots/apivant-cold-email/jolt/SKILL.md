---
name: jolt
description: "The JOLT Effect (Dixon and McKenna) field manual with Coach and Deal audit modes. Use when a buyer stalls, says 'let me think about it', asks for more demos or references, can't choose between options, wants guarantees, or the deal risks ending in no decision. Covers Judge, Offer, Limit, Take risk off the table. Read-only overlay."
---

# JOLT

## What this skill does

This is the single home for the JOLT method. Most lost deals aren't lost to a competitor or to the status quo. They're lost to indecision: the buyer wants to change but is afraid of making the wrong choice. JOLT is a set of four moves to help a buyer who wants to buy actually decide.

It is a read-only overlay. It reads deal records and transcripts and writes its output in chat. It never writes a database.

- **HPE / VME:** any write Liam approves goes through HPE CRO. HPE deals live in the Notion HPE Hub's Enterprise Pipeline only. VME Deals is a retired, read-only archive; don't read from it.
- **Toolbox:** every authorized Toolbox write goes through Toolbox CRO (Twenty is the system of record).
- Never mix HPE, Toolbox and Desk Monkey sources in one analysis.

## When it should trigger

- "JOLT", "indecision", "no decision", "they went dark", "they need to think about it"
- The buyer asks for another demo, more references, or more time to research
- The buyer can't pick between options, keeps comparing features, or wants guarantees
- A deal has pain and budget but no movement
- Post-sale second-guessing: the customer reopens terms, compares, or worries after signing
- Sizing how much of Liam's pipeline is lost to no decision
- Called by `sales-master` for the JOLT lens

## Rules for every mode

- Read full transcripts, never summaries (process-meeting-recording). If speaker labels are unreliable, attribute by context and say so.
- Never invent facts. Write "Unknown" and name who would know.
- Don't use fear to move a buyer (see section VI). JOLT works on the fear of a bad choice, not the fear of standing still.
- All output follows writing-mega-skill at grade 8.
- Never name JOLT or any sales methodology in anything a customer or partner will see.
- Emails: warm emails ask when a call works; cold emails close with a booking link.

---

# Mode A: Coach

Use when Liam asks how to get a stalled buyer to decide, or what to say next.

**Output:**

1. Indecision read: type (valuation, information, outcome), level (low, moderate, high), and the evidence.
2. The JOLT move that matters most right now, and why.
3. 4-6 lines Liam can say, written out.
4. One next step that shrinks the decision.

# Mode B: Deal audit (strict)

Use when Liam gives a deal, a transcript or call notes, or when `sales-master` calls this skill.

**Required output (use this exact structure):**

1. **Intent vs. ability to decide.** Does the buyer want to change? Can they decide? One line each, with evidence.
2. **Indecision read.** Type and level, with the tells you saw (quote them).
3. **JOLT check.** For each letter, write Done, Partial or Missing, with one line of evidence:
   - J: Did we judge the indecision and test intent?
   - O: Did we give a clear recommendation?
   - L: Did we limit the options and the research?
   - T: Did we take risk off the table?
4. **Fear tactics used.** Did we lean on urgency, scarcity, wallowing or isolation? Quote it if so.
5. **JOLT questions to ask next.** 3-5, ranked, written so Liam can say them.
6. **JOLT gaps.** What's missing, in priority order. 3-5 lines.

## Sequencing rules (do not violate)

- Judge before anything else. Don't push a buyer whose intent you haven't tested.
- Recommend before you add options. One clear choice first, alternatives only if asked.
- Never answer a request for more information until you know what it's meant to prove.
- Take risk off with outcomes and protections, not with discounts or deadlines.
- If intent is low, stop. JOLT is for buyers who want to buy. Low intent is a qualifying problem, not an indecision problem.

---

# Field Manual (Reference)

*Distilled from Matthew Dixon and Ted McKenna,* The JOLT Effect *(2022), based on analysis of over 2.5 million recorded sales calls.*

## Contents

- I. The Premise
- II. The Three Sources of Indecision
- III. J: Judge the Indecision
- IV. O: Offer Your Recommendation
- V. L: Limit the Exploration
- VI. T: Take Risk Off the Table
- VII. Be the Buyer's Agent
- VIII. After the Sale
- VIII-b. Why Buyers Freeze: Omission Bias and the Buyer's Agent
- IX. JOLT in Long, Complex Deals
- X. Sizing Indecision in Liam's Pipeline
- Cross-lens note: talk time

## I. The Premise

- In the study, 40-60% of deals were lost to "no decision", depending on the organization. Of deals lost to inaction, 44% came from status quo preference and 56% from indecision (Fig 1.1).
- "A staggering 87 percent of all conversations in our study showed either moderate or high levels of customer indecision".
- Buyers suffer from omission bias. They fear messing up more than they fear missing out. Doing nothing feels safe because no one gets blamed for it.
- "I need to think about it some more" is the phrase most tied to lost deals.
- The classic move is to relitigate the status quo: more fear, uncertainty and doubt about staying put. Reps do it on 73% of calls. It "has a negative impact on win rates 84 percent of the time".
- With JOLT, "sellers go from an 84 percent probability of a bad outcome to a 70 percent probability of a good one."
- The core belief: "overcoming indecision is all about proving to the customer that they won't fail by purchasing your solution."

**Win rates by indecision level:**

| Indecision | Average seller | JOLT seller |
| --- | --- | --- |
| Low | 39% | nearly 70% |
| Moderate | 26% | 57% |
| High | 6% | 31% |

The average win rate across the study is 26%. The two problems need different fixes. Status quo bias says "why change?" and you answer it with the case for change. Indecision says "what if I choose wrong?" and you answer it with JOLT.

## II. The Three Sources of Indecision

1. **Valuation problems.** The buyer can't pick between options. Book tells: wanting it all ("This all looks compelling to me"), pressing on differences ("Can you explain again the difference between . . . ?"), open confusion ("We're stuck between this option and that one"), and distraction by new finds ("We didn't realize you had this capability. Can you tell us more?").
2. **Lack of information.** The buyer feels they never know enough. They ask for more demos, references or SMEs than a typical buyer, delay to collect information, and say they feel overwhelmed or "still far up the learning curve".
3. **Outcome uncertainty.** The buyer doubts they'll get the result. They press for ROI projections and revisions, bring up past burns, talk about how big the risk is, ask for guarantees, and doubt the result is achievable. Book line: "If this thing doesn't work for us, it's on me."

## III. J: Judge the Indecision

Qualify on the ability to decide as well as the ability to buy.

**Test intent.** Use "powerful requests". Ask the buyer to do something that costs them a little, like setting up a meeting with key members of the buying group (IT, legal, finance, procurement). A buyer who wants to change will do it. One who won't is telling you something. You can also just ask what is making them hesitate. In the book's CEO story, the buyer had oversold a past platform to his CFO, and the fix was helping him prep for that conversation.

**Read the depth.** Four screens:

1. **How they take in information** (comfort with ambiguity). Analysis paralysis, "research for research's sake". Backtracking when late-stage news (an analyst report, a start-up) sends them back to the start.
2. **How they compare options** (structured or unstructured). One attribute at a time. A star rep's warning sign: customers who "struggle to explain how they created their short list of vendors". Comparing things that don't compare: "Comparing apples to oranges is one thing but comparing apples to Tuesday is something else altogether."
3. **Satisficer or maximizer.** A satisficer wants good enough. A maximizer wants the best possible and is never sure. The tell: after any step (a pilot, a workshop), ask the main contact how it went. Maximizers lead with what went badly.
4. **What kind of delay** (procrastination or decision avoidance). Pushing a meeting a week is procrastination. "Now's not the right time" or "priorities are shifting", plus next month, quarter or year, is avoidance: the buyer has no intention of deciding.

**Things that make it worse** (exacerbating factors). More time pressure ("You have only until the end of the week to make this decision") and a more important decision (cost, consequences). "Decision importance can turn even seemingly decisive customers into indecisive handwringers." Exploding offers raise indecision instead of lowering it.

**Scorecard (Fig 3.2).** Score each of the four screens from 1 to 7 on a bipolar scale:

| Screen | 1 (decisive) | 7 (indecisive) |
| --- | --- | --- |
| Information | Comfort with ambiguity | Need for certainty |
| Comparison | Structured alternative comparison | Unstructured alternative comparison |
| Standard | Satisficer | Maximizer |
| Delay | Procrastination | Decision avoidance |

The total runs from 4 to 28. "As a rule of thumb, opportunities that score more than twenty-two points total are candidates for disqualification—or, at the very least, are candidates for deprioritization by the salesperson and more careful scrutiny by sales managers". Then weigh the exacerbating factors on top. The book's interactive version is at jolteffect.com and is not reproduced in the text. In audits, show the four scores and the evidence for each. Never show a score to the customer.

## IV. O: Offer Your Recommendation

Buyers want you to tell them what to do.

- **Proactive guidance** ("Here's what you need" instead of "Help me understand your needs") raises win rates from 18% to 44%. Book example: "most of our new customers start with this plan and then upgrade later as their needs evolve."
- **Personal advocacy** ("Here's what I would do if I were you") by itself lifts win rates by 74%.
- Neither technique (about 40% of calls): 13% win rate. At least one: 29%. Both (16% of calls): 48%.
- The lift grows with indecision. High indecision plus low recommend skill wins under 2% of the time; high performers still win 13%.
- Diagnose, then recommend: 36%. Open-ended diagnosis with no recommendation: 14%. Questions like "What's important to you?" asked over and over make indecision worse.
- Recommend before the confusion is voiced, not after.

Lines to use (the first is our adaptation; the rest are the book's):

- "Most teams like yours start with [X]. That's what I'd do in your shoes."
- "These are all good options, but personally, here's what I would do if I were you".
- "If you're not completely happy with this choice, you can blame me . . . but I know you'll be happy with it."

## V. L: Limit the Exploration

More information doesn't fix indecision. It feeds it.

- **Powell's 40-70 rule.** "Once the information is in the 40 to 70 range, go with your gut." Under 40% is guessing. Waiting for over 70% is delaying. "Procrastination in the name of reducing risk actually increases risk."
- **Spot excess requests.** Another demo for the same group, more reference calls, more proposal rounds.
- **Own the flow of information.** Early on, send a short outside reading list you picked, often not your own marketing (the book's line: "I'm going to send you a few links to some pieces that I always recommend to people looking at this technology for the first time."). Don't let the buyer research unchaperoned.
- **Lean less on subject matter experts.** "You get delegated down to the person you sound like." Prep the expert on exactly where to jump in, answer, "and then hand the reins back to me." Learn the answer so you need them less next time. "If you don't know the answer, the last thing you should do is fake it."
- **Get ahead of objections.** Objections come up on 69% of calls, but reps rebut only on 52%. No rebuttal: 17% win rate. One rebuttal: 31%. Raising the likely objection first (a "pre-buttal"): 40%. Lines: "I'm guessing you're wondering about X" or "You know, one of the common concerns I hear at this point is Y."
- **Watch for quiet no's** ("implicit non-acceptance"). "I think so" instead of "Got it" is not a yes. Book line: "I'm sorry for asking," then "but it seems like maybe that didn't resonate with you? I'd love to get any concerns you have on the table so we can have an honest conversation about it."
- **Radical candor** (Kim Scott: care personally and challenge directly; not ruinous empathy, not obnoxious aggression). Book line: "The last thing I want to do is waste your team's time and, I have to be honest, another demo isn't really going to show you anything that we haven't already showed you. But I also know that you aren't ready to move forward so let's talk about why that is and what I can do to help you make the best decision for your organization—whether that's buying from us or going in another direction." Follow candor with questions (the "Five Whys").
- **Ask the question behind the request.** "Absolutely, we can set up a customer reference call for you," then "but, before I do that, can you help me understand what you're looking to validate in the call?" Then: "If you hear from our customer that they achieved the results you're hoping to, is that going to be enough for us to get this deal done or are there other things that are giving you pause about this decision?"
- **Talk more than you'd think.** Reps talk 58% of the time in wins and 52% in losses. Won calls show more interruptions (2.8 vs 1.2) and overtalk (6.2 vs 3.1), which is friendly "cooperative overlapping", not cutting in. Silence of 8-17% of the call wins most (about 30%); under 8% or over 31% wins less. A freeze followed by confusion is toxic. "A high-performer conversation is neither a lecture nor an interrogation."

Limiting the exploration: 42% win rate, vs. 16% for "unchaperoned" research.

## VI. T: Take Risk Off the Table

**Don't use fear.** Avoid the four kinds:

- Urgency, manufactured deadlines on price or terms (book example: "Unfortunately, this is a limited-time offer. We won't be able to give you the same level of discount after this week.")
- Scarcity, a limited window to get the product (book example: "We only have a limited number of that product still in stock...")
- Wallowing, making them stew in their pain (book example: "I'd hate for you to be stuck with your current platform any longer than necessary given how frustrated you are with it.")
- Isolation, "the harshest of the four": being left behind or the cost of delay (book examples: "As you know, we're already working with all of the other big players in your space. I'd hate for you guys to be left behind here." and "our team estimates you guys could lose up to a million dollars by delaying this decision by a quarter.")

The goal "isn't by making the customer feel bad about deciding to walk away from the purchase. It's by making them feel good about deciding to walk into it."

**Set outcome expectations.** Build the case on a believable number, not the maximum one. Book line: "I'm extremely confident we'll see at least a doubling of productivity since we see that in nearly every customer deployment. Let's use that to build the business case." This lifts win rates from 20% to 51% (+155%), yet reps avoided setting any expectation on 81% of calls.

**Downside protection.** 46% win rate vs. 22% (+109%), used on only 14% of calls. Buyers "need confidence givers, not fearmongers." Options:

- Opt-out clauses, a cancellation window, or a plan they can change later
- A money-back guarantee
- A detailed project plan before signature: owners, milestones, and KPIs for the first six months
- Professional services as "purchase insurance" (it "gives them the confidence that they won't be alone on the journey")
- A carve-out contract: in the book, a five-year deal with the riskiest business unit split into a separate one-year agreement the customer could cancel at any time

Reps skip safety nets because of comp clawbacks, fear it signals low confidence, or because it sounds awkward after FUD. Offer it as confidence, not as a last resort.

**Start smaller.** Talk them out of extras before you quote a price; "they will sell more by selling less." Or show three options (all-in, moderate, toe-dipping) and steer to the middle. "Whale-hunting" deals "never close and, if they do, the client is immediately second-guessing their decision."

## VII. Be the Buyer's Agent

Earn trust by acting like you're on their side.

Once intent is clear, JOLT sellers "stop selling to the customer." Instead, they "step in and start buying for them." Four trust moves, with the book's lines:

- Tell them not to overbuy: "You know, if I were you, I would take the number of licenses down from ten to five."
- Praise a competitor, or recommend one when it fits better: "Honestly, if you guys are really focused on that particular use case, I would tell you to talk to our competitor."
- Admit gaps and roadmap items: "We don't actually offer real-time analytics yet." / "I don't want to overpromise here."
- Say "I don't know" when you don't, and offer to find out.

Then make yes the default (the book draws on *Nudge*). Ask for the business with confidence: "You sound ready to me. Let's go." Other book closes: "I'm going to send over the agreement. Once we have it back, we'll be ready to go." Reps ask for the business only 46% of the time. The fix is not to ask on every call: "in more than half of sales opportunities, salespeople haven't earned the right to do so."

## VIII. After the Sale

Indecision doesn't end at signature. Watch for:

- Worrying (second-guessing the choice)
- Checking (comparing what they bought to what they could have bought)
- Decision instability (wanting to reopen the deal)

Keep customer effort low. Make the first weeks easy and show early wins. In Fig 8.2, low-effort deals win 40-87% of the time, moderate effort 9-39%, and high effort 4-26%. Relitigating the status quo raises perceived effort, while setting expectations lowers it: "buyers expect some degree of effort but are especially turned off by unexpected effort."

## VIII-b. Why Buyers Freeze: Omission Bias and the Buyer's Agent

**Errors of commission vs. errors of omission.** People feel more regret when bad things come from their actions than from inaction. The book calls this the omission bias. So the indecisive buyer fears doing the wrong thing more than doing nothing. The book calls it the "silent killer" of sales because it is hard to detect: the deal isn't lost to a competitor, it just dies. "Everybody is culpable when it comes to sticking with the status quo, but somebody is personally responsible for changing it."

**The principal-agent problem.** The buyer (principal) knows the seller (agent) has more information and suspects the seller acts for themselves. Every buyer's-agent move in section VII exists to close that trust gap: tell them not to overbuy, credit a competitor when it fits, admit what the product can't yet do.

**Post-decision dysfunction.** After signing, indecisive buyers show worrying, checking and decision instability (Rassin). Plan the first weeks to cut effort.

**Four flavors of loyalty** (stickiness of the product x effort of the experience): "Nirvana" is the goal (sticky and low effort); "Forgivable" (easy but not sticky); "Bearable" (sticky but hard, sometimes "captive loyalty"); the "Death zone" (hard and not sticky). Labels are from Fig 8.1. For VME after a VMware exit, low effort in the first 90 days is what keeps a sticky platform from feeling captive.

## IX. JOLT in Long, Complex Deals

- High performers will walk away from some buyers even after intent is shown, because the indecision is too deep. The book puts it at "perhaps at most 10–15 percent of potential buyers".
- Indecision shows across the whole cycle, "in emails, voice mails, texts, Slack messages, and more." Small-business buyers fear spending their own money; "buyers in larger businesses fear the wrong decision can end their paycheck altogether."
- In demos, stop and gauge reactions. "a demo feels more like a presentation than a conversation," so buyers voice fewer objections, and "unvoiced objections can translate to unarticulated indecision". Don't run the whole script; pause and ask.
- Don't over-probe. Excess diagnosis replaces a firm recommendation: "the buyer racked with indecision fears action, not inaction." Average performers probe more; high performers see "a time and place for it".
- JOLT sellers set clear guidelines for the purchase and realistic expectations for what comes after on "more than 60 percent of interactions."
- De-risk with a services contract alongside the product, so the supplier is contractually in lockstep with the buyer. "Indecision can be a very lonely state for an executive who wants to buy".
- Downside protection still works in complex deals. Expect "Legal would never allow a money-back guarantee" or "Finance would balk at a backout clause." from your own side; ask anyway, and look for scoped exit points, phased commitments or service credits.
- Endless requests for case studies, references and free pilots usually mean baggage from a past bad purchase. Address the fear, don't just feed the request.

## X. Sizing Indecision in Liam's Pipeline

- Set an acceptable "lost to inaction" rate first. In the study it ran 40-60% by organization.
- Count closed-lost and stalled deals by reason. Treat "no decision", "went dark" and "pushed again" as indecision losses, not status quo losses, unless the buyer said they don't want to change. The book separates deals lost because "the customer says no" from deals where "the customer says yes but still doesn't buy". The second usually points to seller skill.
- Set an "age out" date by deal type and segment from normal cycle times. A deal past it is stuck.
- Watch interaction velocity. Healthy deals show more emails and calls over time; widening gaps point to loss or no decision.
- Audit calls, not just stages. The book's audit pitfalls: samples too small (managers rarely audit every call in a pursuit), binary phrase-spotting instead of competency levels, and listening for too many things at once. With Fathom and Pocket transcripts, audit every call in one pursuit, end to end.
- Win-loss interviews skew to wins: "Without detail from losses, it becomes much more difficult to understand indecision."
- For each audited call, mark which JOLT moves were used (Judge, Offer, Limit, Take risk off) and which indecision source showed up (valuation, lack of information, outcome uncertainty).
- Coaching pays off most in the middle: "the best-quality coaching can improve performance by up to 19 percent" for core performers.

## Cross-lens note: talk time

JOLT's data shows reps talking 58% in wins vs. 52% in losses. Sandler aims for the buyer to talk 70-80%. They fit by stage: listen hard early in discovery (the book agrees "listening is certainly critical—especially early on in a sale"), then engage, recommend and steer once the buyer is choosing.

---

## Mindset (Ch 11)

JOLT is "a booster or overlay to your existing sales methodology", not a replacement. "overcoming indecision is less about proving to the customer that they will win than it is about convincing them they won't lose." The daily check: "Am I increasing or reducing fear?" Managers tap the brakes on "happy ears" and pressure-test deals for decision dysfunction.

---

*Glossary: `references/glossary.md`. Chapter notes: `references/chapter-notes.md`. Data, source tells and environment notes: `references/data-and-tells.md`.*

---

*Compiled from Matthew Dixon and Ted McKenna,* The JOLT Effect*, 2022.*
