---
name: gap-selling
description: "Gap Selling (Keenan) field manual with Coach and Audit modes. Use for gap analysis, discovery coaching, objection handling, or critiquing a transcript or call notes, demo planning, deals gone dark, prospecting cadence, or pipeline health checks. Read-only overlay."
---

> Mirror of Liam's Notion skill. Canonical source: [Skill: Gap Selling](https://app.notion.com/p/5871584160964c1cac6975dab11d5190) . Edit in Notion first, then re-sync here. Links to app.notion.com need Notion access.

# Gap Selling

## What this skill does

The single home for everything Gap Selling. Field manual + Coach mode + Audit mode. The other sales skills (sales-master, sandler-selling, selling-with, jolt, elicitation) and HPE CRO's deal work reference this framework instead of restating it.

- **HPE / VME:** any write Liam approves goes through HPE CRO. HPE deals live in the Notion HPE Hub's Enterprise Pipeline only. VME Deals is a retired, read-only archive; don't read from it.
- **Toolbox:** any write Liam approves goes through Toolbox CRO (Twenty is the system of record).
- Never name Gap Selling or any sales methodology in anything a customer or partner will see.
- Emails: warm emails ask when a call works; cold emails close with a booking link.

## When it should trigger

- Anything tagged "gap selling", "gap analysis", "gap critique"
- Coaching requests on discovery, questions, objections, next steps
- Audit requests on a transcript or call notes
- A skill needs the framework definitions (Current State, Future State, the Gap, Change Cost)
- Called by `sales-master` for the Gap Selling lens (it runs Mode B Audit).
- Demo planning, a deal that went dark, a trial or pricing demand, or a prospecting cadence (sections XIV-XVII, `references/prospecting-and-pipeline.md`)
- Writing meeting-prep questions, or critiquing *how* discovery was asked: run this skill together with `elicitation`.

---

# Mode A — Coach

Use when the user asks for better questions, talk tracks, objection handling, or next steps.

**Output:**

