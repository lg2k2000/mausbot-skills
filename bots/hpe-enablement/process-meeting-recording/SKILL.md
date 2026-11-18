---
name: process-meeting-recording
description: "Use for every meeting recording you file, and whenever any bot answers a question about a meeting or pulls facts from one: read the full raw transcript first (never only the summary), pull out every ask and route it, summarize, update the matching Deal, Project, and tasks, and flag real uncertainty."
---

# Process meeting recording

Process one completed meeting from start to finish in a single pass. The job isn't done when the Recording is linked. Ask routing, summary, and writeback are all part of it.

The finished result must include:

- every ask pulled from the raw transcript and routed to its owner
- an accurate, structured summary that covers every topic
- correct business classification and routing
- the matching Deal and Project updated with current facts
- existing tasks reconciled, and new tasks created only when needed
- a clear uncertainty flag instead of a guess when the evidence conflicts

## Full-transcript rule (hard first step, always)

Liam, Nov 1 2026 1:58 AM MT: "READ THE FULL ACTUAL TRANSCRIPT ALWAYS NOT THE FUCKING SUMMARY". Why: on Oct 31 Okta's MDF deadline rules were missed because only summaries were read; the rules were in the full transcripts.

This applies to every bot, not only the filer: whenever you file a meeting, answer a question about one, or pull facts from one, this step comes before anything else. It is the single home for the rule; bot profiles point here.

