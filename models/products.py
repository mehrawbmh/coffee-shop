from datetime import datetime
from models.category import Category
from config import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    discount = db.Column(db.Integer, default=0)
    img_url = db.Column(db.String(200))

    def __repr__(self):
        return f" id:{self.id} => name {self.name}"

    @staticmethod
    def item_price(item_id: int):
        menu_item = Product.query.filter_by(id=f'{item_id}').first()
        return menu_item.price - menu_item.discount

    @staticmethod
    def add_item(**kwargs):
        new_product = Product(
            name=kwargs['name'],
            category_id=kwargs['category_id'],
            price=kwargs['price'],
            discount=kwargs['discount'],
            img_url=kwargs['img_url'])
        db.session.add(new_product)
        db.session.commit()
        return new_product

