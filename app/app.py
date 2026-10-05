from flask import Flask, render_template
import csv
import ast

app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")


@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/initial_route")
def initialroute():
    try:
        with open('app/RAW_recipes.csv', 'r') as f:
            reader = csv.DictReader(f)
            first_recipe = next(reader)
            ingredients = ast.literal_eval(first_recipe['ingredients'])
        return jsonify({"ingredient": ingredients[0]})
    except Exception as e:
        return jsonify({"error": "Unknown"}), 500

@app.route("/shoutout/<someone>")
def shoutout(someone):
    return render_template('shoutout.html', 
                           page_title = 'Shoutout to {}'.format(someone), 
                           someone = someone)