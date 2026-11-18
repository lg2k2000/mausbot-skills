---
name: launch-motion
description: Story, timing and motion rules for Liam's short video ads drawn in code, specialized on Oct 23, 2026 from a launch-video skill Liam saved. Hook, problem, fix, payoff; every key moment held at least 1.5 s; the offer on screen from about 2 s; the brand named inside the fix; nothing ever fully still; one timeline per cut for 15 s and full cuts in 4:5 and 16:9; sound on every move; and a pre-render checklist. Use it together with motion-reel (or logo-motion-ad) whenever Liam asks for an explainer, a video ad, a storyboard, a cutdown, a 15-second version, a re-cut or a pacing fix, or says a video feels slow, rushed, static, cluttered or hard to read, and before any video ad goes to Liam, a client or an ad account. Apivant's story map and a worked example are in references/apivant.md.
---

# Launch motion

- This skill decides what the film says, in what order, how long each moment stays and how things move. motion-reel (Canvas 2D, a pure `seek(t)` page, Playwright and ffmpeg) or logo-motion-ad (Blender 3D) draws and renders it. Load both.
- It began as a launch-video skill Liam saved to his Google Drive on Oct 23, 2026 (the files name no author). The untouched original, written for Remotion at 60 fps, is in `references/original/` for reference. The rules below are rewritten for our tools and our ads, with what the Apivant agent access explainer taught on Oct 22 and 23, 2026.
- Our films render at 30 fps, so one frame is about 33 ms. Times below are in seconds, with frames at 30 fps where it helps.

## The story: hook, problem, fix, payoff

- Every ad follows one path. The hook stops the scroll, the problem shows a state the viewer recognizes, the fix shows what changes and who does it, and the payoff gives the takeaway and the offer. Cut any beat that serves none of these. In a 15 s cut, also cut the beats that only deepen the problem.
- The hook is on screen on frame 0, because the first frame is the thumbnail and most plays end within 3 s. Make it a question or a business initiative the buyer owns, in about 8 words or fewer.
- Show the problem as a visible state, not a claim: "Owner: none", "Nobody knows.", a red count. Viewers believe what they see change on screen.
- Name the brand inside the fix, not only on the end card, so a viewer who leaves at 8 s knows who fixes this. Use an approved line word for word.
- The payoff is a takeaway line, then the end card with the offer, the credential, the URL and the exact logo files.

## The offer is on screen early

- On Apivant's Reddit video ads from Oct 10 to Oct 22, 2026, about 35% of plays reached 3 s and about 3% finished (18 s videos). An offer that first appears on the end card reaches almost nobody.
- Put the offer on a small pill by about 2 s and keep it there until the end card takes over. Give the pill its own band (4:5 along the bottom, 16:9 top right) so nothing else ever sits in it.

## Timing

- Hold every key moment at least 1.5 s (45 frames): the hook at full size, a key number, a key UI state, the takeaway. Measure from when it lands (settled and readable) to when the next camera move starts or it starts to leave. A camera move that starts early cuts the hold even if the element stays partly in frame.
- Count-ups run about 1 s with an ease-out and tick at most 12 times a second. Never jump to the final value in one frame.
- Hold the finished end card 2.5 to 3 s with the URL readable.
- Let the beats set the length. Write the beat table first (`references/storyboard-template.md`), check every hold, then add up the total. Do not squeeze beats to reach a round number; the agent explainer grew from 26 s to 29 s to meet its holds.

## Motion

- Nothing moves linearly. Entrances take about 0.5 s with a slight overshoot (motion-reel `R.spring(t, 'pop')` or an outBack ease). Exits take about 60% of the entrance with an ease-in.
- Move groups, not pieces: animate the panel with its rows as one. Inside a group, start each element 2 to 4 frames after the one before (0.07 to 0.13 s). Start the next move during the last fifth of the one before it.
- Camera moves ease in and out. A move across the full frame takes at least 0.8 s.
- Nothing fully stops. Every hold pushes in about 2% (camera zoom times 1.02 across the hold), the end card included, and decorative shapes may drift a few pixels.
- Overlays that float over the scene (a header, the offer pill, the brand line, a toast, the takeaway) never cross text while the camera moves. Fade them out before the move starts and bring them back after it settles.
- A click gets a small press (scale 1 to 0.96 to 1 over about 8 frames). A pointer travels on a gentle arc, eases in and out, and settles with a tiny overshoot.

## Cuts and formats

- Keep every cut's times in one object (`CUTS = { long: {...}, short: {...} }`), with camera keyframes per cut and per format, and choose the cut with one switch (`window.FILM_CUT`). A beat a cut leaves out sits past the end (`NEVER = 999`) and the score skips it. Revisions then stay one-line changes, and the score can never drift from the picture.
- Make the full cut (every beat, often 25 to 30 s) and a 15 s cut: hook, problem, fix and end card, plus a short takeaway when the holds leave room for it (the agent explainer's 15 s cut keeps one from 9.75 to 11.75 s). Make 4:5 first (1080 x 1350, the Reddit and LinkedIn feeds), then 16:9. Each format gets its own layout and camera; never crop one format out of another.
- Keep text at motion-reel's floors: in 4:5, labels at least 37 px, headlines 92 px and key numbers 140 px. `phone-360.png` from motion-reel's review is the test.

## Sound

- Every camera move and every landing gets a sound onset within 3 frames. A soft airy glide does not register as an onset on its own, so start each move on a low tap and let the glide follow.
- The biggest hit sits on the main moment (the number, the turn, the answer turning green) and is the loudest half second by at least 0.5 dB, with a short gap before it. Keep the end card chord under it.
- Mix to -14 LUFS integrated with the true peak at -1 dBTP or lower (motion-reel `mix.py`, ceiling -3.5 dBFS).

## Pre-render checklist

- [ ] The beat table shows every key moment held 1.5 s or more, in every cut.
- [ ] The hook reads on frame 0, and the offer pill is up by about 2 s.
- [ ] The brand is named inside the fix with an approved line.
- [ ] Stills at every beat boundary and in the middle of every camera move, in every cut and format, show no overlapping text and no text cut off at a frame edge.
- [ ] Every hold pushes in, and no frame sits fully still for more than about 0.5 s.
- [ ] Counters tick over about 1 s, and repeated items stagger in.
- [ ] Fonts load before frame 0 (no fallback face anywhere), and logos are the exact files.
- [ ] Determinism passes, and the MP4 has no uuid box.
- [ ] motion-reel's review report shows -14 ± 1 LUFS, a true peak of -1 dBTP or lower, the hit as the loudest half second, and an onset within 3 frames of every motion start.

## Revisions

- Change the smallest thing that answers the note, keep everything else, and re-render. With every time in the cut objects and every line of copy in constants at the top of the film, a client note is a one-line change.
- When only the sound changes, re-mix without re-rendering frames (the agent explainer's `render_video.py` takes `SOUND_ONLY=1`).

## References

- `references/apivant.md` holds Apivant's story map (hooks James accepts, the approved fix line, the end card), the attention numbers and the agent access explainer as a worked example with its times and the mistakes it fixed.
- `references/storyboard-template.md` is the beat table with the hold check, filled in for the 15 s agent explainer.
- `references/original/` is the original launch-motion as saved from Liam's Drive: Remotion, 60 fps, 1920 x 1080, with its brief, storyboard and Upwork pitch templates. Read it only when Liam asks about the original.
- motion-reel's `references/clients/apivant.md` holds Apivant's brand files, colours, wording and claims rules.
