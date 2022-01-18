from datetime import datetime
from models.baskets import Basket
from config import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey(Basket.id))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    total_price = db.Column(db.Integer, nullable=False)
    total_price_discount = db.Column(db.Integer, nullable=False)
    estimated_waiting_time = db.Column(db.DateTime)
    is_paid = db.Column(db.Boolean, default=False)
    is_finished = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Order | {self.id=} : {self.basket_id=}"

    @staticmethod
    def add_order(**kwargs):
        new_order = Order(
            basket_id=kwargs['basket_id'],
            total_price=kwargs['total_price'],
            total_price_discount=kwargs['total_price_discount']
        )
        db.session.add(new_order)
        db.session.commit()
        return new_order

    def pay(self):
        self.is_paid = True
        db.session.commit()

    def finish(self):
        self.is_finished = True
        db.session.commit()

#db.create_all()