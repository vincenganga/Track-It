from application import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm
from application.models import IncomeExpenses
import json


@app.route("/")
def index():
    """Display history of the user"""
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template('index.html', entries = entries)


@app.route("/add", methods=["GET", "POST"])
def add_expense():
    """User to fill in the form"""
    form = UserInputForm()

    # Ensure form is valid
    if form.validate_on_submit():
        # Create an instance
        entry = IncomeExpenses(type = form.type.data, amount = form.amount.data, category = form.category.data)

        # Enter the data into the database and commit it
        db.session.add(entry)
        db.session.commit()

        # Inform the user for successful entry 
        flash("Successful", 'success')

        # Redirect user to homepage
        return redirect(url_for('index'))
    
    # If it was not successful redirect the user to fill in the form
    return render_template("add.html", form = form)


@app.route("/delete/<int:entry_id>")
def delete(entry_id):
    """User can delete an entry from history"""
    # Instead of returning an error if element not found, return a 404 
    # Prevents web from crushing
    entry = IncomeExpenses.query.get_or_404(int(entry_id))

    # Delete entry and commit
    db.session.delete(entry)
    db.session.commit()

    # Inform the user about deletion
    flash("Deleted", 'success')

    # Redirect user to homepage
    return redirect(url_for('index'))


@app.route('/dashboard')
def dashboard():
    """Show the user data by charts"""

    # Get data from the database
    income_vs_expense = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.type).group_by(IncomeExpenses.type).order_by(IncomeExpenses.type).all()

    income_expense = []
    for total_amount, _ in income_vs_expense:
        income_expense.append(total_amount)

    # Convert Python objects to JSON strings
    income_vs_expense_data = json.dumps(income_expense)

    return render_template('dashboard.html',
                            income_vs_expense = income_vs_expense_data,
                            )
