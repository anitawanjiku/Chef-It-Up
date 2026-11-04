import sqlite3
import json

ciu = sqlite3.connect('app/data/chefItUp.db')

cursor = ciu.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
recipe_info(recipe_id INTEGER PRIMARY KEY, name TEXT, minutes INTEGER, description TEXT, n_steps INTEGER, 
n_ingredients INTEGER)"""

cursor.execute(command1)

with open('app/data/recipes_data.json') as f:
    recipes = json.load(f)

for recipe in recipes:
    cursor.execute("INSERT OR REPLACE INTO recipe_info VALUES (?, ?, ?, ?, ?, ?)", 
                   (recipe['position'], recipe['name'], recipe['minutes'], recipe['description'], 
                    recipe["n_steps"], recipe['n_ingredients']))

cursor.execute("SELECT name FROM recipe_info limit 5")

results = cursor.fetchall()
print(results)

ciu.commit()
ciu.close()