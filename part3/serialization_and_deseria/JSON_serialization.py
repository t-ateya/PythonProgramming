"""
    Example:

{
        
    "title" : "Fluent Python",
    "author" :{
                "firstName": "Luciano",
                "lastName" : "Ramalho"
    },
    "publisher" : "O'Reilly",
    "isbn": "978-1-491-9-46008",
    "firstReleased": 2015,
    "listPrice": [
        {
            "currency": "USD",
            "price" : 49.99
        },
        {
            "currency": "CAD",
            "price": "57.99"
        }
    ]

}

JSON is essentially a string

import JSON
    -> dump, dumps
    -> load, loads
"""


#JSON Serialization
import json

d1 = {'a': 100, 'b': 200}
d1_json_str = json.dumps(d1, indent=2)
#d1_json_file = json.dump(d1)

d2 = json.loads(d1_json_str)

print(d1_json_str)
print(type(d1_json_str))
print(type(d1_json_str).__name__)

print(d2)
print(type(d2).__name__)