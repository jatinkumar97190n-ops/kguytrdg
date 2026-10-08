# B15 - Fact & Claim Red-Team

## Purpose
Execute Fact & Claim Red-Team tasks based on master orchestration.

## Inputs
- matched_script
- claim_ledger
- sources

## Outputs
- fact_audit.json
- corrected_script.md

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; unsupported certainty -> BLOCK.
