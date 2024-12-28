from flask import Flask
from taipy import Gui

flask_app = Flask(__name__)

@flask_app.route("/home")
def home_page():
    return "Home"

gui = Gui(page="# Taipy application", flask=flask_app)

gui.run()