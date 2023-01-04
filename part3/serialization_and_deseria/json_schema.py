person_schema = {
    "type": "object",
    "properties":{
        "firstName": {
            "type": "string",
            "minLength" : 1,
            },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1

            },
        "lastName": {
            "type": "string",
            "minLength":1,
            },
        "age": {
            "type": "Number",
            "minimum": 0
            },
        "eyeColor":{
            "type": "string",
            "enum": ["amber", "blue", "brown", "gray", "green", "hazel", "red", "violet"]

        }
    },

    "required": ["firstName", "lastName"]
}

p1 = '''
        {
            "firstName": "John",
            "middleInitial": "M",
            "age": 79
        }
'''

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError


json_doc = p1 

print(json_doc)

try:
    validate(loads(json_doc), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f"Validation error: {ex}")
else:
    print('JSON is valid an conforms to schema')