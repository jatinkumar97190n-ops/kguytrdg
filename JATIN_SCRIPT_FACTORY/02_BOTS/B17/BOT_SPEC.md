# B17 - Client Acceptance / Final QA

## Purpose
Execute Client Acceptance / Final QA tasks based on master orchestration.

## Inputs
- all audits
- final script
- original brief

## Outputs
- final_decision.json
- final_script.md

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; hard gate fails -> BLOCK.
