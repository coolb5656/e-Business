from fileinput import filename
import os
from unicodedata import name
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from ..db.models import db, User, Product, Order
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_
from flask_login import login_user, login_required, logout_user

shop_v = Blueprint('shop_v', __name__, url_prefix='/shop')


"""
ROUTES
item
category
search
"""

@shop_v.route('/item/<id>')
def view_item(id):
    p = Product.query.filter_by(id=id).first()
    print(p)
    return render_template("shop/browse_item.html", product=p)