from flask import Flask, render_template, jsonify, abort, request
import json
import random
import sqlite3

app = Flask(__name__, static_folder="../www/static")

@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
# defining function
  return render_template("404.html")

@app.route("/template")
def home():
    return render_template("template.html")

@app.route("/meals")
def get_meals():
    '''
    This is the meal from the home page bottom. We changed it from the json and it is faster.
    '''
    #initialize db
    ciu = sqlite3.connect('data/chefItUp.db')
    cursor = ciu.cursor()
    
    #query to execute
    cursor.execute("""SELECT recipe_id, name, minutes FROM recipe_info ORDER BY random() LIMIT 3""")

    #select id, name, and minutes to webpage
    rec_info = []
    for row in cursor.fetchall():
        rec_info.append({
            "id": row[0], "name": row[1], "minutes": row[2],
        })

    ciu.close()

    return jsonify(rec_info) 

@app.route("/ingredient")
def random_ingredient():
    '''
    This is the ingredient from the home page bottom. We changed it from the json and it is faster.
    '''
    #initialize db
    ciu = sqlite3.connect('data/chefItUp.db')
    cursor = ciu.cursor()
    
    #query to execute
    cursor.execute("""select ingredient from ingredients order by random() limit 1""")
    results = cursor.fetchall()

    ciu.commit()
    ciu.close()

    return jsonify({"ingredient": results})
 
# Find recipes that match a user's search input
@app.route("/search", methods=["GET"])
def search():
    #TODO implement the filters
    #filter_by = request.args.get("filter-by")
    #is_vegetarian = request.args.get("vegetarian")
    #is_vegan = request.args.get("vegan")

    # Get the search text from the search bar
    search_bar = request.args.get("search-bar", "").strip()

    # Connect to the database
    ciu = sqlite3.connect('data/chefItUp.db')
    cursor = ciu.cursor()

    # Query to execute
    query = """SELECT recipe_id, name, minutes, description FROM recipe_info WHERE name LIKE '%' || ? || '%' LIMIT 10;"""
    cursor.execute(query, (search_bar,))

    # Turn each row into a dict so the template can use names like recipe["name"]
    results_lst = []
    for row in cursor.fetchall():
        rec_info = {
            "id" : row[0], "name" : row[1], "minutes" : row[2], "description" : row[3],
            }
        results_lst.append(rec_info)

    ciu.close()

    # Show the results page; "id" is used to link each result to its recipe page
    return render_template('search.html', search_bar=search_bar, results=results_lst)

@app.route("/recipe/<int:recipe_index>")
def recipe(recipe_index):
    ciu = sqlite3.connect('data/chefItUp.db')
    cursor = ciu.cursor()

    #Get name, description, minutes, n_stps, and n_ingredients
    cursor.execute("""SELECT name, description, minutes, n_steps, n_ingredients 
                      FROM recipe_info WHERE recipe_id = ?""", (recipe_index,))
    main_info = cursor.fetchone()

    #if a recipe doesn't come back, 404 error
    if main_info is None:
        ciu.close()
        abort(404)

    #get ingredients and put them into a list
    cursor.execute("""SELECT ingredient FROM ingredients AS ing 
                      JOIN recipe_ingredients AS recing 
                      ON ing.ingredient_id = recing.ingredient_id 
                      WHERE recing.recipe_id = ?""", (recipe_index,))
    ingred_lst = [row[0] for row in cursor.fetchall()]

    #get steps and put them into a list
    cursor.execute("""SELECT step_text FROM steps 
                      WHERE recipe_id = ? ORDER BY step_number""", (recipe_index,))
    step_lst = [row[0] for row in cursor.fetchall()]

    #get nutrition and put it into a list
    cursor.execute("""SELECT calories, total_fat, sugar, sodium, protein, 
                      saturated_fat, carbohydrates 
                      FROM nutrition WHERE recipe_id = ?""", (recipe_index,))
    nutrit = cursor.fetchone()

    #get tags and put them into a list
    cursor.execute("""SELECT tag FROM recipe_tags
                   WHERE recipe_id = ?""", (recipe_index,))
    tag_lst = [row[0] for row in cursor.fetchall()]

    ciu.close()

    recipe_data = {
        "name": main_info[0],
        "description": main_info[1],
        "minutes": main_info[2],
        "n_steps": main_info[3],
        "n_ingredients": main_info[4],
        "ingredients": ingred_lst,
        "steps": step_lst,
        "nutrition": list(nutrit) if nutrit else [],
        "tags": tag_lst
    }

    return render_template("recipe.html", recipe=recipe_data)
    