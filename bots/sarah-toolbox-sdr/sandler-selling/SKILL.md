---
name: sandler-selling
description: "Sandler Selling System field manual (Rich Chiarello, Selling Technology the Sandler Way; Dave Mattson and Brian Sullivan, Sandler Enterprise Selling) with Coach, Script and Deal audit modes. Use for up-front contracts, pain funnel questions, budget and decision qualifying, mutual action plans, reversing, negative reverse, post-sell, objections, DISC tone, stakeholder maps, disqualifying a deal, RFPs, enterprise account plans, pre-call plans and call debriefs, monkey's paw first deals, presentations, or loss debriefs. Read-only overlay."
---

# Sandler Selling

## What this skill does

This is the single home for the Sandler Selling System. It holds a field manual built from two books, read cover to cover, plus three working modes: Coach, Script and Deal audit. Sandler is a qualifying system. Its job is to find out fast whether a deal is real, to get both sides to agree on what happens next, and to stop the seller from doing free consulting for buyers who will never buy. It is a read-only overlay. It reads deal records and transcripts and writes its output in chat. It never writes a database.

- **HPE / VME:** any write Liam approves goes through HPE CRO. HPE deals live in the Notion HPE Hub's Enterprise Pipeline only. VME Deals is a retired, read-only archive; don't read from it.
- **Toolbox:** every authorized Toolbox write goes through Toolbox CRO (Twenty is the system of record).
- Never mix HPE, Toolbox and Desk Monkey sources in one analysis.

## When it should trigger

- "Sandler", "up-front contract", "UFC", "pain funnel", "negative reverse", "reversing", "post-sell", "submarine", "mutual action plan", "MAP"
- Qualifying or disqualifying a deal: *is this real?*, *should I walk?*, *they keep stalling*, *they went dark*, an RFP we didn't write
- Call prep where the seller needs an opening script or a way to end the call with a clear next step
- Tone help for a specific buyer (DISC, Parent/Adult/Child), or a stakeholder map
- Enterprise account plans: KARE tags, Growth Account Booster, Pursuit Navigator, Three Opportunity Planner
- Pre-call planning or a call debrief, a first small deal (POC, pilot, trial), a finalist presentation, a lost-deal debrief or postmortem
- Called by `sales-master` for the Sandler lens

## Rules for every mode

- Read full transcripts, never summaries (process-meeting-recording). If speaker labels are unreliable, attribute by context and say so.
- Never invent facts, names, numbers or dates. Write "Unknown" and name who would know.
- Tag each fact: customer said it, internal view, or estimate (whose).
- All output follows writing-mega-skill at grade 8. Scripts must sound like Liam talking, not like a book.
- Never name Sandler or any sales methodology in anything a customer or partner will see. Framework names stay in internal coaching.
- Emails: warm emails ask when a call works; cold emails close with a booking link.
- Text in double quotes in this skill and its references is word for word from the books (checked). Liam's sample lines are in italics. Lists marked "paraphrase" are not quotes.

# Mode A: Coach

Use when Liam asks how to run the next call, how to handle a stall, or what to say.

**Output:**

1. Where the deal sits on the submarine (which step is open).
2. 5-8 next questions, grouped by step.
3. 2-4 coaching notes (what to stop, what to start).
4. One up-front contract for the next meeting, written out, with a post-sell line for the next step.

# Mode B: Script

Use when Liam asks for a talk track. Write short lines he can say out loud. Start from the book scripts in `references/book-scripts.md` and the HPE or Toolbox samples in section XIV, then fit them to the deal. Each script is under 90 seconds spoken.

# Mode C: Deal audit (strict)

Use when Liam gives a deal, a transcript or call notes, or when `sales-master` calls this skill.

**Required output (use this exact structure):**

