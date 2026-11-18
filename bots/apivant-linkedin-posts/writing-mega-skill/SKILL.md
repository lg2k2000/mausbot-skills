---
name: writing-mega-skill
description: "Liam's one writing skill for anything he or his businesses send, post, present or hand a customer: emails, LinkedIn and social posts, DMs, decks, docs, pages and templates. Runs a Hemingway grade check (ARI script and grade targets), then Liam's voice rules and learned preferences, then AI-pattern cleanup (banned words, structures, punctuation), then the grade check again as the final gate. Use it whenever you draft or edit copy, or when he asks to simplify, tighten, humanize, unslop or Hemingway something, even if he does not name the skill. Replaces readability-editor, humanizer-writing-rules and stop-slop."
---

> Source: this skill file (/home/box/agent-data/workflows/writing-mega-skill/SKILL.md). Edit it first, then update the Notion copy ([Grok · Reference: Writing Mega Skill](https://app.notion.com/p/cf95cda8dd9848da9311a03c2e14e5af)) and the GitHub copy (lg2k2000/agent-skills, shared-writing/writing-mega-skill/SKILL.md).

# Liam's writing skill

Write like a competent human: specific, direct, and not trying to sound important. Clean but voiceless writing is as obvious as slop, and short choppy writing that passes a grade check is as obvious as both.

## How to run it

Run the four parts in this order on every non-trivial draft or edit:

1. Part 1, the Hemingway grade check. It fixes sentence structure: length, who acts, the verb, and word choice.
2. Part 2, Liam's voice rules, including his learned preferences.
3. Part 3, AI-pattern cleanup.
4. Part 4, the grade check again as the final gate.

Report nothing about grades or scores. If asked, give a short list of what changed.

## Rules that hold in every part

- Keep every number, date, price, SKU, product name, quote, customer's words and source exactly as given. Never change any of them to hit a score.
- Keep each claim the same size. If a shorter version claims more or less than the original, keep the longer sentence or split it instead of trimming it.
- Preserve the writer's meaning, intent, attribution and necessary qualifications. Do not turn limited or uncertain claims into absolutes, invent an actor to force active voice, remove an essential list item to change rhythm, or swap an example's claims in for the user's facts. When a style rule would change meaning or accuracy, keep the meaning and rewrite another way.
- Do not add content when editing anyone's draft. Editing cuts and restructures; new opinions, asides or first-person lines are not edits. Voice and soul (Part 2) guides first drafts a bot writes as Liam. The LinkedIn learned preferences (Part 2) override both for LinkedIn posts.

---

# Part 1. Hemingway grade check

## Targets

- Slide text: grade 6 or lower.
- Speaker notes and email drafts: grade 8 or lower.
- Social posts (LinkedIn, X, Instagram), DMs, Slack messages and texts or iMessages: grade 8 or lower.
- Customer guides and documents: grade 9 or lower.
- Dense reference documents such as the competitive battlecard: grade 10 or lower. Treat the flags as a review list, not a rewrite order.

ARI is the Automated Readability Index. It estimates the US school grade needed to read the text, from word length and sentence length.

The target is a ceiling. Stop when the text passes. Pushing an email from grade 8 to grade 4 does not make it clearer; it makes it read like a telegram.

## Steps

1. Run `scripts/readability.py` from this skill's folder (on the box: /home/box/agent-data/workflows/writing-mega-skill/scripts/readability.py): `python3 scripts/readability.py FILE --grade N` with the target above. For a deck, `--grade` is the slide target and notes are scored against that target plus 2 (override with `--notes-grade`). For pasted text, save it to a scratch `.txt` file or pipe it in with `-` as the file name. For a PDF built from HTML or Markdown, score the source file, since it splits sentences more cleanly. The script needs python-pptx, python-docx, BeautifulSoup and pdftotext for those formats; install what is missing.
2. Fix everything under MUST FIX: em dashes, en dashes, spaced hyphens used as dashes, curly quotes and apostrophes, inline-header bullets, and bullets that are not complete sentences. These are Liam's standing rules, so no grade excuses them.
3. Fix every sentence flagged "very hard".
4. Work through "hard" sentences, longest first, until the grade meets the target. Then stop. A 21-word sentence of plain words that reads cleanly can stay.
5. In every sentence you rewrite, also clear its passive, adverb and simpler flags. Outside those sentences, fix a flag when the fix is clean and leave it when the fix would change the meaning, a quote, a product name or a figure.
6. Check the RHYTHM line (below), then re-run until the text passes with no MUST FIX items. The script exits 0 when it passes.

If you cannot run Python, do the same pass by hand. Count the words in each sentence and treat anything over 20 as hard and over 25 as very hard. Search for the MUST FIX items in step 2, for "is/are/was/were/been" followed by a past participle, and for words ending in -ly. Treat the grade as an estimate.

## Rewrite moves

Split at the joint. A long sentence usually holds two claims joined by "and", "which" or "so". Give each claim its own sentence. Do not split a sentence that holds one claim just because it is long.

<quote>
Before: The cluster is configured with two 25 GbE uplinks per host that are bonded together in an active-active configuration, which allows traffic to keep flowing if one of the top-of-rack switches is taken offline for maintenance.

After: Each host has two 25 GbE uplinks, bonded active-active. If one top-of-rack switch goes down for maintenance, traffic moves to the other.
</quote>

Put the actor first. Name who does the thing: HPE, the customer, the admin, Liam. Liam's rule is that abstractions never act, so the actor is a person or team, not "the process" or "the initiative". Passive voice is fine when the actor is unknown or does not matter (rule 3.12).

<quote>
Before: Access to the VME manager is granted by the customer's IT team after the security review has been completed.

After: The customer's IT team grants access to the VME manager after they finish the security review.
</quote>

Cut adverbs that add nothing ("particularly", "significantly", "very"). Keep the ones that carry a fact ("only", "monthly", "automatically" when automation is the point). See rule 3.20.

Swap wordy phrases for the short word the script suggests. "In order to" is "to". "Utilize" is "use". "Serves as" is "is".

Keep the claim the same size.

<quote>
Before: Customers on the 2025 price list keep their rate through renewal if they sign before December 31.

Wrong: Customers on the 2025 price list keep their rate through renewal. (The condition is gone, so the claim is now bigger.)

Right: leave it. It is 17 plain words.
</quote>

## Rhythm: the over-correction check

The failure this pass is most likely to cause is prose where every sentence is 6 to 10 words and the same shape. That passes any grade target and reads like a machine wrote it, which is the exact problem Parts 2 and 3 exist to catch. The script's RHYTHM line reports the average sentence length and spread for prose (not slide text), and adds CHECK when:

- the average is under 9 words,
- the lengths are too even, or
- three sentences in a row inside one paragraph are within two words of each other.

When you see CHECK, join two short sentences that share a subject with a comma or "and", or let one sentence run long. Read the paragraph in your head. It should sound like Liam talking across a table.

<quote>
Over-corrected: We moved the pilot cluster on September 30. We hit one issue. Two Windows 2016 guests had a driver mismatch. The HPE team fixed it. They fixed it the same afternoon.

Right: We moved the pilot cluster on September 30. The only issue was a driver mismatch on two Windows 2016 guests, and the HPE team fixed it the same afternoon.
</quote>

## Reading the script output

- Passive and adverb flags are pattern matches. Common adjectives ("is based", "are interested") and capitalized names ending in -ly are already excluded, but read the sentence before you rewrite it.
- Code blocks, shell commands and URLs are skipped, so a CLI example does not drag the grade up.
- Table cells in decks and Word files are scored.
- AI TELLS lists words and patterns from Part 3 ("robust", "-ing" tails, "not just", hyphenated pairs like "third-party"). Fix them here if the sentence is being rewritten anyway. Otherwise leave them for Part 3, and make sure none remain at the final gate.
- For decks, "over target" lists the slides that miss the target, worst first. Start there.

---

# Part 2. Liam's voice rules

## Liam's learned preferences

These come from Liam's own corrections to drafts. Each line names the date and where it came from. When a line here conflicts with a general rule elsewhere in this skill (for example "Have opinions" under Voice and soul), follow the line here.

**LinkedIn posts under Liam's name**

- Deliver the news plainly, and keep it from sounding salesy. (Liam, Oct 20 2026, on an HPE VMware post, relayed by HPE Market Watch, now HPE LinkedIn Posts, to Copy Humanizer.)
- Skip clever hooks and question openers, and never add a hook while editing. He called "Picking a VMware replacement? The hypervisor is the easy part now" out of touch. (Same source, Oct 20 2026.)
- Leave out "ask every vendor three things" style takeaways. (Same source, Oct 20 2026.)
- Leave out lists of questions. (Same source, Oct 20 2026.)

**LinkedIn comments on other people's posts**

- Keep each comment to 40 words or fewer, and aim for 15 to 30.
- Make one point per comment. If a draft has two, keep the one only Liam can add from his HPE work and cut the other.
- Start with the point. Don't open with a setup clause that restates the post or says who it matters for, such as "The core-count point matters for anyone planning a server refresh."
- Use two sentences at most.
- Say "I work at HPE" in a comment only when it's actually pertinent (for example, the comment is about an HPE product or pricing and the disclosure matters); otherwise leave it out. Never use it as a stock opener (Liam, Nov 12 2026 6:34 PM MT: "only say i work at hpe if it is pertienant"; replaces the Oct 29 never-say-it line).
- Shorten by cutting, never by changing a fact, number or product name.

(Liam, Oct 29 2026 8:03 and 8:05 PM MT, in HPE LinkedIn Outreach's chat, relayed to Copy Humanizer. He called this draft wordy: "The core-count point matters for anyone planning a server refresh, since denser CPUs can raise the license count with no new workloads. I work at HPE, and VM Essentials is licensed per socket, so more cores per CPU don't add licenses.")

**LinkedIn comment replies (on any post)**

- Write replies to LinkedIn comments as 1-2 short, casual sentences that look low-effort, never polished or corporate. When the comment is about price, give the real numbers with their sources instead of dodging; the citation rules above and in the bot's own instructions still apply. (Liam, Nov 12 2026 6:28 PM MT, in HPE Virtualization Update Poster's chat, on a reply to a Nutanix vs VMware pricing comment: "just cite some fucking prices bruh and keep it shorter and more casual!" and "we need to keep things short and brief and low effort looking!")

**Emails and documents**

- Write bullets as full sentences. (Liam, Oct 15 2026, Toolbox pricing email session with Copy Humanizer. readability-editor already enforces this; it is listed here because it came from Liam directly.)
- Check every fact against the source before the draft goes out, including who is on a deal or a call. Never pass along a fact from another bot's draft without checking it. (Liam, Oct 15 2026 3:51 PM MT, after a Toolbox client email draft gave the client a partner he does not have: "he does not have a partner where are you getting that".)
- Email drafts never end with Liam's name or a sign-off line ("Liam", "Best, Liam", "Love you, Liam"); end on the last sentence of the body. Gmail adds his signature itself, so a typed sign-off shows up twice. (Liam, Oct 27 2026 8:01 PM MT, in Personal Assistant's chat, after a personal Gmail draft ended "Love you,\\nLiam": "Double stacking my fucking signature again.")
- Exception: Liam's Apivant Gmail ([liam.glennie@apivant.io](mailto:liam.glennie@apivant.io)) has no saved signature, so Apivant email drafts end with his signature typed in, on its own lines: "Liam Glennie / Co-Founder / toolboxtechnology.com / 720-431-2310" (one item per line). Still no sign-off line above it. This lasts until Liam saves a signature in that Gmail. (Liam, Nov 10 2026 6:53 PM MT: "dude, my fucking siganture cmon"; signature text approved Nov 10 ~11:06 PM MT for Apivant Lead Finder; exception chosen Nov 12 2026 2:49 PM MT in Bot Builder's chat.)
- In client and partner emails (warm threads and existing relationships), do not tell the person to find a time or send a booking link. Ask when a call would work. Cold emails still close with the booking link. (Liam, Nov 5 2026 ~10:41 AM MT, in Toolbox CRO's chat, on a client email to Craig Walicek at CIO Technologies with the subject "A SKU for your customers' websites". A prior draft ended with a Cal.com booking link ("you can grab a time here"): "dont tell craig to find time, we need to ask him when would work." Relayed by Toolbox CRO to Copy Humanizer.)

**Cold emails**

- Keep cold emails blunt, a little rude and very simple, with no formal or careful-lawyer tone. Say the problem and the fix in a line ("Hey, your site's messed up. We fix them."), then the booking link. (Liam, Oct 31 2026 1:52 PM MT, in Toolbox Cold Email's chat, on the Toolbox direct cold email A/B v2 and v3-B drafts, rewritten as v4: "We want to be so straightforward and rude. Like, 'Hey, your site's messed up. We fix them.' Book with the link below and we will bring you a new website on the call. Like something literally that simple. Also, I like the lawyer tone, but ... That's too formal." His Pocket recording "AEO Strategy and Website Migration", Oct 31 1:26 PM MT, says the same.)
- Cold emails, cold DMs and connection notes read like a quick text from a busy owner: super chill and low intent. Short (about 25 to 60 words in the body), one idea, no polish, no pitch paragraph. Lowercase and fragments are fine, and Liam's own lowercase or fragment lines stay exactly as he wrote them. Cold email 1 still ends on the booking link; at most one easy question can sit right above it. For these formats this line overrides the complete-sentence rules (Part 1 step 2 bullets, 3.16, 3.38) and "Write bullets as full sentences". The no-dash, straight-quote and no-invented-facts rules still apply. Soft, low-pressure asks only. (Liam, Nov 12 2026 ~6:30 PM MT, in Bot Builder's chat: "The whole thing with cold emailing is that the future is super chill and it's low intent"; booking link kept in email 1, Nov 12 2026 7:01 PM MT: "keep the booking link in email 1"; also Oct 31 2026: "so straightforward and rude… That's too formal.")
- Never write an "I'll stop emailing you" line ("let me know and I'll stop contacting you", "not a fit? tell me and i'll stop") and never write a breakup email. The opt-out is the email tool's unsubscribe link in the footer, next to the postal address. (Liam, Nov 12 2026 1:32 AM MT, in Toolbox Cold Email's chat, on the Airmail cold sequence rebuild: "never ever say, like, hey, I'll stop emailing you. Never do a breakup email.")

