from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
items = []

class Item(Resource):
    def get(self, name):
        """Returns an item from the server"""
        item = next(filter(lambda item:item["name"]==name, items), None)
        return {'item': item}, 200 if item else 404  #404, not found

    def post(self, name):
        """Creates an item in the server"""
        if next(filter(lambda x:x['name']==name), None):
            return f"{'message': '{name} already exists.'}", 400  #400 bad request
        data = request.get_json()
        item = {"name": name, "price": data['price']}
        items.append(item)
        return item, 201, #200 item created

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1/student/ateya
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)