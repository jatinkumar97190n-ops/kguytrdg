import re
import json

def parse_master_orchestration():
    with open('master_orchestration.txt', 'r') as f:
        content = f.read()

    bots = {}

    bot_blocks = re.split(r'\n.?(B\d{2}) — ([^\n]+)\n', content)

    for i in range(1, len(bot_blocks), 3):
        bot_id = bot_blocks[i]
        name = bot_blocks[i+1]
        body = bot_blocks[i+2]

        # Extract payload structure
        payload_match = re.search(r'"payload":\s*(\{.*?\})', body, re.DOTALL)
        payload = {}
        if payload_match:
            try:
                # Basic cleaning
                p_str = payload_match.group(1).replace('<typed_value>', '"string"').replace('\n', '').replace('\r', '')
                # Find the properties
                props = re.findall(r'"([^"]+)":', p_str)
                payload = {p: "string" for p in props}
            except Exception as e:
                print(f"Error parsing payload for {bot_id}: {e}")

        bots[bot_id] = {
            "name": name.strip(),
            "output_payload_keys": list(payload.keys())
        }

    return bots

def parse_chatgpt_worker():
    with open('chatgpt_worker.txt', 'r') as f:
        content = f.read()

    bots = {}

    # Notice the leading space or form feed
    bot_blocks = re.split(r'\n.?(B\d{2}) — ([^\n]+)\n', content)

    for i in range(1, len(bot_blocks), 3):
        bot_id = bot_blocks[i]
        name = bot_blocks[i+1]
        body = bot_blocks[i+2]

        inputs_match = re.search(r'Inputs:\s*(.*?)\n', body)
        outputs_match = re.search(r'Outputs:\s*(.*?)\n', body)
        tests_match = re.search(r'Individual tests:\s*(.*?)\n', body)

        inputs = [x.strip() for x in inputs_match.group(1).split(',')] if inputs_match else []
        outputs = [x.strip() for x in outputs_match.group(1).split(',')] if outputs_match else []
        tests = tests_match.group(1).strip() if tests_match else ""

        bots[bot_id] = {
            "name": name.strip(),
            "inputs": inputs,
            "outputs": outputs,
            "tests": tests
        }

    return bots

worker_bots = parse_chatgpt_worker()
orchestration_bots = parse_master_orchestration()

combined_bots = {}
for i in range(1, 21):
    bot_id = f"B{i:02d}"
    combined_bots[bot_id] = worker_bots.get(bot_id, {"name": f"Bot {bot_id}", "inputs": [], "outputs": [], "tests": ""})
    if bot_id in orchestration_bots:
        combined_bots[bot_id]["output_payload_keys"] = orchestration_bots[bot_id]["output_payload_keys"]
    else:
        combined_bots[bot_id]["output_payload_keys"] = []

with open('JATIN_SCRIPT_FACTORY/00_MASTER/BOT_REGISTRY.json', 'w') as f:
    json.dump(combined_bots, f, indent=2)

print("Parsed bot requirements and updated BOT_REGISTRY.json")
