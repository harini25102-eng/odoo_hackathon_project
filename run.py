from app import create_app
from app.extensions import db  # Import the SQLAlchemy database instance

app = create_app()

# Open an application context to create the database tables
with app.app_context():
    # Create all database tables if they do not exist
    # This is necessary to ensure that the database schema is set up correctly
    # when the application starts, especially during development.
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode