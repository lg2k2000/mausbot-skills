---
name: logo-motion-ad
description: Make a short 3D motion-graphic video ad in which the buyer's problem (logins, app lists, audit checklists, slipped dates) twirls into the brand's exact logo, a line appears under the logo, and a coded end card carries the offer, with generated sound, in 1:1 and 4:5. Covers the tools checklist, the inputs to gather, the build steps with bundled script templates (Blender, Chromium, ffmpeg, Higgsfield for sound), the checks, what worked, and rules that save time and tokens. Use it whenever Liam asks for a motion graphic, logo animation, 3D or Blender ad, hook-test variants, a re-cut, a longer or shorter version, or this recipe for a new brand or client, including Apivant's logo vortex and mascot videos (references/apivant.md) and the Around The House spec ad for a Toolbox prospect (references/around-the-house.md).
---

# Logo motion ad

A recipe proven on Apivant's ads in October 2026 (`references/apivant.md`) and on a spec ad for Around The House, a home services prospect, with a wide horizontal logo and no ring (`references/around-the-house.md`). It runs on Liam's Mac. Claude Code runs the commands in Bash. From claude.ai, run the same commands on the Mac through Desktop Commander `start_process` (zsh): the claude.ai sandbox has no Blender. There, put renders in `nohup ... &` jobs that write a log and poll the log, because a Desktop Commander call returns after about 60 seconds.

Load launch-motion with this skill for its story, hold and offer rules. By its numbers (about 35% of Reddit plays reach 3 s), the end card below arrives too late to carry the offer alone; propose an offer pill from about 2 s on the next cut.

## What it makes

18 s at 24 fps (432 frames), rendered at 1080 x 1080 and 1080 x 1350.

| Seconds | Beat |
|---|---|
| 0 to 3 | The mess. A readable card fills the first frame (it is the thumbnail), more clutter arrives or pours in, and the camera pulls back. Two hook plates sit on top. |
| 3 to 6.3 | Everything twirls into a vortex on one part of the logo. That part pops out, the rest flips in, and the logo locks. |
| 6.3 to 9.3 | The camera lifts the logo and a line under it flips up, either the tagline or "get help from" plus the proof. |
| 9.3 to 10.2 | One logo part's hole fills with the end card color and grows until the frame is that color. A logo with no ring opens from a polygon instead, such as its house mark (`LOGO_GEOM`). |
| 10.2 to 18 | The coded end card: offer, proof, URL, logos. It is fully built by about 13 s and then holds about 5 s; viewers said 2 s was too short. |

## Tools checklist (install once, check every session)

| Tool | Check | Install | Used for |
|---|---|---|---|
| Blender 4.2 or later (proven on 5.2.2 LTS) | `/Applications/Blender.app/Contents/MacOS/Blender --version` | `brew install --cask blender` | The 3D scene, rendered headless with EEVEE |
| ffmpeg 6 or later (proven on 8.1) | `ffmpeg -version` | `brew install ffmpeg` | Sound, compositing, assembly, checks. Homebrew's build has no `drawtext`, so all text comes from Blender or Chromium. |
| Python venv with Playwright (Chromium), OpenCV, numpy | `.venv/bin/python3 -c "import playwright, cv2, numpy"` | `python3 -m venv .venv && .venv/bin/pip install playwright opencv-python numpy && .venv/bin/playwright install chromium` | End card frames, the over-footage recipe. Use the venv, not the system python3. |
| Higgsfield CLI (optional, sound only) | `higgsfield --version` and `higgsfield account status` | GitHub releases (check the checksum), then `higgsfield auth login` | Sound effects (Mirelo, 0.25 credits a second) and music (Sonilo, 0.94 credits for 15 s) |
| potrace and fontTools (only for new brand assets) | `potrace -v`; `.venv/bin/python3 -c "import fontTools"` | `brew install potrace`; `.venv/bin/pip install fonttools brotli` | `scripts/tools/trace_logo.py` (logo PNG to SVG), `check_trace.py` (the trace against the PNG), `make_fonts.py` (static TTF and woff2 from variable fonts) |

## Inputs checklist (gather before building)

