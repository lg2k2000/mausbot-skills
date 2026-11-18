---
name: style-atlas
description: Pull one animated explainer style prompt from Futurepedia's AI Style Atlas (86 styles, such as Watercolor Wash, Whiteboard Explainer, 1940s Film Noir, 16-Bit Pixel Odyssey, Engineering Blueprint, Synthwave Outrun, Claymation Set and Manim-Style Math) by pressing that style's Copy prompt button in a headless playwright-cli browser, then build Liam's explainer in that style. Use it when Liam names one of these styles, asks for an explainer or animation in the style of something on the Atlas, asks which explainer styles exist, wants a new look for an explainer ad, or says "copy the prompt" for a Style Atlas style. The plugin stores only the style names, and the prompt comes from the site each time.
---

# AI Style Atlas

Futurepedia's AI Style Atlas (https://www.futurepedia.io/resources/ai-style-atlas/view) shows 86 visual styles for animated explainers, each telling the same 15-second story. Each style's Copy prompt button copies a prompt of 75,000 to 105,000 characters: a brief, style rules, a style card and the code of the original explainer. Pasted into Claude with a new topic, it rebuilds that style around the topic.

This plugin keeps only the style names, in `styles.tsv`. `scripts/get_style_prompt.py` opens the Atlas in a headless playwright-cli session named `style-atlas`, presses the chosen style's Copy prompt button, catches the text the button copies, and saves it to `/tmp/style-atlas/`.

## Steps

1. Pick the style. Match Liam's words against `styles.tsv` (number, category, name), or run the script with `--list`. If he describes a mood rather than a name ("something retro", "hand-drawn"), offer three to five styles from the matching categories and let him choose. The Atlas page has a preview video for each style.
2. Pull the prompt:
   ```bash
   python3 ~/.claude/skills/style-atlas/scripts/get_style_prompt.py "Watercolor Wash"
   ```
   A number works too (`15` or `#15`), and so does part of a name when only one style matches. The script prints the saved path, the size and the line where the MY CONTENT section starts. A pull takes about 10 seconds.
3. Read the saved file in full. It runs to 1,000 to 1,400 lines, so read it with `allow_large` or in parts. Expect it to take roughly 20,000 to 26,000 tokens of context; that figure is an estimate from the character count.
4. Put Liam's topic or script into the MY CONTENT section in place of its placeholder text. Then follow the prompt as written: its WHAT TO BUILD, HOW TO STAY IN THE STYLE, STRUCTURE, FLOW BETWEEN BEATS and STYLE CARD sections, and the reference code below them.
5. If Liam would rather run it in claude.ai, add `--clipboard` and tell him to paste it into a new chat. That is how Futurepedia means the button to be used.

For a 9:16 MP4, the iso-explainer-ad skill already renders code-drawn explainers with headless Chromium and ffmpeg, and its look seems to be the Atlas's Isometric Pastel style (#15). Check its scripts before reusing them for another style.

## Rules

- Pull one style per job and use it there. Do not copy pulled prompts into skills, projects, Notion or other permanent files. The prompts belong to Futurepedia ("All rights reserved"), and the file in `/tmp` is a handoff, like the clipboard.
- Keep the `style-atlas` session headless and in memory. It holds no logins, and it closes on its own after an hour without commands.
- Leave the HubSpot cookie banner alone. It sits hidden in the page and does not block the button. If it ever shows, choose Decline all.

## When things go wrong

- "No style matches" or "More than one style matches": the script lists the candidates, so pick one by number.
- "card not found": Futurepedia renamed, renumbered or removed the style. Run the script with `--refresh-index` to rebuild `styles.tsv` from the live page (it reads names only), then pull again.
- A copy of a few characters or none: the site changed how its button copies. Rerun with `--headed`, watch the window and see what the button does now.
- A blank page or a bot check: rerun with `--headed`.
