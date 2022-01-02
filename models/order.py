from app import db


class Order(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    number = db.Column('number', db.INTEGER, default=1)
    timestamp = db.Column('timestamp', db.TIMESTAMP)
    status = db.Column('status', db.String(40))
    table = db.Column('table', db.Integer(), db.ForeignKey('table.id'), nullable=False)
    menu_item = db.Column('item', db.String(30), db.ForeignKey('menu_item.id'), nullable=False)

    def __str__(self):
        return f"Order: id>{self.id} | item>{self.menu_item} | table number>{self.table}"
