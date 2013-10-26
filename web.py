from flask import Flask, render_template, request, session, redirect, url_for
import os
import foodtrucks
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def map():
    trucks_json =json.dumps(foodtrucks.get_closest_food_trucks())
    return render_template("map.html", trucks=trucks_json)

if __name__ == "__main__":
    if not os.environ.get('HEROKU_POSTGRESQL_VIOLET_URL'):
        app.run(debug=True)