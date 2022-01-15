from datetime import datetime
from models.products import Product
from models.table import Table
from config import db


class BasketItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    count = db.Column(db.Integer, nullable=False, default=0)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'))


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey(Table.id))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_finished = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, table_id):
        self.table_id = table_id

    def __str__(self):
        return f"Basket | {self.id} : {self.table_id}"
