from config import db

class Cashier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    phone_number = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"id is {self.id} :name : {self.first_name} {self.last_name}"

