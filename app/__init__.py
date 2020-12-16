# used to bring your application together
from flask import Flask
# exports the app here to app in the root file
app = Flask(__name__)
# these are the files available in rendering
from app import views 
from app import admin_views