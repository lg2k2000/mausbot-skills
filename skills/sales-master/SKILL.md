---
name: sales-master
description: "Multi-lens deal review. Runs one deal or a whole pipeline through Gap Selling, Sandler, Selling With and JOLT, plus an elicitation pass that makes the questions speakable, and returns the questions to ask next and what's missing, merged into one ranked list. Use when Liam asks for a deal review, deal analysis, pipeline review, 'what are we missing', 'what should I ask next', or 'run it through all the frameworks'. Read-only overlay."
---

# Sales Master

## What this skill does

It takes one deal, or every open deal in a pipeline, and runs it through four sales methods. Each method lives in its own skill. This skill loads them, runs each one's Deal audit, then merges the results into one short list Liam can act on: the five questions to ask next, the three biggest gaps, and where the methods disagree.

| Lens | Skill | What it's best at |
| --- | --- | --- |
| Gap Selling (Keenan) | `gap-selling` | Is the problem real, measured and tied to a root cause? |
| Sandler (Mattson, Chiarello) | `sandler-selling` | Is the deal qualified (pain, budget, decision)? Do we have clear agreements? |
| Selling With (Nasralla) | `selling-with` | Do we have a champion, a map of the buying group, a mutual plan and a story they can carry inside? |
| JOLT (Dixon, McKenna) | `jolt` | Will the buyer actually decide, or stall in "no decision"? |
| Elicitation (Schafer, Karlins) | `elicitation` | Are we asking in a way that gets a truthful current state, without an interrogation feel? |

**Optional lenses** (load only when they fit; they don't add sections otherwise):

| Lens | Skill | Load when |
| --- | --- | --- |
| Influence (Cialdini) | `influence` | A champion or exec needs to be moved honestly (proof, authority, commitment), or the buyer may be working on us. Its ethics rules apply: no fake scarcity, no fake social proof, no pressure. |
| Fanatical Prospecting (Blount) | `fanatical-prospecting` | Pipeline mode shows thin coverage, or a deal is single-threaded and needs new contacts in the buying group. |

It is a read-only overlay. It reads records and transcripts and writes its output in chat or to a file Liam asks for. It never writes a CRM, a Notion database or a deal page.

- **HPE / VME:** any write Liam approves goes through HPE CRO.
- **Toolbox:** any write Liam approves goes through Toolbox CRO. Twenty is the system of record, and Toolbox CRO is its only writer.
- Never mix HPE, Toolbox and Desk Monkey sources in one review. HPE and Desk Monkey never go in Twenty.

## When it should trigger

- "deal review", "analyze my deals", "run it through all the frameworks", "multi-skill analysis"
- "what are we missing", "what should I ask next", "pipeline review"
- A deal name plus "Gap, Sandler, Selling With, JOLT", or any two of them
- A request for meeting-prep questions for a deal, or a check of how discovery was asked

For one method only, use that method's skill directly. For a neutral, forwardable status brief, use `deal-anatomy-brief` instead.

---

## Where the data comes from

Gather everything before running any lens. Read full transcripts, never summaries (process-meeting-recording).

**HPE / VME deals**

1. The deal page in the Notion HPE Hub's Enterprise Pipeline (VME Deals is a retired, read-only archive; don't read from it). Read every property and the page body.
2. Every linked recording page in Recordings, then the full transcript behind it: Fathom (get the transcript by recording id) or Pocket. Fathom speaker labels are often wrong. Attribute by context and say so.
3. The Shared Work Ledger row linked from the deal, if there is one.
4. Funding briefs or partner notes in the HPE Hub that name the deal.

**Toolbox deals**

1. The Twenty opportunity (connector `user-Twenty Toolbox`): stage, amount, Next Due, Follow-up #, Stopped reason, Deal source, point of contact.
2. Every Twenty note and task linked to the opportunity. Recording Filer adds call notes there.
3. The full transcript behind each call note: the Notion Recordings page (fetch with the transcript included) or the Pocket recording.
4. The email thread in Toolbox Gmail (toolbox or trytoolbox inbox). Check the Desk Monkey sent mail only to confirm what was sent.
5. Some Toolbox deals live only in Notion and were never copied to Twenty. Today those are Blue Ally, Maverin, p99, Ntier and Apivant recurring work. For those, read the Notion deal page.

If a source is missing or can't be read, say so in the snapshot. Don't fill the hole with a guess.

---

## Relation to deal-anatomy-brief

`deal-anatomy-brief` writes a neutral, forwardable brief with no framework names and no verdicts. This skill writes internal coaching that is full of framework names and verdicts. They serve different readers, so they stay separate.

- **Snapshot:** this skill calls `deal-anatomy-brief` for the snapshot section (Known, Unknown, Ask, Deal size, Timeline, Next step, org chart). That keeps one source of truth for the facts and saves a second read of the same records.
- **Don't merge them.** Merging would break the brief's rule against framework names and verdicts, and Liam forwards those briefs to partners and managers.
- If `deal-anatomy-brief` is not installed or not loaded, build the snapshot here using its headers and rules.

---

## Process

