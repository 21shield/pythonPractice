from app import app

@app.route("/")
# when a user puts this is the url the following will be ran
def index():
    return "Hello world! This is my first flask app"
    
@app.route("/about")
def about():
    return "<h1 style = 'color:red'> ABOUT !!! <h1>"