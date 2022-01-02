from app import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(30), nullable=False, unique=True)

    def __init__(self, parent_id, name):
        self.parent_id = parent_id
        self.name = name

    def __str__(self):
        return f"Category{self.id} : {self.name}"

