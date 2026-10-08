# B16 - Elite Script Critic

## Purpose
Execute Elite Script Critic tasks based on master orchestration.

## Inputs
- fact-checked script
- retention rubric

## Outputs
- critique.json
- revision_requests.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; weak opening/pacing -> REPAIR.