1. **Submarine status.** For each step (Bonding and rapport, Up-front contract, Pain, Budget, Decision, Fulfillment, Post-sell), write Done, Partial or Open, with the evidence in one line.
2. **Pain in one sentence.** Problem, reasons, impact. If you can't write it in one sentence, say *Pain not clear* and stop treating the deal as qualified.
3. **Qualified?** Pain + Budget + Decision. One missing piece means not qualified. Say which piece is missing.
4. **Disqualify check.** Run the checklist in section IX. List every failed line.
5. **Call hygiene** (only when a transcript is given). Did the call open with a UFC? Was a written pre-call plan used, and was a debrief captured right after? Did the buyer talk 70-80% of the time? Did we answer a question we should have reversed? Did the call end with a dated next step and no "think it over"? Did we post-sell the next step?
6. **Sandler questions to ask next.** 3-5, ranked, written so Liam can say them.
7. **Sandler gaps.** What's missing, in priority order. 3-5 lines.

## Sequencing rules (do not violate)

- Pain before budget. Budget before decision. Decision before any presentation, proposal or demo.
- No fulfillment until pain, budget and decision are qualified. Then ask if they want to explore solving it with us, and build a mutual action plan (MAP) before anything else.
- Demos, POCs and presentations inside a MAP are still qualifying, not fulfillment.
- Every meeting has an up-front contract. No contract, no meeting.
- When a buyer asks a question, find out why before you answer (reverse), unless it is a plain fact question.
- After any yes, post-sell before you hang up.
- No real impending event, no forecast. A discount deadline is not an event.
- Meet each stakeholder alone before any group demo.

---

# Field Manual (Reference)

*Distilled from a full read of Rich Chiarello,* Selling Technology the Sandler Way *(Sandler Training, 2015), and Dave Mattson and Brian Sullivan,* Sandler Enterprise Selling *(McGraw-Hill, 2016; "SES" below). Chiarello's copy is a scanned library PDF; quotes from it were checked against the OCR and the page images where the OCR was rough.*

## Contents

- I. The Premise
- II. The Submarine
- III. Up-Front Contracts
- IV. The Pain Step and the Pain Funnel
- V. The Budget Step
- VI. The Decision Step and Stakeholders
- VII. Mutual Action Plans, Fulfillment and Post-Sell
- VIII. Reversing, Negative Reverse and Objections
- IX. The Disqualify List
- X. Tone: DISC and Parent/Adult/Child
- XI. Enterprise Account Planning (SES)
- XII. Chiarello's Technology Lessons
- XIII. SES Stages, Tools, Proposals and Losses
- XIV. Sample Scripts: HPE and Toolbox
- References: `book-scripts.md` (word-for-word scripts and questions), `enterprise-account-tools.md`, `chapter-notes.md`, `glossary.md`

## I. The Premise

Traditional selling makes the seller chase, pitch and hope. Sandler flips it. The seller acts like a peer who is checking for fit, not a vendor who needs the deal. Both sides can say no at any time, and a clear no is a good outcome. A "think it over" is the worst outcome, because it eats time and tells you nothing. David Sandler's definition, quoted by Chiarello: "Selling is what takes place when you lead the prospect through a step-by-step process, each step of which may lead to the prospect's disqualification and removal from the process."

**SES rules (verified):** "Hunt in packs." "Feed the funnel." "Agreements drive actions." "No pain, no sale!" "Validate the funding." "Nothing happens until someone makes a decision." "Early exit or early acceleration." "People are more likely to be persuaded by their own words than by yours." "Bid on the business you've earned the right to win." "You win, or you learn." "Stay focused: drive the win to a fair and workable contract." "There is no better time to win business than after you've won business." "People buy from people they like and from people like themselves." "Know your competitors so well that they bring out the best in you." "Let the client define success." "Do what you say you'll do."

## II. The Submarine

SES names the seven steps: Bonding & Rapport, Up-front Contract, Pain, Budget, Decision, Fulfillment, Post-sell. In standard Sandler training each step is a compartment: close each hatch before you move on, or the deal leaks. SES adds what must happen "before Bonding & Rapport and after Post-Sell" (planning before, delivery and growth after) "without changing any of the core Sandler principles."

