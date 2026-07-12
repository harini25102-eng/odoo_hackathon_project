from flask import Flask

from app.models.user import User
from .extensions import db, login_manager
from .auth import auth_bp
from .vehicles import vehicles as vehicles_blueprint
from .drivers import drivers as drivers_blueprint
from .trips import trips as trips_blueprint
from .maintenance import maintenance as maintenance_blueprint
from .fuel import fuel as fuel_blueprint
from .reports import reports as reports_blueprint

# Application factory

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(vehicles_blueprint, url_prefix='/vehicles')
    app.register_blueprint(drivers_blueprint, url_prefix='/drivers')
    app.register_blueprint(trips_blueprint, url_prefix='/trips')
    app.register_blueprint(maintenance_blueprint, url_prefix='/maintenance')
    app.register_blueprint(fuel_blueprint, url_prefix='/fuel')
    app.register_blueprint(reports_blueprint, url_prefix='/reports')

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))