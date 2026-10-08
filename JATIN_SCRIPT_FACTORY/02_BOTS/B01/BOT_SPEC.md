# B01 - Client Brief & Routing

## Purpose
Execute Client Brief & Routing tasks based on master orchestration.

## Inputs
- raw_request
- client_constraints

## Outputs
- approved_brief.json
- route.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; missing audience/format -> REPAIR.
