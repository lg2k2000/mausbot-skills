#!/usr/bin/env python3
"""Hemingway-style readability check.

Usage:
  python3 readability.py FILE [--grade N] [--notes-grade N]
  python3 readability.py - [--grade N]        (reads plain text from stdin)

For decks, --grade is the slide target and notes default to that target + 2.

Reads .pptx (slide text, tables, grouped shapes, speaker notes), .docx (paragraphs
and tables), .pdf, .html/.htm, .md and .txt. For each group (slide text, notes, or
the whole document) it prints:
  - the ARI grade and whether it meets the target
  - MUST FIX: rule breaks that no score excuses (dashes, curly quotes,
    inline-header bullets, bullets that are not complete sentences)
  - MUST FIX also lists BANNED words from the skill's "Vocabulary to avoid" list
  - REVIEW: judgment calls (title case headings; "key", "highlight" and "honest",
    which are banned only as an adjective, a verb, or a sincerity marker)
  - RHYTHM: average sentence length, spread, and runs of same-length sentences,
    which is how over-correction shows up
  - AI TELLS: words and patterns for the humanizer and stop-slop passes
  - per-sentence flags: hard / very hard, passive, adverbs, simpler words

Exit code 0 means the text meets the target with no MUST FIX items. 1 means work remains.
Code blocks, shell commands and URLs are skipped.
"""
import re
import signal
import statistics
import subprocess
import sys

# ---------------------------------------------------------------- word lists

# (pattern, suggestion). Patterns are matched case-insensitively on word boundaries
# and cover inflections, so "utilized" and "purchasing" are caught.
SIMPLER = [
    (r"in order to", "to"),
    (r"so as to", "to"),
    (r"due to the fact that", "because"),
    (r"in light of the fact that", "because"),
    (r"despite the fact that", "although"),
    (r"at this (point in )?time", "now"),
    (r"at the present time", "now"),
    (r"(has|have|had) the ability to", "can"),
    (r"(is|are) able to", "can"),
    (r"a (large |small |significant )?number of", "many, some, or the number"),
    (r"the (vast )?majority of", "most"),
    (r"in the event that", "if"),
    (r"with (regard|respect) to", "about"),
    (r"in terms of", "about, or cut"),
    (r"for the purpose of", "to, or for"),
    (r"on a (daily|weekly|monthly|quarterly|yearly|regular) basis", "daily, weekly, monthly..."),
    (r"it is (important|worth|key) (to note|noting) that", "cut it"),
    (r"(one thing|something) (that )?(should|needs to|to) be noted is( that)?", "cut it"),
    (r"(please )?(note|be aware) that", "cut it"),
    (r"prior to", "before"),
    (r"subsequent to", "after"),
    (r"utili[sz](e|es|ed|ing|ation)", "use"),
    (r"leverag(e|es|ed|ing)", "use"),
    (r"facilitat(e|es|ed|ing)", "help"),
    (r"commenc(e|es|ed|ing)", "start"),
    (r"initiat(e|es|ed|ing)", "start"),
    (r"terminat(e|es|ed|ing)", "end"),
    (r"approximately", "about"),
    (r"additional", "more, extra"),
    (r"additionally", "also"),
    (r"numerous", "many"),
    (r"obtain(s|ed|ing)?", "get"),
    (r"purchas(e|es|ed|ing)", "buy"),
    (r"requir(e|es|ed|ing)", "need"),
    (r"sufficient", "enough"),
    (r"assistance", "help"),
    (r"individuals", "people"),
    (r"demonstrat(e|es|ed|ing)", "show"),
    (r"indicat(e|es|ed|ing)", "show"),
    (r"enhanc(e|es|ed|ing|ement)", "improve"),
    (r"optimal", "best"),
    (r"regarding", "about"),
    (r"nevertheless", "still"),
    (r"subsequently", "later, then"),
    (r"in close proximity( to)?", "near"),
    (r"methodology", "method"),
    (r"functionality", "features"),
    (r"endeavou?r(s|ed|ing)?", "try"),
    (r"ascertain(s|ed|ing)?", "find out"),
    # copula avoidance (humanizer pattern 8): say "is" or "has"
    (r"(serve|serves|served|serving|stand|stands|stood|standing) as (a|an|the)", "is"),
    (r"boast(s|ed|ing)?", "has"),
]
SIMPLER = [(re.compile(r"\b" + p + r"\b", re.I), s) for p, s in SIMPLER]

