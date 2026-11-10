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

@app.route("/ingredient")
def random_ingredient():
    '''
    This is the ingredient from the home page bottom. We changed it from the json and it is faster.
    '''
    #initialize db
    ciu = sqlite3.connect('data/chefItUp.db')
    cursor = ciu.cursor()
    
    cursor.execute("""select ingredient from ingredients order by random() limit 1""")
    results = cursor.fetchall()

    ciu.commit()
    ciu.close()

    return jsonify({"ingredient": results})
 

@app.route("/search", methods=["POST"])
def search():
    #filter_by = request.form.get("filter-by")
    #is_vegetarian = request.form.get("vegetarian")
    #is_vegan = request.form.get("vegan")
    search_bar = request.form.get("search-bar")


    ciu = sqlite3.connect('data/chefItUp.db')
    cursor = ciu.cursor()
    query = """SELECT name FROM recipe_info WHERE name LIKE '%' || ? || '%' LIMIT 10;"""
    cursor.execute(query, (search_bar,))

    results = [row[0] for row in cursor.fetchall()]
    results_lst = []
    for recipe in results:
        rec_info = {
            "name" : ""
        }
        rec_info["name"] = recipe
        results_lst.append(rec_info)

    ciu.close()

    return render_template('search.html', search_bar=search_bar, results=results_lst)





    # Load json data
    #with open('/app/data/recipes_data.json') as f:
        #recipe_lst = json.load(f)

    #results = []
    #for recipe_dict in recipe_lst:
        # We try to figure out which attribute of the recipe to search.
        #if filter_by != "name":
        #     to_search = ' '.join(recipe_dict[filter_by])
        # else: 
        #     to_search = recipe_dict[filter_by]

        # # We create the list of search terms.
        # search_terms_lst = search_bar.lower().split(' ')
        # for search_bar in search_terms_lst:
        #     # We leave if the element is not found. 
        #     if search_bar not in to_search.lower().split(' '):
        #         break 
        #     else: 
        #         results.append(recipe_dict)
    
    

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
    