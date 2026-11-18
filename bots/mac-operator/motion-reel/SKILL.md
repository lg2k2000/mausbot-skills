---
name: motion-reel
description: One engine for code-drawn video on Liam's Mac. Explainers, product and UI films made from real screenshots (state lists), data stories, animated charts and kinetic type, drawn as a pure seek(t) page in headless Chromium, scored with synthesized sound and encoded with ffmpeg in 9:16, 4:5, 1:1 and 16:9 from one timeline. It has springs, beat sync to a music track, a style-from-reference step, three gates Liam approves (brief, storyboard, final cut) and a scored critic loop with review sheets. Use it whenever Liam asks for an explainer, a how-it-works or process video, a product, website or landing page walkthrough, a UI or app demo film, a chart or data animation, a text or typography animation, a storyboard, a video in the style of a reference clip, cuts on the beat, a Reels, TikTok or LinkedIn video made in code, or the Isometric Pastel or Editorial Chart look, for Apivant, Toolbox or Around The House. It replaces the isometric explainer recipe. For 3D Blender logo vortex ads, use logo-motion-ad.
---

# Motion reel

- A film is one HTML page whose `draw(ctx, t)` is a pure function of time. `render.py` calls `seek(t)` for every frame in headless Chromium, renders the score offline to a WAV, and ffmpeg encodes and mixes the MP4. The same `t` always gives the same pixels, so renders repeat exactly and a storyboard is a set of frames from the finished film.
- One timeline serves every format. The film computes a layout per format from `R.frame(fmt)`, and the times, text and sound stay shared.
- Everything here was written for Liam on Oct 22, 2026. No creator's code or pasted prompt is in it; looks live in `references/styles/` as written descriptions.
- It runs on Liam's Mac. Claude Code runs the commands in Bash. From claude.ai, run the same commands through Desktop Commander `start_process`.
- The `scripts/`, `references/` and `templates/` folders named below exist only in the Mac copy at `~/.claude/skills/motion-reel/`. This file needs no other skill.

## When to use it, and when not

- Use it for anything drawn in code over time: explainers, process and how-it-works pieces, UI and product films from real screenshots, number and chart stories, kinetic type, end cards, and retargeting or mid-funnel ads.
- Use logo-motion-ad for 3D Blender pieces where light, fabric, water or the logo vortex has to look physical. That skill stays separate.
- Load launch-motion with this skill for any ad or explainer. It sets the story order, the 1.5 s holds, the offer pill from about 2 s, the brand inside the fix and the 15 s and full cuts; this skill draws and renders them. Run its pre-render checklist in every critic round.
- Physical products on real homes (Around The House) sell better with real footage. Use motion-reel there for explainers and end cards, not for the product itself.
- Futurepedia's AI Style Atlas prompts are marked all rights reserved: never copy them, or code from them, into this skill, a style file or a film folder. To reuse a look, describe it in our own words (`references/style-from-reference.md`).
- The Isometric Pastel look from the retired isometric explainer recipe is `references/styles/isometric-pastel.md`.

## Folder layout

- Client work lives in `~/projects/client-marketing-assets/<client>/ads/NN-name-yyyy-mm/`: `brief.md` before work starts, `video/` (the film folder), `finals/` (current cuts; replaced cuts go to `finals/archive/`), `review/` (sheets sent to Liam and the critic rounds), and a `README.md` once it is made. Never write one client's files into another client's folder.
- Apivant work lives in `~/projects/apivant marketing/claude/video/<name>-<yyyy-mm-dd>/` with the same four parts, because Apivant writes only under `claude/`. Its `CLAUDE.md` rules apply (`references/clients/apivant.md`).
- The film folder (`video/`) holds `index.html`, `lib/reel.js`, `lib/sound.js`, `film.js`, `score.js`, `fonts/`, `assets/` (exact logo files), and when used `states/` (captures) and `beatmap.js`. Frames are piped to ffmpeg, not saved; work files go to the temp folder unless `--work` says otherwise.

## The three gates Liam approves

1. **Brief and assets.** `brief.md` has the job, audience, formats, length, the beats as a table, every on-screen line with its source, the offer, and what may not be said. The assets list names the exact logo files, fonts, captured screenshots, music and the style file. Liam's yes comes before the storyboard.
2. **Storyboard sheet.** `render.py storyboard` makes one panel per beat at its key time, with the beat's text, move and sound under it and the open questions below. The critic scores it first (hook, readability, brand, variety). Send the main format's sheet plus one sheet of the other formats. Liam's yes comes before the full build.
3. **Final cut.** The finals in every format, `review/contact-2fps.png`, `phone-360.png` and the report, after the critic loop passes. Liam's yes comes before anything is sent to a client, posted, attached to an ad or paid for.

