from flask import Blueprint

# Create a blueprint for trips

trips = Blueprint('trips', __name__)

@trips.route('/')
def index():
    return 'Trips Blueprint Working'