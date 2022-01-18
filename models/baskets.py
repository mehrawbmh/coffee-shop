"""
When a customer clicks to finalize their order, a basket will create first. then every order will be set in a basket item
In other words, every basket could have one or more basket item.
 in final step, the order and receipt will be created and just waiting to serve...
"""

from datetime import datetime
from models.products import Product
from models.table import Table
from config import db


class BasketItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    count = db.Column(db.Integer, default=1)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'), nullable=False)

    def __init__(self, product_id, basket_id, count=None):
        self.product_id = product_id
        self.count = count
        self.basket_id = basket_id

    def total_price(self):
        product = Product.query.get(self.product_id)
        return product.price * self.count

    def total_price_with_discount(self):
        product = Product.query.get(self.product_id)
        return (product.price - product.discount) * self.count

    def __repr__(self):
        return f"BasketItem  {self.id} | related to basket with {self.basket_id=}"


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey(Table.id))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    is_finished = db.Column(db.Boolean, default=False)

    def __init__(self, table_id, created_at=None, updated_at=None, is_finished=None):
        self.table_id = table_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_finished = is_finished

    @classmethod
    def make_new(cls, table_id):
        now = datetime.now()
        new_obj = cls(table_id, now, now)
        db.session.add(new_obj)
        db.session.commit()
        return new_obj

    def finish(self):
        self.is_finished = False
        db.session.commit()

    def __repr__(self):
        return f"Basket | {self.id} : {self.table_id}"
