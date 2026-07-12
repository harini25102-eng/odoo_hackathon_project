from flask import Blueprint

# Create a single Blueprint object for authentication
auth_bp = Blueprint('auth', __name__)

from . import routes  # Import routes to register them with the blueprint