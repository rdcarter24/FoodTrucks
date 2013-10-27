from flask import Flask, render_template
import foodtrucks
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def map():
    # call function to scrape website and put in json format
    trucks_json = json.dumps(foodtrucks.get_closest_food_trucks())
    return render_template("map.html", trucks=trucks_json)

if __name__ == "__main__":
    app.run(debug=True)