Liam sees only gate material. Send sheets and cuts with `SendUserFile`, and say what changed since the last gate.

## The critic loop (between gates)

1. Render, then run `review.py` on each format's cut with `--film`.
2. Look at `contact-2fps.png`, `motion-strip.png`, `phone-360.png` and `loop.png` at full size, and read `report.md`.
3. Score the six criteria from 1 to 10 with `references/critic-rubric.md`: hook in 2 s, phone readability, motion, variety, sound sync and brand accuracy. Every score cites timestamps.
4. Write `review/critic-roundN.md`: the scores, then the worst three problems, each with its timestamp and the fix.
5. Fix those three, re-render and repeat until every score is 8 or better.
6. After four rounds without getting there, stop and bring Liam the scores and the question that blocks it.

Claude cannot watch or listen. Motion is judged from the strip and the contact sheet. Sound sync is judged from the report's table of motion starts against sound onsets and its loudness every half second. Say so when reporting.

## Build steps

1. **Start the folder.** `scripts/new_film.sh VIDEO_DIR basic` (or `state-list`). It copies the page, the harness and a template that already runs.
2. **Write the brief (gate 1).** Check every line against the live source with one script per page (`document.body.innerText.includes(...)` in the built-in browser). Never submit a form on a live site.
3. **Pick the style.** Use a file in `references/styles/`, or measure a reference clip with `reference.py` and write a style guide in our own words. Swap the style's accent for the brand colour; keep the brand's exact logo files.
4. **Write `film.js`.** Put every time in one `T` object at the top so `score.js` reads the same numbers. Write `layout(F)` once per format and `draw(ctx, t, L, F)` as a pure function. Fill `FILM.beats` as you go; the storyboard and critic read it.
5. **Storyboard (gate 2).** Run `render.py storyboard` per format, run a critic round on it, fix, then send.
6. **Score.** Write `score.js` on the same `T`: effects in front, beds and music under them, about three sounds at once at most, a short gap before the biggest hit, and the biggest hit on the number or the turn.
7. **Music (optional).** Run `beats.py` on the track to get `beatmap.js`. Snap cuts and hits to `BEATMAP.beats` with `R.nearest`, place the track with `--music`, and leave the synthesized effects on top.
8. **Render every format** with `render.py video`, then run the critic loop.
9. **Final cut (gate 3),** then file it: the ad's `README.md` (copy and sources, what it shows, checks, rebuild commands), the client `README.md` and `log.md`, or for Apivant `claude/README.md`, `claude/CHANGELOG.md` and, once Liam approves, a copy in `shared/` per its `CLAUDE.md`.

## The film contract

```js
const T = { hookOut: 1.8, land: 4.2, end: 12 };          // every time lives here
const FILM = {
  title, duration: T.end, fps: 30, loop: false, formats: ['9x16', '4x5', '1x1'],
  fonts: [{ family: 'Heading', src: 'fonts/heading.woff2', weight: 800 }],
  images: { logo: 'assets/brand-logo.png' },                // exact files, drawn with R.image
  samples: { chime: 'assets/chime.mp3' },                   // optional, for k.sample
  beats: [{ t, end, key, title, text, move, sound }],       // storyboard panels and critic notes
  notes: ['Open question for Liam ...'],
  layout(F, ctx) { return { /* boxes, sizes, tracks for this format */ }; },
  draw(ctx, t, L, F) { /* pure function of t */ },
};
window.FILM = FILM;
// score.js
FILM.score = (k, F) => { k.bed('room', 0, T.end); k.play('impact', T.land); };
```

The page exposes `window.seek`, `window.grab`, `window.info`, `window.renderSound` and `window.ready`. `?fmt=4x5` picks the format and `?render=1` hides the player bar. Optional globals: `window.STATES` from `capture.py` and `window.BEATMAP` from `beats.py`.

## Harness (lib/reel.js, global R)

