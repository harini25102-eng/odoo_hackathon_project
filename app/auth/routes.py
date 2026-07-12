from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.extensions import db

# Import the Blueprint object
from . import auth_bp

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        role = request.form.get('role')

        # Validate input fields
        if not email:
            flash('Email is required.', 'danger')
        elif not password:
            flash('Password is required.', 'danger')
        elif password != confirm_password:
            flash('Passwords must match.', 'danger')
        elif role not in ['Fleet Manager', 'Driver', 'Safety Officer', 'Financial Analyst']:
            flash('Invalid role selected.', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('Email already exists. Please choose a different one.', 'danger')
        else:
            # Create new user
            new_user = User(
                email=email,
                password_hash=generate_password_hash(password),
                role=role
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate input fields
        if not email:
            flash('Email is required.', 'danger')
        elif not password:
            flash('Password is required.', 'danger')
        else:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard.dashboard'))  # Redirect to dashboard
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))