**Every message, draft and post**

- Never write "just say what you need", "just tell me what you need" or close variants (such as "just let me know what you need"). Liam wants the phrase banned from the vocabulary. (Liam, Oct 23 2026 ~9:57 PM MT, in Toolbox CRO's chat, relayed by Toolbox CRO to Bot Builder.)

**Adding new corrections**

When Liam corrects voice, wording or format on a draft, directly or relayed, the bot that drafted it sends Bot Builder the correction in his words, the date, and the draft it came from. For public posts and articles that is Copy Humanizer; for emails, replies, sequences, DMs and texts (which skip Copy Humanizer since Liam's Nov 12 2026 8:17 PM MT pick "make humanizer posts and articles only") it is the drafting bot. Bot Builder (08307ef4) adds a dated line to this section: Liam's Notion skill page first ([Grok · Reference: Writing Mega Skill](https://app.notion.com/p/cf95cda8dd9848da9311a03c2e14e5af)), then the box copy (/home/box/agent-data/workflows/writing-mega-skill/SKILL.md), then the GitHub copy (lg2k2000/agent-skills, shared-writing/writing-mega-skill/SKILL.md). Copy Humanizer does not keep the correction only in its own memory.

## Email courtesy

- Make requests direct and polite. A request does not need an invented due date.
- Do not tell a recipient to complete something by Friday, EOD, this week, or any other date unless Liam explicitly supplied that external deadline or the recipient already committed to it.
- Keep internal follow-up dates and CRM target dates out of the email.
- When a real commitment date exists, refer to it neutrally instead of turning it into a demand.
- When no date exists, omit the deadline. Do not add "when you have a chance" mechanically to every request.
- Keep asks casual and low-key. No dramatic or confrontational asks ("tell me straight", "be honest with me", "I need a yes or no"); ask plainly, the way you'd ask a friend.

## Voice and soul

Avoiding AI patterns is half the job. Clean but voiceless writing is just as obvious as slop.

Signs of soulless writing, even if technically clean:

- Every sentence is the same length and structure.
- There are no opinions, just neutral reporting.
- There is no acknowledgment of uncertainty or mixed feelings.
- There is no first-person perspective where it would be natural.
- There is no personality, no edge and no point of view.
- It reads like a Wikipedia article or a press release.

How to put voice back in:

- Have opinions. Do not just report facts. React to them. "I don't know how to feel about this" is more human than neutrally listing pros and cons.
- Vary your rhythm. Mix short complete sentences with longer ones that take their time.
- Acknowledge complexity. Real humans have mixed feelings. "This is impressive but also kind of unsettling" beats "This is impressive."
- Use first person when it fits. "I keep coming back to..." signals a real person thinking. First person is not unprofessional.
- Let some mess in. Perfect structure feels algorithmic. A tangent or an aside is human, but every sentence stays complete (rule 3.38).
- Keep feelings to Liam's own first-person reactions that the draft already holds, and make them specific: not "this is concerning" but the concrete thing that concerns him. Claims about a product, service or offer name the mechanism or a number instead (rule 3.44).

---

# Part 3. AI-pattern cleanup

Scan for the patterns below, then rewrite. Preserve meaning and match the intended tone.

## Content

3.1 **Significance inflation.** Do not say something is pivotal, a testament, a turning point, or that it reflects broader trends unless you can name the concrete reason.

3.2 **Promotional language.** Cut groundbreaking, vibrant, stunning, seamless, powerful, nestled, breathtaking, must-visit, renowned.

3.3 **Superficial -ing add-ons.** Cut "highlighting...", "underscoring...", "showcasing...", "fostering...", "ensuring...", "reflecting...". Say the thing directly, or expand it with a real source.

3.4 **Vague attribution.** Avoid "experts say", "experts believe", "industry reports suggest", "observers note", "some critics argue". Name the source or delete the line.

3.5 **Formulaic challenges sections.** Skip the "Despite challenges... continues to thrive" boilerplate. Use specific facts or nothing.

3.6 **False ranges.** Do not use "from X to Y, from A to B" where X and Y are not on a meaningful scale. "From the singularity of the Big Bang to the grand cosmic web" is filler. Say what the thing covers, or list the topics directly.

3.7 **Notability name-dropping.** Do not list outlets without context ("featured in The New York Times, BBC, and Wired"). If you cite a source, say what it said.

3.8 **Telling instead of showing.** Cut "This is genuinely hard", "This is what leadership actually looks like", "This is what X actually looks like", "actually matters". Show the difficulty or significance with specifics.

3.9 **Throat-clearing openers.** Cut "Here's the thing:", "Here's what [X]", "Here's this [X]", "Here's that [X]", "Here's why [X]", "The uncomfortable truth is", "It turns out", "The real [X] is", "Let me be clear", "The truth is,", "I'll say it again:", "I'm going to be honest", "Can we talk about", "Here's what I find interesting", "Here's the problem though". Any "here's what/this/that" construction is throat-clearing. State the point.

3.10 **Emphasis crutches.** Cut "Full stop.", "Period.", "Let that sink in.", "This matters because", "Make no mistake", "Here's why that matters".

3.11 **Vague declaratives.** Cut sentences that announce importance without naming the thing: "The reasons are structural", "The implications are significant", "This is the deepest problem", "The stakes are high", "The consequences are real". Replace each with the specific reason, implication or stake, or cut it.

## Structures

These create false drama. State the point directly.

3.12 **Passive voice.** "X was created", "It is believed that", "Mistakes were made" and "The decision was reached" hide the actor. Catch "is/are/was/were + past participle", find the actor, and put them at the front: "queries are validated" becomes "the compiler validates queries", and "the file is parsed by the loader" becomes "the loader parses the file". In Liam's text the actor is almost always known. Passive is fine when the actor is unknown or does not matter. Never invent an actor to force active voice.

3.13 **False agency.** Inanimate things do not perform human actions. A complaint does not become a fix, a bet does not live or die, decisions do not emerge, cultures do not shift, conversations do not move, data does not tell us, markets do not reward. Name the person who fixed, decided, changed behavior, steered, read the data or paid. When no specific person fits, use "you" to put the reader in the seat.

3.14 **Binary contrasts.** "Not because X. Because Y." / "Not because X, but because Y.", "[X] isn't the problem. [Y] is.", "The answer isn't X. It's Y.", "It feels like X. It's actually Y.", "The question isn't X. It's Y.", "Not X. But Y." / "not X, it's Y" / "isn't X, it's Y", "It's not this. It's that.", "stops being X and starts being Y", "doesn't mean X, but actually Y", "is about X but not Y", "not just X but also Y" (and "It is not just X, it is Y"). Drop the negation and state Y: "The problem is Y."

3.15 **Negative listing.** "Not a X... Not a Y... A Z." and "It wasn't X. It wasn't Y. It was Z." State Z. The reader does not need the runway.

3.16 **Dramatic fragmentation.** "[Noun]. That's it. That's the [thing].", "X. And Y. And Z.", "This unlocks something. [Word]." and stacked staccato fragments perform profundity. Write complete sentences and trust the content.

3.17 **Rhetorical setups.** "What if [reframe]?", "What if I told you...", "Here's what I mean:", "Think about it:", "And that's okay." announce insight instead of delivering it. Make the point and let readers draw conclusions.

3.18 **Formulaic constructions.** "By the time X, I was Y." is a narrative template. "X that isn't Y" is indirect; say "X is broken".

3.19 **Narrator from a distance.** "Nobody designed this.", "This happens because...", "This is why...", "People tend to..." float above the scene. Put the reader in the room: "You don't sit down one day and decide to..." beats "Nobody designed this." "You" beats "People."

## Language

3.20 **Adverbs.** Cut intensifiers, softeners and hedges: "really", "just", "literally", "genuinely", "honestly", "simply", "actually", "deeply", "truly", "fundamentally", "inherently", "inevitably", "interestingly", "importantly", "crucially", "particularly", "significantly", "very". An adverb propping up a weak verb means the verb is wrong: "runs quickly" becomes "is fast" or the number, and "significantly improves" becomes the measured delta. Keep adverbs that carry a fact ("only", "monthly", "automatically" when automation is the point), since cutting them changes the claim.

3.21 **Filler phrases.** "In order to" becomes "To". "Due to the fact that" becomes "Because". Delete "It is important to note that", "At its core", "In today's [X]", "It's worth noting", "At the end of the day", "When it comes to", "In a world where", "The reality is".

3.22 **Lazy extremes.** Avoid "every", "always", "never", "everyone", "everybody", "nobody" doing vague work. Sweeping claims fake authority, so use specifics. Be specific in general: name the thing.

3.23 **Hedging.** "could potentially possibly be argued that it might" becomes "may". Trust readers: state facts directly and skip softening, justification and hand-holding. "Not always. Not perfectly." is hedging disguised as reassurance. Cut stacked hedges down to one word ("may"), but keep any qualifier that limits the claim ("most", "if they sign before December 31"). An unsourced population claim ("most owners...") gets cut or sourced, never widened.

3.24 **Copula avoidance.** Use "is", "are" or "has" instead of "serves as", "stands as", "represents", "boasts", "features".

3.25 **Synonym cycling.** Repeat the clearest noun. Protagonist, main character, central figure and hero in one paragraph is a tell. Pick one.

3.26 **Rule of three and list length.** Do not force ideas into groups of three. Use the real number of items and never drop a real one to change the rhythm. Prefer two over three only when you are picking illustrative examples.

3.27 **Wh- openers.** "What makes this hard is..." becomes "The constraint is...", or better, name the constraint. Lead with the subject or the verb. This applies to statements. Questions and conditions ("When X happens, Y") are fine.

3.28 **Paragraph and sentence starters.** Do not open paragraphs with "So" or sentences with "Look,".

3.29 **Plain words.** "utilize" and "leverage" become "use", "facilitate" becomes "help", "numerous" becomes "many", "in the event that" becomes "if". The script's simpler list has the rest.

3.30 **Abstract metaphor nouns.** Substrate (base), wedge, wedge in (add), vector (way, method), locus, vantage, nexus, primitive as a noun, harness as a metaphor, surface as in "API surface", bedrock, scaffolding as a metaphor, modality, paradigm, gold-plating (more than the job needs), ratchet as a metaphor (the real mechanism, or a limit that only tightens), evacuate for moving code (move out), endgame (the last phase), north star, flywheel. Pick the concrete word.

## Vocabulary to avoid

Additionally, align with, circle back, crucial, deep dive, delve, double down, emphasizing, enduring, enhance, fostering, game-changer, garner, genuinely, highlight (as a verb), honest / honestly, interplay, intricate, key (as adjective), landscape (abstract), lean into, moving forward, navigate (challenges), on the same page, pivotal, showcase, take a step back, tapestry (abstract), testament, the cost of doing nothing, underscore (as verb), unpack (analysis), valuable, vibrant, simple.

Plain replacements for business jargon:

| Avoid | Use instead |
| --- | --- |
| Navigate (challenges) | Handle, address |
| Unpack (analysis) | Explain, examine |
| Lean into | Accept, embrace |
| Landscape (context) | Situation, field |
| Game-changer | Significant, important |
| Double down | Commit, increase |
| Deep dive | Analysis, examination |
| Take a step back | Reconsider |
| Moving forward | Next, from now |
| Circle back | Return to, revisit |
| On the same page | Agreed |

The script flags every word and phrase on this list as MUST FIX under BANNED, and lists the judgment calls (key, highlight, honest) under REVIEW. Its AI TELLS list adds robust, streamline, synergy, spearhead, bespoke, curated, cornerstone, hallmark, unleash, supercharge, revolutionize, empower, skyrocket, reimagine, myriad, plethora, holistic, multifaceted, ever-evolving, elevate and unlock.

## Punctuation and formatting

3.31 **No em dashes.** Remove every one, plus en dashes and spaced hyphens used as dashes. Use a comma or a period first; parentheses are fine for a true aside. A plain hyphen or "to" is fine in a number range ("20-25", "20 to 25"). Never use a hyphen or spaced hyphen as sentence punctuation.

3.32 **Colons.** Colons are fine before a list or example, not as mid-sentence connectors. "If you're coming from traditional automation: instead of registering event handlers, you describe conditions" adds nothing with the colon. Let the point stand on its own without comparison framing.

3.33 **Inline-header lists.** Do not format bullets as a bold label, a colon, then an explanation ("**Performance:** Performance improved..."). If the items are short, write a sentence or a plain list. If they need explanation, use real paragraphs. In reference docs and pages only (never emails or posts), a bold lead-in that ends in a period, names the item, and is followed by new detail is fine ("**Schema in TypeScript.** Tables live in one file.").

3.34 **Bold.** No excessive bold. Bold only what is critical, and do not bold every proper noun or acronym.

3.35 **Headings.** Sentence case, not Title Case. The script flags possible title case under REVIEW; leave product and company names as they are.

3.36 **Emojis.** No emoji bullet headers or decorative emojis in headings and bullets.

3.37 **Quotes.** Straight quotes and apostrophes, never curly.

3.38 **Complete sentences.** Every sentence and every bullet is a complete sentence. No over-compression: dropped articles, verbless fragments, symbol-speak and abbreviations that make the reader decode. "Parser rejects bad date → exit 2, no write" becomes "The parser rejects a bad date, exits with code 2, and writes nothing." Spell out arrows and abbreviations. Short complete sentences are fine.

## Rhythm and tone

3.39 Vary sentence length. If three consecutive sentences share the same length, break one. Do not stack short punchy sentences.

3.40 Vary paragraph endings. A punchy one-liner closing every paragraph is a tell.

3.41 If a sentence sounds like a pull-quote, rewrite it.

3.42 Cut questions that get answered in the next sentence. Let a question breathe or delete it.

3.43 Shorten or split dense sentences. If the reader has to backtrack to parse a sentence, break it in two or drop clauses. One idea per sentence.

3.44 **Say what it does.** "the database stays close at hand", "SQL you can read" and "types that follow your schema" name a feeling. Name the mechanism or a number: "`.toSQL()` returns the exact string sent to the database", "a column rename fails the build". Ask what the sentence tells the reader to do or know, then write that. If you cannot restate it as a concrete instruction, fact or number, cut it. If the sentence could appear unchanged in another project's docs (or another company's copy), it says nothing about this one.

3.45 **Mannered prose.** Replace metaphor or flourish where a literal phrase exists: aphorisms ("wire it or delete it"), rhetorical fragments for effect, personified code or things ("the plan holds it"), figurative verbs ("rides along", "stands on"), stock framing phrases. "A dial worth turning" becomes "a parameter worth varying".

3.46 **Communication artifacts.** No chatbot phrases or sycophancy: "Great question", "You're absolutely right!", "Of course", "Certainly!", "I hope this helps", "Let me know if...", "Just say what you need" (and "just tell me what you need"), "Found the smoking gun!".

3.47 **Generic conclusions.** No "The future looks bright", "Exciting times ahead", "In conclusion". State specific plans or facts.

3.48 **Meta-commentary.** Cut "Hint:", "Plot twist:", "Spoiler:", "You already know this, but", "But that's another post", "X is a feature, not a bug", "Dressed up as", "The rest of this essay explains...", "Let me walk you through...", "In this section, we'll...", "As we'll see...", "I want to explore...". The writing should move, not announce its own structure.

3.49 **Performative emphasis.** Cut false intimacy and manufactured sincerity: "creeps in", "I promise", "They exist, I promise".

## Rewrite loop

1. Draft fast.
2. Ask what would make this sound like a person at a real desk wrote it.
3. Tighten: more concrete nouns, fewer qualifiers, varied rhythm.
4. Anti-AI audit: read the draft and ask "what makes this obviously AI-generated?" Find the remaining tells (flat rhythm, placeholder-sounding examples, slogan-y closers, too-tidy contrasts) and fix them.
5. Final pass: delete any sentence that exists only to sound important.

## Quick checks before Part 4

- Are there adverbs? Cut the empty ones; keep the ones that carry a fact.
- Is anything passive? Find the actor and make them the subject, unless the actor is unknown or does not matter.
- Is an inanimate thing doing a human verb ("the decision emerges")? Name the person.
- Does a statement open with a Wh- word? Restructure it.
- Is there "here's what/this/that" throat-clearing? Cut to the point.
- Is there a "not X, it's Y" contrast? State Y directly.
- Do three consecutive sentences share the same length? Break one.
- Does every paragraph end on a punchy line? Vary the endings.
- Did an em dash slip in? Remove it.
- Is there a vague declarative ("The implications are significant")? Name the specific implication.
- Is the narration floating above the scene ("Nobody designed this")? Put the reader in it.
- Are there meta-joiners ("The rest of this essay...")? Delete them.
- Does any sentence sound like a pull-quote? Rewrite it.

## Scoring

Score the draft 1 to 10 on each dimension and revise anything below 35 of 50. Do not report the score.

| Dimension | Question |
| --- | --- |
| Directness | Does it state points or announce them? |
| Rhythm | Is the pacing varied or metronomic? |
| Trust | Does it respect the reader's intelligence? |
| Authenticity | Does it sound like a person wrote it? |
| Density | Can anything be cut? |

## Before and after examples

The examples show the pattern, not facts to reuse.

1. Before: "The initiative marks a pivotal moment in the evolution of regional statistics, underscoring its vital role in the broader landscape." After: "The initiative was set up to collect regional statistics independently from the national office."
2. Before: "Additionally, these groundbreaking tools are reshaping how engineers ideate, iterate, and deliver, highlighting the intricate interplay between automation and human judgment." After: "The tools are good at boilerplate. They are bad at knowing when they are wrong."
3. Before: "In conclusion, the future looks bright as we continue this journey toward excellence. Let me know if you have questions!" After: "The company plans to open two more locations next year."
4. Before: "Here's the thing: building products is hard. Not because the technology is complex. Because people are complex. Let that sink in." After: "Building products is hard because people are complex." This removes the opener, the binary contrast and the emphasis crutch.
5. Before: "What if I told you that the best teams don't optimize for productivity? Here's what I mean: they optimize for learning. Think about it." After: "The best teams optimize for learning." This removes the rhetorical setup and the contrast.
6. Before: "Speed. Quality. Cost. You can only pick two. That's it. That's the tradeoff." After: "Speed, quality, cost. Pick two." This is one plain line with no performative emphasis.

---

# Part 4. Final gate

1. Run `scripts/readability.py` on the final text at the same target as Part 1.
2. Parts 2 and 3 can lengthen sentences or bring back dashes, so fix any regression here: MUST FIX items, very hard sentences, and anything that pushes the grade over target. Do not redo Parts 2 and 3.
3. Check the RHYTHM line again so the fixes do not leave a telegram.
4. Make sure no AI TELLS remain.
5. The text passes when the script exits 0. Report nothing about grades. If asked, give a short list of what changed.

---

## Sources and license

Merged on Oct 23 2026 from readability-editor and humanizer-writing-rules (Liam's skills, now archived), stop-slop (Hardik Pandya, https://github.com/hardikpandya/stop-slop, MIT, retrieved October 1 2026; full license in LICENSE-stop-slop.txt), and the Cursor-managed unslop skill. The application safeguards under "Rules that hold in every part" were added in the stop-slop copy, separate from the original source. Example 6 is stop-slop's Example 4 with its em dash replaced by a period; stop-slop's Examples 2 and 3 were dropped because their rewrites change the claim.
