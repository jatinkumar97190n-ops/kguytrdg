# B03 - Creator DNA / Twin Builder

## Purpose
Execute Creator DNA / Twin Builder tasks based on master orchestration.

## Inputs
- normalized_sources
- sampling_rules

## Outputs
- creator_dna.json
- evidence_map.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; unsupported trait -> FAIL.
