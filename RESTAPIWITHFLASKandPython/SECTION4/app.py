from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


#JWT === Json Web Token used for auth

app = Flask(__name__)
app.secret_key = "ateya123"
api = Api(app)

jwt = JWT(app, authenticate, identity)
items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required() #We have to authenticate before we can call the get method
    def get(self, name):
        """Returns an item from the server"""
        item = next(filter(lambda item: item["name"] == name, items), None)
        return {'item': item}, 200 if item else 404  #404, not found

    def post(self, name):
        """Creates an item in the server"""

        data = Item.parser.parse_args()

        if next(filter(lambda x:x['name']==name, items), None):
            return f"{'message': '{name} already exists.'}", 400  #400 bad request
        item = {"name": name, "price": data['price']}
        items.append(item)
        return item, 201, #200 item created

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': "Item deleted"}

    def put(self, name):

        data = Item.parser.parse_args()

        item = next(filter(lambda item: item['name'] == name, items), None)
        if not item:
            item = {"name" : name, "price" : data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item





class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1/student/ateya
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)