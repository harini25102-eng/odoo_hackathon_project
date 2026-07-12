from flask import render_template
from flask_login import current_user
from . import main_bp

@main_bp.route("/")
def home():
    return render_template("home.html")