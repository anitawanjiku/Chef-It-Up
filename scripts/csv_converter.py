import csv
import json
import ast
import random



# Define our file paths
csv_file_path = 'RAW_recipes.csv'
json_file_path = 'recipes_data.json'

TARGET_RECIPES = 500     # change this to get more or fewer recipes
TOTAL_ROWS = 231637      # about how many recipes are in the CSV

random.seed(42)          # everyone gets the same recipes
keep_chance = TARGET_RECIPES / TOTAL_ROWS

# Read CSV and convert rows into a list of dictionaries
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    # DictReader treats the first line as dictionary keys
    csv_reader = csv.DictReader(csv_file)
    
    data = []
    for row in csv_reader:
        if row['tags']:
            row['tag']=ast.literal_eval(row['tags'])
        data.append(row)
    
    for row in csv_reader:
        if row['ingredients']:
            row['ingredients']=ast.literal_eval(row['ingredients'])
        data.append(row)

    for row in csv_reader:
        if row['steps']:
            row['steps']=ast.literal_eval(row['steps'])
        data.append(row)
    


# Write the dictionaries into a formatted JSON file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)