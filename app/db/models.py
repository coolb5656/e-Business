from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    pwd = db.Column(db.String(100))
    profile_pic = db.Column(db.String(80), default="/placeholder/profile.jpg")
    address = db.Column(db.String(80), unique=True)
    phonenum = db.Column(db.String(80), unique=True)
    role = db.Column(db.String(100))
    
    club = db.relationship('Club', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

product_orders = db.Table(
    "product_orders",
    db.Column('id', db.Integer()),
    db.Column('product_id', db.ForeignKey('products.id'), primary_key=True),
    db.Column('order_id', db.ForeignKey('orders.id'), primary_key=True),
)

product_category = db.Table(
    "product_category",
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True),
)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000))
    price = db.Column(db.String(1000))
    desc = db.Column(db.String(1000))
    img = db.Column(db.String(1000), default="/placeholder/item.jpg")
    stock = db.Column(db.String(1000))
    key_words = db.Column(db.String(1000))
    sales = db.Column(db.Integer)
    
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"))
    categories = db.relationship("Category", secondary=product_category, backref="products")

    def __repr__(self):
        return '<Product %r>' % self.name

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    products = db.relationship("Product", secondary=product_orders, backref="orders")

    def __repr__(self):
        return '<Order %r>' % self.id

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000))

    def __repr__(self):
        return '<Category %r>' % self.name

class Club(db.Model):
    __tablename__ = 'clubs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000))
    desc = db.Column(db.String(1000))
    img = db.Column(db.String(1000), default="/placeholder/club.jpg")
    key_words = db.Column(db.String(1000))
    phonenum = db.Column(db.String(80), unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    products = db.relationship('Product', backref='club', lazy=True)

    def __repr__(self):
        return '<Club %r>' % self.name
