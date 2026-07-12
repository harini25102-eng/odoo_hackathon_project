from flask import Blueprint

# Create a blueprint for vehicles

vehicles = Blueprint('vehicles', __name__)

@vehicles.route('/')
def index():
    return 'Vehicles Blueprint Working'