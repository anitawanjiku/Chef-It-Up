from flask import Flask, render_template
from flask import Flask, jsonify
import csv
import ast

app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")


@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/ingredient")
def random_ingredient():
    try:
        
        with open('recipes_data.json') as f:
            all_recipes = json.load(f)
        for recipe in recipes:

            ingredients = ast.literal_eval(first_recipe['ingredients'])
        return jsonify(ingredients[0])
        #return jsonify({"ingredient": ingredients[0]})
    except Exception as e:
        return jsonify({"error": "Unknown"}), 500

@app.route("/search")
def search_recipes():
    return

# @app.route("/shoutout/<someone>")
# def shoutout(someone):
#     return render_template('shoutout.html', 
#                            page_title = 'Shoutout to {}'.format(someone), 
#                            someone = someone)