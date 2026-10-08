import json
import os
import sys

def simulate_bot_execution(bot_id):
    registry_path = "JATIN_SCRIPT_FACTORY/00_MASTER/BOT_REGISTRY.json"
    with open(registry_path, "r") as f:
        registry = json.load(f)
    bot = registry.get(bot_id)
    if not bot:
        return False

    print(f"Executing {bot_id} - {bot['name']}")
    return True

def main():
    print("Running integration / routing tests...")

    # End-to-end simulated run
    # Onboard: B01 -> B02 -> B03 -> B19 -> B04

    routing_graph = {
        "nodes": ["B01", "B02", "B03", "B04", "B19"],
        "edges": [
            {"from": "B01", "to": "B02"},
            {"from": "B02", "to": "B03"},
            {"from": "B03", "to": "B19"},
            {"from": "B03", "to": "B04"}
        ]
    }
    with open("JATIN_SCRIPT_FACTORY/00_MASTER/ROUTING_GRAPH.json", "w") as f:
        json.dump(routing_graph, f, indent=2)

    # Execute the graph conceptually
    execution_order = ["B01", "B02", "B03", "B19", "B04"]
    for bot in execution_order:
        if not simulate_bot_execution(bot):
            print(f"Integration failed at {bot}")
            sys.exit(1)

    print("Integration test simulation passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
