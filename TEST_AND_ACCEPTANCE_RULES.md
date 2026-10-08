# Acceptance and testing rules

## Per-bot gate
- Folder and bot instructions exist and are non-empty.
- Input/output schemas are valid and example fixtures validate.
- Invalid input produces a safe, predictable failure.
- Prompt/agent outputs are checked against schemas.
- Dependencies and next-bot handoff are tested.
- A bot cannot be marked LIVE_PASS unless a real authorized invocation was executed and recorded.

## End-to-end gates
1. New creator intake -> source ingestion -> DNA profile.
2. Research with source provenance, fact verification, originality guard.
3. Topic/angle/hook -> script -> speakability -> critic -> final QA.
4. Repeat creator request reuses validated DNA, without inventing facts.
5. Interrupted run resumes from durable checkpoint without duplicate destructive actions.
6. Mock and real execution evidence are separately tabulated.

## Required status report
For each B01..B20: CREATED / SCHEMA / UNIT / MOCK / LIVE / INTEGRATION / BLOCKERS / EVIDENCE PATH.

## Test evidence fields
Timestamp, git commit, command, environment, fixture, expected, actual, status, error, repair and retest result.
