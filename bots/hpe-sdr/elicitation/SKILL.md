---
name: elicitation
description: "The Truth Detector (Schafer & Karlins) field manual with Coach and Audit modes. Use for ethical B2B discovery prompts, meeting-prep questions (5-8), or critiquing a transcript for elicitation moves used and missed. Read-only overlay."
---

# Elicitation

## What this skill does

The single home for ethical elicitation in Liam's sales work. Field manual + Coach mode + Audit mode, distilled from Schafer and Karlins, *The Truth Detector*. It is a way to help an IT leader talk honestly about their estate, their constraints and what would have to be true for a change, without an interrogation feel.

It does not replace Gap Selling discovery. It changes how the questions are asked. `gap-selling` still owns Current State, Future State, the Gap and Change Cost. This skill supplies the conversational moves that get fuller, more accurate answers.

## Read-only overlay

This page is a read-only methodology overlay. It may read deal records and transcripts and produce coaching or an audit in chat. It never writes a CRM, a Notion database or a deal page.

- **HPE / VME:** any write Liam approves goes through HPE CRO. HPE deals live in the Notion HPE Hub's Enterprise Pipeline only. VME Deals is a retired, read-only archive; don't read from it.
- **Toolbox:** any write Liam approves goes through Toolbox CRO (Twenty is the system of record).
- Never name elicitation, the book, or any sales methodology in anything a customer or partner will see. Prompts must read as Liam's own words.
- Emails: warm emails ask when a call works; cold emails close with a booking link.
- Never mix HPE and Toolbox sources in one review.

## When it should trigger

- "elicitation", "truth detector", "discovery prompts", "how should I ask", "meeting prep questions"
- A request for 5-8 discovery questions before a customer or partner meeting
- A transcript or call notes that need critique for how discovery was run, not only for what was learned
- Called by `sales-master` when it writes the merged "questions to ask next", or when a transcript is part of the review
- Called by `gap-selling` Coach mode when it writes discovery questions

For a full gap critique (Current State, Impact, Root Cause, Future State), load `gap-selling` Mode B. This skill audits the *asking*, not the whole deal.

---

# Ethics (do not violate)

Liam is a seller. The buyer already knows that. These techniques exist so the buyer feels safe telling the truth, not so we extract secrets they would not choose to share.

**Required:**

- Lead with rapport and real curiosity. Keep the focus on the buyer, not on us.
- Be honest about why we are in the room. Never disguise the purpose of the meeting.
- Use only facts we actually have. If a presumptive statement or a reported fact is a guess, say so, or frame it as something to correct.
- After a hard operational fact lands, thank them and move on. Do not linger or pile on.

**Forbidden:**

- Manipulation, deception, pressure, traps, or manufactured "spotlight" moments
- Inventing a news item, a rumor, or a source to make a buyer talk
- Status demotion, embarrassment, or cognitive-dissonance setups that put a buyer on the spot
- Fishing for personal data, credentials, passwords, dates of birth, or anything outside the deal
- Gossip used to get one stakeholder to undermine another
- Using these moves to hide a pitch inside small talk

If a move would still work if the buyer knew exactly why we asked, it is in bounds. If it only works because they would feel tricked later, drop it.

---

# How it plugs into other skills

**Meeting prep (default Coach output).** Write 5-8 discovery prompts, not 10-15. Mix statement forms and questions. Map each prompt to a Gap Selling element (facts, problems, impact, root cause, future state, change cost, or buying process). Hand the list to Liam in language he can say out loud.

**`gap-selling`.** That skill still sequences Current State before Future State, and still forbids a proposal or demo when impact is unquantified. This skill only changes the *shape* of the prompts: a presumptive or a third-party frame can replace a blunt "What's your VMware renewal date?" when a direct question would get a thin answer.

**`sales-master`.** After the four lenses draft their question lists, load this skill to rewrite the merged top 5 so they are speakable and not an interrogation. If a transcript exists, add a short elicitation audit (moves used, moves missed) before the merge. After a proposal, `jolt` limits new digging. In that phase, use empathy and listening here, not a new round of prompts.

