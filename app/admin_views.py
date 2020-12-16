from app import app

@app.route("/admin/dashboard")
# when a user puts this is the url the following will be ran
def admin_dashboard():
    return "This is the admin files"
    
@app.route("/admin/profile")
def admin_profile():
    return "<h1 style = 'color:red'> ADMIN PROFILE <h1>"