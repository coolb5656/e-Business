from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_

customer = Blueprint('customer', __name__, url_prefix='/customer')


"""
ROUTES

cart
checkout
"""

@customer.route("/cart")
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

@customer.route("/checkout")
@login_required
def checkout():
    o = Order.query.filter_by(user_id=current_user.id).first()
    total=0
    if o:
        p = o.products
        for prod in p:
            total += float(prod.price)
    return render_template("shop/checkout.html", products = p, total=total)