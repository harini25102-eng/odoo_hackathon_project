from app.extensions import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the vehicle
    registration_number = db.Column(db.String(50), unique=True, nullable=False)  # Vehicle registration number
    name = db.Column(db.String(100), nullable=False)  # Vehicle name
    vehicle_type = db.Column(db.String(50), nullable=False)  # Type of vehicle
    max_load_capacity = db.Column(db.Float, nullable=False)  # Maximum load capacity
    odometer = db.Column(db.Float, nullable=False)  # Odometer reading
    acquisition_cost = db.Column(db.Float, nullable=False)  # Cost of acquisition
    status = db.Column(db.String(50), nullable=False, default="Available")  # Current status of the vehicle

    # Relationships
    trips = db.relationship('Trip', back_populates='vehicle', cascade="all, delete-orphan")  # Relationship to Trip
    maintenance_logs = db.relationship('Maintenance', back_populates='vehicle', cascade="all, delete-orphan")  # Relationship to Maintenance
    fuel_logs = db.relationship('Fuel', back_populates='vehicle', cascade="all, delete-orphan")  # Relationship to Fuel
    expense_logs = db.relationship('Expense', back_populates='vehicle', cascade="all, delete-orphan")  # Relationship to Expense

    def __repr__(self):
        return f'<Vehicle {self.registration_number}>'