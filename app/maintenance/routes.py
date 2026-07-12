from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.maintenance import Maintenance  # Import the Maintenance model
from app.models.vehicle import Vehicle  # Import the Vehicle model
from app.extensions import db  # Import the database instance
from datetime import datetime  # Import datetime for date handling

# Import the existing Blueprint object for maintenance
from . import maintenance_bp

@maintenance_bp.route('/', methods=['GET'])
def list_maintenance():
    """Display all maintenance records."""
    maintenance_records = Maintenance.query.all()  # Query all maintenance records from the database
    return render_template('maintenance/list.html', maintenance_records=maintenance_records)  # Render the list of maintenance records

@maintenance_bp.route('/add', methods=['GET'])
def add_maintenance():
    """Display Add Maintenance form."""
    vehicles = Vehicle.query.all()  # Get all vehicles for the dropdown
    return render_template('maintenance/add.html', vehicles=vehicles)  # Render the add maintenance form

@maintenance_bp.route('/add', methods=['POST'])
def create_maintenance():
    """Create a new maintenance record."""
    vehicle_id = request.form.get('vehicle_id')
    issue_description = request.form.get('issue_description')
    start_date_str = request.form.get('start_date')
    end_date_str = request.form.get('end_date')
    status = request.form.get('status')

    # Validate required fields
    if not vehicle_id or not issue_description or not status:
        flash("Vehicle, issue description, and status are required.", 'danger')  # Flash message for missing fields
        return redirect(url_for('maintenance.add_maintenance'))  # Redirect back to the add maintenance form

    # Convert start_date and end_date from string to datetime object
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None

    # Create a new maintenance instance
    new_maintenance = Maintenance(
        vehicle_id=vehicle_id,
        issue_description=issue_description,
        start_date=start_date,
        end_date=end_date,
        status=status
    )
    db.session.add(new_maintenance)  # Add the new maintenance record to the session

    # Update vehicle status based on maintenance status
    vehicle = Vehicle.query.get(vehicle_id)
    if status == "In Progress":
        vehicle.status = "In Shop"
    elif status == "Completed":
        vehicle.status = "Available"

    db.session.commit()  # Commit the session to save the maintenance record and vehicle status
    flash("Maintenance record added successfully!", 'success')  # Flash success message
    return redirect(url_for('maintenance.list_maintenance'))  # Redirect to the list of maintenance records

@maintenance_bp.route('/edit/<int:id>', methods=['GET'])
def edit_maintenance(id):
    """Display Edit Maintenance form."""
    maintenance_record = Maintenance.query.get_or_404(id)  # Get the maintenance record by ID or return 404 if not found
    vehicles = Vehicle.query.all()  # Get all vehicles for the dropdown
    return render_template('maintenance/edit.html', maintenance_record=maintenance_record, vehicles=vehicles)  # Render the edit maintenance form

@maintenance_bp.route('/edit/<int:id>', methods=['POST'])
def update_maintenance(id):
    """Update maintenance record."""
    maintenance_record = Maintenance.query.get_or_404(id)  # Get the maintenance record by ID or return 404 if not found

    # Update maintenance fields from the form
    maintenance_record.vehicle_id = request.form.get('vehicle_id')
    maintenance_record.issue_description = request.form.get('issue_description')
    start_date_str = request.form.get('start_date')
    end_date_str = request.form.get('end_date')
    maintenance_record.status = request.form.get('status')

    # Convert start_date and end_date from string to datetime object
    maintenance_record.start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    maintenance_record.end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None

    # Validate required fields
    if not maintenance_record.vehicle_id or not maintenance_record.issue_description or not maintenance_record.status:
        flash("Vehicle, issue description, and status are required.", 'danger')  # Flash message for missing fields
        return redirect(url_for('maintenance.edit_maintenance', id=id))  # Redirect back to the edit maintenance form

    # Update vehicle status based on maintenance status
    vehicle = Vehicle.query.get(maintenance_record.vehicle_id)
    if maintenance_record.status == "In Progress":
        vehicle.status = "In Shop"
    elif maintenance_record.status == "Completed":
        vehicle.status = "Available"

    db.session.commit()  # Commit the session to save the updates
    flash("Maintenance record updated successfully!", 'success')  # Flash success message
    return redirect(url_for('maintenance.list_maintenance'))  # Redirect to the list of maintenance records

@maintenance_bp.route('/delete/<int:id>', methods=['POST'])
def delete_maintenance(id):
    """Delete maintenance record."""
    maintenance_record = Maintenance.query.get_or_404(id)  # Get the maintenance record by ID or return 404 if not found
    db.session.delete(maintenance_record)  # Delete the maintenance record from the session
    db.session.commit()  # Commit the session to save the deletion
    flash("Maintenance record deleted successfully!", 'success')  # Flash success message
    return redirect(url_for('maintenance.list_maintenance'))  # Redirect to the list of maintenance records