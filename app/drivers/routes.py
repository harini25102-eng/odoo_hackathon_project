from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.driver import Driver  # Import the Driver model
from app.extensions import db  # Import the database instance
from datetime import datetime  # Import datetime for date conversion

# Import the existing Blueprint object for drivers
from . import drivers_bp

@drivers_bp.route('/', methods=['GET'])
def list_drivers():
    """Display all drivers."""
    drivers = Driver.query.all()  # Query all drivers from the database
    return render_template('drivers/list.html', drivers=drivers)  # Render the list of drivers

@drivers_bp.route('/add', methods=['GET'])
def add_driver():
    """Display Add Driver form."""
    return render_template('drivers/add.html')  # Render the add driver form

@drivers_bp.route('/add', methods=['POST'])
def create_driver():
    """Create a new driver."""
    name = request.form.get('name')
    license_number = request.form.get('license_number')
    license_category = request.form.get('license_category')
    license_expiry_date_str = request.form.get('license_expiry_date')
    contact_number = request.form.get('contact_number')
    safety_score = request.form.get('safety_score')
    status = request.form.get('status')

    # Convert license_expiry_date from string to date object
    license_expiry_date = datetime.strptime(license_expiry_date_str, '%Y-%m-%d').date()

    # Validate unique license number
    if Driver.query.filter_by(license_number=license_number).first():
        flash("License number already exists.", 'danger')  # Flash message for duplicate license number
        return redirect(url_for('drivers.add_driver'))  # Redirect back to the add driver form

    # Create a new driver instance
    new_driver = Driver(
        name=name,
        license_number=license_number,
        license_category=license_category,
        license_expiry_date=license_expiry_date,
        contact_number=contact_number,
        safety_score=safety_score,
        status=status
    )
    db.session.add(new_driver)  # Add the new driver to the session
    db.session.commit()  # Commit the session to save the driver
    flash("Driver added successfully!", 'success')  # Flash success message
    return redirect(url_for('drivers.list_drivers'))  # Redirect to the list of drivers

@drivers_bp.route('/edit/<int:id>', methods=['GET'])
def edit_driver(id):
    """Display Edit Driver form."""
    driver = Driver.query.get_or_404(id)  # Get the driver by ID or return 404 if not found
    return render_template('drivers/edit.html', driver=driver)  # Render the edit driver form

@drivers_bp.route('/edit/<int:id>', methods=['POST'])
def update_driver(id):
    """Update driver."""
    driver = Driver.query.get_or_404(id)  # Get the driver by ID or return 404 if not found

    # Update driver fields from the form
    driver.name = request.form.get('name')
    driver.license_number = request.form.get('license_number')
    driver.license_category = request.form.get('license_category')
    license_expiry_date_str = request.form.get('license_expiry_date')
    contact_number = request.form.get('contact_number')
    safety_score = request.form.get('safety_score')
    status = request.form.get('status')

    # Convert license_expiry_date from string to date object
    driver.license_expiry_date = datetime.strptime(license_expiry_date_str, '%Y-%m-%d').date()

    # Validate unique license number
    if Driver.query.filter(Driver.license_number == driver.license_number, Driver.id != id).first():
        flash("License number already exists.", 'danger')  # Flash message for duplicate license number
        return redirect(url_for('drivers.edit_driver', id=id))  # Redirect back to the edit driver form

    # Update other fields
    driver.contact_number = contact_number
    driver.safety_score = safety_score
    driver.status = status

    db.session.commit()  # Commit the session to save the updates
    flash("Driver updated successfully!", 'success')  # Flash success message
    return redirect(url_for('drivers.list_drivers'))  # Redirect to the list of drivers

@drivers_bp.route('/delete/<int:id>', methods=['POST'])
def delete_driver(id):
    """Delete driver."""
    driver = Driver.query.get_or_404(id)  # Get the driver by ID or return 404 if not found
    db.session.delete(driver)  # Delete the driver from the session
    db.session.commit()  # Commit the session to save the deletion
    flash("Driver deleted successfully!", 'success')  # Flash success message
    return redirect(url_for('drivers.list_drivers'))  # Redirect to the list of drivers