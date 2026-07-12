from app.extensions import db

class Maintenance(db.Model):
    __tablename__ = 'maintenance'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the maintenance record
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)  # Associated vehicle
    issue_description = db.Column(db.String(255), nullable=False)  # Description of the issue
    start_date = db.Column(db.DateTime, nullable=False)  # Start date of maintenance
    end_date = db.Column(db.DateTime, nullable=True)  # End date of maintenance
    status = db.Column(db.String(50), nullable=False)  # Current status of the maintenance

    vehicle = db.relationship('Vehicle', back_populates='maintenance_logs')  # Relationship to Vehicle

    def __repr__(self):
        return f'<Maintenance {self.id}>'