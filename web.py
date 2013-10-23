from flask import Flask, render_template, request, session, redirect, url_for
import os
import foodtrucks

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def new_index():
    return render_template("new_index.html")

@app.route("/input")
def input():
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")
    user_location = [latitude, longitude]
    print user_location
    return "this is bull shit"

if __name__ == "__main__":
    if not os.environ.get('HEROKU_POSTGRESQL_VIOLET_URL'):
        app.run(debug=True)