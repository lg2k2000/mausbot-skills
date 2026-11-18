---
name: outbound-guardrails
description: "Use before any Toolbox or Apivant cold touch or lead handoff: the do-not-touch and already-touched audit list builders run before a row goes Ready or a lead leaves their hands, and the pause rules, row state and day-two board the cold email bots run on their sequences. Grants no new sends, writes or spend."
---

# Outbound guardrails

Adapted from two marketplace bots: Prospector (Caro Scalercio) for the do-not-touch audit, and Sequencer (Simon Lackowski) for pause rules, row state and the day-two board. Liam picked both Nov 12 2026 11:22 PM MT ("do the sequencer fold into the cold email bots", "do the prospector do-not-touch audit for prospect list and lead finder").

This skill adds checks. It grants nothing. Your profile's approvals, caps, walls and quiet hours still win. Toolbox and Apivant stay walled: each bot checks only its own business's sources.

Who uses which part:

- Toolbox Prospect List and Apivant Lead Finder: Part 1, before a row goes Ready or onto a dial sheet, and before a lead is sent or handed off.
- Toolbox Cold Email and Apivant Cold Email: Part 1 on each lead before each touch, then Parts 2 and 3.

## Part 1: do-not-touch audit

Run it per row, and as one dated pass over the whole list when your weekly hygiene run happens.

1. Dedupe key, in order:
   - Toolbox: website domain (no www, http(s) or path), then phone (digits only), then owner email (lowercased), then Owner LinkedIn URL.
   - Apivant: the Apivant Leads Dedupe key: lowercased work email, else LinkedIn URL, else name|company, with mailto formatting stripped.
2. Do not touch (never contact):
   - Toolbox: a Twenty client or open-deal contact (people by email, companies by domain, open opportunities; read-only); an unsubscribe, "remove me" or stop reply in Toolbox or trytoolbox Gmail or in Instantly; a hard bounce; rows that are Suppressed, Disqualified or Pass. For calls and texts, also Mobile DNC "On DNC list".
   - Apivant: a key with a Sent, Rejected or Do not contact row; a company with a Sent row in the last 8 weeks; the open or past Apivant opportunities listed in Lead Finder's profile (Affirm, Workday) until HubSpot access; any opt-out from Apivant Cold Email or Apivant; for dialer lists, a number on the National Do Not Call Registry.
3. Already touched (hold, don't drop): anyone our side contacted by any channel in the last 30 days outside the sequence they are in now, whether by Liam, Bruce, Sarah's LinkedIn, a cold email bot or a CRO; anyone with a booked meeting or an open thread with Liam.
   - Hold means: not Ready, not on a dial sheet, not enrolled, and one Notes line: "Held (<date>): touched <date> by <channel>, <source link>". The hold clears when the 30 days pass and nothing else blocks the row.
   - Toolbox sources: Toolbox and trytoolbox sent mail, the Toolbox outreach send log ([Toolbox outreach send log](https://app.notion.com/p/4141acdf10d281068a0bffd25148a9ef)), the row's Last touch and Channels, Twenty Notes and tasks.
   - Apivant sources: the Apivant Leads row and its Notes (Apivant Cold Email writes enrollment, pauses and opt-outs there), /workspace/fleet/apivant-send-log.md, and Apivant sent mail for the weekly §3.9 send.
4. Conflicts: when two sources disagree (a CRM title vs a public profile, two owner emails, a Twenty client whose row still looks cold), show both with their dates and sources. Never merge them and never pick one by guess. The row stays out until it's settled and goes under Unknowns.
5. Write only what your profile already lets you write. Toolbox Prospect List sets Stage "Suppressed" and appends Notes. Lead Finder sets Status. Cold email bots append a Notes line (Apivant Cold Email may also set Status "Do not contact"; see Part 2). Never change a schema, and never delete, archive or merge rows. If a property you need is missing, use Notes.
6. Report each pass as Result / Evidence / Unknowns: counts by reason (suppressed, held, cleared), one source link per reason, and each Unknown with the question that would settle it. Stamp the pass date. Stay quiet when nothing changed and nothing is unclear.

## Part 2: pause rules (cold email bots)

Before each touch and on every reply check:

- Pause the lead in Instantly (stop it in its campaign; never delete it) when they replied, booked a meeting, asked to stop or unsubscribed, hard-bounced, became a Twenty client or open deal (Toolbox), or Part 1 flags or holds them.
- An out-of-office reply doesn't stop the sequence. If it gives a return date, push the next step past it.
- Write the reason and date on the row the same run:
  - Toolbox prospects: Reply status (none, replied, positive or negative), clear Next step date, and a Notes line "Paused (<date>): <reason>, <source link>". Bounces and unsubscribes go in that Notes line.
  - Apivant Leads: a Notes line "Paused (<date>): <reason>, <source link>". Set Status "Do not contact" only for an opt-out or a hard bounce. Touch no other field; Lead Finder owns the row.
- Never resume a paused lead without Liam's yes in your chat.

## Part 3: row state and the day-two board (cold email bots)

- The prospect row is the record, not only Instantly. After each touch, write what your profile says plus the Instantly campaign and step in Notes or the page body ("<campaign>, email 2 of 3, <date>").
- Day-two board: the first message of each sending day's run to Liam is a short board, sent only when it has something on it:
  - Due today: how many touches go out, from which sender and campaign.
  - Waiting on Liam: templates, lists or replies waiting on his yes, with their ledger refs.
  - Paused since the last board: name, reason, date.
  - Problems: bounces, spam complaints, warmup or placement flags.
    Then run today's queue within your approved limits. Nothing due, waiting, paused or wrong means no message.
- A yes to a plan or a board is never a yes to a new routine, a new template or more volume.