# Words and patterns the humanizer and stop-slop passes remove. Reported, not scored.
AI_WORDS = re.compile(
    r"\b(delv(e|es|ed|ing)|tapestr(y|ies)|testament|pivotal|underscor(e|es|ed|ing)|"
    r"foster(s|ed|ing)?|intricat(e|ely|ies|y)|interplay|garner(s|ed|ing)?|"
    r"showcas(e|es|ed|ing)|vibrant|seamless(ly)?|robust|streamlin(e|es|ed|ing)|"
    r"synerg(y|ies|istic)|paradigm|spearhead(s|ed|ing)?|bespoke|curated|cornerstone|"
    r"hallmark|unleash(es|ed|ing)?|supercharg(e|es|ed|ing)|revolutioni[sz](e|es|ed|ing)|"
    r"empower(s|ed|ing|ment)?|harness(es|ed|ing)?|skyrocket(s|ed|ing)?|reimagin(e|es|ed|ing)|"
    r"game[- ]changer|groundbreaking|nestled|renowned|breathtaking|stunning|captivating|"
    r"myriad|plethora|holistic|multifaceted|ever[- ]evolving|crucial|"
    r"elevat(e|es|ed|ing)|unlock(s|ed|ing)?|landscape)\b", re.I)
ING_TAIL = re.compile(
    r",\s+(highlighting|underscoring|emphasi[sz]ing|reflecting|showcasing|ensuring|fostering|"
    r"signal(l)?ing|symboli[sz]ing|demonstrating|cementing|solidifying|paving|marking|"
    r"contributing)\b", re.I)
# The skill's "Vocabulary to avoid" list (SKILL.md Part 3). Clear matches are MUST FIX;
# BANNED_REVIEW holds words that are banned only in one sense, so a person checks them.
BANNED = re.compile(
    r"\b(additionally|align(s|ed|ing)? with|circl(e|es|ed|ing) back|crucial(ly)?|deep[- ]dives?|"
    r"delv(e|es|ed|ing)|doubl(e|es|ed|ing) down|emphasi[sz]ing|enduring|enhanc(e|es|ed|ing|ement)|"
    r"foster(s|ed|ing)?|game[- ]changers?|garner(s|ed|ing)?|genuinely|interplay|intricate(ly)?|"
    r"landscapes?|lean(s|ed|ing)? into|moving forward|navigat(e|es|ed|ing)|on the same page|"
    r"pivotal|showcas(e|es|ed|ing)|tak(e|es|ing) a step back|took a step back|tapestr(y|ies)|testament|"
    r"the cost of doing nothing|underscor(e|es|ed|ing)|unpack(s|ed|ing)?|valuable|vibrant|simple)\b", re.I)
BANNED_REVIEW = re.compile(
    r"\b(key(?!\s+(to|is|was|in|on|for|of|and|or|that|it)\b)(?=\s+[a-z])|"
    r"highlight(s|ed|ing)?|honest(ly)?)\b", re.I)
CONTRAST = re.compile(r"\bnot (just|only|merely|simply)\b|\bit'?s not [^.,;]{1,40}, it'?s\b", re.I)
HYPHEN_PAIRS = re.compile(
    r"\b(well-known|high-quality|long-term|real-time|data-driven|decision-making|third-party|"
    r"cross-functional|client-facing|end-to-end)\b", re.I)

# -ly words that are not adverbs, or that carry a fact. Capitalized -ly words
# mid-sentence (names like Kelly or Emily) are skipped automatically.
LY_OK = set("""only early family apply supply reply comply imply multiply rely ally rally tally
belly jelly holy ugly silly lonely costly timely untimely friendly unfriendly elderly assembly
anomaly daily weekly monthly quarterly yearly hourly nightly biweekly annually likely unlikely
july italy fully reliably curly burly surly orderly scholarly lovely deadly lively lowly
unruly chilly hilly wobbly bubbly oily fly butterfly bully lily""".split())

