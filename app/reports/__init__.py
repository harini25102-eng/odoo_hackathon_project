from flask import Blueprint

# Create a blueprint for reports

reports = Blueprint('reports', __name__)

@reports.route('/')
def index():
    return 'Reports Blueprint Working'