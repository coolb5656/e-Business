import json
from unicodedata import category
from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import Club, Pending_Order, db, User, Product, Order, Category
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, or_

from app.routes.shop.shop import search

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
            return jsonify({"Login": "Sucess", "Token": token})
    if password:
        if check_password_hash(user.pwd, password):
            token = user.generate_auth_token(expiration=0)
            return jsonify({"Login": "Sucess", "Token": token.decode("utf-8")})
    return jsonify({"Login": "Failure"})


@api.route("app/main")
def app_main():
    category = request.json.get('category')
    club = request.json.get('club')
    search = request.json.get('search')
    p = Product.query.order_by(Product.name.desc()).all()
    if category:
        c = Category.query.filter_by(id=category).first()
        p = c.products
    if club:
        c = Club.query.filter_by(id=club).first()
        p = c.products
    if search:
        n = Product.query.filter(Product.name.like('%' + search + '%')).all()
        k = Product.query.filter(
            Product.key_words.like('%' + search + '%')).all()
        p = list(set(n + k))

    products = []
    for item in p:
        products.append(item.as_dict())
    return products
