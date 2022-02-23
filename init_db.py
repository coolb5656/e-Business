from numpy import insert
from app import create_app
from app.db.models import db, User, Product, Order
import os

def insert_dummy_data():
    p = []
    for i in range(9):
        p.append(Product(
            name="Product " + str(i),
            price = "5.00",
            desc="A Dummy Product",
            stock = "TEST"
        ))

    db.session.add_all(p)
    db.session.commit()

        


os.remove("app/db.sqlite")
app = create_app()

with app.app_context():
    db.create_all()
    if(app.config["DEBUG"]):
        insert_dummy_data()

