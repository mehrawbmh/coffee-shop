from datetime import datetime

from config import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    total_price = db.Column(db.Integer, nullable=False, default=0)
    total_price_discount = db.Column(db.Integer, nullable=False, default=0)
    estimated_waiting_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_paid = db.Column(db.Boolean, nullable=False, default=False)
    is_finished = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, basket_id):
        self.basket_id = basket_id

    def __str__(self):
        return f"Order | {self.id} : {self.basket_id}"

