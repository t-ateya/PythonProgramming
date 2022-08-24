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
            item.save_to_db()
        except:
            return {"message": "An error occurred inserted the item"}, 500  # Internal server error

        return item.json(), 201

    def put(self, name):

        data = Item.parser.parse_args()

        item = ItemModel.find_item(name)

        if not item:
            item = ItemModel.find_item(name)
        else:
            item = ItemModel(name, data['price'])

        item.save_to_db()

        return item.json()

    def delete(self, name):

        item = ItemModel.find_item(name)
        if item:
            item.delete_from_db()
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
