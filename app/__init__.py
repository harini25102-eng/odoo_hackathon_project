from flask import Flask

from app.models.user import User
from .extensions import db, login_manager
from .auth import auth_bp
from .main import main_bp
from .vehicles import vehicles as vehicles_blueprint
from .drivers import drivers_bp
from .trips import  trips_bp
from .maintenance import maintenance_bp
from .fuel import fuel_bp
from .expenses import expenses_bp
from .dashboard import dashboard_bp
from .reports import reports_bp

# Application factory

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(vehicles_blueprint, url_prefix='/vehicles')
    app.register_blueprint(drivers_bp, url_prefix='/drivers')
    app.register_blueprint(trips_bp, url_prefix='/trips')
    app.register_blueprint(maintenance_bp, url_prefix='/maintenance')
    app.register_blueprint(fuel_bp, url_prefix='/fuel')
    app.register_blueprint(expenses_bp, url_prefix='/expenses')
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(reports_bp, url_prefix='/reports')

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))