1. Get the full raw transcript: the transcript block on the Notion meeting note, the Pocket transcript (Pocket MCP), the Fathom transcript (Fathom connected since Nov 3 2026), or the Granola transcript (Granola connected Nov 13 2026; Liam's outbound phone calls). The AI summary, takeaways, or action-item list are not the transcript.
   - Notion: fetch the meeting note with `include_transcript: true`. By default the Notion connector returns a placeholder with the note's URL instead of the transcript. A placeholder means the transcript has not been read yet, never that it is empty or that the summary is enough. Also check `truncated` and `unknown_block_ids` and fetch anything omitted.
   - Pocket: read the full transcript text of the conversation. Pocket's summary and action items are not the transcript.
   - Fathom (connected since Nov 3 2026, namespace user-Fathom): read the full transcript text with get_meeting_transcript. Fathom's summary, highlights and action items are not the transcript. Notion and Pocket stay as the fallback queues; dropping the Notion queue after 3 good Fathom calls needs Liam's yes. HPE calls on Fathom are fine (Liam, Nov 9 2026): file them and hand them to HPE CRO as usual.
   - Granola (namespace user-Granola, account [liamglennie@gmail.com](mailto:liamglennie@gmail.com)): read the full transcript with get_meeting_transcript, passing next_offset until no next_offset is left. Granola's summary, private notes and query_granola_meetings answers are not the transcript. A get_meetings note can say transcript available while get_meeting_transcript returns no_transcript; trust get_meeting_transcript, and treat no transcript as no transcript (step 4). Granola is reads only: never create or edit notes or folders, never change sharing, never generate summaries.
2. Read it all, start to finish. For long calls read it in chunks until you reach the end. Never skip, skim, or sample a chunk, and never stop early because the summary seems to cover it.
3. The summary is only a cross-check after the full read, never a source. If the summary and the transcript disagree, the transcript wins; note the conflict.
4. If only a summary is available (no transcript, or it won't load), say so plainly: tell Liam the full transcript isn't available (the filer hands that to Chief of Staff in its batched handoff, since it never messages Liam; any other bot says it in its own reply). Never silently fall back to the summary, never answer from it as if it were the transcript, and never mark the recording Filed, Parsed, or complete. Set Needs Parse and retry next run.
5. Scope: meetings only. Liam's personal Pocket notes, voice memos, and private thoughts are not meetings; this rule never pulls them in, and the Personal rule below still stands (Skipped, nothing in business records anywhere).
6. HPE: full HPE meeting transcripts and anything drawn from them stay on HPE/VME pages only (HPE CRO files them). Never quote HPE meeting content into Toolbox, Apivant, Personal, or shared pages, and never put HPE call outputs in Twenty. The filer's handoff to HPE CRO is fine; any other bot gets only the link and a one-line pointer.

## Transcript intake (after the full read)

1. Confirm the full-transcript rule above was met for this recording. If it wasn't, stop here.
2. Before writing anything else, build the ask list: every thing a participant on our side (Liam, Bruce, or whoever owns the business) says they want, should do, will try, or wants a bot to do. Include new ideas, tools, channels, and experiments, even ones that sound casual. A product, tool or vendor to look into ("we should look into X") on any call, personal calls included, goes to Product Research (SendToAgent 04dff081-7bb2-441c-b7ec-a5a8a88935b5). Each ask gets a rough timestamp, the exact gist, and the owner bot it goes to (or Chief of Staff if nothing owns it).
3. Route every ask to its owner. Asks are never trimmed, merged away, or ranked out of the output. A new ask that would become work must become a handoff, not just a line in a recap.
4. Then list every distinct topic and decision with a rough timestamp. No top-N cutting.
5. Only this skill's runner (the recording filer) summarizes calls. Coordinators relay its output rather than writing their own summary of the same call.

## Evidence and meeting identity

Use evidence in this order:

1. The full raw transcript (always read, per the rule above).
2. The meeting title, the strongest first clue for routing.
3. Existing Deal, Project, Contact, and company relations.
4. The native meeting summary, as a cross-check only.
5. The current Deal, Project, and open tasks, compared against the meeting before you write anything.

The title is a hint, not truth. Check it against the participants and what was actually discussed. A passing mention of another customer doesn't change the destination. Check the calendar and email for misheard names, and apply the misheard-name fixes on the rules page.

If one recording contains several calls or unrelated sections:

- Split them by customer, project, or business.
- Keep each section's facts, decisions, asks, tasks, and terms with that section.
- Never copy one section's pricing, people, channels, or next steps into another destination.
- If the sections can't be separated safely, set Needs Parse, explain why in one sentence, and stop before changing any commercial records.

## Business and destination routing

Classify each recording as Toolbox, Apivant, HPE / VME, Desk Monkey / Proverbly, or Personal.

**Toolbox** (Liam and Bruce's websites and ops business)

- Twenty trial (2 weeks; Liam, Nov 1 2026 6:57 PM MT, in Chief of Staff's chat: "Okay, accurate."): Twenty (connector `user-Twenty Toolbox`) is the source of truth for Toolbox deals, pipeline and client to-dos. The Notion Toolbox deals database is read-only, so never write to it.
- Search Twenty for the matching company, people and deal (opportunity).
- Add one Twenty Note per Toolbox call with the recap and the transcript link, linked to that company, people and deal (`create_one_note`, then `create_one_note_target`). The Note is the filer's only Twenty write. Never create tasks, edit records, or change a stage or amount in Twenty.
- Hand every deal ask, commitment, new opportunity, and stage or amount change to Toolbox CRO (SendToAgent 4c957bbb-0da9-4c5c-b63c-8503977b4b9b, priority true). Toolbox CRO writes Twenty and pings Liam the same turn. If Twenty has no matching company or deal, add no Note and say so in the handoff.
- Search Projects before creating one. When the meeting establishes real delivery work, link the matching Project or create one Toolbox Project.
- Optional follow-on ideas stay as parking-lot tasks or separate opportunities until approved, not new Projects. They still appear on the ask list and get routed.

**Apivant**

- Route to the matching Apivant deal or project page. Mercor is Apivant's deal. "Oppivant", "AppAvant", and similar spellings all mean Apivant.
- Hand Apivant delivery asks and anything that needs a non-money Apivant Slack or email reply to Apivant Chief (SendToAgent 68b97da1-ee63-4201-8d13-543a8a7f6a86); Apivant invoices and payments to Toolbox RevOps; new SOWs, change orders, renewals and MDF deal terms to Toolbox CRO.

**HPE / VME**

- Link a specific customer opportunity to its deal page in the Enterprise Pipeline ([Enterprise Pipeline](https://app.notion.com/p/58cd4d00f64247e8ae02792dffddf8ce)). Create an Enterprise Pipeline deal only for a clearly identified customer with no existing match. VME Deals is retired and read-only (Liam, Nov 2 2026).
- Keep internal enablement, training, team coordination, and general pipeline talk out of customer deals.
- HPE confidentiality applies: HPE material goes only on HPE/VME pages.

**Desk Monkey / Proverbly**

- Desk Monkey is Liam's solo entity and now mainly the business side of Proverbly, his iPhone app. File it there and never cc Bruce.

**Personal**

- Mark it Skipped (Handed to: Personal Assistant if it had asks, else None). Personal recordings never go into business records.
- Personal calls (family, such as Liam's calls with his dad; Liam, Nov 13 2026): hand Liam's own personal asks to Personal Assistant (SendToAgent 1ea12cac-5338-4a01-bcc0-96d8a3f7e7b6) and to no other bot. A product, tool or vendor idea from the call also goes to Product Research (SendToAgent 04dff081-7bb2-441c-b7ec-a5a8a88935b5), as the idea only, with no personal details beyond what it needs. Copy nothing else anywhere.
- On any call, Will Glennie is never a lead, task or outreach target (standing do-not-contact rule).

## Post-call pack trigger (sales calls)

Liam, Nov 12 2026 11:22 PM MT ("do the call follow-ups fold into both cros"). A sales call has a prospect or customer on it and a deal in play: a Toolbox prospect or client deal, Toolbox's own sales to Apivant (new SOW, change order, renewal, upsell), or an HPE enterprise customer meeting. Internal calls, Apivant delivery calls, Toolbox client delivery calls, partner enablement and personal recordings are not sales calls.

After you file a sales call, always hand it to the CRO that owns the deal, even when the call has no other asks: Toolbox CRO (SendToAgent 4c957bbb-0da9-4c5c-b63c-8503977b4b9b) for Toolbox and Apivant sales, HPE CRO (SendToAgent 94ffa9cc-2c4c-46b0-accc-d8a11daacbce) for HPE, priority true. The first line is "Post-call pack: yes". Then give the recording link, the date and start time (MT), attendee names and emails where the calendar or recorder shows them, and the Twenty Note or deal link. Put it in the handoff you already send for that call; never send a second message for the same call. The CRO stages the follow-up email, CRM diff and promise list with the post-call-pack skill. You never draft follow-ups.

## Summary format

Asks: the full ask list from the intake rule, first, one line each (timestamp, ask, owner bot it was routed to).

Recording Summary: three to six short sentences covering who met and why, what changed, where things stand commercially or on delivery, and the most important next action and blocker.

Topics: every distinct topic discussed, one line each with a rough timestamp. Nothing dropped for length.

Takeaways: bullets, in this order:

1. Decisions made.
2. Commercial terms, with exact amounts, timing, and whether each is proposed, verbally accepted, signed, invoiced, or paid.
3. Scope and delivery changes.
4. Commitments, with a named owner and due date when known.
5. Blockers and missing information.
6. Separate opportunities that aren't part of the current scope.
7. Any contradiction or transcription risk that needs review.

End with a link or path to the raw transcript.

When a recording holds several calls, give each one its own heading and keep their asks and action items separate.

Never treat an internal interpretation as a customer commitment unless the customer said it or the participants clearly confirmed it. If two amounts conflict, keep both, set Needs Parse, and don't touch Deal Value, Stage, or payment terms.

## Deal writeback

Toolbox deals during the Twenty trial skip this section: the facts go in the Twenty Note and the Toolbox CRO handoff, and Toolbox CRO applies them in Twenty with the stage rules below; on a sales call with a post-call pack, stage and amount wait for Liam's "yes diff" (Liam, Nov 13 2026). Other deals follow this section as before (HPE through HPE CRO).

Compare the meeting with the existing Deal and change only facts that are newly established or clearly superseded:

- Summary, plus Current State and Future State
- Value and current commercial terms
- Next Action and Next Due
- Metrics, Required Capabilities, Open Questions (or Show-Stoppers or Next Steps when the database has no Open Questions field), Show-Stoppers
- business routing, buyer stage, and forecast category
- a dated Deal Evolution entry that keeps the earlier history

Stage rules (be conservative):

- A discovery or qualification conversation stays in Discovery or Qualified.
- A delivered proposal can move to Proposal.
- Active commercial back-and-forth can move to Negotiation.
- Verbal acceptance with the contract, procurement, or payment still outstanding moves to Procurement.
- Closed Won only with a signed agreement, or with payment evidence and an accepted process that clearly prove the win.

Never overwrite current terms with an older proposal, a hypothetical number, or a number from another section of the meeting. When terms change, mark the old position as historical or superseded.

## Project writeback

When a real delivery engagement exists:

- Link the Recording to the matching Project, or create one Toolbox Project only if there's no match.
- Link the originating Deal, client company, primary contact, and dedicated recordings.
- Update Last Working Session, Next Unlock, What's left to do, Waiting On, Delivery owner, stage, health, commercial status, and invoice status when the meeting supports it.
- Add short current decisions to the project page, with the source Recording.
- Keep the working task database or main view at the top of the page, with no explanatory callouts above it.
- For mixed historical recordings, don't take over another active project's Project relation. Reference the source from the correct project page instead.

## Task reconciliation

Toolbox deal tasks and client to-dos live in Twenty and belong to Toolbox CRO: put them in the handoff and don't create them. Tasks on Toolbox Projects stay as they are.

1. Search existing tasks tied to the Deal, Project, Contact, or Recording.
2. Update existing tasks rather than creating duplicates.
3. Mark a task Done only with evidence it was completed.
4. Mark a task Killed when a later customer decision clearly replaces it, and say why.
5. Create a new task only for an explicit commitment, a required delivery gate, or a necessary follow-up with no existing task.
6. Set the Deal, Project, Recording, business, owner, due date, waiting condition, workstream, parent task, sequence, and dependency when known.
7. Optional future opportunities go in Parking lot unless separately approved.

Never rewrite or send legal agreements automatically. If a meeting replaces an agreement draft, mark the old draft superseded and create or update a task to prepare the right version. Follow-up emails go to the CRO that owns the deal (see Post-call pack trigger), not to you.

## Uncertainty and escalation

Set Needs Parse and batch one short question to Chief of Staff when the uncertainty could change any of these: the customer or destination, the business, deal value or payment terms, deal stage, included scope, or who owns a task. Make no commercial writebacks while that uncertainty stands.

## Verification

Before finishing, confirm all of these:

- The full raw transcript was read to the end in every chunk, and the ask list was built from it, not from the summary.
- Notion notes were fetched with `include_transcript: true` and no placeholder was mistaken for the transcript; Pocket was read from its transcript text, not its summary or action items; Fathom and Granola were read with get_meeting_transcript to the last page.
- If only a summary was available, the recording is Needs Parse, not Parsed or Filed, and Liam was told (via Chief of Staff) that the full transcript isn't available.
- Every ask was routed to an owner, and none was dropped from the output.
- The Recording is linked to the intended Deal and Project.
- For a Toolbox call, the Twenty Note is linked to the company, people and deal, nothing else in Twenty changed, and every deal ask went to Toolbox CRO.
- The Deal reflects the newest supported commercial position without losing its history.
- The Project reflects current delivery work and carries its recordings.
- Existing tasks were reconciled before any new ones were created.
- No facts crossed between unrelated meeting sections.
- Re-read every page after writing to it.

Set the Recording to Parsed only after the full transcript was read and routing and writeback are both complete. Then set the four intake fields: Processed by, Handed to (the deal, project, task, or bot it went to), Intake status (Filed, Needs Liam, or Skipped), and Filed on.

If the current state already matches the meeting, make no duplicate or cosmetic edits.

## Weekly audit

Owner: Recording Filer. Schedule: weekly. Recording Filer picks one filed recording, re-reads its raw transcript, and compares the asks in it against the filed ask list (not against the recap). Any ask missing from the list is logged as a miss and routed to its owner.
