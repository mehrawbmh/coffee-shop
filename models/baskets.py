from datetime import datetime

from config import db


class BasketItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    count = db.Column(db.Integer, nullable=True, default=0)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'))


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True, default=datetime.now)

    def __init__(self, table_id):
        self.table_id = table_id

    def __str__(self):
        return f"Basket | {self.id} : {self.table_id}"
