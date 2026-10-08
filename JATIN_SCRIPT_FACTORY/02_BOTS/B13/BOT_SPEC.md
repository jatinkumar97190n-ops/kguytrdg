# B13 - Speakability / Performance

## Purpose
Execute Speakability / Performance tasks based on master orchestration.

## Inputs
- draft_script
- creator_dna

## Outputs
- spoken_script.md
- delivery_notes.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; awkward line -> REPAIR.