1. **Bonding and rapport.** Get the buyer talking. Match their DISC style (section X).
2. **Up-front contract.** Agree on the purpose, time, agendas and outcome of every meeting.
3. **Pain.** The problem, the underlying reasons and the impact, business and personal.
4. **Budget.** Willing and able to invest money, time, resources and political capital.
5. **Decision.** Who decides, how, where, when, why, and who can veto.
6. **Fulfillment.** Present only what fixes the pain they told you about.
7. **Post-sell.** Lock the decision in and head off buyer's remorse or a competitor's counterattack.

## III. Up-Front Contracts

An up-front contract (UFC) is a short spoken agreement at the start of every meeting. SES's five components:

1. **Objective.** A clear objective that moves the process forward.
2. **Time.** How long. If it's two hours, the buyer must agree to give two hours.
3. **Prospect's agenda.** What we need them to bring or be ready to discuss, agreed in advance so they're prepared.
4. **Salesperson's agenda.** What we plan to do in the meeting, and they're okay with it.
5. **Outcome.** A defined ending agreed in advance: a decision, a next meeting with others, or ending the process. "Playing it by ear" is not a strategy.

Chiarello's cold-call UFC asks permission to ask questions, then gets two promises: if either side decides it's not a fit, say so; if it merits a follow-up, say that too. It ends with an agreement that neither side will say "let me think it over." Full exact text: `references/book-scripts.md`.

UFCs work inside the seller's team too: between sales and delivery, between manager and rep, and on forecasts. Before a big call, agree who leads, who covers what, and what we need to leave with.

## IV. The Pain Step and the Pain Funnel

SES: "Pain exists when there is a real or perceived gap between an existing situation and the desire for a better situation." Three pieces make a complete picture: "the problem, the underlying reasons, and the impact."

**One-sentence test (SES):** "What is the single biggest problem you solve for that person and that organization? If you can't express that in a single sentence, or if the sentence is built around features or product specifications, you've still got some work to do."

Open with Chiarello's first pain question: "Which would you say is the highest priority? Tell me more about that. Where are you today, and where would you like to be?"

**The pain funnel (SES Figure 12.2).** Go down in order. Don't skip to the bottom. The figure is an image in the book, so its text couldn't be checked word for word; these are the standard Sandler pain funnel questions, not a verified quote.

1. "Tell me more about that . . ."
2. "Can you be more specific? Give me an example."
3. "How long has that been a problem?"
4. "What have you tried to do about that?"
5. "And did it work?"
6. "How much do you think that has cost you?"
7. "How do you feel about that?"
8. "Have you given up trying to deal with the problem?"

The questions move from the problem as the buyer sees it to the impact if nothing is done. "People are willing to take action to resolve a problem situation only when they fully realize the depth of their pain."

**Three kinds of pain (Chiarello):** surface, business and personal. Most sellers stop at surface pain and rush to a discount close. Find the person with the most personal gain from fixing the business problem. David Sandler: "people buy for emotional reasons and then later back up their decision with facts."

