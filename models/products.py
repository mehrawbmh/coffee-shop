from datetime import datetime

from config import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    discount = db.Column(db.Integer)
    img_url = db.Column(db.String(200))

    def __repr__(self):
        return f" id:{self.id} => name {self.name}"

    @staticmethod
    def item_price(item_id: int):
        menu_item = Product.query.filter_by(id=f'{item_id}').first()
        return menu_item.price
