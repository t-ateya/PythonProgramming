"""
    Loading JSON
        We have seen how to serialize Python objects to JSON
        Now we need to look at deserializing JSON to Python objects.

Example:
import json
j = '{"a":1, "b": {"sub1": [2, 3]}}'
d = json.loads(j)



Schemas
    Describing custom JSON types and object is difficult
     ->In general, we need to know the structure of the JSON data in order to custom deserialize
     ->this is referred to as the schema
        -> a pre-defined agreement on how the JSON is going to be structured or serialized
     ->If JSON has a pre-determined schema, then we can handle custom deserialization
     -> schema might be for the entire JSON, or for sub-components only
     e.g 
        {
            "createdAt":
            {
                "objecttype": "isodatetime",
                "value": "2022-12-27T23:59:59"
            }
        }

import json
j = '{"a":1, "b": {"sub1": [2, 3]}}'
d = json.loads(j)
print(d)

Example:
from decimal import Decimal
def make_decimal(arg):
    return Decimal(arg)

    ->loads(j, parse_float=make_decimal)
"""

import json 
j = """
    {
        "name": "Python",
        "age": 27,
        "version": ["2.x", "3.x"]
    }
"""

d = json.loads(j)
#print(d)

p = """
    {
        "time":{
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:00"
        },

        "message": "created this json string"
    }
"""

d = json.loads(p)
from pprint import pprint
#pprint(d)

from datetime import datetime 

for key, value in d.items():
    if isinstance(value, dict) and "objecttype" in value \
    and value["objecttype"] == "datetime":
        d[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')

#pprint(d)

j = '''
    {
        "cake": "yummy chocolate cake",
        "myShare": {
            "objecttype": "fraction",
            "numerator": 1,
            "denominator": 8
        }
    }
'''

d = json.loads(j)

from fractions import Fraction

for key, value in d.items():
    if (isinstance(value, dict) and 'objecttype' in value \
        and value['objecttype'] == 'fraction'):
        numerator = value["numerator"]
        denominator = value["denominator"]
        d[key] = Fraction(numerator, denominator)


def custom_decoder(arg):
    print('decoding: ', arg)
    return arg 


j = '''
    {
        "a": 1,
        "b": 2,
        "c" : {
            "c.1" : 1,
            "c.2" : 2,
            "c.3" :{
                "c.3.1" :1,
                "c.3.2": 2
            }
        }
    }
'''

def custom_decoder(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
    else:
        return arg



d = json.loads(j, object_hook=custom_decoder)
#print(d)

class Person:
    def __init__(self, name, ssn) -> None:
        self.name = name 
        self.ssn = ssn 

    def __repr__(self) -> str:
        return f'Person(name={self.name}, ssn={self.ssn})'

    def toJSON(self):
        return dict(objecttype="person", name=self.name, ssn=self.ssn)


j = """
    {
        "accountHolder":{
            "objecttype": "person",
            "name": "Eric Idle",
            "ssn": 100
        },
        "created" : {
            "objecttype": "datetime",
            "value": "2022-10-21T03:00:00"
        }
    }
"""

def custom_decoder(arg):
    if "objecttype" in arg:
        if arg['objecttype'] == 'datetime':
            return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            return Fraction(arg['numerator'], arg['denominator'])
        elif arg['objecttype'] == 'person':
            return Person(arg['name'], arg['ssn'])
        return arg 
    return arg

d = json.loads(j, object_hook=custom_decoder)
print(d)