# B08 - Research Intelligence

## Purpose
Execute Research Intelligence tasks based on master orchestration.

## Inputs
- research_plan
- trusted source connectors

## Outputs
- research_pack.json
- claim_ledger.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; unsourced claims -> FAIL.
