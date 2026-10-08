# B09 - Research-to-Creator Translator

## Purpose
Execute Research-to-Creator Translator tasks based on master orchestration.

## Inputs
- research_pack
- creator_dna

## Outputs
- creator_insight_pack.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; invented creator story -> FAIL.
