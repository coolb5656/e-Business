from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from app.db.models import Club, db, User, Product, Order, Category
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
    views = sales = num_items = 0
    most_popular_ratio = 0
    most_popular = most_sold = most_viewed = Product(name="None Sold Yet", sales=0, views=0)
    for p in club.products:
        views += p.views
        sales += p.sales
        num_items += 1
        if p.sales / p.views > most_popular_ratio:
            most_popular_ratio = p.sales / p.views
            most_popular = p
        if p.views > most_viewed.views:
            most_viewed = p
        if p.sales > most_sold.sales:
            most_sold = p

    stats = {
        "views":views,
        "sales":sales,
        "most_popular":most_popular,
        "most_sold":most_sold,
        "most_viewed":most_viewed,
        "num_items":num_items
    }
    return stats

@student.route("/cart")
@login_required
def cart():
    p = []
    o = Order.query.filter_by(user_id=current_user.id).first()
    total = 0.0
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
        c = Club.query.filter_by(user_id=current_user.id).first()
        stats = generate_stats(c)
        pending_orders = c.pending_orders
        return render_template("student/dashboard.html", s=stats, pending_orders=pending_orders)
    else:
        flash("You must be affiliated with a club!", "Error")
        return redirect(url_for("main.index"))