IRREGULAR = ("built|done|made|given|taken|seen|known|shown|sold|paid|run|held|kept|left|set|sent|"
             "written|driven|chosen|broken|spoken|bought|brought|thought|found|told|won|begun|"
             "grown|drawn|hidden|put|cut|led|lost|met|read|said|spent|taught|understood|proven|"
             "bound|hit|thrown|shut|split|spread|upheld|withdrawn|forgotten|gotten|frozen|stolen|"
             "overridden|rebuilt|rewritten|undone|hung|laid|meant|sought|shot|struck|worn|torn")
AUX = r"(am|is|are|was|were|be|been|being|get|gets|got|getting)"
PASSIVE = re.compile(rf"\b{AUX}\s+(?:\w+ly\s+)?(\w{{2,}}ed|{IRREGULAR})\b", re.I)
NOT_PASSIVE = set("""based located interested involved concerned excited supposed used pleased
surprised worried tired married bored related dedicated experienced qualified skilled
detailed advanced red bed shed need speed""".split())

DASH_EM = re.compile(r"[\N{EM DASH}\N{HORIZONTAL BAR}]|(?<=\w)\s?--\s?(?=\w)")
DASH_EN = re.compile(r"\N{EN DASH}")
DASH_SPACED = re.compile(r"(?<=[A-Za-z0-9,)])\s-\s(?=[A-Za-z0-9(])")
CURLY = re.compile(r"[\N{LEFT DOUBLE QUOTATION MARK}\N{RIGHT DOUBLE QUOTATION MARK}\N{LEFT SINGLE QUOTATION MARK}\N{RIGHT SINGLE QUOTATION MARK}]")
BULLET_MARK = re.compile(r"^\s*(?:[-*+\N{BULLET}\N{BLACK SMALL SQUARE}\N{BLACK CIRCLE}]|\d+[.)])\s+")
MD_INLINE_HEADER = re.compile(r"^\s*(?:[-*+\N{BULLET}]|\d+[.)])\s+(\*\*|__)[^*_\n]{1,60}?(:\s*\1|\1\s*:)")
SMALL_WORDS = set("a an and as at but by for from in into nor of on or per the to vs via with".split())


# ---------------------------------------------------------------- readers
# Each reader yields (where, kind, text, inline_header) where kind is one of
# title, heading, bullet, para, cell, notes.

def lead_bold_label(runs):
    """True when a paragraph starts with a bold label followed by a colon."""
    lead = ""
    rest = ""
    for i, (txt, bold) in enumerate(runs):
        if not txt:
            continue
        if bold and not rest:
            lead += txt
        else:
            rest += txt
    lead = lead.strip()
    if not lead or len(lead.split()) > 8:
        return False
    return lead.endswith(":") or rest.lstrip().startswith(":")


def read_pptx(path):
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER
    titles = {PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE, PP_PLACEHOLDER.SUBTITLE,
              PP_PLACEHOLDER.VERTICAL_TITLE}

    def walk(shapes, where):
        for sh in shapes:
            if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
                yield from walk(sh.shapes, where)
                continue
            if getattr(sh, "has_table", False) and sh.has_table:
                for r, row in enumerate(sh.table.rows, 1):
                    for c, cell in enumerate(row.cells, 1):
                        if cell.text.strip():
                            yield f"{where}t{r}.{c}", "cell", cell.text, False
                continue
            if not getattr(sh, "has_text_frame", False) or not sh.has_text_frame:
                continue
            kind = "para"
            if sh.is_placeholder:
                kind = "title" if sh.placeholder_format.type in titles else "bullet"
            for para in sh.text_frame.paragraphs:
                text = para.text if hasattr(para, "text") else "".join(r.text for r in para.runs)
                if not text.strip():
                    continue
                ih = kind == "bullet" and lead_bold_label([(r.text, r.font.bold) for r in para.runs])
                yield where, kind, text, ih

    prs = Presentation(path)
    for i, slide in enumerate(prs.slides, 1):
        yield from walk(slide.shapes, f"S{i}")
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text
            for para in notes.split("\n"):
                if para.strip():
                    yield f"N{i}", "notes", para, False


