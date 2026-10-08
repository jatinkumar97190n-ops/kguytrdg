# B02 - Creator Source Ingestion

## Purpose
Execute Creator Source Ingestion tasks based on master orchestration.

## Inputs
- creator_urls
- permissions
- source_manifest

## Outputs
- normalized_sources.jsonl
- ingestion_report.json

## Test Conditions
valid fixture -> schema PASS; missing required field -> clear failure; broken URLs/empty transcript -> BLOCKED.
