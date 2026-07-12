from app.extensions import db

class Fuel(db.Model):
    __tablename__ = 'fuel'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the fuel log
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)  # Associated vehicle
    liters = db.Column(db.Float, nullable=False)  # Amount of fuel in liters
    cost = db.Column(db.Float, nullable=False)  # Cost of the fuel
    date = db.Column(db.Date, nullable=False)  # Date of the fuel log

    vehicle = db.relationship('Vehicle', backref='fuel_logs')  # Relationship to Vehicle

    def __repr__(self):
        return f'<Fuel {self.id}>'