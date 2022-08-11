from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
     'name': 'My Wonderful Store',
     'items': [
                 {
                  'name': "My Item",
                  'price':15.99
                  }
            ]
     },

]

#Create another endpoint
@app.route('/')
def home():
    return render_template('index.html')

"""
@app.route('/')
def home():
    return "Hello World"
"""

"""
    We are setting up the server. This is server end

    POST - used to receive data
    GET - Used to send data back only

    POST /store data: {name}
    GET /store/<string:name>
    GET /store
    POST /store/<string:name>/item {name: price}
    GET /store/<string:name>/item
"""

#POST /store data: {name}
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json() #Request data from the browser
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': "store not found"})


#GET STORE
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    requested_item = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name":requested_item["name"],
                "price": requested_item["price"]
            }
        store['items'].append(new_item)
        return jsonify(store)
    return jsonify({"message": f"The store {name} is not found"})



#GET
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})
    return jsonify({"message": "Item not found"})


app.run(port =5000)