def read_docx(path):
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    d = docx.Document(path)

    def para_kind(p):
        style = (p.style.name if p.style is not None else "").lower()
        if style.startswith("heading") or style == "title":
            return "heading"
        has_num = p._p.pPr is not None and p._p.pPr.numPr is not None
        return "bullet" if ("list" in style or has_num) else "para"

    pi = ti = 0
    for child in d.element.body.iterchildren():
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "p":
            pi += 1
            p = Paragraph(child, d)
            if p.text.strip():
                k = para_kind(p)
                ih = k == "bullet" and lead_bold_label([(r.text, r.bold) for r in p.runs])
                yield f"P{pi}", k, p.text, ih
        elif tag == "tbl":
            ti += 1
            for r, row in enumerate(Table(child, d).rows, 1):
                seen = set()
                for c, cell in enumerate(row.cells, 1):
                    if id(cell._tc) in seen:      # merged cells repeat
                        continue
                    seen.add(id(cell._tc))
                    if cell.text.strip():
                        yield f"T{ti}r{r}c{c}", "cell", cell.text, False


def read_pdf(path):
    t = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
    for i, para in enumerate(re.split(r"\n\s*\n|\f", t), 1):
        para = re.sub(r"-\n(?=[a-z])", "", para).replace("\n", " ").strip()
        if para:
            kind = "bullet" if BULLET_MARK.match(para) else "para"
            yield f"B{i}", kind, para, False


def read_html(path):
    from bs4 import BeautifulSoup, Tag
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    for x in soup(["style", "script", "svg", "pre", "code", "noscript", "template"]):
        x.decompose()
    blocks = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "td", "th", "dt", "dd",
              "blockquote", "figcaption", "div", "section", "article"]
    for i, el in enumerate(soup.find_all(blocks), 1):
        if el.find(blocks):
            continue
        text = el.get_text(" ").strip()
        if not text:
            continue
        name = el.name
        kind = ("heading" if re.match(r"h\d", name) else "bullet" if name == "li"
                else "cell" if name in ("td", "th") else "para")
        ih = False
        if kind == "bullet":
            first = next((c for c in el.children if not (isinstance(c, str) and not c.strip())), None)
            if isinstance(first, Tag) and first.name in ("strong", "b"):
                label = first.get_text().strip()
                after = first.next_sibling
                after = after if isinstance(after, str) else ""
                ih = len(label.split()) <= 8 and (label.endswith(":") or after.lstrip().startswith(":"))
        yield f"H{i}", kind, text, ih


def read_text(lines):
    in_code = False
    for i, line in enumerate(lines, 1):
        if line.strip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        if in_code or not line.strip():
            continue
        if line.startswith(("    ", "\t")) and not BULLET_MARK.match(line):
            continue                                   # indented code
        if line.lstrip().startswith("|"):
            if re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line):
                continue                               # table separator row
            for c, cell in enumerate([x for x in line.strip().strip("|").split("|")], 1):
                if cell.strip():
                    yield f"L{i}c{c}", "cell", cell, False
            continue
        if re.match(r"^\s*#{1,6}\s", line):
            yield f"L{i}", "heading", line, False
        elif BULLET_MARK.match(line):
            yield f"L{i}", "bullet", line, bool(MD_INLINE_HEADER.match(line))
        else:
            yield f"L{i}", "para", line, False


def blocks(path):
    p = path.lower()
    if path == "-":
        return read_text(sys.stdin.read().split("\n"))
    if p.endswith(".pptx"):
        return read_pptx(path)
    if p.endswith(".docx"):
        return read_docx(path)
    if p.endswith(".pdf"):
        return read_pdf(path)
    if p.endswith((".html", ".htm")):
        return read_html(path)
    return read_text(open(path, encoding="utf-8").read().split("\n"))


# ---------------------------------------------------------------- analysis

def clean(t):
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", t)      # markdown links and images
    t = re.sub(r"`[^`]*`", "code", t)                      # inline code
    t = re.sub(r"https?://\S+|www\.\S+", "", t)            # URLs
    t = re.sub(r"<[^>]+>", "", t)                          # stray tags
    t = re.sub(r"^\s*(#{1,6}|>)\s*", "", t)                # heading and quote markers
    t = BULLET_MARK.sub("", t)                             # list markers
    t = re.sub(r"(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1", r"\2", t)   # bold and italics
    return t


def sentences(t):
    t = re.sub(r"\s+", " ", clean(t)).strip()
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+(?=[A-Z0-9\"'$\N{EURO SIGN}(\N{LEFT DOUBLE QUOTATION MARK}])", t) if s.strip()]