- Time: `R.seg(t, a, b)`, `R.ez(t, a, b, 'out3')`, `R.window(t, a, b, fin, fout)`, `R.bump(t, at, width)`, `R.stagger(i, gap, start)`, `R.nearest(times, t)`, `R.pulseOn(times, t, decay)`.
- Random: `R.rand(seed)` with `.between`, `.int`, `.pick`, `.normal`, `.shuffle`; `R.hash(...parts)`; `R.noise(seed)` with `n1`, `n2`, `n3`, `fbm`; `R.wiggle(t, freq, amp, seed)`. Never use `Math.random`.
- Easing: `R.ease.out3`, `inOut3`, `outExpo`, `outBack` and the rest; `R.bezier(x1, y1, x2, y2)` matches a CSS curve.
- Springs: `R.spring(t, 'snappy')` is closed form, so any frame stands alone. Presets are `gentle`, `smooth`, `snappy`, `pop`, `bouncy`, `heavy` and `stiff`, or pass `{ f, z }` (frequency in Hz, damping ratio). `R.settle(spring)` gives the seconds to rest, and `R.sp(t, start)` is shorthand.
- Tracks: `R.track(v0, [[t1, v1], [t2, v2, spring]])` is the stacked spring `v0 + Σ (v_i − v_(i−1)) × spring(t − t_i)`, for numbers or arrays (points, boxes, colours), with smooth retargets mid-flight. `R.tween(keys, ease)` covers moves that must land on an exact frame.
- Colour: `R.mix(a, b, u)` in OKLab, `R.tint(c, ±amount)`, `R.css(c, alpha)`, `R.hexOf`.
- Type: `R.family`, `R.font(size, weight, family)`, `R.wrap`, `R.fitSize`, `R.text`. `R.reveal(ctx, t, text, { by: 'word' | 'line' | 'char', start, gap, spring, out })` springs words in and out and returns the block's box. Also `R.typeOn`, `R.pill`, `R.num`.
- Layout: `R.frame(fmt)` returns `F` (`W`, `H`, `box` = safe area, `min` sizes, `pw`, `ph`, `portrait`). Use it with `R.rows`, `R.cols`, `R.place`, `R.inset`, `R.fitBox` and `R.camera(ctx, F, { x, y, zoom, rot })`.
- Finish: `R.grain(ctx, W, H, t, { amount, loop })`, `R.vignette`, `R.paper`, `R.shadow`, `R.cache` for anything static.
- Images and UI: `R.image(ctx, img, box, { fit })` draws exact files. `R.device(ctx, box, { kind })`, `R.screen(ctx, img, scr, view)`, `R.toScreen`, `R.cursor(ctx, x, y, { press })`, `R.tap` and `R.ring` are for state-list films.

## Sound kit (lib/sound.js, `k` in the score)

- `k.play(name, t, { gain, pan, ... })` takes these names. Interface: `tap`, `click`, `pop`, `tick`, `count`, `toggle`, `key`, `typing`, `scroll`, `swipe`. Motion: `whoosh`, `glide`, `rise`. Weight: `thump`, `impact`, `sub`, `lock`, `snap`, `buzz`. Tone: `ding`, `chime`, `success`, `wrong`, `shimmer`. Hand-made: `pen`, `paper`, `stamp`.
- `k.bed('room' | 'air' | 'drone' | 'clock', t0, t1)` lays a bed. `k.music('pad' | 'pulse', t0, t1, { bpm, chords, beats })` adds music. `k.sample(name, t)` plays a file. `k.osc` and `k.noise` build new sounds, and `k.onTimes(times, fn)` runs something on each time in a list.
- Counters tick at most 12 times a second, computed from the same easing the picture uses (see `templates/basic/score.js`).
- Set `FILM.vo = true` for a voiceover cut. Beds and music then drop, and effects sit lower.

## Formats

| Format | Canvas | Safe box (left, top, right, bottom) | Smallest label, headline, key number |
|---|---|---|---|
| 9x16 | 1080 x 1920 | 64, 230, 140, 440 | 37, 92, 140 px |
| 4x5 | 1080 x 1350 | 64, 64, 64, 96 | 37, 92, 140 px |
| 1x1 | 1080 x 1080 | 60, 60, 60, 72 | 37, 92, 140 px |
| 16x9 | 1920 x 1080 | 110, 64, 110, 80 | 65, 163, 250 px |

- Phones show every format about 360 points wide, so the minimum sizes scale with width. `phone-360.png` is the test.
- In 9:16 the platform covers the top strip and the bottom 440 px (caption, buttons, progress bar) and the right edge (buttons). Keep text and the offer inside the safe box.
- Each format gets its own layout. Do not crop 9:16 into 4:5.

