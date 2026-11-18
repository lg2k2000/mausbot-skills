---
name: selling-with
description: "Selling With (Nasralla) field manual and deal worksheet generator. Use for champion scorecards, buyer committee maps, account maps, MAPs, deal autopsies, multithreading, forwardable champion emails, demo plans, hidden objections, buying urgency, and pipeline updates for a manager. Read-only overlay."
---

> Mirror of Liam's Notion skill. Canonical source: [Selling With — Shared Methodology](https://app.notion.com/p/061cc81d888c4bc1b2e57943f19390b2) . Edit in Notion first, then re-sync here. Links to app.notion.com need Notion access.

# Selling With

## What this skill does

The single home for everything Selling With (Nasralla). Field manual + worksheet generator. Replaces the prior "Selling With (Deal Worksheet Generator)" and "Selling with Skill" pages.

## Read-only methodology and adapters

This page is a read-only methodology overlay. It may read source records and produce Selling With analysis or artifacts in chat, but it never writes any database.

- **HPE / VME:** any write Liam approves goes through HPE CRO. HPE deals live in the Notion HPE Hub's Enterprise Pipeline only. VME Deals is a retired, read-only archive; don't read from it. HPE CRO owns the field mapping for HPE deal writes.
- **Toolbox:** any write Liam approves goes through Toolbox CRO (Twenty is the system of record).
- **Desk Monkey:** use the read-only [Reference — Selling With Desk Monkey Adapter](https://app.notion.com/p/6f5b714b2ac241f1a56514e9f7116870) for schema interpretation. Send every authorized Desk Monkey Contact or Deal write to [Desk Monkey CRM Writer](https://app.notion.com/p/19e04ec72f524f45a81b9f1f450a009a).

Never mix HPE and Desk Monkey sources or schemas. If Liam requests a write, produce a structured handoff with the stable target URL, exact proposed fields, source evidence, and unresolved unknowns. The canonical writer must fetch the record before writing, re-read it afterward, and return verification. This overlay never performs or claims the write.

- Never name Selling With or any sales methodology in anything a customer or partner will see.
- Emails: warm emails ask when a call works; cold emails close with a booking link.

## When it should trigger

- "selling with", "worksheets", "buyer committee map", "champion scorecard", "deal autopsy", "MAP", "account map"
- Any request to apply Nasralla framework to a specific deal
- Champion enablement, narrative drafting, executive meeting prep, multithreading
- Forwardable emails a champion can send up, demo plans, pricing talk, hidden objections, urgency, Liam's pipeline update to his manager
- Called by `sales-master` for the Selling With lens (Champion Scorecard, Buyer Committee Map and a MAP check).

---

# Worksheet Generator Mode

Generate filled, deal-specific versions of the Selling With worksheets in chat.

## Inputs required

- Target deal (load deal page if needed)
- Which worksheet(s): Deal Autopsy, Buyer Committee Map, Champion Scorecard, Power Discovery Questions, Account Map, Internal Narrative Camouflage Checklist, Mutual Action Plan, 90-Day Habit Commitment

## Workflow

1. Pull deal data from the deal page (stakeholders, stage, technical environment, gap analysis, next steps).
2. Pre-fill every cell you can defensibly fill from the deal record. Brackets for unknowns.
3. Where the worksheet asks for buyer-owned inputs (Hypothesis, Measurables, etc.), leave a clear `[Champion to fill]` marker rather than guessing.
4. Output the worksheet as a Markdown table or structured form Liam can paste into a deal page or share with a champion.

## Output rules

- Specific to the named deal. Generic answers fail.
- No invented stakeholders. If the role isn't on the deal page, write the role with a question mark.
- For the Buyer Committee Map, always include silent/fading contacts.
- For the Champion Scorecard, score honestly against the four tests. If they pass fewer than three, the verdict is not "true champion."

---

# Field Manual (Reference)

*Distilled from Nate Nasralla,* Selling With *(2023, *[*Fluint.io*](http://Fluint.io)*).*

## Contents

01 The Premise · 02 The Three Types of Contacts · 03 The Three I's of a Champion · 04 The Emotional Journey · 05 Ocean Maps, not Org Charts · 06 The Discovery Roadmap · 07 The Narrative · 08 Executive Meetings · 09 Multithreading · 10 Mutual Action Plans · 11 The Hardwired POC · 12 Deal Momentum · 13 The Change Equation · 14 The Trust Hurdle · 15 The Non-Anxious Seller · 16-21 Mid-Funnel Playbook

Parts: I Mental Shift (01-03), II Buyer's Journey (04-05), III Think & Sell Differently (06-11), IV Mental Frameworks (12-15), Mid-Funnel Playbook (16-21).

---

## 01 The Premise

B2B sales is internal communication. Most of what closes a deal happens when the seller isn't in the room.

> "Effective sales reps don't sell to buyers. They sell with them. They influence their buyer's thinking about the problem. They enable them to deliver a clear, compelling narrative that gets their team aligned on what to do next." — Nasralla

**Three voices:** Active ("I'm selling you"), Middle ("I'm selling with you"), Passive ("I'm being sold by you"). The middle voice is the entire mental shift.

**Your new job description:** create and enable committed champions for every deal. Champions are the real inside sales reps. They need a strong message, the coaching to deliver it, and the content to support it.

**Who runs what.** We run the process terms: the meeting agreements, the mutual action plan and the two-way commitments. The champion runs the internal story. Don't hand the champion the process, and don't try to tell the story for them.

## 02 The Three Types of Contacts

A buying committee has three groups. If only two are on your side, you've lost.

- **Daily Users** — Live with the consequences of the choice. Required for adoption.
- **Key Stakeholders (SLIP)** — Security, Legal, IT, Procurement. Don't pick the winner, can veto.
- **Decision Makers** — Budget pays the bill, signature ends up on the contract.

A champion can come from any of these groups. Title doesn't make a champion.

## 03 The Three I's

A champion always has all three.

- **Incentive** — Personal connection or reward tying them to the deal.
- **Influence** — Position to leverage titles, relationships, social capital.
- **Information** — Can lay out the treasure map. Hard-to-find deal intelligence.

Taxonomy:

- Champion = Incentive + Influence + Information
- Influencer = Influence + Information, no incentive
- Coach = Incentive + Information, no influence

**Believability.** The book treats believability as "a discount rate to a champion’s level of influence" (from Ray Dalio). A contact who is flaky, exaggerates or ran a past trainwreck can't be your champion, whatever their title. Champions are defined by behavior: they move a piece of the deal forward between meetings and follow through. Liam's field test: *if my champion brought this to their CTO tomorrow without me in the room, what would the CTO do with it?* If the honest answer is "nothing meaningful," you don't have a champion.

**Two closes.** "First, you close your champion(s)." "Second, you close the contract with them." Ask Brett Queener's two questions: "What happens to this contact if they don’t buy my solution?" and "What happens to this company if they don’t buy my solution?" Overinvesting in dead-end deals is "deal debt". Mantra: no champion, no deal.

**Four champion tests** (scorecard): 1 change the channel ("Would you mind if I shoot you a quick text if I hit a question before our next call? Also happy to set up a Slack Connect channel if it’s easier?"), 2 ask them to lay out the buying process, 3 assign action items with black-or-white follow-through, 4 train them on how they'll explain us internally.

**Enterprise realities and stages:** load `references/buying-process-and-business-case.md` (handshake overhead, failure allergy, "a priority" vs "priorities", the seven buyer-behavior stages with exit criteria, the one-page business case and the Build Loop).

## 04 The Emotional Journey

Buying confidence is the single most important emotion. When buyers feel confident, close rates jump 2.6x. "facts communicate information, but feelings create influence."

Plan every interaction backwards from: *how do I want this buyer to feel after this meeting, call or email?* The book's points (its journey diagram didn't survive extraction, so no per-stage emotion list here):

- **Begin with the emotion in mind:** confidence.
- **Surprise and delight in the first minute.** One to two minutes, not ten of a 30-minute exec call.
- **Guard against the inevitable dip.** Find your weakest stage-to-stage conversion and design for it. Ask: "Based on what you’ve seen, on a rough scale of one to ten, and ten being a perfect fit, how do you feel about working together?" Then: "Oh, a six? Why not five? … and what do you think getting to an eight might look like?"
- **Make your champions look good.** "Who does my buyer want to become? What can I do to help them get there?"
- **You're just the start.** Before handoff: "Does customer success know this customer as well as I do? Have I thoroughly documented any concerns or unique needs my buyer has? Will the handoff I’m about to make keep up the momentum I’ve built?"

## 05 Ocean Maps, Not Org Charts

The org chart documents the chain of command. The ocean map documents the flow of internal communications ("More GIF than JPEG").

> "Enterprise account mapping is about designing the flow of internal communications. Who needs to say what, to who, when, to keep a deal moving."

Three reframes: influence, not information; design, not documentation; communication, not the corporate hierarchy.

Process:

1. Inventory typical communications from your last five closed deals.
2. Profile each buying contact: buying role, current priority ("What project absorbs most of their time and attention?"), key metrics.
3. Discover which communications this account needs (ask the champion which steps apply; request their templates and vendor assessments).
4. Design the ideal flow: link contacts by who sends what to whom, not reporting lines.
5. Update throughout the cycle: map from the sky (senior context) and from the surface (daily users).

## 06 The Discovery Roadmap

Three categories: **Problem → Process → Payoff**. Checklist acronyms (BANT, MEDDPICC) used as checklists are qualifying, not discovering; map their points into the roadmap instead. "curious sales reps aren’t enough—we need to create curious buyers." Discovery is continuous, open-ended and reflective.

### Power questions (exact)

**Problem**

- "What’s something about this issue others you’ve shared it with don’t always seem to understand?"
- "I’m guessing [relevant project or problem] isn’t your full-time focus. Which projects would you prioritize over this one in your team’s next meeting agenda?"
- "It seems like you’re getting by with [current process] okay. So why not hold off and come back to this project later?" (Write the answer down; replay it if momentum slows.)

**Process**

- "Does your team have a standard structure or template for sharing new projects with everyone?"
- "What do you believe must be true of a solution for it to work in your case?"
- "I don’t imagine you have extra budget for software just sitting around. It typically has to be created. So if we assume for a minute that you feel it’s worth the effort, how would you go about creating a budget for this?"

**Payoff**

- "During your last all-hands or executive update, did you hear any certain phrases being repeated? What’s the link between that priority and our project?"
- "Being able to [main product benefit here] is obviously helpful. But beyond the obvious, what does a successful project like this enable you to do that you can’t today?"
- "Everyone tracks their work a bit differently. For example, I use OKRs. Are you personally working toward any certain metrics this year?"

**Trigger phrases:** phrases an executive repeats internally, "usually three to five words long". Find one and link your narrative to it. More questions: `references/buying-process-and-business-case.md` (punch list).

### Discovery techniques

- **Release emotion** with targeted questions about what's happening in their world.
- **Stories, not statements.** "Tell me about when…"
- **More follow-ups.** "So how does this relate to…?" "What does this mean for…?" Use the five whys.
- **Share why you're asking.** "The reason I’m asking is…" or "Typically, I find that… so I’m wondering…"
- **Build a logical bridge.** "When you shared… was that related to this?" "Aha, so does this connect back to when you said…?"
- **Ask 100-degree questions**, not 30-degree (leading) or 360-degree (tangents). **Ask the obvious.**
- **Pepper, don't pour.** Mix questions with your point of view and customer stories.

### The problem statement

Build it role by role, confirm each in writing, then hold one group meeting whose only goal is agreeing on the problem.

> "Despite trying [failed solution], we still can’t [desired outcome], because of [this problem], caused by [root cause]."

Then size it:

<quote>
<p />

1. Costs: "Every [frequency], at least [reach] are [pain], costing us [loss]."
2. Consequences: "That means [implication #1]. If it’s not addressed by [timeline], then [implication #2]."
</quote>

"Loss = Reach (x) frequency (x) severity". "Don’t give this your best guess. Ask your buyer what their guess is." Then sanity-check: "How does this estimate of $2.5 million compare to what you expected to see?" Lead with active loss before opportunity, and name consequences at three levels: functional, strategic and personal. "How you frame the problem defines what type of solution will be seen as a fit."

## 07 The Narrative

Decks die when forwarded. A written narrative, co-created with your champion, survives the meetings you're not in. "Buyers are having meetings about you, without you."

> "We don’t do PowerPoint presentations at Amazon. Instead, we write narratively structured memos" — Bezos

**Why writing wins** (seven reasons): controlled message, discovers truth, co-creates commitment, prunes excess, brings new buyers up to speed, optimizes for understanding, influences when you're not there.

**Mental models:** Minto Pyramid (answer first, MECE support; BLUF), Zoom Out, Zoom In (10+ year industry view, then the six-month project), and driver trees (target metric on the left, input metrics on the right).

**One-page business case:** headline, problem statement, recommended approach (vendor-agnostic: "how you solve a problem. Not who or what solves it."), payoff, required investment. Byline: "Don’t list your name as the author." Formatting: "Please don’t send me a billboard." Use the buyer's look ("camouflage"). Template, Build Loop and language levels: `references/buying-process-and-business-case.md`.

### The strategic soundbite

> "Because of [a massive, industry-wide shift], now is the time to [respond with this nonobvious approach]. When you do, [good outcomes help key metrics]. If you don’t, [bad, costly problems continue]."

## 08 Executive Meetings

Each minute with an executive is worth ~16x every minute spent with the rest of the buying team. Executives think about seismic shifts in an industry, looming and existential risks, and massive, untapped opportunities.

### Five pre-meeting must-dos (book)

1. Refine the narrative with your champion, tied to the exec's trigger phrases.
2. Compress it into the strategic soundbite.
3. The 25% rule: planned material fills about a quarter of the slot (15 of 60 minutes), because execs go off-agenda.
4. Lock down the "executive whisperer" and ask beforehand: "What area of this project gives you the most concern?" "If it were to go off the rails, why do you think that would be?"
5. Attach a short memo (the one-page business case) as a pre-read; start the invite at :05 so they read first.

**Minute by minute:** :00-:05 a nonobvious insight ("Most people believe _________, but actually, ___________."); :05-:10 adapt to their quirks; :10-:20 confirm or correct the narrative, and answer the question you're asked; :20-:25 frame the decision path ("Are there certain projects this discussion will need to take a backseat to?"); :25-:30 confirm named owners and outcomes. Facilitate; don't be the main voice. After: "[Executive], no reply needed here—just keeping you in the loop." and ask "How would you like us to keep you updated?"

## 09 Multithreading

Single-threaded deals die when your one contact gets reorged. Contact stages are not the deal stage: forecast on group behavior, and move deals backward when that's the truth. "champions always move faster than groups reach consensus."

Account-map practices:

- Beware the shadow org chart. Influence flows through informal networks.
- Start discovery as far upstream as possible.
- Time-sensitive requests should come from inside the same team.
- Use forwardable emails, so the sender is internal.
- "Spread information broadly and calls to action individually."
- Beware shadow players; label them with your champion.
- Build bridges from up high, not down low. Plant seeds with key stakeholders early.
- Mind the medium (standing agendas, Slack or Teams channels).

Book scripts:

- Widen the circle: "Who else might this project impact that hasn’t had a chance to weigh in yet?"
- "Let us sync up internally" answer: "I imagine you’ll want to sync with your team before we meet again. Can you think of a scenario where it doesn’t make sense for us to meet again?"
- Invite dissent: "Seems like everything’s moving forward smoothly, so I’m wondering, is there someone on your team who you think might be willing to disagree with us, so we can be sure we have a good fit?"
- Access mirrors access: bring an executive, meet their executive. Remember the champion's line: "I live here, you don’t." Every step costs them social capital.

**Keep the committee minimally viable.** An ever-growing committee signals low decision confidence (Challenger data: purchase likelihood falls from 81% with one stakeholder to 31% with six). **Name the drama.** "Math problems have solutions. Drama doesn’t." When the math says yes and the room stalls, label what's felt and connect it back to the math problem. **Don't multithread pricing.** Hold price talks with the champion and decider, not the group.

House addition (not from the book): ask early whether anyone outside the team reviews decisions like this before signature, and offer to include them.

## 10 Mutual Action Plans

"MAPs are a backdated series of tasks—each task carrying a specific date and owner—that lead the buying team from where they are today, through a buying decision and to their desired outcome."

Order matters: the business case (decision memo) is the why, the MAP is the how. Buyers use a MAP only after they're bought in; it helps them weigh effort against value; the audience is the working team, not the executive.

How to build it (book's five steps):

1. Lay out the customer's typical buying process through onboarding and adoption (security, legal, procurement, finance). Check it against a recent customer: ask your champion what they did internally that you never saw.
2. Organize it into a simple grid of epics; split tasks across both teams; each task gets a DRI and a deadline.
3. Adapt it with your champion: "How does this compare to any past purchases you’ve made? It’d be great to cut what you don’t think applies and add anything I’ve missed."
4. Work backward from a compelling event: "a timebound need or goal that already exists inside the account," discovered with the buyer, never manufactured.
5. Use it strategically, not administratively: spot common friction steps, owners dropping the ball, and tasks you can take on.

**Run it past signature.** A plan that stops at the contract is a close plan. Tom Williams: "This is not a plan to sell my software; it’s a plan to solve your problem."

**Set an early cutoff.** "What amount of time is reasonable to spend getting them involved? I’d hate to just spin our wheels, if this doesn’t become a priority for everyone." If it passes: "Does it still make sense for us to track down their feedback? Or, is this not as big of a priority as we thought?"

**Go-dark agreement (cross-book, Chiarello pp. 111-112).** "I’m not sure that it will happen here, but I feel like I should mention it." Then: "If that were to happen here, can I count on you just to let me know?"

**House commitment tests (not from Selling With):** if the buyer balks at owning tasks, there isn't enough pain; check whether the project is sanctioned (an exec-to-exec call) or just research.

## 11 The Hardwired POC

The standard POC is a paid trial. Turn what the committee sees as a Type 1 (one-way door) decision into a Type 2 (two-way door) decision (Bezos).

- **Five elements:** scope, timeline, hypothesis, measurables, next steps.
- **Shape:** least activity, shortest time, a single big uncertainty, lower perceived risk, a clear go/no-go condition.
- A POC is not a pilot: it strips out about 80% of scope. Constrain it: "What must be true to do this in less than [timeline, e.g., 2 weeks]?"
- Start with the customer, not features: "Why haven’t they already changed?" Find the one shared risk, then test a hypothesis: "If [this condition is true], then [a reasonable conclusion]."
- Go/no-go: "If we’re able to show X, then we’ll want to move forward with Y. But if we only show Z, we’ll agree we don’t have enough evidence to rule out the main risks to moving forward." The buying team defines X; Y (commercial terms) is set upfront. Then ask: "If we hit this goal, and you’re NOT confident moving forward, why would that be?"
- Hardwire it into the MSA: "If [ X ] is delivered by [date], then [ Y ] terms are triggered. If [ X ] is not delivered by [date], the agreement terminates."
- Readout: recommendation, context, complication, conclusions, presented with your champion.

## 12 Deal Momentum and Urgency

"[Level of Title (x) # Buyer Interactions (x) Deal Stage] / [Time in Weeks]"

- **Mass (title):** Executive 5, VP 4, Director 3, Manager 2, Analyst 1.
- **Velocity (stage):** one point per pipeline stage advanced.
- **Interactions:** buyer activity only. "Seller activities aren’t factored into deal momentum—only the activities buyers participate in."

Four drivers: expanded reach, effective follow-up, increased commitment, shorter cycles. Not literal math: use it to compare two deals in the same stage.

**Urgency.** Internal urgency beats urgency you create. Take notes in two columns: functional pains and internal pains. Remove your own limiters, segment the pipeline by seasons of pain (spring, summer, fall), and clarify what inaction means ("How long would you say this has been a problem?"). "set the close date for each new deal to the latest likely date. Move up the date based on your buyer’s behavior only."

**Pricing.** Raise price after discovery and before the demo ends:

- "You haven’t asked, but I imagine you’re curious about our pricing."
- "The reason our pricing model is structured this way is so that you…"
- "How does that price range compare to your expectations?" Then pause.
- "Some providers charge as little as $X for this. Let me share why we charge more and why we might be the smarter choice for you."
- "Let’s say our solution was free. Would we be the right fit for you?"

## 13-15 Mental Frameworks (load `references/mental-frameworks.md`)

- **13 The Change Equation:** "Change = [ D x V x FS ] > R". Dissatisfaction, vision and first steps must outweigh resistance. Hyperlinked decisions.
- **14 Trust:** the trust hurdle and the trust quotient (withdrawals count double).
- **15 The Non-Anxious Seller:** presence and calm as a sales skill; detailed vs superficial leaders.

## 16-21 Mid-Funnel Playbook (load `references/mid-funnel-playbook.md`)

- **16 Copywriting shortcuts:** seven rules; lead with the truth, write to a single person, answer the "WIFM".
- **17 Forwardable emails:** "You’re writing through your champions. Not to them." Five-part framework, idea email, account-team forward.
- **18 Demos that don't suck:** the five-step scenario demo, the reverse demo, and "Outcomes, not operations."
- **19 Why buyers hide objections:** understand, unpack, respond; invert, challenge the assumption, add complexity.
- **20 Minimum Viable Sentence:** goal, necessary context, call to reply.
- **21 Managing up:** narrative weekly pipeline update in scenarios; "Surface bad news early and often."

---

*Worksheet library: `references/worksheet-library.md`. Buying process and business case: `references/buying-process-and-business-case.md`. Glossary: `references/glossary.md`. Chapter notes: `references/chapter-notes.md`.*