**`sandler-selling`.** Keep the up-front contract. Elicitation starts after purpose, time and outcome are agreed.

---

# Mode A — Coach

Use for meeting prep, better questions, or talk tracks.

**Output:**

- 5-8 discovery prompts, grouped by what we need to learn. Each line is something Liam can say. Label the technique in parentheses, then the Gap Selling element.
- 3-5 coaching notes (what to open with, what not to ask head-on, where to stay quiet)
- 1 clear next step

**Prompt rules:**

- Prefer one prompt at a time. Do not stack three questions in a row.
- Prefer a statement, a curiosity frame, or a third-party comparison when the fact is sensitive (budget, renewal date, who can say no, a failed tool).
- Use a direct question when the buyer is already volunteering detail, or when a number or owner must be named.
- Never invent a stakeholder, a date, a count or a quote. If the fact is unknown, say so in the coaching notes and write the prompt as a hypothesis to correct.

# Mode B — Audit (strict)

Use when the user provides a transcript or call notes and asks for critique.

**Required output (use this exact structure):**

1. **What we actually learned (facts only)**
2. **Moves used** — technique, a short quote, and what it unlocked
3. **Moves missed** — where a direct question got a defensive, vague or one-word answer, and a better prompt
4. **Call hygiene**
   - Did we agree purpose and time up front? (For the method, load `sandler-selling`.)
   - Did the buyer talk most of the time?
   - Did we listen, reflect with "So you..." language, and avoid parroting?
   - Did we ask one thing at a time, or stack questions?
   - Did we stay ethical (no trap, no fake source, no pressure)?
   - Did we leak HPE pricing, roadmap or unconfirmed Enablement facts? (See Counter-elicitation.)
5. **Best next prompts** (5-8 max)
6. **Red flags** — the buyer closed up, a fact was guessed and treated as known, or we should walk back a question

Read full transcripts, never summaries. If speaker labels are unreliable, attribute by context and say so.

---

# Field Manual (Reference)

*Distilled from Jack Schafer and Marvin Karlins,* The Truth Detector*. Adapted for HPE Morpheus / VM Essentials discovery with IT leaders. The book's covert and personal-data examples are not part of this skill.*

## Contents

- I. The premise
- II. Why people tell the truth in conversation
- III. Rapport and listening
- IV. How to run the conversation
- V. The toolkit
- VI. Personality
- VII. Counter-elicitation
- VIII. Checklist

---

## I. The premise

People tighten up when they feel examined. A direct "What's your budget?" or "When does VMware support end?" often gets a polite, incomplete answer. A calm statement, a moment of curiosity, or a request to correct our picture gets a fuller one.

Scharff's lesson, kept and stripped of its wartime setting: be respectful, do not press, and let the other person be the expert. Empathy and rapport are the conditions. The techniques are just the tools.

Elicitation works when two things are true: we know what we need to learn, and the buyer feels good about the conversation. The win is a clearer current state, not a confession.

## II. Why people tell the truth in conversation

Use these tendencies. Do not exploit them.

- **The need to correct.** People will fix a wrong picture, and they will often add the real number or date while doing it. Offer a hypothesis you are willing to have corrected.
- **Pride in the work.** Infrastructure and platform owners like to explain how their estate actually runs. Invite that expertise.
- **Curiosity.** An honest information gap ("I'm still missing how you handle the branch sites") gets them talking more than a checklist does.
- **Reciprocity.** If we share a relevant, non-confidential observation first, they are more willing to share theirs. Never trade HPE secrets for theirs.
- **Talking about a third case.** People speak more plainly about "a shop like yours" or "another VMware estate in this range" than about their own politics.
- **Recognition.** Sincere credit for a hard migration, a tight operating model, or a clear standard makes people more specific. Fake praise does the opposite.
- **Bits add up.** Socket counts, who opens a ticket, which backup tool they run, and which date is real, each look small. Together they are the current state. Do not treat a small fact as worthless, and do not stitch guesswork into a fact.