- The logo as an SVG of filled shapes, traced from the exact logo file and compared with it. Never let an image or video model draw or animate the logo; it redraws it.
  - Use the largest transparent PNG the client publishes (the site header logo, the share image) and ask for a master vector.
  - `tools/trace_logo.py SRC.png OUT.svg --colors "#hex1,#hex2"` traces one path per color on the PNG's own pixel grid. `tools/check_trace.py` scores it; expect an overlap above 0.97 per color.
  - Sample each color's exact hex from the PNG's pixels (the most common opaque colors), not from the site's CSS.
- Which logo part is smallest (it pops out of the vortex first) and which is largest (it flips in and locks). The template expects two parts; more parts need a small change where it sorts `parts`. A two-color logo traced by color gives exactly two parts.
- Where the end card opens from: the small part's hole (a ring), or, for a logo without one, a polygon such as a house mark. `trace_logo.py --geom OUT.json --opening "#hex" --inside "#hex"` measures it for `LOGO_GEOM`.
- Colors: each logo part's exact hex, a light background, and the end card color. Check that both lines under the logo read on the background; a light brand color (orange, yellow) needs another color for type.
- The brand font as TTF files named `<Family>-Black.ttf`, `-Bold.ttf` and `-Medium.ttf`, plus woff2 copies for the end card. `tools/make_fonts.py` cuts them from variable fonts, and each weight may come from a different family (display type for Black, interface type for Bold and Medium).
- Copy:
  - two hook lines, about 22 characters each at most;
  - the line under the logo (one to three lines): the client's slogan word for word. If none is stated anywhere, propose a heading from the client's own site and get the person's OK;
  - the end card headline, proof line and URL;
  - any partner logos required for co-branding.
  Check every claim against the client's rules, and take proof only from the client's own site or documents.
- The clutter story: 5 to 8 object types a viewer can read in 3 seconds, with real interface words ("Approve sign-in?", "Not enrolled", "AT RISK").
- A sound plan and a credit budget. Get the person's yes on the quoted cost before generating anything.

## Build steps

1. A new client's work goes in `~/projects/client-marketing-assets/<client-slug>/` (Liam set this up on Oct 17, 2026; its `CLAUDE.md` has the layout and rules). Apivant stays in `~/projects/apivant marketing`. Never write a client's files into another client's folder. Lay it out as `<client>/assets/` (logo files), `<client>/video/` (scripts, fonts, audio) and `<client>/finals/`, with a venv at `<client>/.venv`. Reusable sound takes are in `~/projects/client-marketing-assets/library/sound/`. Copy `scripts/` from this skill into `video/`:
   - `ad_15s.py`, `brand.env`, `test_stills.sh`, `render_all.sh`, `make_mix.sh`, `make_audio.sh`, `assemble_ad.sh`, `check_cut.sh` and `tools/`;
   - `endcard/endcard_ad.html` and `endcard/render_card.py`. Put the woff2 fonts and the white logos next to the HTML.
   - For existing footage, also `over-footage/` (`compose_v2.py`, `render_card_v2.py`, `assemble_v2.sh`) with `endcard/endcard_v2.html` and `endcard/tagline_v2.html`.

   `make_audio.sh` and `assemble_v2.sh` still name Apivant's folders, so set their paths. For Apivant, use the live copies in the project instead (see the reference).
