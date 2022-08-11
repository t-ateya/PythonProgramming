
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @classmethod
    def find_item(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'Item': {"name": row[0], "price": row[1]}}

    @classmethod
    def insert_item(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ? )"
        cursor.execute(query, (item["name"], item['price']))

        connection.commit()
        connection.close()

    @jwt_required() #We have to authenticate before we can call the get method
    def get(self, name):
        try:
            item = self.find_item(name)
        except:
            return {"message": "An error occurred while finding the item from the ddata base"}

        return item if item else {"message": "Item not found"}, 404


    def post(self, name):

        if self.find_item(name):
            return {"message": f" an item with name {name} already exists"}, 400 #When something goes wrong with the request

        data = Item.parser.parse_args()

        item = {"name": name, "price": data["price"]}

        try:
            Item.insert_item(item)
        except:
            return {"message": "An error occurred inserted the item"}, 500 # Internal server error

        return item, 201

    def delete(self, name):
        item = self.find_item(name)

        if not item:
            return {"message": f"the item with name {name} does not exist."}

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {"message": "Item deleted"}

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=? "
        cursor.execute(query, (item["price"], item["name"]))
        connection.commit()
        connection.close()


    def put(self,name):

        data = Item.parser.parse_args()
        updated_item = {"name": name, "price": data["price"]}

        item = self.find_item(name)

        if not item:
            try:
                self.insert_item(updated_item)
            except:
                return {"message": "An error occurred inserting the item"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occurred updating the itme"}, 500

        return updated_item


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items"

        rows = cursor.execute(query)
        items = []

        for row in rows:
            items.append({"name":row[0], "price": row[1]})

        connection.close()

        return {"items": items}