The book names ten natural tendencies (Ch 3 headings): people tend to correct others, talk about other people, have a need for recognition, gossip, are naturally curious, reciprocate, have difficulty keeping secrets, consider themselves experts in their fields, underestimate the value of the information they possess, and can't hold two opposing ideas at the same time (cognitive dissonance). We use correcting, talking about others (as the third-person habit), recognition, curiosity, reciprocity, expertise and "bits add up" above. Gossip, secret-sharing for status, and induced dissonance stay out of customer work.

Two book findings worth keeping in mind: reciprocity "is felt most strongly right after the initial gesture of goodwill is made," and people "talk more than they listen" when an information gap makes them curious.

## III. Rapport and listening

Rapport is the foundation. Without it, the toolkit is just a list of tricks, and we will not use it that way.

- **Make them feel well treated.** The book's Golden Rule of Friendship: "If you want people to like you, make them feel good about themselves." Drop our ego (the book calls ego suspension "The single most important skill"). They are the expert on their environment.
- **Friend signals, used naturally.** A real smile, a slight head tilt, brief eye contact. Do not perform this.
- **Empathy, not parroting.** "So you..." plus the meaning, in our own words. "So the renewal is the forcing event, and the platform team is already at capacity" is useful. Repeating their sentence back word for word sounds like a tactic.
- **Let them compliment themselves.** "It takes a lot of discipline to keep two hypervisors in production and still hit your change window." Then be quiet.
- **Common ground,** when it is real: a shared account history, a known standard, a prior workshop. Do not invent one.
- **Active listening.** In the book's words, "we can think four times as fast as most people talk," so the failure mode is planning the next pitch while they are still answering. Concentrate, wait a second or two after they finish, keep natural eye contact, and do not interrupt. Listen for the fact, then form the next prompt.

Verbal encouragers ("Go on", "I see") and a nod keep an extrovert talking; the book says frequent nodding "increases the amount of speech by a factor of three or four." With an introvert, ask once and wait.

## IV. How to run the conversation

