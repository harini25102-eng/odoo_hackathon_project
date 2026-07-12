from flask import Blueprint

# Create a blueprint for fuel

fuel = Blueprint('fuel', __name__)

@fuel.route('/')
def index():
    return 'Fuel Blueprint Working'