import json
import jsonschema
import glob
import os
import sys

def main():
    bot_dirs = glob.glob("JATIN_SCRIPT_FACTORY/02_BOTS/B*")
    bot_dirs.sort()

    all_passed = True

    for bot_dir in bot_dirs:
        bot_id = os.path.basename(bot_dir)
        print(f"Testing {bot_id}...")

        # Load schemas
        try:
            with open(f"{bot_dir}/INPUT.schema.json", "r") as f:
                input_schema = json.load(f)
            with open(f"{bot_dir}/OUTPUT.schema.json", "r") as f:
                output_schema = json.load(f)
        except Exception as e:
            print(f"  [ERROR] Failed to load schemas for {bot_id}: {e}")
            all_passed = False
            continue

        # Load EXAMPLES
        try:
            with open(f"{bot_dir}/EXAMPLES.jsonl", "r") as f:
                for line_idx, line in enumerate(f):
                    if not line.strip(): continue
                    example = json.loads(line)

                    try:
                        jsonschema.validate(instance=example["input"], schema=input_schema)
                        print(f"  [OK] Example {line_idx} Input Valid")
                    except jsonschema.exceptions.ValidationError as e:
                        print(f"  [ERROR] Example {line_idx} Input Validation Failed: {e.message}")
                        all_passed = False

                    try:
                        jsonschema.validate(instance=example["output"], schema=output_schema)
                        print(f"  [OK] Example {line_idx} Output Valid")
                    except jsonschema.exceptions.ValidationError as e:
                        print(f"  [ERROR] Example {line_idx} Output Validation Failed: {e.message}")
                        all_passed = False
        except Exception as e:
            print(f"  [ERROR] Failed to test examples for {bot_id}: {e}")
            all_passed = False

    if all_passed:
        print("\nAll contract tests passed!")
        sys.exit(0)
    else:
        print("\nSome contract tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