1. **Decide what you need to learn** (the book's "determine what you want to achieve with the elicitation"). One or two truths per meeting, not twelve. In this motion that is often: the VMware forcing event and date, who owns the platform, whether the pain is a hypervisor swap or a provisioning and governance problem, and what would have to be true for a yes.
2. **Agree the purpose of the meeting first, then build the environment.** In the book, "create the right elicitation environment" means rapport: friend signals, the Golden Rule, ego suspension. We add an unhurried setting with no audience to perform for. Do not hide discovery inside small talk.
3. **Open with them, not us.** A short check on their world, then pivot to the topic they already agreed to discuss. The book calls the pivot "the key to a successful elicitation." Pick your moment: the book's advice for a hard conversation with a boss is "Wait for a time when your chair is not busy."
4. **Use one or two techniques at a time.** Daisy-chain only when the first prompt is working (for example, empathy, then a presumptive, then a bracket on the date).
5. **When the fact lands, close that thread cleanly.** Confirm what you heard, then go to the next agreed topic. The book's "elicitation sandwich" is recast here as courtesy, not camouflage.
6. **Leave them better than you found them.** They should feel understood, not examined.

Do not follow the book's "DON'T ASK QUESTIONS" step ("The best way to elicit information is to ask nary a question."). In enterprise discovery we will ask. We just will not lead with a barrage, and we will not use a question when a statement would get a more honest answer.

## V. The toolkit

Each move below is the book's technique, rewritten for a Morpheus / VM Essentials conversation. The left column is the name to use in Coach and Audit output.

### Presumptive statement

Offer a picture of their world that can be right or wrong. If it is right, they confirm and usually add detail. If it is wrong, they correct it, and the correction is the fact.

*"From the last working session, it sounded like the forcing event is the VMware renewal, not a greenfield build. Tell me if I've got that wrong."*

Do not bluff that we know more than we do. If it is a hypothesis, say it is one.

**Presumptive question**, when a statement is too soft: *"When is the last date you can still choose a path for that renewal?"* assumes a date exists, which in this motion it usually does.

**Negative presumptive**, when we need to know if a problem is real: *"Is the operational load of running two consoles going to be a problem for the platform team in the first year?"* A positive "everything is fine, right?" invites a brush-off.

**Tag questions** can confirm a known fact: *"The POC still needs written success criteria before it starts, doesn't it?"* Use sparingly.

**Escape clause.** If the presumption is wrong and they bristle: *"Good, I wanted to get that straight rather than take it as given."*

### Third-party perspective, and storytelling

Ask about a comparable situation, not their internal politics.

*"A lot of VMware shops in this range are cutting footprint workload by workload, not leaving in one move. How close is that to what you are seeing?"*

Storytelling works when the story is a real, relevant case (a public reference, or a pattern we have actually seen) and does not name a confidential customer. The book's test: "the story should be relevant to your targeted individual's current situation, have a moral, and suggest a course of action". Do not invent a "friend of mine" to smuggle in a pitch. Many of the book's third-party examples use invented friends; we don't.

### Bracketing

For numbers and dates. Offer a realistic range and let them place the truth inside it. Too narrow, and they will not bother to correct. Too wide, or insulting (a cluster "of a few hundred hosts" when they run twelve), and we lose them. When age or size could sound like a slight, bracket toward the more favorable side.

*"Renewals like this often land somewhere between the next quarter and the next twelve months. Where does yours fall?"*

Use for socket counts, host counts, VM counts, renewal windows, and POC length. Not for fishing a budget number they have said they will not share.

### Curiosity

Name the gap between what we know and what we do not. Then stop.

*"I still don't have a clear picture of how a new VM gets approved today. I'd like to understand that."*

Curiosity is not a cliff-hanger we set as a trap. It is honest interest.

### Status: elevate, never demote

Treat the buyer as the expert on their estate. Ask for their advice on what would actually work here. Do not puff them up past what is true. The book's own rule: "the status and/or recognition should be deserved and not manufactured". Never lower their status to provoke a correction. The book warns that demotion "can negatively impact the self-esteem" of the person. We will not use it.

The book's one sales example: a textbook rep who implied the professor's current choice was inferior got shown the door. The fix was asking for advice: "Hi, Professor [insert last name], I'd like your advice about a new textbook we've just put out if you have the time." Asking their opinion "will yield a more truthful and willing evaluation without putting pressure on him or her to make a purchase." Never open by implying their current platform choice was a mistake.

*"I'd value your read on whether the gap is the hypervisor, or the lack of a catalog and policy around it."*

### Empathetic statements

Mirror the meaning, not the wording. Basic form: "So you..." In the book, "The empathetic statement presents a fact but leaves the interpretation of that fact to the customer." If it is right, they add detail; if it is wrong, they correct it. Listen for loaded words: in the book's washer example, "have to buy" signaled a serious buyer with an immediate need.

*"So the team can keep VMware running, but self-service is still a ticket queue."*

If we have nothing useful to say, an empathetic line is better than a pitch.

### Naïveté (genuine, not an act)

When we are not the expert in *their* environment, say so, and ask them to walk us through it. This is especially useful with a platform owner or a senior engineer. It is not playing dumb about our own product. The book agrees: "Naïveté doesn't mean pretending you're stupid. Even the smartest people have gaps in knowledge." It works best "combined with a sincere dose of curiosity."

*"I don't want to assume how you run Kubernetes today. Walk me through it from the ticket to the cluster."*

With people in authority (a CIO, a CRO), the book's approach: "daisy-chain naïveté, empathetic statements, and presumptive statements." That lets them keep their status and show their expertise. Don't raise yourself to their level.

### Quotation of reported facts

Only with a real, sourced public fact. Then invite correction against *their* estate.

*"There's a June 2026 HPE program around a free year of VME for new customers, but I want to confirm what's current before we lean on it. What's the commercial pressure on your side?"*

Never invent "I read that your company..."

### Quid pro quo

Share a non-confidential, useful observation first, then pause. Example: the pattern that Enterprise fit usually shows up as several teams, a catalog need, and a named platform owner, not as "they are leaving VMware." Do not disclose unconfirmed pricing, roadmap, or another customer's private facts.

### Light skepticism, and real disbelief

A raised eyebrow at a clean story can open a more precise one: *"Really? No exception process at all?"* Use only when the disbelief is genuine. Theatrical fake shock is deception, and it is out.

### Word echo, and hanging chad

Repeat the last one or two words, then wait. *"Ticket queue."* Useful when they pause. A hanging chad (leaving a sentence unfinished) can work with an extrovert. Never finish an introvert's sentence.

### Techniques we do not use

Erroneous misattribution (crediting someone with a skill they plainly lack so they correct you), induced cognitive dissonance, status demotion, feigned disbelief, invented sources (the book's reported-facts definition allows "whether true or false"; we allow only true), and any "gotcha" document slide-across-the-table move. Also out is Holmes's advice to make people think their information is of no importance to you. Those belong to the book's interrogation and covert examples, not to a customer meeting.

## VI. Personality (keep it light)

Do not remote-profile a buyer into an MBTI type, and do not claim a type you have not been given. Do watch the E/I split, which is usually visible in the first meeting.

- **Extroverts** think out loud, may finish our sentences, and fill a silence. Let them talk. Nudges help. Have a few topics ready. Hanging chad, curiosity, and a presumptive often work. Then sift their words for the few facts that matter.
- **Introverts** think, then speak, and mean what they say. Ask one thing, count to three, and do not jump in. Word echo, quid pro quo, bracketing, and a real curiosity gap work better than a rapid back-and-forth. They often want time before a decision. Do not force one in the room.

If they clearly favor logic (the book's Thinkers), lead with numbers and trade-offs: "don't ask how they feel, ask what they think". If they weigh people and values (Feelers), lead with the team impact and points of agreement. If they keep options open (Perceivers), give choices and don't force a quick decision. If they clearly favor facts and sequence (sensing / judging), go in order, use numbers, and send material ahead. If they favor the big picture, do not bury them in socket math first.

## VII. Counter-elicitation

Partners, customers, and other sellers will use the same moves on us. That is normal. Protect what is not ours to give: unconfirmed Advanced pricing, PCAI claims, Enablement items still marked verify, another customer's private details, internal forecast numbers, and roadmap we have not been cleared to share.

The practical defense, adapted from the book's "Bryan's loop": decide in advance what we can say. The book's business version: answer "Yes plus," "No plus," or "I don't know plus" (the plus is the fact we pre-cleared), then redirect the conversation back to the person asking.

*"I don't know if that program is still open. I can confirm with Enablement and come back. What date are you working toward on your side?"*

Name the move when we notice it, at least to ourselves (the book: "Your best defense against elicitation being used against you is identifying it, giving it a label"). Don't go into "automatic response" mode. One stray fact can be a mistake. A string of them is a jigsaw puzzle someone else is assembling, from one person over several conversations or from several people at one event. Before giving out anything internal, check who is really asking. If we leak, say so in the audit.

## VIII. Checklist

**Before**

- What one or two truths do we need from this meeting?
- Which prompts (5-8) will we actually use, and which technique does each one use?
- What are we not allowed to share?

**During**

- Purpose agreed. Buyer is the focus. We are listening.
- One prompt at a time. Hypothesis offered for correction, not as a bluff.
- Empathy in our own words. No parroting, no pile-on, no pressure.

**After**

- Close the topic cleanly and leave on normal terms (the book's after-steps: pivot away, disengage as after any conversation).
- Process what we heard and decide what still needs clarifying (the book's checklist step 3). Confirm the facts in writing, as *their* words or as our paraphrase clearly marked.
- Write the 5-8 prompts for the next meeting from what is still unknown.
- If a technique felt slick or deceptive in retrospect, retire it.

---

*Compiled from* The Truth Detector *by Jack Schafer and Marvin Karlins. This skill is an ethical overlay for HPE discovery. It is not a license to practice the book's covert or personal-data examples.*

*Glossary (the book's 16 named tools, marked use or don't use): `references/glossary.md`. Chapter notes, including per-preference technique lists: `references/chapter-notes.md`.*
