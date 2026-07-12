from flask import render_template
from . import dashboard_bp

from app.models.vehicle import Vehicle
from app.models.driver import Driver
from app.models.trip import Trip
from app.models.maintenance import Maintenance
from app.models.fuel import Fuel
from app.models.expense import Expense


@dashboard_bp.route("/")
def dashboard():

    total_vehicles = Vehicle.query.count()

    total_drivers = Driver.query.count()

    total_trips = Trip.query.count()

    total_maintenance = Maintenance.query.count()

    total_fuel_logs = Fuel.query.count()

    total_expenses = Expense.query.count()

    vehicles_in_shop = Vehicle.query.filter_by(
        status="In Shop"
    ).count()

    available_vehicles = Vehicle.query.filter_by(
        status="Available"
    ).count()

    recent_trips = Trip.query.order_by(
        Trip.id.desc()
    ).limit(5).all()

    return render_template(

        "dashboard/index.html",

        total_vehicles=total_vehicles,
        total_drivers=total_drivers,
        total_trips=total_trips,
        total_maintenance=total_maintenance,
        total_fuel_logs=total_fuel_logs,
        total_expenses=total_expenses,
        vehicles_in_shop=vehicles_in_shop,
        available_vehicles=available_vehicles,
        recent_trips=recent_trips

    )