1. **Gather.** Pull every source above for the deal. Note anything missing.
2. **Snapshot.** Load `deal-anatomy-brief` and produce its brief for the deal. Keep it under half a page.
3. **Run each lens.** Load each skill and run its Deal audit (Audit) mode on the same facts:
   - `gap-selling`: Mode B Audit
   - `sandler-selling`: Mode C Deal audit
   - `selling-with`: Champion Scorecard (Worksheet 3) and Buyer Committee Map (Worksheet 2), plus a MAP check (Worksheet 7)
   - `jolt`: Mode B Deal audit
   - If a transcript exists: `elicitation` Mode B Audit (short form: moves used, moves missed, any leak)
   - Optional lenses only when their "Load when" fits: `influence` Audit, `fanatical-prospecting` Audit
   From each lens, keep only 3-5 questions to ask next and 3-5 lines on what's missing.
4. **Merge, then make it speakable.** Combine the four lists. Remove duplicates: two questions that would get the same answer are one question. Rank by what moves the deal most, then pick the top 5 questions and the top 3 gaps. Then load `elicitation` Mode A and rewrite the merged top 5 so Liam can say them: mix statement forms (presumptive, bracketing, third-party, empathetic) with questions, no barrage, no trap. Keep each question's meaning and lens tags.
5. **Conflicts.** Where the lenses give different advice, say which one wins for this deal and why. Use the rules below.
6. **Check.** Every fact has a source. Every guess is labeled. Run the writing-mega-skill grade check at grade 8.

### Pipeline mode

For a whole pipeline, do steps 1-5 per deal, but cut each lens to its top 2 questions and top 2 gaps. Then add a one-page summary at the top:

- deals ranked by readiness (qualified and deciding, qualified but stalling, not yet qualified, walk)
- the one question per deal that matters most this week
- deals that every lens flags (these need Liam first)

---

## Conflict rules

Use these when two lenses disagree. Say which rule you used.

- **Trials.** Keep Selling With's hardwired POC (narrow scope, short time, one hypothesis, agreed measures, agreed next step). Add Sandler's removal date as the deadline: the buyer agrees up front that the trial is removed on a set date unless they sign (Chiarello's paid-trial example).
- **Who runs the process.** We run the process terms: up-front contracts, the mutual plan and two-way commitments. The champion runs the internal story.
- **When to walk.** Walk now on a hard showstopper: a must-have we can't meet, a corporate overrule, or a refusal to build a mutual plan. When the pain is real but small, dig more before walking.
- **Mutual plan vs. narrative order.** Selling With wants the business case first and the plan second. Sandler builds the plan early as a qualifying test. Default: build a short plan early (owners and dates for the next two or three steps) to test commitment, then build the full plan after the business case is agreed. Say which one you used.
- **Likeability.** Rapport gets the buyer talking. Credibility wins the deal. Don't trade one for the other.
- **Budget.** The methods only differ in words. Budget means the buyer is willing and able to move money, people and time.
- **More information.** Gap Selling and Selling With push for deeper discovery. JOLT warns that too many questions raise indecision. Default: dig deep before the proposal, and limit new questions after it.
- **Talk time.** Sandler aims for the buyer to talk 70-80%. JOLT's data shows winning reps talk more (58% in wins vs. 52% in losses). Default: listen hard in discovery; once the buyer is choosing, engage, recommend and steer.
- **RFPs.** Sandler and Gap Selling agree: an RFP that blocks discovery is not a sale. Default: don't commit time unless we helped shape it or can get a discovery conversation first.
- **Pressure.** Sandler and Gap Selling use the cost of staying put. JOLT says fear tactics backfire on an indecisive buyer. Default: use the cost of staying put to build the case, but never as a deadline threat.

---

## Output format (per deal)

Use these headers in this order.

```
# [Deal name]: multi-lens review ([date])

Sources read: [list, with dates]. Missing: [list].

## Snapshot
[deal-anatomy-brief output]

## Gap Selling
Questions to ask next:
1. ...
What's missing:
- ...

## Sandler
Questions to ask next:
What's missing:

## Selling With
Questions to ask next:
What's missing:

## JOLT
Questions to ask next:
What's missing:

## Elicitation (only if a transcript was read)
Moves used / moves missed / leaks:

## [Optional lens] (only if loaded)
Questions to ask next:
What's missing:

## Top 5 questions (merged)
1. [question, rewritten to be speakable] (lenses: Gap, Sandler)
...

## Top 3 gaps (merged)
1. [gap]: [why it matters, one line]
...

## Where the lenses disagree
- [conflict]: [which lens wins here, and why]

## Next step
[One action, with an owner and a date.]
```

## Output rules

- Every question is written so Liam can say it out loud, in his voice.
- Every fact is sourced. Mark "customer said", "internal view" or "estimate (whose)".
- Never invent names, numbers, dates or titles. Write "Unknown" and name who would know.
- No sends, no CRM writes, no Notion edits. If Liam wants a field updated, write a handoff for HPE CRO or Toolbox CRO with the exact change.
- All prose follows writing-mega-skill: grade 8, no dashes as punctuation, straight quotes, banned words removed.
