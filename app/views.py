from app import app

from flask import render_template

@app.route("/")
# when a user puts this is the url the following will be ran
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "<h1 style = 'color:red'> ABOUT !!! <h1>"