import json
from pathlib import Path
from flask import Flask, render_template, jsonify, abort, request
import ast

app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")


@app.route("/ingredient")
def random_ingredient():
    try:
        data_path = Path(__file__).resolve().parent.parent / "recipes_data.json"
        with data_path.open(encoding="utf-8") as f:
            recipes = json.load(f)

        first_recipe = recipes[0]
        ingredients = first_recipe['ingredients']

        return jsonify({"ingredient": ingredients[0]})

    except (KeyError, IndexError) as e:
        return jsonify({"error": f"Data issue: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e), "type": type(e).__name__}), 500  # 👈 expose the real error

@app.route("/search", methods=["POST"])
def search_recipes():
    filter_by = request.form.get("filter-by")
    is_vegetarian = request.form.get("vegetarian")
    is_vegan = request.form.get("vegan")
    search_bar = request.form.get("search-bar")

    # Load json data
    all_recipes = [] 
    with open('recipes_data_{}.json') as f:
        recipe_lst = json.load(f)

    all_recipes += recipe_lst

    results = []
    for recipe_dict in all_recipes:
        # We try to figure out which attribute of the recipe to search.
        if filter_by != 'name':
            to_search = ' '.join(recipe_dict[filter_by])
        else: 
            to_search = recipe_dict[filter_by]

        # We create the list of search terms.
        search_terms_lst = search_bar.lower().split(' ')
        for search_term in search_terms_lst:
            # We leave if the element is not found. 
            if search_term not in to_search.lower().split(' '):
                break 
        else: 
            if is_vegetarian or is_vegan:
                results.append(recipe_dict)
    results.sort(key = lambda recipe: recipe, reverse = True)
    
    
    return render_template('search.html', search_bar = search_bar, results = results)




@app.route("/recipe/<int:recipe_index>")
def recipe(recipe_index):
    data_path = Path(__file__).resolve().parent.parent / "recipes_data.json"
    with data_path.open(encoding="utf-8") as f:
        recipes = json.load(f)

    if recipe_index >= len(recipes):
        abort(404)

    return render_template("recipe.html", recipe=recipes[recipe_index])

# @app.route("/shoutout/<someone>")
# def shoutout(someone):
#     return render_template('shoutout.html', 
#                            page_title = 'Shoutout to {}'.format(someone), 
#                            someone = someone)