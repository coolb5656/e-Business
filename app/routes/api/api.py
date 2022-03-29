import json
from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import Club, Pending_Order, db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_
import pandas as pd

api = Blueprint('api', __name__, url_prefix='/api')


"""
ROUTES
add_to_cart - add to cart
delete_item - delete item from cart
delete_item
checkout
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
    return redirect(url_for("student.cart"))


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


@api.route('/item/delete/<id>')
@login_required
def delete_item(id):
    p = Product.query.filter_by(id=id).first()
    c = Club.query.filter_by(user_id=current_user.id).first()
    if c:
        if p in c.products:
            if p.pending_orders:
                flash("This item has pending orders!", "Error")
                return redirect(url_for("club.items"))
            Product.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("club.items"))


############# APP STUFF ############
class MobileLoggedIn:
    def __init__(self, function):
        self.function = function

    def __call__(self):

        # We can add some code
        # before function call

        self.function()

        # We can also add some code
        # after function call.


@api.route("app/signup")
def app_signup():
    pass


@api.route("app/login", methods=["POST"])
def verify_password():
    username = request.json.get('username')
    password = request.json.get('password')
    token = request.json.get('token')

    user = User.query.filter_by(username=username).first()
    if token:
        user = user.verify_auth_token(token)
        if user:
            return jsonify({"Token": "Sucess"})
    if password:
        if check_password_hash(user.pwd, password):
            return jsonify({"Password": "Sucess"})
    return jsonify({"Login": "Failure"})
