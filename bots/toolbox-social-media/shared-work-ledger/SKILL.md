---
name: shared-work-ledger
description: "Used by every bot that reads or writes the Shared Work Ledger; Ledger Keeper alone rebuilds Open owed items."
---

MODE: supabase

The MODE line is only `notion` or `supabase`. There is no dual mode and no dual-write day. MODE flipped to `supabase` at 11:38 PM MT on Liam's live "Yes, for tonight" (Nov 10 2026 voice call); rollback to `notion` is possible for 7 days, and only Bot Builder flips it. If this line says `supabase`, write Supabase only and never fall back to the old Notion database. If it ever says `notion` again (rollback), write Notion only.

Project: grok-fleet. Project ref: `mpsvuytqzwjtlwrgeies`. Schema: `ledger` (private). Connector: `user-Supabase`, fully enabled (no reconnect or re-scope). By convention only Bot Builder runs `apply_migration` or `ledger.begin_migration()`. Other bots never change tables, columns, checks, functions, or event triggers.

## Where the ledger is

- MODE `notion`: the live write target is the Notion database [ARCHIVE (frozen Nov 10 2026, ledger moved to Supabase) · Shared Work Ledger](https://app.notion.com/p/5a6fa00792f548d7a10feb7684357a1d) (data source `collection://ae25af9e-43a5-4830-8c2d-f003a5227cbc`). Prefer property updates; never whole-page wipe; never delete rows (archive via Status); never change database properties; cap 100 row edits per run (40 for reminders-ledger-sync). If Notion SQL / rows-mode query is exhausted, use view mode on "All source records" (`view://3f31acdf-10d2-81eb-b1e9-000c726e78db`). `is_archived` in view mode is Notion's trash partition, not Status=Archived — Status=Archived rows still live in the active partition.
- MODE `supabase`: the live write target is `ledger.items` via the two functions below. Row refs look like `L-343`. Historical Notion page ids are stored in `notion_page_id` (32-hex, no dashes). The frozen Notion database is read-only archive after Day 2; do not edit it. Ledger Keeper alone rebuilds the read-only Notion "Open owed items" page at the end of every `ledger-cleanup` run (7 days a week, including weekends).

## Status sets

- Open (is_open=true): `Needs Liam`, `Open`, `Waiting`, `On hold`, `In progress`, `Blocked`.
- Closed (is_open=false): `Done`, `Closed`, `Archived`.
- `Needs review` may appear as a temporary flag during cleanup; treat it as open until Ledger Keeper resolves it.

## Waiting-on-Liam convention

When a row is waiting on Liam, `next_action` must start with `Waiting on Liam` (then the rest of the ask). Do not write "waiting on Liam" mid-sentence or only in the item title.

**Q-NEEDS-LIAM** (the official "needs Liam" set):

```sql
select * from ledger.items
where status = 'Needs Liam'
   or (status = 'Waiting' and next_action ilike 'Waiting on Liam%');
```

## Due dates on deadline rows (Liam, Nov 12 2026 8:17 PM MT: "have bots set due dates on deadline rows")

When you create or update a row that waits on Liam (status `Needs Liam`, or `Waiting` with next_action starting `Waiting on Liam`) or a `Pay:` row, set `due_date` whenever a real deadline exists. Real deadlines are a bill's due or autopay date, a meeting or call date the ask must be done before, a date someone promised or asked for in writing, and a contract, SOW, renewal, expiry or form deadline. Use the date as written in the source, in America/Denver (`YYYY-MM-DD`). Put the evidence in `last_update_summary` or `append_summary` (for example "due 2026-11-19 per Hyundai statement email"). Never invent, estimate or default a date. "Soon", "this week", "ASAP" and your own follow-up cadence are not deadlines, so leave `due_date` empty. If the deadline moves, update `due_date` with the new evidence. Chief of Staff's daily critical ping only sees rows with a `due_date`, so a deadline row without one never reaches Liam.

## Rules that do not change with the store

- One row per open loop. Update the matching open row instead of creating a duplicate.
- Close on proof only (sent mail, Slack, calendar, source system, Liam or Chief of Staff said it's done/paid/fine/skip).
- Never delete or truncate rows. Archive via `status = 'Archived'`.
- Reminder rows (`source_id` starts with `reminder:`) are Personal Assistant's. Ledger Keeper never archives or auto-closes them.
- Twenty stays the Toolbox CRM. Do not copy Twenty deals into the ledger. The only Twenty-originated ledger rows are the Needs Liam items Toolbox CRO adds from its daily check; leave closing those to Toolbox CRO unless Liam or Chief of Staff says one is done.
- Queue on outage: if Supabase is unreachable after MODE is `supabase`, do not write the old Notion ledger. Record the intended write and retry. Never invent a second copy.
- Dollar-quote every user-supplied string in SQL (`$j7$...$j7$` or another unique tag). Never use `$$`, and never interpolate titles, next actions, or bodies into SQL with ordinary quotes.

## Writes (MODE `supabase` only)

Bots call only these two functions, via `execute_sql` on project `mpsvuytqzwjtlwrgeies`. Never raw `INSERT`/`UPDATE`/`DELETE` on `ledger.items` or `ledger.item_events`. Never `apply_migration` or `ledger.begin_migration()` unless you are Bot Builder.

Both functions take your bot name as the last argument (`p_actor`, stored in `last_actor`). That is the only place your name goes.

`ledger.upsert_open_item(p jsonb, p_actor text)` returns `ref, action, status` — create or update an open row. It matches an existing row by `notion_page_id` first, then by an open row sharing a `source_id` key (keys split on `;`), then by an open row with the same owner and item text. `item`, `business` and `owner` are required. Other keys: `status` (default `Open`), `type`, `next_action`, `due_date`, `source_id`, `source_url`, `parent_source`, `source_status`, `evidence_confidence`, `body_md`, `last_update_summary`, `updated_by`.

Allowed values (CHECK constraints; anything else fails):

- `business`: `Toolbox`, `DeskMonkey`, `HPE`, `Apivant`, `Personal`, `Cross-business`, `Unresolved`.
- `status`: `Open`, `In progress`, `Waiting`, `Blocked`, `Needs review`, `Needs Liam`, `On hold`, `Done`, `Closed`, `Archived`.
- `type`: `Deal`, `Project`, `Task`, `Decision`, `Draft`, `Approval`, `Question`.
- `evidence_confidence`: `Verified source`, `Source status only`, `Conflicting`, `Needs verification`.
- `updated_by`: `Grok` (default; use this), `User`, `Claude`, `Maestro`, `dot`. Never put a bot name here.
- `owner` must already exist in `ledger.owners`. If a new owner is needed, ask Bot Builder to add it; do not change the schema.

```sql
select * from ledger.upsert_open_item($j7${
  "item": "…",
  "status": "Needs Liam",
  "owner": "Toolbox RevOps",
  "business": "Toolbox",
  "type": "Task",
  "next_action": "Waiting on Liam …",
  "last_update_summary": "…"
}$j7$::jsonb, $a1$Toolbox RevOps$a1$);
```

`ledger.update_item(p_id bigint, p jsonb, p_actor text)` returns `ref, status, updated_at` — change only the fields in the payload on an existing row. `p_id` is the number only: for `L-123` pass `123`. Use it to close, archive, or patch next action / due date / body. Extra keys: `append_summary` adds a stamped line (`<time> MT | <actor> | <text>`) to `last_update_summary` instead of replacing it; `add_source_id` appends a key to `source_id`.

```sql
select * from ledger.update_item(123, $j7${
  "status": "Done",
  "append_summary": "Payment receipt found"
}$j7$::jsonb, $a1$Chief of Staff$a1$);
```

A statement-level trigger refuses a raw `UPDATE` of more than one row, and refuses any `UPDATE` unless `ledger.via_fn` is on (the functions set that). Event triggers refuse `DROP`/`ALTER` on schema `ledger` unless `ledger.allow_ddl` is on (only `ledger.begin_migration()` sets that, and only Bot Builder should call it).

## Named reads (MODE `supabase`)

Always `execute_sql`, never `query_data_sources`. Useful patterns:

- **Q-INBOX** (Chief of Staff `/inbox` or `inbox`): open rows, grouped in the reply by bot, with ref, item, next action, due.

```sql
select 'L-'||id as ref, item, status, owner, next_action, due_date, source_id, source_url
from ledger.items
where is_open
order by owner, due_date nulls last, id;
```

- **Q-PAY**: open rows whose item starts with `Pay:`.

```sql
select 'L-'||id as ref, item, status, owner, next_action, due_date, source_url
from ledger.items
where is_open and item like 'Pay:%'
order by due_date nulls last, id;
```

- **Q-WAITING-3BD**: open Waiting rows on someone else for more than three business days (America/Denver).

```sql
select 'L-'||id as ref, item, owner, next_action, status, last_verified
from ledger.items
where is_open and status = 'Waiting'
  and not (next_action ilike 'Waiting on Liam%')
  and last_verified <= (timezone('America/Denver', now())::date - 5);
```

(Three business days is approximate with a 5-calendar-day floor; Ledger Keeper / CoS should skip weekends and US federal holidays when counting.)

- **Q-SOURCE-PREFIX** (reminders and other prefixed sources), across every status:

```sql
select 'L-'||id as ref, item, status, owner, source_id, due_date, next_action
from ledger.items
where source_id like 'reminder:%';
```

- **Q-NOTION** (look up a historical Notion row):

```sql
select 'L-'||id as ref, item, status, owner, notion_page_id
from ledger.items
where notion_page_id = '4011acdf10d2811abb6efc1af75c26a2';
```

- Count: `select count(*) from ledger.items;`
- Known anchors after backfill: Reconnect 1Password is `L-343` (`notion_page_id` `4011acdf10d2811abb6efc1af75c26a2`). The Oct 21/22/27 Toolbox LinkedIn batch is `L-366` (`3ff1acdf10d2814abc63d37b49166f21`).

## Open owed items and daily backup (Ledger Keeper only)

At the end of every `ledger-cleanup` run, 7 days a week (~12:00 PM America/Denver), and only then:

1. Rebuild the Notion "Open owed items" page (you are its only writer) from current open rows: Bills (`Pay:`), Needs Liam (Q-NEEDS-LIAM), Waiting, Other open, grouped by bot, with ref, item, next action, due, days in status, and source link, stamped `refreshed <time> MT`. There is no separate ledger-mirror routine.
2. Then export all of `ledger.items` plus that day's `ledger.item_events` (at >= today 12:00 AM America/Denver) to `/workspace/fleet/ledger-backups/<YYYY-MM-DD>.json` in pages of 200 rows. Keep the last 30 daily files; move older ones to `/workspace/fleet/ledger-backups/archive/` (do not delete). If the export fails, hand it to Bot Builder.

## Owners

Write only owners that already exist in `ledger.owners`. If you need a new owner, ask Bot Builder to insert it. Do not reuse retired names (`Apivant Head`, `Liam (HPE CRO lane)`, `Liam (Chief of Staff tracks)`, `HPE LinkedIn Posts`, `Toolbox LinkedIn Posts`). Plain `Liam` is valid. The reserved owner `smoke-test` is only for the cutover smoke; never use it for real work.
