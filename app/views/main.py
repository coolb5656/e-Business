from fileinput import filename
import os
from unicodedata import name
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from ..db.models import db, User, Product, Order
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_
from flask_login import login_user, login_required, logout_user

main = Blueprint('main', __name__)


"""
ROUTES
index


"""

@main.route('/main')
def index():
    return render_template("main/index.html")