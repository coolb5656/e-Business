from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_

student = Blueprint('student', __name__, url_prefix='/student')


"""
ROUTES

cart
checkout
dashboard
"""

def generate_stats(club):
    stats = {
        "views":1000,
        "sales":500
    }
    return stats

@student.route("/cart")
@login_required
def cart():
    p = []
    o = Order.query.filter_by(user_id=current_user.id).first()
    total = 0
    if o:
        p = o.products
        for prod in p:
            total += float(prod.price)
    return render_template("shop/cart.html", products = p, total=total)

@student.route("/checkout")
@login_required
def checkout():
    o = Order.query.filter_by(user_id=current_user.id).first()
    total=0
    if o:
        p = o.products
        for prod in p:
            total += float(prod.price)
    return render_template("shop/checkout.html", products = p, total=total)

@student.route('/dashboard')
@login_required
def dashboard():
    if(current_user.club):
        c = current_user.club
        stats = generate_stats(c)
        return render_template("student/dashboard.html", s=stats)
    else:
        flash("You must be affiliated with a club!", "Error")
        return redirect(url_for("main.index"))
