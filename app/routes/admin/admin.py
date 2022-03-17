from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_

admin = Blueprint('admin', __name__, url_prefix='/admin')


"""
ROUTES
dashboard
items
    add
    analytics
    reports
orders
    reports
clubs
    add
    analytics
    reports
settings
"""

@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template("admin/dashboard.html")

@admin.route('/items')
@login_required
def items():
    return render_template("admin/dashboard.html")

@admin.route('/items/add')
@login_required
def add_items():
    return render_template("admin/dashboard.html")

@admin.route('/items/analytics')
@login_required
def item_analytics():
    return render_template("admin/dashboard.html")

@admin.route('/items/reports')
@login_required
def report_items():
    return render_template("admin/dashboard.html")

@admin.route('/orders')
@login_required
def orders():
    return render_template("admin/dashboard.html")

@admin.route('/orders/reports')
@login_required
def report_orders():
    return render_template("admin/dashboard.html")

@admin.route('/settings')
@login_required
def settings():
    return render_template("admin/dashboard.html")

@admin.route('/clubs')
@login_required
def clubs():
    return render_template("admin/dashboard.html")

@admin.route('/clubs/add')
@login_required
def add_clubs():
    return render_template("admin/dashboard.html")

@admin.route('/clubs/analytics')
@login_required
def club_analytics():
    return render_template("admin/dashboard.html")

@admin.route('/clubs/reports')
@login_required
def report_clubs():
    return render_template("admin/dashboard.html")