## Commands

Use the project's Python (`~/projects/apivant marketing/.venv/bin/python`, or `~/projects/client-marketing-assets/<client>/.venv/bin/python3`) with `SK=~/.claude/skills/motion-reel/scripts`.

```bash
$SK/new_film.sh ads/03-name-2026-10/video state-list
"$PY" $SK/render.py serve video                                   # player in a browser, every format
"$PY" $SK/render.py storyboard video --fmt 9x16 --out review/storyboard-9x16-r1.png
"$PY" $SK/render.py sheet video --fmt 4x5 --every 0.5 --out review/sheet-4x5.png
"$PY" $SK/render.py video video --fmt 9x16,4x5,1x1 --out finals --name client-topic-15s-draft1 [--music track.m4a --music-gain 0.2] [--stem chime.mp3@11.2:0.9]
"$PY" $SK/review.py finals/client-topic-15s-draft1-9x16.mp4 --out review/round-1-9x16 --film video --fmt 9x16
uv run $SK/beats.py music.m4a --out video/beats.json --js video/beatmap.js
"$PY" $SK/capture.py video/states.json video/states
"$PY" $SK/reference.py reference.mp4 review/reference
"$PY" $SK/mix.py --picture picture.mp4 --fx sfx.wav --out final.mp4 --target -14
```

- `render.py video` encodes at CRF 15 and mixes to -14 LUFS integrated. It measures the raw mix, applies one gain, limits at -1.5 dBFS, then re-measures and corrects the gain if the limiter cost loudness. A 15 s film renders in under a minute per format.
- `review.py` also checks determinism (one frame rendered three times across two pages with seeks in between) and the loop (first against last frame), and flags a `uuid` box that could carry Content Credentials.

## Rules

- Logos are the exact files, drawn with `R.image`. Never redraw a logo in code, and never let an image or video model draw a logo or a client's product.
- Every claim, number and label has a source on the client's own pages or documents, named in `brief.md`. Use no invented numbers, ROI, savings or guarantees.
- UI films use only real screenshots captured by `capture.py` (`references/state-list.md`). Never paint, retouch or invent a screen. Cropping and zooming real pixels is fine.
- Never submit a live form, not even as a test. `capture.py` aborts every non-GET request, disables form submission and refuses typing; do not work around it.
- Nothing is sent, posted, attached to an ad or paid for (Higgsfield credits, music licences) without Liam's yes in the conversation.
- Frames are pure functions of `t`. Caching static things is fine; carrying state from frame to frame is not.
- Write in Liam's style on screen and in briefs: plain lines, bullets of complete sentences, no em dashes.

## Traps already hit

- `R.reveal` with `start: 0` shows nothing at 0 s. The first frame is the thumbnail, so the hook starts visible (`start: -5`) or lands by about 0.3 s.
- A looping film needs every spring and caption settled before the last frame. `R.settle` gives the time, and the review's loop check measures it (aim under 2 of 255).
- Screens shown whole in 9:16 make the page's own text unreadable on a phone. Frame the real screen at most of the safe width, crop its height, and pan and zoom between steps.
- Sound onsets under a louder sound are hard to measure. The sync table compares motion starts, not motion peaks, because sounds are scheduled where a move begins.
- A peaky mix (one big impact over quiet effects) loses loudness in the limiter. `mix.py` corrects for it; check the final LUFS in its line.
- Fonts load from `fonts/` as woff2, and renders need no network. Liam's Mac also has system faces such as Avenir Next and Helvetica Neue for drafts.
- zsh prints whole floats as `14.`, so format times with `printf %.3f` in shell loops.

## References

- `references/critic-rubric.md` gives what 4, 6, 8 and 10 look like for each criterion, and how to measure each one. Read it before every critic round.
- `references/state-list.md` covers UI and product films from real screenshots: capture, the morph, the pointer and the loop.
- `references/style-from-reference.md` turns a reference clip into our own `style_guide.md`.
- `references/styles/isometric-pastel.md` and `references/styles/editorial-chart.md` are two looks Liam has used, written out.
- `references/styles/hidden-line-wireframe.md` (the Apivant identity model film) and `references/styles/glassmorphism-ui.md` (the Apivant AI agent access film) are the two Apivant explainer looks, written out the same way.
- `references/clients/apivant.md`, `toolbox.md` and `around-the-house.md` hold brand files, colours, fonts, claims rules, past films and open items. Read the client's file before gate 1.
