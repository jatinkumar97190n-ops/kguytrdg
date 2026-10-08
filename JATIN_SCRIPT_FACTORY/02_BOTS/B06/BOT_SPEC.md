# B06 - Topic & Packaging Intelligence

## Purpose
Execute Topic & Packaging Intelligence tasks based on master orchestration.

## Inputs
- brief
- audience_profile
- topic

## Outputs
- packaging_contract.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; promise/title mismatch -> REPAIR.
