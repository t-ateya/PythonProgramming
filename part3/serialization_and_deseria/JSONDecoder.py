#Using JSONDecoder
import json 
j= """
    {
        "a":100,
        "b": [1, 2, 3],
        "c": "Python",
        "d" : {
            "e" : 4,
            "f" : 5.5
        }
    }
"""

class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        pass 

class Point:
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y 

    def __repr__(self) -> str:
        return f'Person(x={self.x}, y={self.y})'
    
j_points= """
    "points":[
        [10, 20],
        [-1, -2],
        [0.5, 0.5]
    ]
"""

j_other = '''
        {
            "a":1,
            "b" : 2
        }
'''

class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        if 'points' in arg:
            obj = json.loads(arg)
            return "parsing object for points"
        else:
            return super().decode(arg)

#result = json.loads(j_points, cls=CustomDecoder)
#print(result)

class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        if "points" in obj:
            obj["points"] = [Point(x,y) for x, y in obj['points']]
        return obj

#result = json.loads(j_points, cls=CustomDecoder)
#print(result)

import re 

"""
pattern = r'"_type"\s*:\s*"point"' #r stands for raw string meaning python should not interpret \t as a tab, rather leave it as it is.
print("word\tword")
print(r"word\tword")

regexp = re.compile(pattern)
print(regexp.search('"a": 1'))
print(regexp.search('"_type": "point"'))
print(regexp.search('"_type": \t"point"'))
print(re.search(r'"_type"\s*:\s*"point"','"_type": \t"point"' ))
"""

class CustomDecoder(json.JSONDecoder):
    def decoder(self, arg):
        obj = json.loads(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            if obj.get('_type', None) == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj


