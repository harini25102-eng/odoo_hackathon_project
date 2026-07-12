from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the user
    email = db.Column(db.String(120), unique=True, nullable=False)  # User's email address
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    role = db.Column(db.String(50), nullable=False)  # User's role

    def __repr__(self):
        return f'<User {self.email}>'