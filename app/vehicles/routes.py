from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.vehicle import Vehicle  # Import the Vehicle model
from app.extensions import db  # Import the database instance

# Import the existing Blueprint object for vehicles
from . import vehicles

@vehicles.route('/', methods=['GET'])
def list_vehicles():
    """Display all vehicles."""
    vehicles = Vehicle.query.all()  # Query all vehicles from the database
    return render_template('vehicles/list.html', vehicles=vehicles)  # Render the list of vehicles

@vehicles.route('/add', methods=['GET'])
def add_vehicle():
    """Display Add Vehicle form."""
    return render_template('vehicles/add.html')  # Render the add vehicle form

@vehicles.route('/add', methods=['POST'])
def create_vehicle():
    """Create a new vehicle."""
    registration_number = request.form.get('registration_number')
    name = request.form.get('name')
    vehicle_type = request.form.get('vehicle_type')
    max_load_capacity = request.form.get('max_load_capacity')
    odometer = request.form.get('odometer')
    acquisition_cost = request.form.get('acquisition_cost')
    status = request.form.get('status')

    # Validate unique registration number
    if Vehicle.query.filter_by(registration_number=registration_number).first():
        flash("Registration Number already exists.", 'danger')  # Flash message for duplicate registration number
        return redirect(url_for('vehicles.add_vehicle'))  # Redirect back to the add vehicle form

    # Validate vehicle status
    allowed_statuses = ['Available', 'On Trip', 'In Shop', 'Retired']
    if status not in allowed_statuses:
        flash("Invalid vehicle status.", "danger")  # Flash message for invalid status
        return redirect(url_for('vehicles.add_vehicle'))  # Redirect back to the add vehicle form

    # Create a new vehicle instance
    new_vehicle = Vehicle(
        registration_number=registration_number,
        name=name,
        vehicle_type=vehicle_type,
        max_load_capacity=max_load_capacity,
        odometer=odometer,
        acquisition_cost=acquisition_cost,
        status=status
    )
    db.session.add(new_vehicle)  # Add the new vehicle to the session
    db.session.commit()  # Commit the session to save the vehicle
    flash("Vehicle added successfully!", 'success')  # Flash success message
    return redirect(url_for('vehicles.list_vehicles'))  # Redirect to the list of vehicles

@vehicles.route('/edit/<int:id>', methods=['GET'])
def edit_vehicle(id):
    """Display Edit Vehicle form."""
    vehicle = Vehicle.query.get_or_404(id)  # Get the vehicle by ID or return 404 if not found
    return render_template('vehicles/edit.html', vehicle=vehicle)  # Render the edit vehicle form

@vehicles.route('/edit/<int:id>', methods=['POST'])
def update_vehicle(id):
    """Update vehicle."""
    vehicle = Vehicle.query.get_or_404(id)  # Get the vehicle by ID or return 404 if not found

    # Update vehicle fields from the form
    vehicle.registration_number = request.form.get('registration_number')
    vehicle.name = request.form.get('name')
    vehicle.vehicle_type = request.form.get('vehicle_type')
    vehicle.max_load_capacity = request.form.get('max_load_capacity')
    vehicle.odometer = request.form.get('odometer')
    vehicle.acquisition_cost = request.form.get('acquisition_cost')
    status = request.form.get('status')

    # Validate unique registration number
    if Vehicle.query.filter(Vehicle.registration_number == vehicle.registration_number, Vehicle.id != id).first():
        flash("Registration Number already exists.", 'danger')  # Flash message for duplicate registration number
        return redirect(url_for('vehicles.edit_vehicle', id=id))  # Redirect back to the edit vehicle form

    # Validate vehicle status
    allowed_statuses = ['Available', 'On Trip', 'In Shop', 'Retired']
    if status not in allowed_statuses:
        flash("Invalid vehicle status.", "danger")  # Flash message for invalid status
        return redirect(url_for('vehicles.edit_vehicle', id=id))  # Redirect back to the edit vehicle form

    # Update the vehicle status
    vehicle.status = status

    db.session.commit()  # Commit the session to save the updates
    flash("Vehicle updated successfully!", 'success')  # Flash success message
    return redirect(url_for('vehicles.list_vehicles'))  # Redirect to the list of vehicles

@vehicles.route('/delete/<int:id>', methods=['POST'])
def delete_vehicle(id):
    """Delete vehicle."""
    vehicle = Vehicle.query.get_or_404(id)  # Get the vehicle by ID or return 404 if not found
    db.session.delete(vehicle)  # Delete the vehicle from the session
    db.session.commit()  # Commit the session to save the deletion
    flash("Vehicle deleted successfully!", 'success')  # Flash success message
    return redirect(url_for('vehicles.list_vehicles'))  # Redirect to the list of vehicles