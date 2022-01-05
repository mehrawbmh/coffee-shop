from config import db

class MenuItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    discount = db.Column(db.Integer)
    img_url = db.Column(db.String(200))

    def __repr__(self):
        return f" id:{self.id} => name {self.name}"

    @staticmethod
    def item_price(item_id:int):
        menu_item = MenuItems.query.filter_by(id=f'{item_id}').first()
        return menu_item.price
