---
name: deal-anatomy-brief
description: "Use when someone asks for a brief, status or 'where are we' on a deal or account (for a funder, manager, partner or exec): a short, neutral, just-the-facts brief of the deal's current state plus an org chart of everyone involved and where they sit. Also use its Account brief section for sourced research on one named account before a meeting or a first move."
---

# Deal anatomy brief

A short, neutral, lawyer-precise brief on a deal that can be forwarded to many readers, with an org chart of everyone involved.

## Rules

- Just the facts. Each line is sourced, labeled "estimate" (with whose estimate), or labeled "Unknown".
- Neutral tone. Never make a deal sound dead. Write risks as open questions or conditions ("Unknown: ...", "Depends on: ..."), never as red flags or verdicts.
- No sales-method names or framework jargon in the output (no Gap Selling, MEDDICC, Change Equation, "current state/future state", etc.). Use the methods privately to decide what matters, but write in plain words.
- Concise: half a page per deal at most, one-line bullets, short sentences.
- Never invent numbers, dates, names, titles or reporting lines. Leave gaps as [TBD] blanks.
- Read full transcripts, not summaries (process-meeting-recording). On recordings without speaker labels, don't attribute lines to a specific person unless the source makes it certain.
- Leave out internal chatter, personal remarks, speculative budgets, comments about colleagues, competitor gossip and private pricing notes, unless the requester asks for them.
- Draft only. Never send it; the owner sends it.

## Steps

1. Gather every source for the deal: the deal page or CRM record, call recordings (full transcripts), meeting notes, emails the owner shared on purpose, and quotes or orders.
2. Pull the anatomy:
   - account
   - partner(s), noting any conflict between what was said and what the CRM shows
   - what they've already bought
   - what they run today
   - the problem they named, in their words
   - what they want instead
   - the ask (money, people, or the next yes)
   - deal size (sourced or labeled estimate, with its basis)
   - timeline and key dates (renewals, terms, close dates)
   - next step
3. Split the facts into Known and Unknown. Every Unknown gets the question or the person who would answer it.
4. Write the brief per deal under these headers:
   - Bought so far (only if relevant)
   - Known
   - Unknown
   - Ask
   - Deal size
   - Timeline
   - Next step
     For more than one deal, open with a one-table cover: account, partner, ask, investment, est. deal size, timeline.
5. Build the org chart ("Who's involved"):
   - A Mermaid flowchart grouped into customer, partner and our side.
   - Each node shows name, title and deal role: decision maker, champion, technical evaluator, budget, influencer, or unknown.
   - Solid lines for confirmed reporting or working links, dashed lines for unconfirmed ones.
   - Under the chart, one line per person: what they care about, and how confident we are in that.
   - If the destination doesn't render Mermaid, render it to PNG (e.g. `npx @mermaid-js/mermaid-cli`).
6. Check the draft:
   - every number has a source or label
   - no framework names
   - nothing reads as a verdict
   - blanks are visible
   - excluded material is out
7. Return it to the owner with three lists: the [TBD] blanks to fill, the facts that couldn't be verified, and any partner or CRM conflicts.

## Account brief (one named account)

Adapted from the marketplace GTM Account Research bot (Stefan Markarian). Liam picked it Nov 12 2026 11:22 PM MT ("do the account research brief for hpe cro and hpe sdr").

Use it for research on one named account before a first move or a meeting. HPE CRO owns HPE account briefs, and HPE SDR does the public people and signals research when HPE CRO asks. Toolbox CRO may use it for a Toolbox or Apivant strategic account. It is internal prep. If it will be forwarded, the neutral, method-free rules above apply too. It is never a bulk list and never outreach.

Sections, in this order. Every line has a source and a date, or says Unknown:

1. Company now: what changed in the last 12 months (leadership, funding, layoffs, M&A, earnings lines, public statements on infrastructure, VMware/Broadcom, cloud, or the problem we solve).
2. Stakeholders: name, title, likely role (champion, economic buyer, technical evaluator, blocker, unknown), what they said in public with date and link, and how sure we are. A role is labeled "estimate" unless the person or a document says it.
3. Relationship history: every past touch we can see (deal pages, calls with the full transcript read, mail Liam shared on purpose, LinkedIn engagement logs), with dates. "None found" is an answer.
4. Technical and competitive context: what they run today and who else is in, from public sources or our own calls only.
5. Open questions: each Unknown with who could answer it.
6. Meeting plan, when a meeting is booked: the goal, the next yes, 5-8 discovery questions (gap-selling), and who should be in the room.
7. Sources: every link with the date it was read.

Rules:

- Sourced or Unknown. Never fill a gap with a guess.
- When sources conflict, show both with their dates. Never merge them silently.
- HPE accounts: public sources plus HPE CRO's own deal and account pages; no HPE mailbox content. The brief lives only on the HPE Hub account page or the Enterprise Pipeline deal page.
- No LinkedIn profile opens or LinkedIn search for this research; use what web search snippets show (LinkedIn pace rule).
- Save it on the account or deal page with the date. Refresh that brief before each meeting instead of writing a new one.
