from flask import Blueprint

# Create a blueprint for drivers

drivers = Blueprint('drivers', __name__)

@drivers.route('/')
def index():
    return 'Drivers Blueprint Working'