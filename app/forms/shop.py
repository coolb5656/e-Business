from flask import Blueprint, render_template, redirect, url_for, request, flash
from ..db.models import db, User, Product, Order
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_

shop_f = Blueprint('shop_f', __name__, url_prefix='/shop')


"""
ROUTES
cart - shows cart contents
checkout - handles payment
"""

@shop_f.route("/cart")
def cart():
    
    return render_template("shop/cart.html")
