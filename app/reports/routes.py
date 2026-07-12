from flask import render_template
from . import reports_bp

from app.models.vehicle import Vehicle
from app.models.driver import Driver
from app.models.trip import Trip
from app.models.maintenance import Maintenance
from app.models.fuel import Fuel
from app.models.expense import Expense

from app.extensions import db
from sqlalchemy import func


@reports_bp.route("/")
def reports():

    # Fleet Statistics
    total_vehicles = Vehicle.query.count()
    total_drivers = Driver.query.count()
    total_trips = Trip.query.count()
    maintenance_records = Maintenance.query.count()
    fuel_logs = Fuel.query.count()
    expense_records = Expense.query.count()

    # Cost Statistics
    total_fuel_cost = (
        db.session.query(func.sum(Fuel.cost)).scalar() or 0
    )

    total_expense_cost = (
        db.session.query(func.sum(Expense.cost)).scalar() or 0
    )

    operational_cost = total_fuel_cost + total_expense_cost

    # -----------------------------
    # Chart Data
    # -----------------------------

    expense_chart = [
        total_fuel_cost,
        total_expense_cost
    ]

    fleet_chart = [
        total_vehicles,
        total_drivers,
        total_trips,
        maintenance_records,
        fuel_logs,
        expense_records
    ]

    return render_template(
        "reports/index.html",

        total_vehicles=total_vehicles,
        total_drivers=total_drivers,
        total_trips=total_trips,

        maintenance_records=maintenance_records,
        fuel_logs=fuel_logs,
        expense_records=expense_records,

        total_fuel_cost=total_fuel_cost,
        total_expense_cost=total_expense_cost,
        operational_cost=operational_cost,

        expense_chart=expense_chart,
        fleet_chart=fleet_chart
    )