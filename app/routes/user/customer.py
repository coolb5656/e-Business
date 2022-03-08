from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_

customer = Blueprint('customer', __name__, url_prefix='/customer')


"""
ROUTES

dashboard
orders
settings
"""

@customer.route('/dashboard')
@login_required
def dashboard():
    return render_template("customer/dashboard.html")

@customer.route('/orders')
@login_required
def orders():
    return render_template("customer/dashboard.html")

@customer.route('/settings')
@login_required
def settings():
    return render_template("customer/dashboard.html")