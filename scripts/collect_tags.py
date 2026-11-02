import json
from pathlib import Path

# Paths are resolved relative to this file, so the script works from any directory.
# Layout: project/
#           app/data/recipes_data.json
#           scripts/collect_tags.py  <-- this file
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "app" / "data" / "recipes_data.json"
OUTPUT_FILE = Path(__file__).resolve().parent / "all_tags.txt"


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        recipes = json.load(f)

    master_tags = []

    for recipe in recipes:
        for tag in recipe.get("tags", []):
            if tag not in master_tags:
                master_tags.append(tag)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for tag in master_tags:
            f.write(tag + "\n")

    print(f"Found {len(master_tags)} unique tags across {len(recipes)} recipes.")
    print(f"Wrote tags to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()