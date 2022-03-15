import numpy as np
from functools import total_ordering
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_

shop = Blueprint('shop', __name__, url_prefix='/shop')


"""
ROUTES
item
category
search
"""


@shop.route('/item/<id>')
def view_item(id):
    p = Product.query.filter_by(id=id).first()
    return render_template("shop/browse_item.html", product=p)

@shop.route('/category/<id>')
def search_category(id):
    c = Category.query.filter_by(id=id).first()
    print(c)
    p = c.products
    return render_template("shop/browse_items.html", products=p, title=c.name)

@shop.route('/search')
def search():
    q = request.args.get("search")
    n = Product.query.filter(Product.name.like('%' + q + '%')).all()
    k = Product.query.filter(Product.key_words.like('%' + q + '%')).all()
    p = list(set(n + k))
    return render_template("shop/browse_items.html", products=p, title="Showing results for: " + q)