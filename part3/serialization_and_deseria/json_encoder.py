"""
    Python uses an instance of the JSONEncoder class in the json module to serialize data
    The JSONEncoder class shares many arguments with the dump / dumps functions
        default skipkeys sort_keys indent separators etc

    
    How to create a custom JSONEncoder
        -> subclass JSONEncoder
        -> custom initialize parent class we want to 
        -> override the default method
            ->handle what we want to handle ourselves
            ->otherwise delegate back to the parent class

class CustomEncoder(JSONEncoder):
    def __init__(self):
        super().__init__(skipkey=True, allow_nan=False,
        indent='---', separators=('', ' = '))

    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(self, arg)
"""

#Custom JSON Encoding using JSONEncoder

import json 
default_encoder = json.JSONEncoder()
jenc= default_encoder.encode((1, 2, 3))
#print(jenc)

from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg) 
        

custom_encoder = CustomJSONEncoder()

c_enc = custom_encoder.encode(True)

#print(c_enc)
#print(type(c_enc).__name__)
#print(custom_encoder.encode(datetime.utcnow()))

json.dumps(dict(name='test', time=datetime.utcnow()), 
            cls=CustomJSONEncoder)


d = {10: "int", 10.5:"float", (1, 1): "complex"}

d ={
    'name': 'Python',
    'age': 27,
    'created_by': 'Guido van Rossum',
    'list': [1, 2, 3]
}

#seria = json.dumps(d, skipkeys=True)
#seria = json.dumps(d, indent='---')
seria = json.dumps(d, separators=(',', ':'))
#print(seria)

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        #print(kwargs)
        super().__init__(skipkeys=True, 
                        allow_nan=False,
                        indent='---',
                        separators=('', ' = '))

    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)


d = {
    'time': datetime.utcnow(),
    1+1j: 'complex',
    'name': 'Python'
}

seria = json.dumps(d, cls=CustomEncoder)
#print(seria)

class CustomEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            obj = dict(
                datatype="datetime",
                iso=arg.isoformat(),
                date=arg.date().isoformat(),
                time=arg.time().isoformat(),
                year=arg.year,
                month=arg.month,
                day=arg.day,
                hour=arg.hour,
                minutes=arg.minute,
                seconds=arg.second

            )
            return obj 
        else:
            return super().default(arg)

d = {"time": datetime.utcnow()}
print(d)


seria = json.dumps(d, cls=CustomEncoder, indent=2)
print(seria)