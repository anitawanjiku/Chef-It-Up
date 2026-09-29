from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")


@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/initial_route")
def initialroute():
    with open('app/RAW_recipes.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        # Access the 5th row (index 4)
        target_row = rows[0]
        print(target_row)

    title = target_row[0]
    
    return title