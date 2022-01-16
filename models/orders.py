from datetime import datetime
from models.baskets import Basket
from config import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey(Basket.id))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    total_price = db.Column(db.Integer, nullable=False, default=0)
    total_price_discount = db.Column(db.Integer, nullable=False, default=0)
    estimated_waiting_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_paid = db.Column(db.Boolean, nullable=False, default=False)
    is_finished = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"Order | {self.id} : {self.basket_id}"


def add_order(**kwargs):
    new_order = Order(
        basket_id=kwargs['basket_id'],
        total_price=kwargs['total_price'],
        total_price_discount=kwargs['total_price_discount'],
        is_paid=kwargs['is_paid'],
        is_finished=kwargs['is_finished']
    )
    db.session.add(new_order)
    db.session.commit()
    return 'status:200'
