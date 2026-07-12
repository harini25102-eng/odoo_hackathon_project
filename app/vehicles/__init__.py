from flask import Blueprint

# Create the blueprint
vehicles = Blueprint("vehicles", __name__)

# Import routes so Flask registers them
from . import routes