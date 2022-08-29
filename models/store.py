from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship("ItemModel", lazy='dynamic')

    def __init__(self, _name):
        self.name = _name

    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}#query builder

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