2. Set the brand in `video/brand.env`, which every script sources. The template holds the Around The House values as a worked example; with nothing set, `ad_15s.py` falls back to Apivant's.
   - `LOGO_SVG`, `FONTS_DIR`, `FONT_FAMILY`
   - `COLOR_SMALL`, `COLOR_LARGE`, `BG_COLOR`, `CARD_COLOR`
   - `AD_VARIANT` (picks an entry in `VARIANTS`) and `AD_NAME` (the finals' file names)
   - optional: `LOGO_FIT_W` (cap a wide wordmark's width), `LOGO_GEOM` (open the card from a polygon), `LOGO_SHADOW`, `LINE_W`, `LINE2_COLOR`, `HOOK2_TEXT`
   - `WORD_POPS` and `AUDIO_DIR` (for `make_mix.sh`)
3. Edit `endcard_ad.html` for the brand's copy, colors and logos. For a dark card, the client's icon with a transparent cutout (a share image or favicon source) works where a dark wordmark would vanish.
4. In `ad_15s.py`, add clutter builders: copy an existing one. The parts are `empty`, `slab`, `text`, `disc` and `torus`. Keep the first-frame card about 2.7 x 1.5 units so the hook plates clear its header.
5. Add a `VARIANTS` entry with these keys:
   - `hook`: the two plate lines;
   - `hero`: the first-frame card builder;
   - `early`: the name prefix of two more cards that land beside it;
   - `specs`: the clutter mix, about 30 objects;
   - `under`: the lines under the logo and the frames they flip on;
   - `pour=True` if the screen should fill up from the edges.
6. Take test stills at 540 px, about a minute each: `test_stills.sh OUT "1,30,60,152,200,236" "1,30" [675]` renders the main pass and the hook overlay in parallel and writes one contact sheet with the overlay on top (675 is the 4:5 height). By hand it is
   `AD_VARIANT=x Blender -b -P ad_15s.py -- main OUT 540 540 1,30,60,200`
   and the same with `overlay ... 1,30,60`. For a single still, write `152,`; without the comma, a lone number renders from that frame to the end. Check frame 245's corner color too: it must be exactly the card color.
7. Sound, if new takes are needed: write prompts in `make_audio.sh`, quote with `higgsfield generate cost <model> ...`, get the yes, then run it in the background. Screen the takes (rules below), then build the mix: `DUR=18 WORD_POPS="..." ./make_mix.sh audio/mix.wav`.
8. Steps 8 to 11 run as one background job: `render_all.sh FRAMES_DIR` (about 3 minutes per format on an M-series Mac). By hand, per format:
   - Full renders: `overlay` and `main` at `1080 1080` and `1080 1350`.
9. Render the end card: `.venv/bin/python3 endcard/render_card.py MAIN/ring.json CARD_DIR 186` (186 frames is 7.75 s).
10. Assemble: `DUR=18 ./assemble_ad.sh MAIN OVER CARD MIX OUT.mp4`.
11. Check: `check_cut.sh OUT.mp4 432 <card hex> 245 sheet.png`. Then look at the sheet and one zoomed crop of the line under the logo. Write the copy, its sources, the checks and the rebuild commands into the project's `README.md`.
12. File and log: copy the finals to the client's finished folder, archive what they replace, update the indexes and changelog, and send the 1:1 cut.

## What worked (keep it)

- A buyer situation in the hook, then "get help" from a named, proven company. Liam said the first cuts read like a product, and a services firm has to say it does the work.
- The first frame carries the hook and one readable card, because platforms use it as the thumbnail.
- Hook plates are rendered in their own pass (transparent film, no depth of field) and laid on top. They stay sharp while the scene keeps its depth of field.
- Clutter with real interface text, which reads as "logins and MFA" in 3 seconds. The first test failed because the clutter was not recognizable fast enough.
- The "pour" style, with clutter arriving from the edges until the screen is full. This was Liam's favorite ("overwhelmed").
- Emission shading on the logo's camera-facing faces, so it renders in exact brand colors while its edges stay lit.
- The same hook on two different visuals, so a test compares the pictures and not the copy.
- An end card that holds about 5 s, with the URL pill pulsing again during the hold.
- For a home services brand (Around The House), physical things read instantly: leaves, ladders, icicles on a gutter, a hot sun. A few cards with real words (a buzzing "Clean the gutters" reminder, a "Weekend chores" list, "Freeze warning" alerts) carry the story, and every item maps to something the client installs.
- A hook that sets up the client's name ("So much to do" / "around the house?"), so the logo lands as the punch line.
- Opening the end card from the logo's own mark (Around The House's house outline fills with charcoal and grows) when the logo has no ring.
- Reusing a paid sound library across clients when the person agrees; Around The House used Apivant's takes and spent no new credits.

## Rules that save time and tokens

Blender:
- Never full-render just to look. Test with 540 px stills from a comma list.
- Send Blender's output to a log file and read only `grep -E "Error|Traceback|^info"`. The script prints the numbers it computes (ring position, text size, camera distance), so many checks need no image at all.
- Render in the background and wait for the completion notice. Do not poll with sleep.
- Look at one contact sheet (4 to 6 frames tiled with ffmpeg), not single frames. Zoom only into type, to check for seams.
- Keep render frames in scratch space and reuse them. A change to only the end card, the sound or the length needs no 3D re-render; that saved about 25 minutes on the length change.
- Keep one scene script with variants, not copies of it.

Higgsfield:
- Quote first, get the yes, then generate every take in one background script with `--wait`. That script downloads each file and logs its job ID.
- Make two takes of each sound. About a third came back almost silent, so screen takes by a loudness envelope (`astats` RMS every 0.1 s) and one waveform and spectrogram image. Claude cannot listen.
- Reuse an approved take library across ads, and never regenerate for a re-cut.
- Use the CLI. The claude.ai Higgsfield connector cannot generate or upload. Video models must never animate the logo.

ffmpeg:
- Always use `-v error`. Never print ebur128's per-frame lines (one call flooded the context); use `check_cut.sh` or grep the Summary.
- Place each sound as its own stem trimmed to an exact sample count, then sum the stems. Mixing delayed sounds in one graph misplaced them by about 0.7 s.
- Normalize with one measured gain plus `alimiter`. The dynamic `loudnorm` thinned the last second.

General:
- Write files with the editor tool, run whole pipelines as one script, and chain read-only checks into one command.
- Report only what a check confirmed.

## Traps already hit

- A bevel on Blender text leaves 1 px seams across letters like e and s, so keep `bevel_depth = 0` on type. The color mask uses the Geometry node's True Normal, not Normal, for the same reason.
- Depth of field blurs anything near the lens. Screen text never goes in the main pass.
- `sensor_fit = HORIZONTAL` keeps 1:1 and 4:5 the same width; 4:5 just shows more above and below.
- The growing part must cover the far corner with its hole, not its middle, or its rim shows at the cut. The script computes the needed scale from the camera at the last frame.
- zsh traps:
  - `$2:all` reads as `$2` with the `:a` modifier, so write `${2}`.
  - `$END[m]` is an array subscript, so write `${END}[m]`.
  - A `#` comment after `do` on a one-line loop swallows the loop body.
  - zsh does float math in `$(( ))`, which ffmpeg accepts.
- Text a viewer must read stays at or above about 60 px cap height at 1080 px.
- A wide wordmark casts a large, blurred copy of itself on the back wall that reads as a second logo. `LOGO_SHADOW=0` (the default with `LOGO_GEOM`) turns the logo's and the line's shadows off; the clutter keeps its shadows.
- A wide wordmark sized by height (`LOGO_H`) runs off the frame at the lock, so cap its width with `LOGO_FIT_W` (8.2 units fit at 1:1).
- `LOGO_GEOM` coordinates are the source PNG's pixels, so the SVG must keep the PNG's pixel grid, as `trace_logo.py` writes it.
- zsh does not split a default like `${@:-1x1 4x5}` into two words; the loop saw one format named "1x1 4x5". Use `if (( $# )); then A=("$@"); else A=(1x1 4x5); fi`.
- A background command piped through `sed` reports the pipe's exit code, which hid a failed render job once. Run render jobs unpiped. Piping a step into `head -1` inside a `set -o pipefail` script kills the step with SIGPIPE (exit 141) and stops the job.
- Blender's PNGs carry a pixel density tag that ffmpeg reads as SAR 2834:2834, so concatenating them with frames ffmpeg made fails ("parameters do not match"). Put `setsar=1` on every input before `concat`.

## Over existing footage

`compose_v2.py BODY.mp4 HOOK_DIR OUT_DIR W H` puts footage that is already finished (for example, a generated character clip) on a 1:1 or 4:5 canvas:
- In 1:1 the footage is scaled to 85% and set at the bottom; in 4:5 it is full size, 240 px from the top.
- The edges are feathered into the footage's own background color, measured on every frame.
- It lays the hook overlay frames on top and renders the tagline in Chromium.
- It writes `ring.json` from the logo's measured position, so the end card opens from it.

Pair it with an end card page that opens from that frame, as the Apivant mascot cut does (`references/apivant.md`).

Live-action footage with a voiceover (Apivant's office video v3, Oct 18, 2026) works another way:
- Cut the footage to the voice. Crop it to 4:3, set it full width at the top, and fill the rest with the scene's background color.
- Render the text as Blender plates in their own transparent pass, one plate per spoken line, timed from the voice stem's silence gaps (`silencedetect`). Keep the plates in the color of the hook plates.
- For the logo, render the 3D scene without clutter (`hero=None`, `specs=[]`) from frame 109. A variant with `screen=True` maps the last footage frame (`SCREEN_IMG`) onto a camera-fixed plane that fills the view at frame 108 and twirls into the ring, and the plates twirl in with it. Cut straight from the last footage frame to render frame 109; the render is a little softer than the footage, so a cut on the still frame shows.
- Reuse the end card frames when the ring lands where it did in an earlier cut. Compare `ring.json`.
