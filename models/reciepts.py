from app import db


class Receipts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Integer, nullable=False)
    final_price_discount = db.Column(db.Integer, default=order_price)
    order_list = db.Column(db.ARRAY(db.Integer))

    def __repr__(self):
        return f"receipt id is {self.id} and total price is {self.final_price_discount}"

