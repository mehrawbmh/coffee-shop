from config import db


class Cashier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, user_name, fname, lname, phone, email, pas):
        self.username = user_name
        self.first_name = fname
        self.last_name = lname
        self.phone_number = phone
        self.email = email
        self.password = pas

    def __repr__(self):
        return f"id is {self.id} :name : {self.first_name} {self.last_name}"
