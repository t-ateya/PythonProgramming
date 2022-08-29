import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


# Resources are things that the client (webserver or mobileapp) can ask for.
# Our clients think that they're interacting with Resources. That's what they see
# API responds with Resources

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()  # We have to authenticate before we can call the get method
    def get(self, name):
        try:
            item = ItemModel.find_item(name)
        except:
            return {"message": "An error occurred while finding the item from the data base"}

        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):

        if ItemModel.find_item(name):
            return {
                       "message": f" an item with name {name} already exists"}, 400  # When something goes wrong with the request

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.insert_item()
        except:
            return {"message": "An error occurred inserted the item"}, 500  # Internal server error

        return item.json(), 201

    def put(self, name):

        data = Item.parser.parse_args()
        updated_item = ItemModel(name, data["price"])

        item = ItemModel.find_item(name)

        if not item:
            try:
                updated_item.insert_item()
            except:
                return {"message": "An error occurred inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error occurred updating the itme"}, 500

        return updated_item.json()

    def delete(self, name):
        item = ItemModel.find_item(name)

        if not item:
            return {"message": f"the item with name {name} does not exist."}

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {"message": "Item deleted"}


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items"

        rows = cursor.execute(query)
        items = []

        for row in rows:
            items.append({"name": row[0], "price": row[1]})

        connection.close()

        return {"items": items}
