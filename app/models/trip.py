from app.extensions import db

class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the trip
    source = db.Column(db.String(100), nullable=False)  # Trip source location
    destination = db.Column(db.String(100), nullable=False)  # Trip destination location
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)  # Associated vehicle
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)  # Associated driver
    cargo_weight = db.Column(db.Float, nullable=False)  # Weight of the cargo
    planned_distance = db.Column(db.Float, nullable=False)  # Planned distance for the trip
    status = db.Column(db.String(50), nullable=False, default="Draft")  # Current status of the trip

    # Relationships
    vehicle = db.relationship('Vehicle', back_populates='trips')  # Relationship to Vehicle
    driver = db.relationship('Driver', back_populates='trips')  # Relationship to Driver

    def __repr__(self):
        return f'<Trip {self.id}>'