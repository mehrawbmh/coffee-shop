# from config import db
# from models.menu_items import MenuItems
#
# class Order(db.Model):
#     """
#     Order status can be one of these modes:
#     -submitted
#     -cooking
#     -serving
#     -paid
#     -canceled
#
#     """
#     id = db.Column('id', db.Integer, primary_key=True)
#     number = db.Column('number', db.INTEGER, default=1)
#     timestamp = db.Column('timestamp', db.TIMESTAMP)
#     status = db.Column('status', db.String(40))
#     table = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)
#     menu_item = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)
#
#     def __str__(self):
#         return f"Order: id>{self.id} | item>{self.menu_item} | table number>{self.table}"
#
#     @staticmethod
#     def order_price(order_id):
#         order = Order.query.filter_by(id=f'{order_id}').first()
#         order_price = order.number * MenuItems.item_price(order.menu_item)
#         return order_price
