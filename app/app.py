import json
from pathlib import Path
from flask import Flask, render_template, jsonify, abort, request
import ast
import random

app = Flask(__name__, static_folder="../www/static")


@app.route("/template")
def home():
    return render_template("template.html")

@app.route("/ingredient")
def random_ingredient():
    try:
        # Loads the json file from the data folder. 
        with open('/app/data/recipes_data.json') as f:
            recipes = json.load(f)

        ########################################
        # Ingredient randomizer. 
        recipe = random.choice(recipes)
        ingredients = recipe['ingredients']

        return jsonify({"ingredient": random.choice(ingredients)})

    # Possible errors that may occur. 
    except (KeyError, IndexError) as e:
        return jsonify({"error": f"Data issue: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e), "type": type(e).__name__}), 500  

@app.route("/search", methods=["POST"])
def search():
    filter_by = request.form.get("filter-by")
    #is_vegetarian = request.form.get("vegetarian")
    #is_vegan = request.form.get("vegan")
    search_bar = request.form.get("search-bar")

    # Load json data
    with open('/app/data/recipes_data.json') as f:
        recipe_lst = json.load(f)

    results = []
    for recipe_dict in recipe_lst:
        # We try to figure out which attribute of the recipe to search.
        if filter_by != "name":
            to_search = ' '.join(recipe_dict[filter_by])
        else: 
            to_search = recipe_dict[filter_by]

        # We create the list of search terms.
        search_terms_lst = search_bar.lower().split(' ')
        for search_bar in search_terms_lst:
            # We leave if the element is not found. 
            if search_bar not in to_search.lower().split(' '):
                break 
            else: 
                results.append(recipe_dict)
    
    return render_template('search.html', search_bar=search_bar, results=results)




@app.route("/recipe/<int:recipe_index>")
def recipe(recipe_index):
    with open('/app/data/recipes_data.json') as f:
        recipes = json.load(f)

    # We are checking for possible out of index files. 
    if recipe_index >= len(recipes):
        abort(404)

    return render_template("recipe.html", recipe=recipes[recipe_index])

#################################################
# Exercise in class
#################################################
# @app.route("/shoutout/<someone>")
# def shoutout(someone):
#     return render_template('shoutout.html', 
#                            page_title = 'Shoutout to {}'.format(someone), 
#                            someone = someone)