---
name: instantly-expert
description: "Use before any Instantly.ai work: campaigns, sequences, variables, lead uploads, warmup, deliverability, inbox placement, AI features, API calls or plan limits. Points to the local docs corpus and the key facts."
---

# Instantly expert

A full crawl of Instantly's docs (Nov 11 2026) lives on the shared computer:

- Distilled guide (read first): `/workspace/instantly-docs/INSTANTLY_EXPERT.md`
- Help articles: `/workspace/instantly-docs/help/articles/` (index: `maps/HELP_INDEX.md`)
- API v2 docs: `/workspace/instantly-docs/developer/` plus `openapi/api_v2.json` and `llms-full.txt`
- Pricing: `/workspace/instantly-docs/pricing/pricing.md`

Before any decision, read the matching section of the guide. If the guide says "not documented", grep the corpus with `rg`, then re-check the live help article. Never invent UI labels, limits or syntax.

## Key facts

- Variables: `{{name}}`, case-sensitive. Fallback is `{{firstName | there}}`. Spintax is `{{RANDOM | a | b}}`, not `{a|b}`.
- Custom variables: in a CSV, map the column as Custom variable (header max 20 chars, max 50 vars). In the API, `custom_variables` on `POST /api/v2/leads` or bulk `POST /api/v2/leads/add` (up to 1,000). Values must be string, number, boolean or null.
- Threading: leave follow-up subjects empty or identical and keep the same sender. Stop-on-reply is a campaign setting. A/Z testing allows up to 26 variants per step.
- API sequences: only the first `sequences` item is used. Steps are `type: email`, and bodies are HTML with `<br/>`.
- Timezone: the API enum has no `America/Denver`. Use `America/Boise` for Mountain Time.
- Deliverability: plain text and open tracking off on email 1. Keep bounces under 2%. Auto-pause defaults to 5% bounces after 200 sends.
- Per-inbox caps: 30/day recommended for normal inboxes, 20/day max for Airmail. Even a pre-warmed inbox should start at about 5/day and ramp up.
- AI: only AI Prompts & Enrichment takes your own LLM key (Anthropic, OpenAI and others). Copilot, Sequence Writer and Spintax Writer have no documented own-key option. The AI Reply Agent costs 5 Instantly credits per generated reply. A cheap alternative is to write per-lead lines outside Instantly with your own LLM and upload them as a custom variable.
- Auth: Bearer API key from Settings > Integrations > API Keys. Test it read-only with `GET /api/v2/accounts`.

## Safety

Read live state before changing anything. Never pause, edit or delete someone else's campaign, warmup or placement test without the owner's yes. Load campaigns paused and start nothing without approval.
