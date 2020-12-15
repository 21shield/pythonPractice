from flask import Flask

app = Flask(__name__)
# allows acess to the inital route
# decorator below (url)
@app.route("/")
# when a user puts this is the url the following will be ran
def index():
    return "Hello world! This is my first flask app"
@app.route("/about")
def about():
    return "<h1 style = 'color:red'> ABOUT !!! <h1>"
# to run python 
if __name__ == "__main__":
    app.run()


