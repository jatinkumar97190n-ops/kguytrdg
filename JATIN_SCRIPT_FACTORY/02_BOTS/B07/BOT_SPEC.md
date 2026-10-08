# B07 - Research Planner

## Purpose
Execute Research Planner tasks based on master orchestration.

## Inputs
- brief
- packaging_contract

## Outputs
- research_plan.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; missing evidence questions -> REPAIR.
