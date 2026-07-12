from flask import render_template, redirect, url_for, flash, request
from app.extensions import db
from app.models.trip import Trip
from app.models.vehicle import Vehicle
from app.models.driver import Driver

from . import trips_bp


@trips_bp.route("/")
def list_trips():
    trips = Trip.query.all()
    return render_template("trips/list.html", trips=trips)


@trips_bp.route("/add", methods=["GET", "POST"])
def add_trip():

    if request.method == "POST":

        vehicle_id = request.form.get("vehicle_id")
        driver_id = request.form.get("driver_id")
        source = request.form.get("source")
        destination = request.form.get("destination")
        cargo_weight = request.form.get("cargo_weight")
        planned_distance = request.form.get("planned_distance")
        status = request.form.get("status")

        vehicle = Vehicle.query.get(vehicle_id)
        driver = Driver.query.get(driver_id)

        # ----------------------------
        # BUSINESS RULE
        # Vehicle must exist
        # ----------------------------
        if not vehicle:
            flash("Selected vehicle not found.", "danger")
            return redirect(url_for("trips.add_trip"))

        # ----------------------------
        # BUSINESS RULE
        # Driver must exist
        # ----------------------------
        if not driver:
            flash("Selected driver not found.", "danger")
            return redirect(url_for("trips.add_trip"))

        # ----------------------------
        # BUSINESS RULE
        # Vehicle cannot exceed load
        # ----------------------------
        if float(cargo_weight) > vehicle.max_load_capacity:
            flash("Cargo exceeds vehicle capacity.", "danger")
            return redirect(url_for("trips.add_trip"))

        trip = Trip(
            source=source,
            destination=destination,
            vehicle_id=vehicle_id,
            driver_id=driver_id,
            cargo_weight=cargo_weight,
            planned_distance=planned_distance,
            status=status
        )

        db.session.add(trip)
        db.session.commit()

        flash("Trip created successfully.", "success")
        return redirect(url_for("trips.list_trips"))

    vehicles = Vehicle.query.all()
    drivers = Driver.query.all()

    return render_template(
        "trips/add.html",
        vehicles=vehicles,
        drivers=drivers
    )


@trips_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_trip(id):

    trip = Trip.query.get_or_404(id)

    if request.method == "POST":

        vehicle_id = request.form.get("vehicle_id")
        driver_id = request.form.get("driver_id")

        vehicle = Vehicle.query.get(vehicle_id)

        if float(request.form.get("cargo_weight")) > vehicle.max_load_capacity:
            flash("Cargo exceeds vehicle capacity.", "danger")
            return redirect(url_for("trips.edit_trip", id=id))

        trip.vehicle_id = vehicle_id
        trip.driver_id = driver_id
        trip.source = request.form.get("source")
        trip.destination = request.form.get("destination")
        trip.cargo_weight = request.form.get("cargo_weight")
        trip.planned_distance = request.form.get("planned_distance")
        trip.status = request.form.get("status")

        db.session.commit()

        flash("Trip updated successfully.", "success")
        return redirect(url_for("trips.list_trips"))

    vehicles = Vehicle.query.all()
    drivers = Driver.query.all()

    return render_template(
        "trips/edit.html",
        trip=trip,
        vehicles=vehicles,
        drivers=drivers
    )


@trips_bp.route("/delete/<int:id>", methods=["POST"])
def delete_trip(id):

    trip = Trip.query.get_or_404(id)

    db.session.delete(trip)
    db.session.commit()

    flash("Trip deleted successfully.", "success")

    return redirect(url_for("trips.list_trips"))