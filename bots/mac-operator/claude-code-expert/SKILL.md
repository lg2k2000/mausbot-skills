---
name: claude-code-expert
description: "Use when planning, briefing, running, debugging or tuning Claude Code, especially headless claude -p jobs on Liam's Mac (flags, permissions, models and effort, usage limits, long renders, skills, hooks, settings)."
---

# Claude Code expert

Source pack (41 sources, Nov 11 2026): `/workspace/research/claude-code-expert-sources-2026-11-11.md`. Official docs live at code.claude.com (index: https://code.claude.com/docs/llms.txt). When this skill and the docs disagree, the docs win; check the [changelog](https://code.claude.com/docs/en/changelog) for version-gated flags.

## 1. Before a job

- `claude --version`; update with `claude update` only with the owner's yes (it counts as installing software). New models can need a newer CLI (an unknown model id prints `unrecognized_model`).
- Verify the model: `claude -p "Reply with only your exact model id." --model <alias-or-id>`. Aliases: `fable`, `opus`, `sonnet`, `haiku`, `opusplan`.
- Check subscription usage headless: `claude -p "/usage" --output-format text`. It shows session (5-hour) %, weekly all-models %, weekly Fable %, the reset times, and what's eating usage. The `total_cost_usd` / session dollar figure is a local estimate, not subscription billing.
- Never trigger a usage reset or buy extra usage unless the owner explicitly says so.

## 2. Headless run recipe

```
cd <job-folder> && env -u ANTHROPIC_API_KEY TMPDIR=$PWD/tmp \
  claude -p "<brief>" --model <model> --effort <low|medium|high|xhigh|max> \
  --allowedTools "Read,Write,Edit,Glob,Grep" --output-format json > run.json
```

- Research jobs that need live web facts may add WebSearch and WebFetch to `--allowedTools` (Liam, Nov 15 2026); never tools that post, send, upload or sign in.
- Unset `ANTHROPIC_API_KEY` so the run bills the subscription, not the API. (`--bare` skips skills, hooks and CLAUDE.md and needs an API key, so don't use it for subscription jobs.)
- Start in the job folder and keep it alive: file tools center on cwd. Use `--add-dir` for read-only extra inputs.
- Prefer `--output-format json` (parse `.result`, `.session_id`, `.permission_denials`) or `stream-json --verbose` for long jobs, and log it to a file in the job folder.
- Resume instead of restarting: `claude -p "continue: <next step>" --resume <session_id>`.
- Branch on the exit code (0 = ok). SIGTERM exits 143 and abandons the turn; prefer SIGINT to stop a stuck run.
- Caps: `--max-turns N`, `--max-budget-usd X` (an estimate, so leave headroom), plus your own wall-clock timeout. macOS has no `timeout`, so background the run and kill it with SIGINT when it's over the cap. `-p` waits up to 10 min for background work (`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`).
- Unattended: `--permission-prompts none` (v2.1.259+) or `--permission-mode dontAsk` makes would-be prompts fail closed instead of hanging.

## 3. Safety

- Permission precedence: deny > ask > allow. Rule syntax puts a space before `*`: `Bash(ffmpeg *)`.
- Allow only the tools the job needs. Add `Bash` only when needed and scope it (`Bash(ffmpeg *)`, `Bash(node *)`, `Bash(npx remotion *)`). Add `Skill` when the brief names skills.
- Never use `--dangerously-skip-permissions` / `bypassPermissions` on a personal machine. Avoid `acceptEdits` when deletes need consent: it auto-approves `rm`, `mv`, `cp` and `sed` in the working dir.
- Block deletes with `--disallowedTools "Bash(rm *)" "Bash(rmdir *)"` and/or a PreToolUse hook (exit 2 blocks even an allow rule). CLAUDE.md text is context, not enforcement.
- `-p` shows no trust dialog and auto-loads `.mcp.json`, hooks and skills from cwd and `~/.claude`, so only run in folders you created. Drop MCP tools with `--disallowedTools "mcp__*"` when they aren't needed (they also cost about 30k tokens per request).
- Don't pipe untrusted web content into a prompt as instructions.

## 4. Models, effort, usage

- Everyday default: Opus 5.5 (`--model claude-opus-5-5`). Use Fable 5.2 (`--model claude-fable-5-2`) only when the owner asks for a deliberate token-burn run; when Fable runs out, fall back to `claude-opus-5-5 --effort high`. Use Sonnet or lower effort for routine encode/scripting steps, or `opusplan`.
- Default effort on current models is `medium`; set `--effort` explicitly. Only `ultrathink` in a prompt is a special keyword; "think hard" is plain text.
- Max plan: one shared pool across claude.ai, Desktop and Code. There's a 5-hour session window (it starts at the first message and resets in full) plus weekly all-models and weekly Fable limits that reset at a fixed time each week.
- To burn usage on purpose: run the most valuable jobs first, use top model plus high effort, make variants, and check `/usage` between jobs. To save usage: start fresh sessions per task, keep CLAUDE.md under ~200 lines, put long procedures in skills, and skip unneeded MCP.

## 5. Long jobs (renders, multi-piece batches)

- Treat a long render as a harness, not one giant prompt. The first pass sets up a shot list, a progress file and an init script. Later `--resume` passes each do one increment and leave a clean state.
- Never mark a shot or piece done without an end-to-end check: ffprobe duration/size/fps, extracted frames or a contact sheet, a loudness check for audio.
- Teach custom tools in the brief with one example invocation (e.g. the exact ffmpeg or render command).
- One Claude job at a time on a shared machine: check `pgrep -fl "claude -p"` before starting.
- **Queues at the usage limit: pause, don't fail (Liam, Nov 11 2026: "the other 12 jobs in line failed at once").** Before each queued job, check `/usage`. If the 5-hour session is at about 90% or more, or a job stops on a usage-limit error, stop the queue: start nothing else, mark the unstarted jobs "paused" (not failed) in the progress file, and keep the interrupted job's `session_id`. Set a resume for the session reset time `/usage` shows, then `--resume` the interrupted job and run the rest in order. If a weekly limit (for example Fable) resets before the session does, tell the owner what will go unused and ask before switching models.

## 6. Writing the brief

State the goal, the inputs (paths), the exact on-screen copy (never let Claude invent copy or facts), specs (size, fps, length, holds, audio target), the skills and repo paths to use, the folder boundary for Bash, the outputs and where they go, and the self-checks to run before finishing.

## 7. Settings and extensions (look up when needed)

- Settings precedence: managed > `--settings` > `.claude/settings.local.json` > `.claude/settings.json` > `~/.claude/settings.json`. Lists merge. Confirm with `/status` or `claude doctor`.
- Skills: `.claude/skills/<name>/SKILL.md`. Subagents: `.claude/agents/`. Hooks: https://code.claude.com/docs/en/hooks. MCP: https://code.claude.com/docs/en/mcp.
- Long-running agent pattern: https://www.anthropic.com/research/effective-harnesses-for-long-running-agents. Original best practices (dated Apr 2025, but the core still holds): https://www.anthropic.com/research/claude-code-best-practices.
