from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.fuel import Fuel  # Import the Fuel model
from app.models.vehicle import Vehicle  # Import the Vehicle model
from app.extensions import db  # Import the database instance
from datetime import datetime  # Import datetime for date handling

# Import the existing Blueprint object for fuel
from . import fuel_bp

@fuel_bp.route('/', methods=['GET'])
def list_fuel():
    """Display all fuel logs."""
    fuel_logs = Fuel.query.all()  # Query all fuel logs from the database
    return render_template('fuel/list.html', fuel_logs=fuel_logs)  # Render the list of fuel logs

@fuel_bp.route('/add', methods=['GET'])
def add_fuel():
    """Display Add Fuel form."""
    vehicles = Vehicle.query.all()  # Get all vehicles for the dropdown
    return render_template('fuel/add.html', vehicles=vehicles)  # Render the add fuel form

@fuel_bp.route('/add', methods=['POST'])
def create_fuel():
    """Create a new fuel log."""
    vehicle_id = request.form.get('vehicle_id')
    liters = request.form.get('liters', type=float)
    cost = request.form.get('cost', type=float)
    date_str = request.form.get('date')

    # Validate required fields
    if not vehicle_id or liters <= 0 or cost <= 0:
        flash("Vehicle must exist, liters must be greater than zero, and cost must be greater than zero.", 'danger')  # Flash message for validation errors
        return redirect(url_for('fuel.add_fuel'))  # Redirect back to the add fuel form

    # Convert date from string to datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')

    # Create a new fuel instance
    new_fuel = Fuel(
        vehicle_id=vehicle_id,
        liters=liters,
        cost=cost,
        date=date
    )
    db.session.add(new_fuel)  # Add the new fuel log to the session
    db.session.commit()  # Commit the session to save the fuel log
    flash("Fuel log added successfully!", 'success')  # Flash success message
    return redirect(url_for('fuel.list_fuel'))  # Redirect to the list of fuel logs

@fuel_bp.route('/edit/<int:id>', methods=['GET'])
def edit_fuel(id):
    """Display Edit Fuel form."""
    fuel_log = Fuel.query.get_or_404(id)  # Get the fuel log by ID or return 404 if not found
    vehicles = Vehicle.query.all()  # Get all vehicles for the dropdown
    return render_template('fuel/edit.html', fuel_log=fuel_log, vehicles=vehicles)  # Render the edit fuel form

@fuel_bp.route('/edit/<int:id>', methods=['POST'])
def update_fuel(id):
    """Update fuel log."""
    fuel_log = Fuel.query.get_or_404(id)  # Get the fuel log by ID or return 404 if not found

    # Update fuel fields from the form
    fuel_log.vehicle_id = request.form.get('vehicle_id')
    fuel_log.liters = request.form.get('liters', type=float)
    fuel_log.cost = request.form.get('cost', type=float)
    date_str = request.form.get('date')

    # Convert date from string to datetime object
    fuel_log.date = datetime.strptime(date_str, '%Y-%m-%d')

    # Validate required fields
    if not fuel_log.vehicle_id or fuel_log.liters <= 0 or fuel_log.cost <= 0:
        flash("Vehicle must exist, liters must be greater than zero, and cost must be greater than zero.", 'danger')  # Flash message for validation errors
        return redirect(url_for('fuel.edit_fuel', id=id))  # Redirect back to the edit fuel form

    db.session.commit()  # Commit the session to save the updates
    flash("Fuel log updated successfully!", 'success')  # Flash success message
    return redirect(url_for('fuel.list_fuel'))  # Redirect to the list of fuel logs

@fuel_bp.route('/delete/<int:id>', methods=['POST'])
def delete_fuel(id):
    """Delete fuel log."""
    fuel_log = Fuel.query.get_or_404(id)  # Get the fuel log by ID or return 404 if not found
    db.session.delete(fuel_log)  # Delete the fuel log from the session
    db.session.commit()  # Commit the session to save the deletion
    flash("Fuel log deleted successfully!", 'success')  # Flash success message
    return redirect(url_for('fuel.list_fuel'))  # Redirect to the list of fuel logs