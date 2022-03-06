from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.db.models import Category, User, db
from flask_migrate import Migrate
import os

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    is_prod = os.environ.get('IS_HEROKU', None)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://arcmlpkkktnfui:5170d135b04f8b0e8b0daee17b31e690b1d3e70a9b5f3c0a6df5a68f3a01f083@ec2-35-174-56-18.compute-1.amazonaws.com:5432/d3p2h47beia405'
    if is_prod:
        app.config["DEBUG"] = False
    else:
        app.config["DEBUG"] = True

    # Upload folder
    UPLOAD_FOLDER = 'app/static/upload'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Add Categories
    @app.context_processor
    def utility_processor():
        def c():
            return Category.query.all()
        return dict(categories=c)

    ####### ASSETS ########
    assets = Environment(app)

    bundles = {
        'js': Bundle(
            'js/app.js',
            output='gen/app.js'),
        'adminjs': Bundle(
            'js/app.js',
            'js/customer.js',
            'js/admin.js',
            output='gen/admin.js'),
        'customerjs': Bundle(
            'js/app.js',
            'js/customer.js',
            output='gen/customer.js'),
        'css': Bundle(
            'css/style.css',
            # 'css/themes/tequila.css',
            output='gen/style.css'),

    }

    assets.register(bundles)

    ############# CONFIG #############
    app.config['SECRET_KEY'] = 'FBLA'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    ######### DB #################
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    ############ LOGIN ##############
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    ###########ADDING ROUTES/BLUEPRINTS#############

    # Forms
    from app.routes.forms.auth import auth
    app.register_blueprint(auth)

    # from .forms.shop import shop_f
    # app.register_blueprint(shop_f)

    from app.routes.api.api import api
    app.register_blueprint(api)

    # # Views
    from app.routes.views.main import main
    app.register_blueprint(main)

    from app.routes.shop.shop import shop
    app.register_blueprint(shop)

    # # Admin
    # from .admin.admin import admin
    # app.register_blueprint(admin)

    # # User
    # from .user.customer import customer
    # app.register_blueprint(customer)

    db.app = app
    return app
