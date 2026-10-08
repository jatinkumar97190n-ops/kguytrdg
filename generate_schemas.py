import json
import os

with open('JATIN_SCRIPT_FACTORY/00_MASTER/BOT_REGISTRY.json', 'r') as f:
    registry = json.load(f)

for i in range(1, 21):
    bot_id = f"B{i:02d}"
    bot_dir = f"JATIN_SCRIPT_FACTORY/02_BOTS/{bot_id}"
    bot_info = registry.get(bot_id, {})

    # Generate INPUT schema with better typing
    input_props = {}
    for inp in bot_info.get("inputs", []):
        if inp.endswith("urls") or inp.endswith("id") or inp.endswith("manifest"):
            input_props[inp] = {"type": "string"}
        elif "constraints" in inp or "rules" in inp:
            input_props[inp] = {"type": "object"}
        else:
            input_props[inp] = {"type": ["string", "object", "array"]}

    input_schema = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "schema_version": {"type": "string"},
        "run_id": {"type": "string"},
        "bot_id": {"type": "string", "enum": [bot_id]},
        "payload": {
          "type": "object",
          "properties": input_props,
          "required": list(input_props.keys()) if input_props else []
        }
      },
      "required": ["schema_version", "run_id", "bot_id", "payload"]
    }

    with open(f"{bot_dir}/INPUT.schema.json", "w") as f:
        json.dump(input_schema, f, indent=2)

    # Generate OUTPUT schema
    output_props = {}
    for out in bot_info.get("outputs", []):
        if out.endswith(".json") or out.endswith(".jsonl") or out.endswith(".md"):
            output_props[out] = {"type": "string"}
        else:
            output_props[out] = {"type": ["string", "object", "array"]}

    for key in bot_info.get("output_payload_keys", []):
        output_props[key] = {"type": "string"}

    output_schema = {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "schema_version": {"type": "string"},
        "run_id": {"type": "string"},
        "bot_id": {"type": "string", "enum": [bot_id]},
        "status": {"type": "string", "enum": ["PASS", "REPAIR", "BLOCK", "FAIL"]},
        "payload": {
          "type": "object",
          "properties": output_props,
          "required": list(output_props.keys()) if output_props else []
        }
      },
      "required": ["schema_version", "run_id", "bot_id", "status", "payload"]
    }

    with open(f"{bot_dir}/OUTPUT.schema.json", "w") as f:
        json.dump(output_schema, f, indent=2)

print("Generated schemas with better typing.")
