from flask import render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models.expense import Expense
from app.models.vehicle import Vehicle
from . import expenses_bp
from datetime import datetime


@expenses_bp.route('/')
def list_expenses():
    expenses = Expense.query.all()
    return render_template(
        'expenses/list.html',
        expenses=expenses
    )


@expenses_bp.route('/add', methods=['GET', 'POST'])
def add_expense():

    if request.method == 'POST':

        expense = Expense(
            vehicle_id=request.form['vehicle_id'],
            expense_type=request.form['expense_type'],
            cost=float(request.form['cost']),
            date=datetime.strptime(
                request.form['date'],
                '%Y-%m-%d'
            ).date()
        )

        db.session.add(expense)
        db.session.commit()

        flash("Expense added successfully.", "success")
        return redirect(url_for('expenses.list_expenses'))

    vehicles = Vehicle.query.all()

    return render_template(
        'expenses/add.html',
        vehicles=vehicles
    )


@expenses_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):

    expense = Expense.query.get_or_404(id)

    if request.method == 'POST':

        expense.vehicle_id = request.form['vehicle_id']
        expense.expense_type = request.form['expense_type']
        expense.cost = float(request.form['cost'])
        expense.date = datetime.strptime(
            request.form['date'],
            '%Y-%m-%d'
        ).date()

        db.session.commit()

        flash("Expense updated successfully.", "success")
        return redirect(url_for('expenses.list_expenses'))

    vehicles = Vehicle.query.all()

    return render_template(
        'expenses/edit.html',
        expense=expense,
        vehicles=vehicles
    )


@expenses_bp.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):

    expense = Expense.query.get_or_404(id)

    db.session.delete(expense)
    db.session.commit()

    flash("Expense deleted successfully.", "success")

    return redirect(url_for('expenses.list_expenses'))