def is_code(s):
    toks = s.split()
    if not toks:
        return False
    codey = sum(1 for w in toks if w.startswith("--") or "://" in w or re.search(r"[=/\\{}<>|_]", w)
                or re.match(r"^[a-z0-9]+(-[a-z0-9]+)+$", w) and len(w) > 12)
    return codey / len(toks) > 0.3


WORD = re.compile(r"[A-Za-z0-9$\N{EURO SIGN}][A-Za-z0-9$\N{EURO SIGN},.\-']*")


def ari(chars, words, sents):
    return 4.71 * chars / max(words, 1) + 0.5 * words / max(sents, 1) - 21.43


def title_case(text):
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", clean(text))
    if len(words) < 2:
        return False
    rest = [w for w in words[1:] if w.lower() not in SMALL_WORDS and not w.isupper()]
    return len(rest) >= 1 and all(w[0].isupper() for w in rest)


def analyse(items, target, slides_mode):
    tc = tw = ts = 0
    per_unit = {}
    must, review, tells, flagged, lengths, runs = [], [], [], [], [], []

    for where, kind, text, inline_header in items:
        raw = text
        # rule breaks, checked on raw text
        if DASH_EM.search(raw):
            must.append(f"{where} em dash")
        if DASH_EN.search(raw):
            must.append(f"{where} en dash (use a hyphen, 'to', or a comma)")
        if DASH_SPACED.search(BULLET_MARK.sub("", raw)) and not is_code(raw):
            must.append(f"{where} spaced hyphen used as a dash")
        if CURLY.search(raw):
            must.append(f"{where} curly quote or apostrophe")
        if inline_header:
            must.append(f"{where} inline-header bullet (bold label + colon)")
        for m in BANNED.finditer(clean(raw)):
            must.append(f"{where} BANNED word: \"{m.group(0)}\" (see Vocabulary to avoid)")
        for m in BANNED_REVIEW.finditer(clean(raw)):
            review.append(f"{where} BANNED if used as adjective/verb/sincerity marker: \"{m.group(0)}\"")
        body = clean(raw).strip()
        if kind == "bullet" and len(body.split()) >= 1 and not is_code(body) \
                and not re.search(r"[.?!:)\"']$", body):
            must.append(f"{where} bullet does not end as a sentence: \"{body[:60]}\"")
        if kind in ("heading", "title") and title_case(raw):
            review.append(f"{where} title case? \"{body[:60]}\" (leave product and company names alone)")

        for rx, label in ((AI_WORDS, None), (ING_TAIL, "-ing tail"), (CONTRAST, "contrast scaffold"),
                          (HYPHEN_PAIRS, "hyphenated pair")):
            for m in rx.finditer(raw):
                tells.append(f"{where} {label + ': ' if label else ''}{m.group(0).strip(', ')}")

        prose_lengths = []
        for s in sentences(raw):
            if is_code(s):
                continue
            ws = WORD.findall(s)
            if len(ws) < 3:
                continue
            c = sum(len(re.sub(r"[^A-Za-z0-9]", "", w)) for w in ws)
            tc += c; tw += len(ws); ts += 1
            unit = re.match(r"[A-Z]\d+", where).group(0) if slides_mode else None
            if unit:
                u = per_unit.setdefault(unit, [0, 0, 0])
                u[0] += c; u[1] += len(ws); u[2] += 1
            if kind in ("para", "notes"):
                prose_lengths.append(len(ws))
            if kind in ("para", "notes", "bullet"):
                lengths.append(len(ws))

            g = ari(c, len(ws), 1)
            f = []
            # per-sentence ARI is noise under 8 words (a 3-word table cell of long
            # product names is not a hard sentence), so short units are judged on length only
            long_words = len(ws) >= 8 and g >= 14
            if len(ws) > 20 or long_words:
                f.append(("very hard" if (len(ws) > 25 or (len(ws) >= 8 and g >= 16)) else "hard") + f" {len(ws)}w")
            adv = []
            for i, w in enumerate(ws):
                lw = w.lower().strip(".,;:'\"")
                if lw.endswith("ly") and len(lw) > 4 and lw not in LY_OK and not (i > 0 and w[0].isupper()):
                    adv.append(lw)
            if adv:
                f.append("adverb: " + ", ".join(adv))
            pas = []
            for m in PASSIVE.finditer(s):
                aux, part = m.group(1).lower(), m.group(2).lower()
                if part in NOT_PASSIVE or (aux.startswith("get") or aux == "got") and part == "started":
                    continue
                pas.append(m.group(0))
            if pas:
                f.append("passive: " + ", ".join(pas))
            wd, spans = [], []
            for rx, sug in SIMPLER:
                for m in rx.finditer(s):
                    if any(a <= m.start() and m.end() <= b for a, b in spans):
                        continue                       # already inside a longer match
                    spans.append(m.span())
                    wd.append(f"{m.group(0)} -> {sug}")
            if wd:
                f.append("simpler: " + "; ".join(wd))
            if f:
                flagged.append((where, "; ".join(f), s))

        # runs of three similar-length sentences inside one paragraph
        for i in range(len(prose_lengths) - 2):
            trio = prose_lengths[i:i + 3]
            if min(trio) >= 4 and max(trio) - min(trio) <= 2:
                runs.append(f"{where} ({'/'.join(map(str, trio))} words)")
                break

    return dict(grade=ari(tc, tw, ts), words=tw, sents=ts, must=must, review=review,
                tells=tells, flagged=flagged, lengths=lengths, runs=runs,
                units={k: ari(*v) for k, v in per_unit.items()})


