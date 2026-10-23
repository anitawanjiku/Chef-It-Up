import json
from pathlib import Path
from flask import Flask, render_template
from flask import Flask, jsonify
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

@app.route("/search")
def search_recipes():
    return

@app.route("/recipe/<id>")
def recipe():
    return


# @app.route("/shoutout/<someone>")
# def shoutout(someone):
#     return render_template('shoutout.html', 
#                            page_title = 'Shoutout to {}'.format(someone), 
#                            someone = someone)