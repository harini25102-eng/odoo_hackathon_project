from app.extensions import db

class Driver(db.Model):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the driver
    name = db.Column(db.String(100), nullable=False)  # Driver's name
    license_number = db.Column(db.String(50), unique=True, nullable=False)  # Driver's license number
    license_category = db.Column(db.String(50), nullable=False)  # Category of the driver's license
    license_expiry_date = db.Column(db.Date, nullable=False)  # Expiry date of the license
    contact_number = db.Column(db.String(15), nullable=False)  # Driver's contact number
    safety_score = db.Column(db.Float, nullable=False)  # Driver's safety score
    status = db.Column(db.String(50), nullable=False, default="Available")  # Current status of the driver

    # Relationships
    trips = db.relationship('Trip', back_populates='driver', cascade="all, delete-orphan")  # Relationship to Trip

    def __repr__(self):
        return f'<Driver {self.name}>'