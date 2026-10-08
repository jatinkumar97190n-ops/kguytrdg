# JATIN — 20-Bot Script Intelligence Factory

This is a **source package for Google Jules**, not a completed 20-bot implementation.

## Start in 5 steps
1. Create a **private** GitHub repository (e.g. `JATIN-20-BOT-FACTORY`) with a README.
2. Extract this ZIP locally; upload **its contents** to the repository, preserving folders (`docs/`, `AGENTS.md`, `JULES_TASK_PROMPT.txt`, etc.). GitHub's web uploader accepts files, not a ZIP that Jules automatically unpacks.
3. Commit the files to the default branch. Keep any secrets, tokens, private creator datasets and passwords OUT of GitHub.
4. In Jules, select that repository, open a new task, paste the entire `JULES_TASK_PROMPT.txt` instruction and submit. Review/approve the execution plan if asked.
5. Later inspect commits/PR, test evidence and `reports/FINAL_STATUS.md`. Merge only after review.

Jules cloud execution can continue after you leave, but it can pause for approval, quota, permission, runtime, or other genuine blockers. It cannot guarantee a full 20-bot production-ready factory in one task.

## Source precedence
- Three PDFs in `docs/` are authoritative **requirements**, not proof of implementation.
- `AGENTS.md` adds operational guardrails and evidence requirements.
- Conflicts: record in `reports/CONFLICTS.md`; don't silently discard requirements.

## Expected final deliverables
`bots/B01` through `bots/B20`, `schemas/`, `tests/`, `chatgpt_project/`, `reports/`, `sources/`, and `dist/` where supported.

ChatGPT Projects can interpret instructions/knowledge files, but merely uploading files does **not** execute Python, shell scripts, or a multi-agent runtime. Verify behavior in ChatGPT separately.
