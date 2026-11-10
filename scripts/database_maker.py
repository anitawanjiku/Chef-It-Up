import sqlite3
import json

ciu = sqlite3.connect('app/data/chefItUp.db')

cursor = ciu.cursor()

# recipe_info
# Recipe_id | int
# Name | str
# Minutes | int
# Description | str
# N_steps | int
# N_ingredients | int
command1 = """CREATE TABLE IF NOT EXISTS
recipe_info(recipe_id INTEGER, name TEXT, minutes INTEGER, description TEXT, n_steps INTEGER, 
n_ingredients INTEGER)"""

# steps
# Recipe_id | int
# Step_number | int
# Step_text | str
command2 = """CREATE TABLE IF NOT EXISTS
steps(recipe_id INTEGER, step_number INTEGER, step_text TEXT)"""

# ingredients
# Ingredient | str
# Ingredient_id | int
command3 = """CREATE TABLE IF NOT EXISTS
ingredients(ingredient_id INTEGER, ingredient TEXT)"""

# recipe_ingredients
# recipe_id | int
# ingredient_id | int
command4 = """CREATE TABLE IF NOT EXISTS
recipe_ingredients(recipe_id INTEGER, ingredient_id INTEGER)"""

# nutrition
# Recipe_id | int
# Calories | int
# Total Fat | int
# Sugar | int
# Sodium | int
# Protein | int
# Saturated Fat | int
# Carbohydrates | int
command5 = """CREATE TABLE IF NOT EXISTS
nutrition(recipe_id INTEGER, calories INTEGER, total_fat INTEGER, sugar INTEGER, sodium INTEGER, 
protein INTEGER, saturated_fat INTEGER, carbohydrates INTEGER)"""

# recipe_tags
# Recipe_id | int
# Tag | str
# Tag_category | str
command6 = """CREATE TABLE IF NOT EXISTS
recipe_tags(recipe_id INTEGER, tag TEXT, tag_category TEXT)"""

# reviews
# Recipe_id | int
# Review_text | str
# Rating | int
# Review_id | int
# Review_parent | int(default 0 if first review in a thread)
command7 = """CREATE TABLE IF NOT EXISTS
reviews(recipe_id INTEGER, review_text TEXT, rating INTEGER, review_id INTEGER, 
review_parent INTEGER)"""

cursor.execute(command1)
cursor.execute(command2)
cursor.execute(command3)
cursor.execute(command4)
cursor.execute(command5)
cursor.execute(command6)
cursor.execute(command7)

cursor.execute("DELETE FROM ingredients")
cursor.execute("DELETE FROM recipe_ingredients")
cursor.execute("DELETE FROM steps")

with open('app/data/recipes_data.json') as f:
    recipes = json.load(f)

ingredient_count = 0
for recipe in recipes:
    cursor.execute("INSERT OR REPLACE INTO recipe_info VALUES (?, ?, ?, ?, ?, ?)", 
                   (recipe['position'], recipe['name'], recipe['minutes'], recipe['description'], 
                    recipe["n_steps"], recipe['n_ingredients']))

    step_count = 1 
    for step in recipe['steps']:
        cursor.execute("INSERT OR REPLACE INTO steps VALUES (?, ?, ?)", 
                    (recipe['position'], step_count, step))
        step_count += 1

    ingredients = {}
    for ingred in recipe['ingredients']:
        if ingred not in ingredients.keys():
            ingredients[ingred] = ingredient_count
            ingredient_count += 1
        cursor.execute("INSERT OR REPLACE INTO ingredients VALUES (?, ?)", 
                            (ingredients.get(ingred), ingred))
        cursor.execute("INSERT OR REPLACE INTO recipe_ingredients VALUES (?, ?)", 
                            (recipe['position'], ingredients.get(ingred)))

    nutri = recipe['nutrition']
    cursor.execute("INSERT OR REPLACE INTO nutrition VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                       (recipe['position'], nutri[0], nutri[1], nutri[2], nutri[3], nutri[4], nutri[5], 
                        nutri[6]))

    tag_cats = {
        "time" : [],
        "meal_type" : [],
        "dish_type" : [],
        "restriction" : [],
        "occasion" : [],
        "cuisine" : [],
        "nutrition" : [],
        "other" : []
    }

    with open('scripts/used_tags.txt') as f:
        for line in f:
            tag, category = line.split(",")
            tag_cats[category.strip().lower()].append(tag.strip().lower())

    for tag in recipe['tags']:
        for cat in tag_cats:
            if tag in tag_cats[cat]:
                cursor.execute("INSERT OR REPLACE INTO recipe_tags VALUES (?, ?, ?)", 
                                    (recipe['position'], tag, cat))

ciu.commit()
ciu.close()