**Diagnose before you treat.** Prospects rarely bring you the real problem first. A symptom (reps don't use the CRM) can come from many root causes. "Sales ‘peddlers’ start selling too soon."

**The 3x rule (Chiarello):** to qualify, the problem should cost the company "at least three times what your fully implemented solution will cost."

## V. The Budget Step

Budget means willing and able to invest money, time, resources and political capital. SES: "Willing minus able equals unqualified for budget." Then broaden the talk to people who are able.

Chiarello: the question is not whether there's a line item, but "whether they have a demonstrated willingness and ability to move money around to fund a desired business outcome." A buyer in real pain usually tells you budget and decision freely.

**Two roadblocks to willingness (SES):** technical (doubts it will fit or work in their environment) and conceptual (doubts it fits their larger strategy). Find both early.

**SES budget questions** (pick one to use word for word): see `references/book-scripts.md`. Short forms: is funding available now, or when; what part price plays; will the lowest bidder win; any limits on spend; how past purchases affect this one.

Ask about time and people too. A buyer with money but no staff time to run a POC is not qualified. Check your own money messages: if talking money makes you uneasy, you'll skip this step.

## VI. The Decision Step and Stakeholders

SES lists three outcomes: fully qualified and it fails, so exit; not finished, so keep qualifying; fully qualified and it passes, so advance. "Qualification is pain, budget, and decision—as confirmed for a specific, unique enterprise selling opportunity. One missing piece means there is no qualification."

Ask who, what, how, where, when and why. Use open questions first, then element-specific ones (exact SES lines in `references/book-scripts.md`), e.g. "Yolanda, what will you need from me to be comfortable making a decision?"

**Four decisions in every tech sale (Chiarello):** "1) technical, 2) business, 3) financial and 4) political." Map who makes each.

**Corporate overrule.** A local buyer may win the choice and lose at headquarters when it breaks a corporate standard. Get proof they can buy off-standard before you invest nine to twelve months. "you can't always take the prospect's word on this kind of thing." For VME, ask early who owns the virtualization standard.

**Cast of characters.** Decision maker, user buyer, tech buyer, financial buyer, coach, key influencers. Mark each friend, neutral or enemy: "This can only be ascertained through a one-on-one conversation." Get all to at least neutral, "since even one negative stakeholder can torpedo a deal." "Assume nothing!" The boss's goals don't trickle down, and nobody voices a personal objection in a group.

**Off the org chart.** A trusted outside advisor can stop a deal cold with "Why switch?" Once the cast is known, ask your main contact who they'll go to for advice at the end, and offer to include that person. Script in `references/book-scripts.md`.

**Three outcomes, one pays:** "your solution, a competitor's solution, or no decision at all." Chiarello: "Most ‘waste of time’ sales cycles get started because the salesperson does not qualify the Decision Step with the same effort as the Pain and Budget Steps."

## VII. Mutual Action Plans, Fulfillment and Post-Sell

**The bridge to a MAP (Chiarello).** Once pain, budget and decision are qualified, ask: "Is X something you would like to explore solving with us?" A yes means you've been "invited in." Then propose a list of tasks both sides complete to reach a yes or no decision. You can't ask them to promise to buy; you can ask for a plan to decide.

**What goes in the MAP.** Both sides get tasks with dates. Ours: stakeholder interviews, demo, POC structure, proposal, references, intro to the post-sales team. Theirs: intros to stakeholders, demo data, ROI requirements, legal review, exec-to-exec meetings, internal visibility. "If the prospect starts to balk at assuming any action items, you should take this as a big red flag that you have not uncovered enough personal pain." Offer to be the project manager, not the one doing every task.

**Executive bridging.** Line up our executives with theirs during the cycle. It tells a sanctioned project from a research project, firms up the forecast date and sets up the price talk. Buyers give our executives different answers than they give the rep.

**Fulfillment.** Present only what fixes the pain they told you. Open with a UFC. Take their temperature at key points. Close with next steps. Beat the time you agreed.

**SES "refine the position" check, run with the whole team before any proposal.** Confirm the ten business requirements (problem or pain, capability needed, users, how it fixes the pain, benefits, when needed, dependencies, risks, scope in and out, key assumptions), the cast, needs and pains, and the competition's value proposition.

**Fingerprinting (SES).** Share your themes and plan with trusted contacts and let them shape it. Don't ask leading questions. "it's tough for people to say ‘no’ to an idea they helped create." If procurement rules block direct input, follow the rules and use coaches in informal talks.

**Post-sell.** After any yes, raise what could undo it and let the buyer promise it won't. Chiarello's two versions are in `references/book-scripts.md`: post-selling the next appointment, and the "biggest fear" agreement once the MAP is built ("our project might go on the back burner. If that were to happen here, can I count on you just to let me know?"). After a verbal win, don't broadcast it until the contract is signed.

## VIII. Reversing, Negative Reverse and Objections

**Reversing.** Answer a question with a question to find the reason behind it. Chiarello: "It is much more important to understand why the prospect asked a certain question than it is to answer it." His example: "That's a great question. And you're asking it because...?" Don't reverse plain fact questions, or you'll sound evasive.

**Negative reverse** (standard Sandler; not in either book). Say the thing the buyer may be thinking, in the negative, so they push back toward you. Example in section XIV.

**Objections (Chiarello's three keys):** "Handle your own anxiety. Understand the real objection. Defuse the prospect's emotion and put him back into a receptive mode." "objections are a salesperson's best friend." No objections halfway through usually means you're not a finalist.

How to defuse (paraphrase of his steps):

1. Listen all the way through. Never cut them off.
2. Play back what you heard and get them to confirm. If there are several, isolate them and take one at a time.
3. Agree with the feeling, not the objection, like a nurturing parent: "If I were you I'd feel the same way." Then a logical adult next step.
4. Find the source. Did a competitor plant it? "You must be telling me that for a reason—which is...?"
5. Answer calmly, then check: "Did I address your concern?"

Most objections "are not well-rooted," so be ready to answer on the spot. A must-have we can't meet is a showstopper, so disqualify. Skillful tension is fine; price pushback is a role, not a personal attack.

## IX. The Disqualify List

Walk now if any of these is a hard no. Keep digging if it's a maybe.

1. Does the problem cost at least 3x the fully implemented price?
2. Does our contact have a strong personal stake and the power to fix it, or will they take us to who does?
3. Can someone above them, or a corporate standard, overrule the choice?
4. Will they share the decision process in a timely way?
5. Will they own tasks with dates in a mutual plan?
6. Will they let us sell our way, as a peer, or do they dictate every step (an RFP we didn't help write, or "RFP-like" rules)?
7. Is there a real event, other than a discount, that forces a decision?
8. Is there a must-have we can't meet?
9. Is this a sanctioned project or one person's research project?

**When to walk.** Walk on a hard showstopper: a must-have we can't meet, a corporate overrule, refusal to build a plan, or a buyer who won't move on pain, budget and decision. SES on stalled deals: "If someone fails to move forward with you on specific, timely, commitment-driven discussions about pain, budget, and decision process, that disqualifies the opportunity." Dig more when the pain is real but small.

## X. Tone: DISC and Parent/Adult/Child

**DISC (both books).** Most people lead with one style, sometimes two, never three or four. Read it from their words and emails: action words ("win", "do it") vs reserved ones ("plan", "process"); task words ("on time") vs people words ("consensus").

- **D (Dominant):** "tell them the bottom line, give them a few choices, and then let them decide how to proceed." Clear ground rules and a clear UFC. No small talk.
- **I (Influencer):** friendly, not rushed or controlled; they get "around" to business. Talk ideas and people, not figures. They may presume rather than plan, so pin down terms and next steps in writing.
- **S (Steady Relator):** steady pace, no hard sell, no surprises. "Voicemail, e-mail, or memos give high S's time to digest and respond." Work in stages. Show how it helps them personally.
- **C (Compliant):** "Forget small talk and pleasantries." Facts in a logical order and time to weigh every option before you ask for a decision. Send data before the call.

Not adapting means you connect with about 25 percent of people. Staff the team to match: a bottom-line buyer may need a bottom-line person on our side.

**Parent/Adult/Child (transactional analysis).** Both books use it; the rules below are standard Sandler.

- Stay in the Adult: calm, factual, curious.
- Use the Nurturing Parent to agree with a feeling ("I'd feel the same way").
- Avoid the Critical Parent (lecturing) and the Child (eager to please, scared to lose the deal). Buying emotions, such as fear, come from the buyer's Child.
- A seller in the Child gives free consulting and chases. A seller in the Adult asks for a clear yes or no.

## XI. Enterprise Account Planning (SES)

Full tool notes: `references/enterprise-account-tools.md` (KARE, Growth Account Booster, RACI, value arrows, 30-second commercial, LinkedIn Levers, Relationship Builder, coaches, Three Opportunity Planner, Positioning, Pre-call Planner, Call Debrief, Opportunity, Pursuit Navigator, compelling themes and value links, presentations, loss debriefs, Client-centric Satisfaction, Team Storm, Client2, retention).

Load it for any account plan. The checks to run every time:

- **Wake-up call test:** "how many people within that account could you reach out to over the weekend and expect to hear back from before Monday morning?" Most teams say zero.
- **Pursuit Navigator:** "Even one unmitigated risk means the deal is probably unwinnable or would result in a piece of business you might come to regret winning." A single point of contact is a major risk.
- **Three Opportunity Planner:** the three most likely deals to close in about 60 days. "Sooner and smaller is more accurate for income/cash-flow predictions than later, bigger and less certain."
- **Competitor's value proposition:** SES says the most important thing to know about a competitor is "their value proposition for a specific buyer in a specific opportunity."

## XII. Chiarello's Technology Lessons

**Rules quoted in the book:** "Sell today. Educate tomorrow." "If everyone is a prospect, then no one is a prospect." "You don't have to like prospecting. You just have to do it." "Your outlook dictates your results."

**End-user/feature disengagement.** Buyers of tech "are strongly predisposed not to care about the features and specifications." Lead with the problem. Before you answer a feature question, ask "May I ask you what makes you think you need a hammer?" Product knowledge is a landmine: it tempts sellers to sell too soon and show off.

**The pipeline math.** "$ = QPRxC%": revenue from qualified prospects times close rate. Getting twice as good at qualifying can take a 2-in-10 close rate to 4 in 10.

**The call-back test.** "If you stopped calling all of your qualified prospects, how many would pick up the phone and call you first?" The ones who wouldn't "do not feel that they need to buy from you as much as you feel you need to sell to them."

**Pain is the best impending event.** Tech buyers can always keep what they have, so deals slip. Discount deadlines teach buyers to wait and cause the "hockey stick" quarter. "If you don't have that kind of situation, don't forecast the sale!" "Impending events can be created in qualified prospects, as long as you focus on the personal pain of the buyer." A paid trial that the buyer agrees will be removed at the end is a real event. For VME, *just renew VMware* is the competitor in every deal, and the renewal date is the event only if someone feels the pain of it.

**Who's leading this dance?** A buyer can pass pain, budget and decision and still be unqualified: "If they will not let you sell to them in a manner that historically has provided you with a high level of success, you should consider them disqualified." An RFP you didn't help write usually shows which competitor got there first.

**Abundance.** Act like you have more prospects than time. "People cannot force you to sell to them."

**Opening a cold call.** The first 90 seconds are scripted, the rest is not. A pattern interrupt uses curiosity: "I'm not even sure if we need to have a conversation today." The 30-second commercial names three problems with pain words (frustrated, challenged, concerned), then asks which applies and stops talking. "By using the concept of ‘struggling’ in your opening, you make the prospect feel OK about himself."

**Head trash.** "a problem that lies between the ears" that a seller treats as reality (*my contact told me not to call the CFO*). Its most common cause is failing to separate who you are from the role you play. Coach it out of Liam's prospecting block; it is never a reason to skip the work. Agree a weekly prospecting "cookbook" (calls, intro requests, meetings with new department heads) and schedule prospecting time in stone.

## XIII. SES Stages, Tools, Proposals and Losses

**Six stages** wrap the submarine: 1 Territory and Account Planning, 2 Opportunity Identification, 3 Qualification, 4 Solution Development, 5 Proposing and Advancement, 6 Service Delivery. In practice it's a continuous cycle.

**BAT (Success Triangle).** Behavior (daily habits, "muscle memory"), Attitude (outlook), Technique (what you do and say). Technique training alone gives short-lived gains; coach all three.

**Pre-call Planner.** A written plan before every enterprise meeting: who attends on each side, each person's impact, DISC and stance, goals for the call, questions to ask, questions they may ask and our answers, and the planned UFC. **Call Debrief.** Right after the call: new information, next steps, red flags, topics for next time, and actions with owner, date and intended result. "Write it all down!"

**Coaches.** You need several, from the user, buying, technical and influencer groups. The top person may be "the last and least informed."

**Monkey's paw.** "a little, easy-to-gain agreement that sets up a big partnership with the target organization." Forms: Proof-of-Concept, Prototype, Pilot, Trial, Quick-Start. Choose based on client culture, competitive strategy, need for quick results, funding limits and need to verify our approach. Price it under the buyer's own signing limit to skip committees. It's high risk, high reward: "failure usually means that you are done for good."

**Proposal rules (eight tips).** Client-centric guidance throughout. Leave an empty chair for the customer at planning meetings. Staff the right people, not the available ones. Fresh, relevant references. A truly custom solution. Fingerprint "at every critical point." A custom value proposition with value links. The buyer's industry words throughout.

**Presentations.** Know if it's with the proposal or a down-select. Find out who will attend; new executives often appear here. Rehearse at least an hour with people from other teams, in a similar room, and plan a bare-bones version. Open with a UFC, give every presenter a clear role, and send each buyer a personal follow-up within 24 hours. Full checklist: `references/enterprise-account-tools.md`.

**No anvil sales.** "a loss is the first step to a win." Thank the buyer first; you're judged by how you take the loss. Ask for a client debrief, then run an internal postmortem against the Pursuit Navigator. Run one after a win too.

**Haze of victory.** "At all costs, avoid broadcasting your win until the contract is signed." "Celebrating early is a margin-killer." "Do not rejoice over what has not yet happened." Defer big hiring and spending until it's signed.

**After the win.** Let the client define success (Client-centric Satisfaction), keep the ten business requirements in front of delivery, use Team Storm for fast fixes, and grow the account with Client2. Ask: "What have I done today to grow this client?"

## XIV. Sample Scripts: HPE and Toolbox

These are Liam's lines, not book quotes. Fit them to the deal.

### HPE: VME as a VMware exit

**UFC:** *We've got 30 minutes. I'd like to hear how you run VMware today and what the renewal quote did, and you can grill me on VME. At the end, either of us can say it's not a fit, and that's fine. If it is, we pick a next step with a date before we hang up. Does that work, and is there anything you want to add?*

**Pain:** *Which would you say is the highest priority right now: the renewal cost, the upgrade pain, or the team's time? Tell me more about that.*

**Negative reverse:** *If you just signed a three-year VMware renewal, this probably isn't worth your time this year. Is that where you are?*

**Budget:** *I don't imagine there's extra money sitting around for this. How have projects like this been funded before?*

**Decision:** *Who besides you would need to be comfortable before this moves? Could anyone above you, or a corporate standard, overrule it?*

**MAP:** *Would it make sense for us to list what both sides need to do to get to a yes or a no by the renewal date?*

**Post-sell:** *Sometimes the renewal gets pushed and these projects slide. If that happens here, will you just tell me?*

### Toolbox: small-business websites

**UFC:** *We've got 20 minutes. I'll ask how customers find you now and what the site is costing you. Ask me anything. At the end you either tell me it's not for you, or we book the build call. Fair?*

**Pain:** *When someone searches for what you do in your town, what happens? How many jobs a month do you think that costs you?*

**Negative reverse:** *If the site's bringing in enough work right now, you probably don't need us. Is that where you are?*

**Reversing:** *Good question. What made you ask?*

**Cold email close:** end on the gap question, not an "I'll stop contacting you" line, and never a breakup email (Liam, Nov 12 2026; see writing-mega-skill). Example: *Are you getting enough jobs right now, or do you want more?*

---

*Compiled from Rich Chiarello,* Selling Technology the Sandler Way *(Sandler Training, 2015), and Dave Mattson and Brian Sullivan,* Sandler Enterprise Selling *(McGraw-Hill, 2016). Word-for-word scripts: `references/book-scripts.md`. Tools: `references/enterprise-account-tools.md`. Chapter notes: `references/chapter-notes.md`. Glossary: `references/glossary.md`.*