def report(label, r, target, slides_mode):
    ok = True
    head = f"== {label}: ARI grade {r['grade']:.1f}, {r['words']} words, {r['sents']} sentences"
    if target is not None:
        if r["grade"] <= target:
            head += f"  PASS (target {target:g})"
        else:
            head += f"  ABOVE TARGET {target:g}"
            ok = False
    print(head)
    if r["units"] and target is not None:
        over = sorted(((g, u) for u, g in r["units"].items() if g > target), reverse=True)
        if over:
            print("  over target: " + ", ".join(f"{u} {g:.1f}" for g, u in over))
    if r["must"]:
        ok = False
        print(f"  MUST FIX ({len(r['must'])}):")
        for m in r["must"]:
            print("    " + m)
    if r["review"]:
        print(f"  REVIEW ({len(r['review'])}):")
        for m in r["review"]:
            print("    " + m)
    if not slides_mode and len(r["lengths"]) >= 5:
        avg = statistics.mean(r["lengths"])
        spread = statistics.pstdev(r["lengths"])
        line = f"  RHYTHM: average {avg:.1f} words, spread {spread:.1f}"
        notes = []
        if avg < 9:
            notes.append("short average, check it does not read like a telegram")
        if r["lengths"] and len(r["lengths"]) >= 6 and spread < 3:
            notes.append("lengths too even")
        if r["runs"]:
            notes.append("3 similar-length sentences in a row at " + ", ".join(r["runs"][:5]))
        print(line + ("  CHECK: " + "; ".join(notes) if notes else ""))
    if r["tells"]:
        print(f"  AI TELLS for humanizer and stop-slop ({len(r['tells'])}): " + ", ".join(r["tells"][:20]))
    for where, why, s in r["flagged"]:
        print(f"  {where} [{why}] {s[:170]}")
    return ok


def main():
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # quiet exit when piped into head
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    def take(flag):
        if flag in args:
            i = args.index(flag)
            val = float(args[i + 1])
            del args[i:i + 2]
            return val
        return None

    target = take("--grade")
    notes_target = take("--notes-grade")
    if notes_target is None and target is not None:
        notes_target = target + 2            # slides 6 -> notes 8, per the skill's targets
    path = args[0]
    groups = {}
    for where, kind, text, ih in blocks(path):
        groups.setdefault("NOTES" if kind == "notes" else "TEXT", []).append((where, kind, text, ih))
    is_deck = path.lower().endswith(".pptx")
    ok = True
    for label in ("TEXT", "NOTES"):
        if label not in groups:
            continue
        t = notes_target if label == "NOTES" else target
        r = analyse(groups[label], t, is_deck)
        # slide text gets no rhythm check (slides are short by design); notes are prose
        ok &= report(label, r, t, is_deck and label == "TEXT")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
