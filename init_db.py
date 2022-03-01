from random import randint
from numpy import insert, product
from app import create_app
from werkzeug.security import generate_password_hash
from app.db.models import db, User, Product, Order, Category
import os

def insert_dummy_data():
    p = []
    b = []
    s = []
    o = []
    c = [Category(name="Clothing, Shoes, & Jewelry"),
         Category(name="Tech"),
         Category(name="Food"),
         Category(name="Home"),
         Category(name="Toys, Kids, & Baby"),
         Category(name="Outdoors"),
         Category(name="Beauty & Health"),
         ]
    db.session.add_all(c)
    db.session.commit()
    for i in range(9):
        product = Product(
            name="Product " + str(i),
            price = "5.00",
            desc="A Dummy Product",
            stock = "TEST",
            key_words="test dummy product " + str(i) 
        )

        product.categories.append(c[randint(0, 3)])

        buyer = User(
            email="buyer" + str(i) + "@buyer.com",
            username="buyer" + str(i),
            pwd=generate_password_hash("1234", method='sha256'),
            address="buyer" + str(i),
            role="buyer",
            phonenum="b"+str(i)
            )

        seller = User(
            email="seller" + str(i) + "@seller.com",
            username="seller" + str(i),
            pwd=generate_password_hash("1234", method='sha256'),
            address="seller" + str(i),
            role="seller",
            phonenum="s"+str(i)
            )


        p.append(product)
        b.append(buyer)
        s.append(seller)

    db.session.add_all(p + b + s)
    db.session.commit()
    
    for i in range(5):
        order = Order(user_id = b[randint(0, 8)].id)
        order.products.append(p[0])

        o.append(order)

    db.session.add_all(o)
    db.session.commit()

    


        


os.remove("app/db.sqlite")
app = create_app()

with app.app_context():
    db.create_all()
    if(app.config["DEBUG"]):
        insert_dummy_data()


