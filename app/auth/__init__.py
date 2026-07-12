from flask import Blueprint

# Create a blueprint for auth

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return 'Auth Blueprint Working'