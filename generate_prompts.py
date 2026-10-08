import json
import os

with open('JATIN_SCRIPT_FACTORY/00_MASTER/BOT_REGISTRY.json', 'r') as f:
    registry = json.load(f)

for i in range(1, 21):
    bot_id = f"B{i:02d}"
    bot_dir = f"JATIN_SCRIPT_FACTORY/02_BOTS/{bot_id}"
    bot_info = registry.get(bot_id, {"name": f"Bot {bot_id}", "inputs": [], "outputs": [], "tests": ""})

    # Generate BOT_SPEC.md
    with open(f"{bot_dir}/BOT_SPEC.md", "w") as f:
        f.write(f"# {bot_id} - {bot_info['name']}\n\n")
        f.write("## Purpose\n")
        f.write(f"Execute {bot_info['name']} tasks based on master orchestration.\n\n")
        f.write("## Inputs\n")
        for inp in bot_info.get('inputs', []):
            f.write(f"- {inp}\n")
        f.write("\n## Outputs\n")
        for out in bot_info.get('outputs', []):
            f.write(f"- {out}\n")
        for out in bot_info.get('output_payload_keys', []):
            f.write(f"- {out}\n")
        f.write("\n## Test Conditions\n")
        f.write(f"{bot_info.get('tests', 'Standard validation.')}\n")

    # Generate SYSTEM_PROMPT.md
    # Create specific prompts for specific bots
    prompt_text = f"You are {bot_id}: {bot_info['name']}.\n\n"
    if bot_id == "B01":
        prompt_text += "Your objective is to validate the client brief and route it to the appropriate downstream specialists. You must check that raw_request and client_constraints are valid and output approved_brief.json and route.json.\n"
    elif bot_id == "B02":
        prompt_text += "Your objective is to ingest creator sources from URLs, check permissions, and normalize them into normalized_sources.jsonl.\n"
    elif bot_id == "B03":
        prompt_text += "Your objective is to analyze normalized sources and construct a Creator DNA / Twin profile containing tone and cadence.\n"
    else:
        prompt_text += "Your task is to process the provided inputs and generate the correct output according to the JSON schema and the orchestration rules for your capability.\n"

    prompt_text += "You must strictly adhere to the schema and return a valid JSON object wrapped in the envelope schema.\n"
    prompt_text += "Ensure you preserve source traces and do not invent facts.\n"

    with open(f"{bot_dir}/SYSTEM_PROMPT.md", "w") as f:
        f.write(prompt_text)

    # Generate EXAMPLES.jsonl
    # Define sensible defaults for types instead of "sample_value"
    def get_sample(key):
        if key.endswith("id") or key.endswith("url"): return f"sample_{key}_123"
        if key == "status": return "PASS"
        if key.endswith("json") or key.endswith("jsonl") or key.endswith("md"): return f"content_of_{key}"
        return f"sample_{key}"

    input_payload = {k: get_sample(k) for k in bot_info.get('inputs', [])}
    output_payload = {k: get_sample(k) for k in bot_info.get('outputs', []) + bot_info.get('output_payload_keys', [])}

    valid_input = {
        "schema_version": "1.0",
        "run_id": "test_run",
        "bot_id": bot_id,
        "payload": input_payload
    }

    valid_output = {
        "schema_version": "1.0",
        "run_id": "test_run",
        "bot_id": bot_id,
        "status": "PASS",
        "payload": output_payload
    }

    with open(f"{bot_dir}/EXAMPLES.jsonl", "w") as f:
        f.write(json.dumps({"input": valid_input, "output": valid_output}) + "\n")

    # Generate TEST_CASES.json
    test_cases = [
        {
            "name": "Valid Execution",
            "input": valid_input,
            "expected_status": "PASS"
        },
        {
            "name": "Missing Required Field",
            "input": {
                "schema_version": "1.0",
                "run_id": "test_run",
                "bot_id": bot_id,
                "payload": {}
            },
            "expected_status": "FAIL"
        }
    ]
    with open(f"{bot_dir}/TEST_CASES.json", "w") as f:
        json.dump(test_cases, f, indent=2)

print("Regenerated Prompts and Fixtures with better stubs.")
