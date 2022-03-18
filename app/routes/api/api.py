from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import Pending_Order, db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_
import pandas as pd

api = Blueprint('api', __name__, url_prefix='/api')


"""
ROUTES
add_to_cart - add to cart
delete_item - delete item from cart
"""


@api.route('/cart/add')
@login_required
def add_to_cart():
    q = request.args.get("item_id")
    p = Product.query.filter_by(id=q).first()
    o = Order.query.filter_by(user_id=current_user.id).first()
    if not o:
        o = Order(
            user_id=current_user.id
        )
        db.session.add(o)
    o.products.append(p)
    db.session.commit()
    return redirect(url_for("main.index"))


@api.route('/cart/delete/<id>')
@login_required
def delete_from_cart(id):
    p = Product.query.filter_by(id=id).first()
    o = Order.query.filter_by(user_id=current_user.id).first()
    if o:
        o.products.remove(p)
    db.session.commit()
    return redirect(url_for("shop.cart"))


@api.route("/checkout", methods=["POST"])
@login_required
def checkout():
    o = Order.query.filter_by(user_id=current_user.id).first()
    for p in o.products:
        new_pending_order = Pending_Order(
            user_id=o.user_id,
            product_id=p.id,
            club_id=p.club.id,
            quantity=1
        )
        p.sales += 1
        db.session.add(new_pending_order)
    db.session.commit()
    flash("Success!", "Notification")
    return redirect(url_for("main.index"))
