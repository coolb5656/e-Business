from fileinput import filename
import os
from unicodedata import name
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from app.db.models import Club, db, User, Product, Order
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, desc
from flask_login import login_user, login_required, logout_user

main = Blueprint('main', __name__)


"""
ROUTES
index


"""

@main.route('/')
def index():
    products = [Product()]
    products = Product.query.order_by(Product.name.desc()).all()
    clubs = Club.query.order_by(Club.name.desc()).all()
    featured = Product.query.order_by(Product.views.desc()).all()
    featured = featured[:5]
    return render_template("main/index.html", products=products, featured=featured, clubs=clubs)