from fileinput import filename
import os
from unicodedata import name
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from app.db.models import db, User, Product, Order, Club
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_
from flask_login import login_user, login_required, logout_user, current_user

club = Blueprint('club', __name__, url_prefix='/club')


"""
ROUTES

items
    add
    analytics
    reports
orders
    reports
settings
"""

@club.route('/items')
@login_required
def items():
    c = Club.query.filter_by(user_id=current_user.id).first()
    i = Product.query.filter_by(club_id=c.id).all()
    return render_template("club/items.html", i=i)

@club.route('/items/add', methods=['GET', 'POST'])
@login_required
def add_items():
    c = Club.query.filter_by(user_id=current_user.id).first()
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        desc = request.form.get('desc')
        picture = request.files['file']
        stock = request.form.get('stock')
        key_words = request.form.get('key_words')
        categories = request.form.get('categories')

        p = Product.query.filter_by(name=name).first()

        if p: 
            flash('Item already exists!', "Error")
            return redirect(url_for('club.add_items'))

        if picture.filename != '':
            fname = secure_filename(picture.filename)
            ext = os.path.splitext(fname)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], c.name, name + ext[1])
            picture.save(file_path)

        new_item = Product(
            img=file_path.replace("app/static/", ""),
            price=price,
            desc=desc,
            stock=stock,
            key_words=key_words,
            name = name
            )
        # add the new user to the database
        db.session.add(new_item)
        db.session.commit()
        c.products.append(new_item)
        db.session.commit()
        flash("Successfully added item!", "Notification")
        return redirect(url_for('club.items'))
    return render_template("club/add/item.html")

@club.route('/items/reports')
@login_required
def report_items():
    return render_template("club/reports/item.html")

@club.route('/orders')
@login_required
def orders():
    c = Club.query.filter_by(user_id=current_user.id).first()
    o = c.pending_orders
    p = []
    for order in o:
        p.append(order.product)
    return render_template("club/orders.html", o=o)

@club.route('/orders/reports')
@login_required
def report_orders():
    return render_template("club/reports/order.html")

@club.route('/settings')
@login_required
def settings():
    return render_template("club/settings.html")