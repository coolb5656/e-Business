from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_

seller = Blueprint('seller', __name__, url_prefix='/seller')


"""
ROUTES

dashboard
items
    add
    analytics
    reports
orders
    reports
settings
"""

@seller.route('/dashboard')
@login_required
def dashboard():
    return render_template("seller/dashboard.html")

@seller.route('/items')
@login_required
def items():
    return render_template("seller/dashboard.html")

@seller.route('/items/add')
@login_required
def add_items():
    return render_template("seller/dashboard.html")

@seller.route('/items/analytics')
@login_required
def item_analytics():
    return render_template("seller/dashboard.html")

@seller.route('/items/reports')
@login_required
def report_items():
    return render_template("seller/dashboard.html")

@seller.route('/orders')
@login_required
def orders():
    return render_template("seller/dashboard.html")

@seller.route('/orders/reports')
@login_required
def report_orders():
    return render_template("seller/dashboard.html")

@seller.route('/settings')
@login_required
def settings():
    return render_template("seller/dashboard.html")