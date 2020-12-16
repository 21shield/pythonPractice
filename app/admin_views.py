from app import app
from flask import render_template

@app.route("/admin/dashboard")
# when a user puts this is the url the following will be ran
def admin_dashboard():
    return render_template("admin/dashboard.html")
    
@app.route("/admin/profile")
def admin_profile():
    return "<h1 style = 'color:red'> ADMIN PROFILE <h1>"