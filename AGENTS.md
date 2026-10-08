# Jules / Coding Agent Project Instructions

## Mission
Implement and verify the 20-bot script intelligence factory described by **all three** PDFs under `docs/`. This is a build/test/repair job, not a planning-only job.

## Mandatory operating rules
1. First inventory and read the PDFs. Extract text with available tools; inspect diagrams/tables visually or record a blocker if extraction is incomplete. Produce `reports/REQUIREMENTS_MATRIX.md` mapping each bot to requirements and PDF page references.
2. Inspect current repository state and preserve existing work. Never overwrite unrelated files, credentials, or protected artifacts.
3. Build bots as **B01–B20**, with separate folders, versioned prompts, JSON input/output schemas, fixtures, and tests. Implement in dependency order, which may differ from numeric order; record the DAG.
4. A passing syntax check is not proof of functioning AI behavior. Separate `STATIC_PASS`, `MOCK_PASS`, `INTEGRATION_PASS`, `LIVE_PASS`, `BLOCKED`, `FAIL`, `NOT_RUN`. Never inflate status.
5. Run tests after each bot. On failure, diagnose, repair, rerun and save commands, logs, expected vs actual outputs and code revision. Cap repetitive repair attempts; mark blockers honestly and move to independent tasks.
6. Run integration, negative, security and end-to-end tests, including first-creator onboarding and repeat script using cached creator DNA.
7. GitHub sources referenced by PDFs are **candidates**, not automatically safe or licensed for reuse. Check reachability, license, commit/version, dependency fit, attribution, and risks. Log findings in `sources/SOURCE_AUDIT.md`. If network unavailable, mark UNVERIFIED; do not claim downloaded/reused.
8. Do not use unauthorized private repos, scrape protected content, evade quotas, weaken security, or incur paid API costs. No secret exfiltration, hardcoded API keys, destructive commands or production deployments without explicit permission.
9. Save checkpoints and commit cohesive changes. Do not require approval after each bot; ask only when permission, paid action, sensitive operation, or genuine ambiguity demands it.
10. Final delivery: `reports/FINAL_STATUS.md`, `reports/TEST_EVIDENCE.md`, `reports/BLOCKERS.md`, reproducible test commands, `chatgpt_project/` instructions, and a ZIP in `dist/` if possible.

## Bot registry
B01 Client Brief & Routing; B02 Creator Source Ingestion; B03 Creator DNA/Twin Builder; B04 Creator Evolution Intelligence; B05 Audience + Niche Intelligence; B06 Topic + Packaging Intelligence; B07 Research Planner; B08 Research Intelligence; B09 Research-to-Creator Translator; B10 Angle & Originality Guard; B11 Script Architect; B12 Script Generator; B13 Speakability/Performance; B14 Creator Match + Revision; B15 Fact & Claim Red-Team; B16 Elite Script Critic; B17 Client Acceptance/Final QA; B18 Feedback + Performance Learning; B19 Creator Story & Knowledge Vault; B20 Hook & Opening Lab.

## Implementation standard
- Choose a practical, documented language/runtime after repo inspection; prefer low-resource reproducibility.
- No fake providers or silent fallback to hardcoded answers. A mock must be explicitly labeled.
- Validate schemas, timeouts, error handling, traceability and idempotent recovery.
- Never claim ChatGPT Project has background automation or direct execution capabilities without an actual compatible integration.
