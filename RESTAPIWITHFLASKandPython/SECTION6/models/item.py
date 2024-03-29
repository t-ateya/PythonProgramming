from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship('StoreModel')

    def __init__(self, _name, price):
        self.name = _name
        self.price = price


    def json(self):
        return {"name": self.name, "price": self.price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_item(cls, name):
        return cls.query.filter_by(
            name=name).first()  # Select * from items where name = name LIMIT 1 i.e first row only
