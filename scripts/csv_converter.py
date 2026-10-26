import csv
import json
import ast
import random

csv_file_path = 'RAW_recipes.csv'
json_file_path = 'recipes_data.json'

TARGET_RECIPES = 500
TOTAL_ROWS = 231637

random.seed(42)
keep_chance = TARGET_RECIPES / TOTAL_ROWS

def safe_eval_list(value, fallback=None):
    """Safely parse a string representation of a list."""
    if fallback is None:
        fallback = []
    try:
        result = ast.literal_eval(value)
        return result if isinstance(result, list) else fallback
    except (ValueError, SyntaxError):
        return fallback

def safe_int(value, fallback=None):
    """Safely parse an integer string."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return fallback

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    data = []
    skipped = 0
    number = 0
    for row in csv_reader:
        # Check for truncated/malformed rows — skip them
        steps_raw = row.get('steps', '')
        if steps_raw and not steps_raw.strip().endswith(']'):
            skipped += 1
            continue

        # List fields
        row['tags']        = safe_eval_list(row.get('tags', '[]'))
        row['ingredients'] = safe_eval_list(row.get('ingredients', '[]'))
        row['steps']       = safe_eval_list(row.get('steps', '[]'))
        row['nutrition']   = safe_eval_list(row.get('nutrition', '[]'))

        # Integer fields
        row['minutes']       = safe_int(row.get('minutes'))
        row['n_steps']       = safe_int(row.get('n_steps'))
        row['n_ingredients'] = safe_int(row.get('n_ingredients'))
        row['position'] = number

        data.append(row)

        number += 1

with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Done! Saved {len(data)} recipes to {json_file_path}")
print(f"Skipped {skipped} malformed rows.")