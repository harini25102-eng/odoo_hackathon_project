from app.extensions import db

class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the expense
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)  # Associated vehicle
    expense_type = db.Column(db.String(50), nullable=False)  # Type of expense
    cost = db.Column(db.Float, nullable=False)  # Cost of the expense
    date = db.Column(db.Date, nullable=False)  # Date of the expense

    vehicle = db.relationship('Vehicle', back_populates='expense_logs')  # Relationship to Vehicle

    def __repr__(self):
        return f'<Expense {self.id}>'