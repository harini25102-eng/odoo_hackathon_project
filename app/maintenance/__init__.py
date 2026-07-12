from flask import Blueprint

# Create a blueprint for maintenance

maintenance = Blueprint('maintenance', __name__)

@maintenance.route('/')
def index():
    return 'Maintenance Blueprint Working'