# B05 - Audience & Niche Intelligence

## Purpose
Execute Audience & Niche Intelligence tasks based on master orchestration.

## Inputs
- approved_brief
- audience_evidence

## Outputs
- audience_profile.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; unsupported demographic inference -> flag.