- 5–12 best next questions (grouped by stage). When the ask is discovery or meeting-prep questions, also load `elicitation`: keep the final list to 5-8 prompts and mix statement forms with questions so it doesn't feel like an interrogation.
- 3–6 coaching notes (what they're doing wrong, what to fix)
- 1 clear next step

# Mode B — Audit (strict)

Use when the user provides a transcript or call notes and asks for critique.

**Required output (use this exact structure):**

1. **What we actually learned (facts only)**
2. **What's missing (by stage)**
   - Current State
   - Impact
   - Root Cause
   - Future State
   - Gap Recognition
   - Change Cost / Risk
3. **Best next questions** (10–15 max)
4. **Red flags / disqualifiers**
5. **Call hygiene** (only when a transcript is given)
   - Did the call open with an up-front contract (purpose, time, both agendas, outcome)?
   - Did the buyer do most of the talking? (Keenan cites Gong: in lost discovery calls buyers talked only 28% of the time and sellers almost 80%; in won calls sellers listened more than half the time.)
   - Did we answer a question we should have asked back ("What made you ask?")?
   - Did the call end with a dated next step and no mystery about what happens next?
   - Did we post-sell (house check: ask them to tell us if it slides)?
   - How was each question asked (presumptive, curiosity, third-party, empathy)? For that check, load `elicitation`.
  For the method behind these checks, load `sandler-selling`. Don't restate it here.

## Sequencing rules (do not violate)

- Current State before Future State
- Quantify impact before solution mapping
- Root cause must be stated in one sentence
- Gap recognition must be explicit
- If there is no quantified impact, do not recommend a proposal or demo
- If the buyer wants to change but can't choose, that is indecision, not a weak gap. Don't add more discovery. Load `jolt`.
- Never combine discovery and a demo in one meeting. No discovery, no demo.
- Every new buyer on the deal gets their own discovery. Never assume they share the first buyer's current or future state.

---

# Field Manual (Reference)

*Distilled from Keenan, Gap Selling. Read top to bottom or jump to a section.*

Quotes in "double quotes" are verbatim from the book. Italic lines without quote marks are paraphrase or Liam's own examples.

## Contents

- I. The Premise · II. The Nine Truthbombs · III. Anatomy of a Sale · IV. Current State · V. Future State · VI. The Gap
- VII. The Discovery Toolkit · VIII. The Pipeline Path · IX. Tactical Tools ("I'm confused", objections, price)
- X. The Ten Emotional Threats (Kanter) · XI. B.A.N.T. Is Bunk · XII. Pipeline Validation · XIII. The Mindset
- XIV. Get Them to Let You Help · XV. The Kickass Demo · XVI. Troubleshooting (dark, stalled, walk away)
- XVII. Gap Prospecting · XVIII. The Healthy Pipeline and Commit Culture
- References: `references/prospecting-and-pipeline.md` (cadence, offers, pipeline reviews, commits, trials, hiring), glossary, chapter notes

---

## I. The Premise

Every sale exists because a customer has a gap between where they are and where they want to be. Your job is not to pitch your product. Your job is to diagnose the gap, quantify it, and earn the right to prescribe.

> "Your customers aren’t really buying products and services like software, consulting services, training, or widgets; they’re buying change." — Keenan

"Gap selling is a process of tactfully challenging buyers’ assumptions, exposing (and sometimes confirming) the true size of their problem, then correctly assessing the impact it will have on their lives."

## II. The Nine Truthbombs

1. **No problem, no sale.** "Problems get you to the impact and the impact is where urgency, value, and need live and where the sale takes root."
2. **In every sale there's a gap.** Never sell to need ("I only needed a charge."). The real gap is usually deeper than the surface complaint.
3. **All sales are about change.**
4. **Customers don't like change.** Even when they say they want it, they often fear it.
5. **Sales are emotional.** "Every sale is about change. Change is emotional. Therefore, every sale is emotional."
6. **Customers do like change when they feel it's worth the cost.**
7. **Asking "Why?" gets customers to "Yes."** Find the intrinsic motivation or you're guessing.
8. **Sales happen when the future state is a better state.** Sell the outcome, not the product.
9. **No one gives a shit about you.** "We are now in the show-me economy." Company history and awards belong online, not in the meeting.

## III. Anatomy of a Sale

Three pillars: Current State, the Gap, Future State.

- **Current State:** where they are. Five elements: facts, problems, impact, root cause, emotional state.
- **The Gap:** future minus current. Quantified. The reason the deal exists.
- **Future State:** where they want to be. Technical, business and "the core of the future state", plus emotion.

The gap is the byproduct of discovery done well. If you struggle to say the gap, you didn't dig deep enough on one of the pillars. "The gap is where the value of the sale lives."

**The change cost gate:** is the gap big enough to justify the total cost of change (disruption, learning curve, political risk, time), not just the price? If yes, the deal moves. If no, widen the gap or walk away.

## IV. Current State (Pillar I)

"There is a direct correlation between how much a salesperson knows about their buyer’s current state and the probability they will win the deal." The current state is the unique identifier for every prospect.

1. **Facts & figures:** the operational reality your product touches (headcount, tools, processes, volumes, infrastructure).
2. **Problems:** specific to what you sell, built from your Problem Identification Chart. "half of your customers won’t even know they have a problem."
3. **Impact:** business consequences. The technical problem is "the conversation starter"; the business problem drives the sale. Keenan's police example: the technical problem was "not being able to communicate across various chains of command"; the business problem was "increased gang violence and decreased conviction rates". "Your prospects can have the same technical problem(s), but never, ever, the same business problems."
4. **Root cause:** why the problem exists. Four layers to reach: technical problem, business problem, existential problem (could the company stall or fold?), root cause.
5. **Emotional state:** frustrated, afraid, resigned. It tells you how to deliver advice so it can be heard.

Discovery order: facts, then problems, then impact, then root cause.

## V. Future State (Pillar II)

Ask the book's two questions: "1. What is the buyer looking to accomplish? and 2. What would solving these problems mean to their organization, their employees, and to them?"

1. **Technical future:** quantified. "“Better efficiency,” is not a specific impact; “reducing turnaround by 20% and increasing production by 50%” is."
2. **Business future:** organization-level outcomes in CFO language (revenue, savings, competitive position).
3. **The core of the future state:** the real why. Why 20% growth and not 30%? Maybe it meets a Wall Street commitment or positions the company for sale. Trigger: "Tell me a bit about what is driving this change." "If you find out that your product can’t fulfill a customer’s intrinsic motivation, walk away from the sale."
4. **Emotion:** how they'll feel once it's solved. "Once your customers believe that the benefits of the future state will outweigh the cost of getting there, the deal is done."

Only after current state, future state and intrinsic motivation may you pitch.

## VI. The Gap

"Future State – Current State = The Gap". The customer wants 20% growth and is at 10%: a 10% and $10M gap. "you’re selling $10M in additional revenue!"

**Is the gap worth it?** Ask yourself: "Is this gap big enough to warrant what it’s going to cost my customer to change and get them to reach their desired future state?" $100K against a $10M gap is easy. $100K against a $1M gap ($900K net) is not clear-cut once you add implementation time, comfort with the status quo, uncertainty and politics.

### The threat-o-meter

The buyer silently asks: "Is this going to take a lot of research? Am I willing to take the time to learn what I need to know to make this decision? Do I want to make the effort? Will this switch be worth the expense? Will this move make me vulnerable? What will be the consequences if I don’t? Is this change worth the risk?" Change happens when the answers add up to yes.

### Widening the gap

If the gap isn't big enough, don't walk yet. Go back to discovery: there's usually more impact (compliance risk, hardware refresh, downstream disruption). Don't rush to close with lines like "If we could solve those problems, would you buy?" If you still can't widen it, tell the customer you don't think you're the right fit and point them to someone who can help.

**House exception: walk now on a hard showstopper.** Don't keep digging if there's a must-have we can't meet, someone above the buyer has already overruled the change, or the buyer refuses to build a plan with owners and dates.

## VII. The Discovery Toolkit

"The sale is won or lost during the discovery." "The close happens at the beginning, not at the end." "there is no gap-selling discovery script": "your goal is not to ask specific questions. It’s to get specific information."

### Four question types

- **Probing:** "open-ended questions that press for specific details". Starters (Keenan borrows Deb Calvert's command statements): "Help me understand . . ." "Please describe . . ." "Walk me through . . ." Impact starters: "Tell me how this issue is affecting you." "What are the consequences every time this problem occurs?"
- **Process:** "open-ended questions that ask “How?”" The tactical steps behind the work. *Liam's example: we use Veeam is high-level; Veeam 12 on a dedicated VM backing up to a SAN over NFS daily at 2am is process.*
- **Provoking:** push them to see their current state from a new angle. Stems: "What happens when you…? Has there ever been a time when…? If you did X, what do you think would happen?" Example: "What if you could see which customers were first-timers and which ones were repeat attendees?" Root cause: "Why do you think this problem is happening?"
- **Validating:** not open-ended; repeat back before shifting topics. "What I hear you saying is that ..." "Am I understanding you correctly?" "Did I get this right?"

**Banish open-ended answers.** "Open-ended answers are unacceptable." Ask "Define that for me? What does “fast enough” mean to you?" or "What is ‘a lot’ to you?" until you have a number.

**Tone and timing.** "Just because you can ask a question, it doesn’t mean you should." Be humble when the buyer built the system at the root of the problem.

**Demand creation.** Gap sellers find latent problems the buyer hasn't seen ("Holy crap. You can do that?"). "Gap sellers never take their prospects’ word for granted when it comes to their needs. Ever." Don't pander to the buyer's self-diagnosis: in Keenan's ARMS Reliability story he won by naming three problems the COO hadn't seen.

### Problem Identification Chart (PIC)

Build it before you prospect. Three columns: problems your product solves, the impact of each, and the root causes. "The reason my product or service exists is to ________." It doubles as your demo map and your ICP filter.

### The diagnostician mindset

Keenan uses doctor analogies (heartburn vs angioplasty, benign vs malignant). Examine, listen, name the condition and its cause, then recommend. By then the prescription feels inevitable.

## VIII. The Pipeline Path

1. **Decision criteria:** "How are you going to decide what’s the best solution for you? What will be the most important factors in helping you make your decision?" Then check each criterion against the future state ("to confirm that the criteria they value the most and are using to make their decision will actually get them the desired outcome they say they want"). If one doesn't serve it, use "I'm confused." "Make them own their decisions."
2. **Buying process:** "Can you tell me a little about your company’s buying process?" The literal steps (RFP, finalists, committee, contract, CEO). Gartner: "the average decision process involves 5.4 buyers!" Criteria plus process gives you the deal strategy.
3. **The next yes:** a rising staircase of small commitments. "every yes you hear is a small sale." The next yes comes from the customer, not from you, and you must say why they value it. If they resist it, go back to discovery. "Good closers are bad salespeople."

**Pipeline test:** name the customer's current next yes, why they value it, and its date. If you can't, you don't have a deal; you have a hope.

## IX. Tactical Tools

### "I'm confused. You said . . ." (Keenan's "My Four Favorite Words")

Challenge any position while letting the buyer save face; the mistake is framed as yours. Alternatives: "I was under the impression," and "I thought . . ." Say it, then shut up.

### Objections

Don't ask the buyer to clarify the objection; ask them to clarify the desired outcome, then hold the objection against it. If resolving it moves them toward the outcome, solve it or get out. If not, say "I'm confused." "Never defend your product or service. Use gap selling and what you learn in the process to make the buyer defend their objection." *Liam's adaptation (not a book quote): I'm confused. You said the main goal was cutting costs by 80%, but you'd walk away from those savings over a feature used by 5% of your VMs?*

### Three price objections

1. **"It's too expensive."** "I’m confused. This product will increase lead conversion rates by 30%, reduce lead generation costs by 50%, and decrease the average sale by thirty days, all of which would lead your company to reach its $50M goal by 2020 [the desired future state]. Why do you find this to be too expensive?" Then shut up.
2. **"We don't have the budget."** The money exists but is allocated elsewhere: "If you don’t move forward till next year’s budget, you’ll lose $50K a month for the next six months. That’s $300K."
3. **"We can't afford it."** They truly don't have the money. Walk.

"So don’t let anyone determine the price of what you’re selling. Ever!" More scripts: `references/prospecting-and-pipeline.md`.

### Conversation tools (supplement: Chris Voss, not from Gap Selling)

- **Mirroring:** repeat the last 1–3 words with a curious tone, then pause.
- **Labeling:** name the emotion. *It seems like… It sounds like…*
- **Calibrated questions:** "what" and "how" questions.
- **That's right:** summarize their reality until they say "that's right" (not "you're right").

## X. The Ten Emotional Threats (Rosabeth Moss Kanter, cited by Keenan)

1 Loss of control. 2 Excess uncertainty. 3 Surprises (a pushy end-of-quarter discount counts). 4 Too much change at once. 5 Loss of face. 6 Insecurity. 7 Extra work. 8 The ripple effect. 9 Past resentments (the last vendor's surprise fees). 10 Real danger (jobs).

**The remedy:** the gap. Restate the current state, the cost of inaction and the desired future state. Make not changing more vivid than changing.

## XI. B.A.N.T. Is Bunk

"B.A.N.T. is bunk." "It’s self-centered."

- **Budget:** "when prospects see enough value in what you’re selling, they’ll find the budget."
- **Authority:** "Today, authority is a committee of influencers, champions, mobilizers, and more." (Gartner, 2014: "at least 5.4 decision makers per B2B sale".)
- **Need:** sell to problems, and create demand rather than only react to it.
- **Timing:** "Timing will take care of itself." Every day unfixed compounds the problem.

**Qualified when yes to all four:** "1. Does the prospect have a problem you can fix? 2. Does the prospect agree they have a problem? 3. Does the prospect want to fix the problem? 4. Will the prospect go on a journey with you to fix the problem?"

## XII. Pipeline Validation (Seven-Question Test)

1. Do you understand the customer's current state? (literal physical business, critical problems, impact, emotional state, root cause)
2. Do you understand the customer's future state? (desired outcome, literal physical impact)
3. Can you identify the gap and explain how you calculated it?
4. Can you name the customer's intrinsic motivations for buying?
5. Can you list the buyer's decision-making criteria?
6. Can you provide evidence the information is accurate?
7. "Do they know what will happen next and when?"

House checks before forecasting: 8 If we stopped calling, would they call us? 9 What real event, other than a discount, forces a decision, and when? No real event, no commit.

**The CRM Challenge:** a peer reads your notes with the customer's name removed. If they can't tell which opportunity it is, "it’s a tell-tale sign you’re selling your product, not selling to the desired outcome."

## XIII. The Mindset

> "Likeability gets you a handshake, a smile, and maybe a warm and fuzzy feeling. Expertise makes you money."

- **Be an expert, not a friend.** "People want to go to hockey games with their friends; they want to buy from people who know their shit."
- **Honesty as a sales weapon.** Tell the truth even against your short-term interest.
- **Selling is giving.** On every touch ask: what am I giving?
- **Partner, not servant.** "The customer is not always right." "If you find yourself afraid of losing the deal, it’s probably a sign you’ve lost control." Trials, pricing-before-discovery and the servant-vs-asset test: `references/prospecting-and-pipeline.md`.

## XIV. Get Them to Let You Help

"Your number one job when selling is to get the customer, buyer, or prospect to let you help them." Test: "Am I selling to these individuals, or are they allowing me to help them?" Are they sharing numbers, issues and worries? "If you can’t get buyers to let you help them, the sale is dead."

**RFPs.** "Bidding on an RFP is not selling, it’s participating in a beauty contest." If an RFP blocks discovery, gap selling can't help. Pair with `sandler-selling` before Liam commits time.

## XV. The Kickass Demo

1. **No discovery, no demo.** "You should never, ever combine a discovery and a demo." Separate days, three to four days apart to customize; tell the buyer the demo is a two-step process.
2. **No ifs.** "There is no “if” during a demo because you’re supposed to already know!" Challenge: run the whole 45-60 minutes without saying the word if.
3. **Stick to six features.** "prospects that buy only do so because of a select few." An hour max.
4. **Anchor your customer.** Make your solution their baseline by asking affirming questions after each feature: "Can you see how this feature will improve your churn rate?" If they say no, "Stop the demo right away and start digging for more information".

**Demo map.** Rank PIC problems by impact, greatest to least. "If an issue or problem doesn’t appear on the list, don’t mention it."

## XVI. Troubleshooting

**Deal gone dark.** "Prospects know when they owe you a response." Don't send "just checking in." "don’t become desperate. Instead, be direct." Book script: "I’m confused. You said you were tired of getting beat out for bigger, more complex projects, and you agreed that my product would improve your value proposition tenfold and get you to your financial goals. So I’m surprised I haven’t heard from you. Has something changed?" Write Liam's version short, as a warm email that asks when a call works.

**Stalled deal.** Book script: "Tom, I’m more than happy to push that meeting off another week, but I’m a little confused. You said that every month that goes by without a new system in place you’re losing money, and yet you were hoping to increase your profits next year by 4%." Then: "It’s going to get awfully hard for you to reach that goal if we keep going at this rate, isn’t it? Is that OK?" If the gap is still real but the buyer keeps asking for more demos, references or time, that's fear of choosing wrong: load `jolt` and give one clear recommendation.

**Walking away.** Summarize their current state, remind them what they want to achieve, say you can't help, and recommend someone who can. "knowing when to walk away from a sale can be one of the most helpful things you can do for a customer and for yourself."

## XVII. Gap Prospecting (details in `references/prospecting-and-pipeline.md`)

- **Prep:** healthy pipeline math, know who you're calling (PIC-based ICP ranked A-D by problems × impact), be a problem finder, think like a buyer.
- **Intrigue:** surprise, mystery, a knowledge gap; "An exploration of unseen or unrecognized opportunities", not features.
- **Offer vs ask:** "Offer – Ask = Value". "Don’t ask for a chance to talk. Ask for a chance to give value."
- **Cadence:** every channel, a new impact each touch; it "could take anywhere from 8–12 touches". Every touch "must include: intrigue, a clear and reasonable ask, an offer, and a net benefit to the customer". "Never say no for your buyer." Cold emails close with Liam's booking link. Pair with `fanatical-prospecting`.

## XVIII. The Healthy Pipeline and Commit Culture

**Reviews:** the seven questions (XII), 2-10 minutes per opportunity, 15-30 minutes total. "Be skeptical of the “talker.”" If the rep only thinks they know, they don't.

**The Healthy Pipeline Checklist.** Accurate close dates (within 30 days), accurate quarterly commits within 15% on either side, clear next steps (the next yes), clear deal strategies, adequate pipeline coverage, and evidence for all of the above.

**Commit culture.** "Commit is an accuracy game, not a goal game." Commits land within 15% either way; challenge an over-commit, then accept it ("It’s their commit, not yours."). "Surprise is the enemy of a sales leader."

---

*Compiled from* Gap Selling *by Keenan, A Sales Guy Publishing. Prospecting, pipeline and trials: `references/prospecting-and-pipeline.md`. Glossary: `references/glossary.md`. Chapter notes: `references/chapter-notes.md`.*
