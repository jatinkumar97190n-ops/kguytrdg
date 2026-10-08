import os
import json

bots = [
    ("B01", "Client Brief & Routing"),
    ("B02", "Creator Source Ingestion"),
    ("B03", "Creator DNA / Twin Builder"),
    ("B04", "Creator Evolution Intelligence"),
    ("B05", "Audience & Niche Intelligence"),
    ("B06", "Topic & Packaging Intelligence"),
    ("B07", "Research Planner"),
    ("B08", "Research Intelligence"),
    ("B09", "Research-to-Creator Translator"),
    ("B10", "Angle & Originality Guard"),
    ("B11", "Script Architect"),
    ("B12", "Script Generator"),
    ("B13", "Speakability / Performance"),
    ("B14", "Creator Match & Revision"),
    ("B15", "Fact & Claim Red-Team"),
    ("B16", "Elite Script Critic"),
    ("B17", "Client Acceptance / Final QA"),
    ("B18", "Feedback & Performance Learning"),
    ("B19", "Creator Story & Knowledge Vault"),
    ("B20", "Hook & Opening Lab")
]

for bot_id, name in bots:
    bot_dir = f"JATIN_SCRIPT_FACTORY/02_BOTS/{bot_id}"

    with open(f"{bot_dir}/BOT_SPEC.md", "w") as f:
        f.write(f"# {bot_id} - {name}\n\n## Purpose\n\n...\n")

    with open(f"{bot_dir}/SYSTEM_PROMPT.md", "w") as f:
        f.write(f"You are the {bot_id} bot: {name}. Your job is to process the inputs and return the requested schema.\n")

    with open(f"{bot_dir}/INPUT.schema.json", "w") as f:
        json.dump({"type": "object", "properties": {"schema_version": {"type": "string"}, "bot_id": {"type": "string"}, "payload": {"type": "object"}}, "required": ["schema_version", "bot_id", "payload"]}, f, indent=2)

    with open(f"{bot_dir}/OUTPUT.schema.json", "w") as f:
        json.dump({"type": "object", "properties": {"schema_version": {"type": "string"}, "bot_id": {"type": "string"}, "status": {"type": "string"}, "payload": {"type": "object"}}, "required": ["schema_version", "bot_id", "status", "payload"]}, f, indent=2)

    with open(f"{bot_dir}/EXAMPLES.jsonl", "w") as f:
        f.write(json.dumps({"input": {"schema_version": "1.0", "bot_id": bot_id, "payload": {}}, "output": {"schema_version": "1.0", "bot_id": bot_id, "status": "PASS", "payload": {}}}) + "\n")

    with open(f"{bot_dir}/TEST_CASES.json", "w") as f:
        json.dump([{"name": "Valid schema", "input": {"schema_version": "1.0", "bot_id": bot_id, "payload": {}}, "expected_status": "PASS"}], f, indent=2)

print("Generated dummy files for all bots.")
