from app import app

from flask import render_template

@app.route("/")
# when a user puts this is the url the following will be ran
def index():
    return render_template("public/index.html")

@app.route("/jinja")

def jinja():
    # python obj that can be then passed as an obj to the given template
    my_name = "Netaly"
    langs = ["Python", "JS", "Bash", "c", "Ruby"]
    friends = {
        "Tom": 24,
        "Amy": 15,
        "All": 26,
    }
    colors = ("red", "green")

    class GitRemote:
        def __init__( self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        
        def pull(self):
            return "Pullin repo {}".format(self.name)
        def clone(self):
            return "Cloning info {}".format(self.url)

    my_remote = GitRemote(
        name = "Flask Jinja",
        description= "Template tutorial",
        url = "https://github.com/21shield"
    )

    def repeat(x, qty):
        ans = x * qty
        return ans


    return render_template("public/jinja.html",
    
    my_name=my_name, langs=langs, 
    
    friends=friends, GitRemote=GitRemote, 
    
    repeat=repeat, my_remote=my_remote
    )

@app.route("/about")
def about():
    return render_template("public/about.html")