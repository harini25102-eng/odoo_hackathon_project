from flask import Blueprint

fuel_bp = Blueprint("fuel", __name__)

from . import routes