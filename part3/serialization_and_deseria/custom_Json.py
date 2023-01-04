from datetime import datetime

current = datetime.utcnow()

#print(current)

import json 
#time_json = json.dumps(current)

#print(str(current))

def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

current = format_iso(current)
#print(current)


log_record = {
    #'title': format_iso(datetime.utcnow()), 
    'title': datetime.utcnow(), 
    'message': 'testing',
    'args': {10, "test"}
}


def format_general(arg):
    return 'Unkown serialization'

logs = json.dumps(log_record, indent=2, default= format_general)

#print(logs)

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person):
        return arg.toJSON()

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        self.create_dt = datetime.utcnow()

    def __repr__(self) -> str:
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt.isoformat()
        }
    def toJSON2(self):
        return vars(self)  #Returns all the instance variables in JSON format.


p = Person('John', 82)
log_record = dict(time=datetime.utcnow(),
                message='Create new Person Record.',
                person=p)
#print(p)

#print(p.toJSON())
serial_json = json.dumps(log_record, default=custom_json_formatter)
#print(serial_json)


class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    
    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y})'


def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)


from decimal import Decimal

pt1 = Point(1,2)
p= Person('John', 10)
pt2 = Point(Decimal('10.5'), Decimal(100.5))

log_record = dict(time=datetime.utcnow(),
             message='Created new point',
             point=pt1,
             point_2=pt2,
             created_by=p 
)

serial_json = json.dumps(log_record, default=custom_json_formatter)

print(serial_json)


from functools import singledispatch

@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON()...')
        return arg.toJSON()
    except AttributeError:
        print('\tfailed -trying to use vars...')
        try:
            return vars(arg)
        except TypeError:
            print('\tfailed - using string repr---')
            return str(arg)

@json_format.register(datetime)
def _(arg):
    return arg.isoformat()

@json_format.register(set)
def _(arg):
    return list(arg)



log_record = dict(time=datetime.utcnow(),
             message='Created new point',
             point=pt1,
             created_by=p 
)

print(json.dumps(log_record, indent=2, default=json_format))