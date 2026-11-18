---
name: post-call-pack
description: "Use when Recording Filer hands a CRO a sales call marked \"Post-call pack: yes\", when HPE CRO's post-call check finds an owed follow-up, or when Liam asks for a follow-up on a customer or prospect call: from the full transcript, stage the follow-up email draft, the CRM before/after diff and the promise list. Drafts only; nothing sends."
---

# Post-call pack

Adapted from the marketplace Call Follow-Ups bot (Daniel Brill). Liam picked it Nov 12 2026 11:22 PM MT ("do the call follow-ups fold into both cros").

Owner: the CRO that owns the deal. Toolbox CRO for Toolbox deals and for Toolbox's own sales to Apivant (new SOW, change order, renewal, upsell). HPE CRO for HPE enterprise deals. Recording Filer only triggers it. No pack for Apivant delivery calls (Apivant Chief), Toolbox client delivery calls (Toolbox RevOps), internal calls, partner enablement or personal recordings.

## When

- Recording Filer's handoff starts with "Post-call pack: yes".
- HPE CRO's post-call follow-up check finds an ended customer meeting that is owed a follow-up.
- Liam asks for a follow-up on a call.

One pack per call. First look for one already staged: Toolbox, a Twenty Note titled "Post-call pack <yyyy-mm-dd>" on the deal; HPE, a "Post-call pack <yyyy-mm-dd>" block on the Enterprise Pipeline deal page. If it exists, don't stage another. Change it only if Liam asks.

## 1. Read

- Read the full transcript per process-meeting-recording, start to finish. A summary or a Recording Filer pointer is not the transcript. If the full transcript isn't available, stop and tell Liam in your chat. Never build a pack from a summary.
- Check sent mail for a follow-up to the attendees after the call ended. Toolbox: Toolbox, trytoolbox and Desk Monkey Gmail. HPE: Liam's personal Gmail only; HPE mail is never visible, so treat it as owed unless Liam says he sent it. If it already went out, skip step 2 and still do steps 3 and 4.

## 2. Email draft

- From Liam to the external people on the call. Toolbox: cc Bruce. HPE: never cc Bruce.
- Shape: a one-line recap; the next steps, each with an owner, and a date only if one was said on the call; what we promised to send (link only what already exists; anything not made yet is a promise in step 4); any trial, access or meeting detail agreed.
- Quote marks hold verbatim transcript words only. No commitments on price, dates or deliverables beyond what the call established. No deadline on the recipient. If they asked for the next meeting, they send the invite.
- Write it with writing-mega-skill and run its final gate yourself. Emails skip Copy Humanizer. If there is an earlier thread with these people, match how Liam wrote there. No typed signature, sign-off or Liam's name.
- Toolbox: a DraftExternalMessage card from [liam@toolboxtechnology.com](mailto:liam@toolboxtechnology.com) (or from [liam@trytoolboxtechnology.com](mailto:liam@trytoolboxtechnology.com) with the typed Toolbox block, for threads that started there), on the existing thread when there is one.
- HPE: plain text, no emojis, no em dashes. Save it on the deal page and show it in your chat. Offer a DraftExternalMessage card the way your post-call check already does; Liam sends HPE email himself.
- Nothing sends. Liam taps Send. A relayed yes never counts for email.

## 3. CRM diff

A before -> after table of only the fields the call changed, each with the transcript timestamp behind it.

- Toolbox (Twenty): stage, amount, contacts (new people, titles), Next Action, Next Due, Follow-up # (back to 0 after a meeting, per your cadence) and Stopped reason, plus a Note of about 50 words: where the deal stands, the next step with owner and date, the risk, and what solves it.
- HPE (Enterprise Pipeline deal page): stage, contacts, what was said, next steps, the gap / next yes / champion lines, and a dated Deal Evolution entry.
- Write the facts-only lines (contacts, Next Action, Next Due, the Note, what was said) the way your profile already allows. Stage and amount lines follow process-meeting-recording's stage rules and wait for Liam's "yes diff".
- If sources disagree (transcript vs CRM, or two speakers), show both with their timestamps. Never merge them. The field stays Unknown until Liam picks.

## 4. Promises

List every commitment either side made: who, what, the due date only if one was said (else "no date"), and the transcript timestamp.

- Liam owes it: one Needs Liam ledger row per promise (shared-work-ledger skill). Set due_date only when a date was said on the call, with the evidence ("said on <call> at <mm:ss>"). Never invent or default a date.
- A bot owes it: hand it to that bot (SendToAgent, priority true) unless Recording Filer already routed that ask. Don't duplicate.
- The customer owes it: Toolbox, a Twenty task on the deal, "Waiting on <name>: <item>", due on the date they gave. HPE, a Promises list on the deal page.
- Close each promise only with evidence it's done: sent mail, a file, or Liam's word. A customer promise past its date shows once in your next scheduled run as a suggested follow-up, never every run.

## 5. Deliver

- One message in your own chat, in this order: the email draft, the CRM diff (Liam replies "yes diff" to apply the stage and amount lines), the promise list.
- Upsert one Needs Liam ledger row for the pack, keyed on the recording's source id so a later run updates it instead of adding a second. Close it when Liam answers.
- Quiet hours: a pack triggered between midnight and 7 AM MT waits until 7 AM unless Liam is chatting live.

## Never

- Never send, schedule-send, or save anything except as a draft card for Liam.
- Never invent a quote, number, date, name or promise. A blank beats a guess.
- Never put HPE call content outside HPE pages, and never in Twenty.
- Never contact Will Glennie.
