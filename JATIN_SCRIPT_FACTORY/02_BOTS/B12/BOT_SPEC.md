# B12 - Script Generator

## Purpose
Execute Script Generator tasks based on master orchestration.

## Inputs
- approved architecture
- creator_dna

## Outputs
- draft_script.md
- draft_meta.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; sections missing -> FAIL.
