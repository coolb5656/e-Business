from fileinput import filename
import os
from unicodedata import name
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from app.db.models import db, User, Product, Order, Club
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


"""
ROUTES
login
signup
    club signup
    student signup
dashboard
logout
"""


@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("pwd")

        u = User.query.filter_by(email=email).first()

        if not u or not check_password_hash(u.pwd, password):
            flash("Wrong Email or Password!", "Error")
            return redirect(url_for("auth.login"))

        login_user(u)
        return redirect(url_for('main.index'))

    return render_template('auth/login.html', error=error)


@auth.route('/login-guest', methods=['GET', 'POST'])
def login_guest():
    error = None
    email = "guestClub@guest.com"
    password = "1234"

    u = User.query.filter_by(email=email).first()

    if not u or not check_password_hash(u.pwd, password):
        flash("Wrong Email or Password!", "Error")
        return redirect(url_for("auth.login"))

    login_user(u)
    return redirect(url_for('main.index'))


@auth.route("/signup/student", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        uname = request.form.get('uname')
        email = request.form.get('email')
        password = request.form.get('pwd')
        picture = request.files['file']
        address = request.form.get('address')
        phonenum = request.form.get('phonenum')

        u = User.query.filter_by(email=email).first()

        if u:
            flash('Email address already registered!', "Error")
            return redirect(url_for('auth.signup'))

        if picture.filename != '':
            fname = secure_filename(picture.filename)
            ext = os.path.splitext(fname)
            file_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'], email + ext[1])
            picture.save(file_path)

        new_user = User(
            email=email,
            name=name,
            username=uname,
            pwd=generate_password_hash(password, method='sha256'),
            profile_pic=file_path.replace("app/static/", ""),
            address=address,
            role="student",
            phonenum=phonenum
        )
        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        flash("Successfully signed up! Login now", "Notification")
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html')


@auth.route("/signup/club", methods=["GET", "POST"])
@login_required
def signup_club():
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('desc')
        key_words = request.form.get('keywords')
        logo = request.files['file']
        phonenum = request.form.get('phonenum')

        c = Club.query.filter_by(name=name).first()
        if c:
            flash('Club name already registered!', "Error")
            return redirect(url_for('auth.signup_club'))

        if logo.filename != '':
            fname = secure_filename(logo.filename)
            ext = os.path.splitext(fname)
            file_path = os.path.join(
                current_app.config['UPLOAD_FOLDER'], name + ext[1])
            logo.save(file_path)

        new_club = Club(
            name=name,
            img=file_path.replace("app/static/", ""),
            desc=desc,
            key_words=key_words,
            phonenum=phonenum
        )
        # add the new user to the database
        db.session.add(new_club)
        os.mkdir(os.path.join(current_app.config['UPLOAD_FOLDER'], name))
        db.session.commit()
        current_user.club.append(new_club)
        db.session.commit()
        flash("Successfully signed up!", "Notification")
        return redirect(url_for('student.dashboard'))

    return render_template('auth/club/signup.html')


@auth.route("/dashboard")
@login_required
def auth_dashboard():
    if current_user.role == "student":
        return redirect(url_for("student.dashboard"))
    if current_user.role == "admin":
        return redirect(url_for("admin.dashboard"))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
