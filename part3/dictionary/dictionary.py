"""
    Requirments
    If an object is hashable:
        -> The hash of the object must be an integer value
        -> If two objects compare equal(==), the hashes must also be equal

    {
        'john': ['John', 'Cleese', 78],
        (0, 0) : 'origin',
        'repr' : lambda x: x **2,
        'eric': {'name': 'Eric Idle',
        'age' : 75}
    }

    #You cannot have a tuple(0,0) as a key in when dict
    dict(john=['John', 'Cleese', 78],
         repr = lambda x: x**2,
         eric = {
            'name' : 'Eric Idle',
            'age' :75},
         twin=dict(name='Eric Idle', age=75)
         
    )

    Creating Dictionaries: fromkeys()
        -> class method on dict
        -> creates a dictionary with specified keys all assigned the same value
        d = dict.fromkeys(iterable, value)
"""

from urllib import request, response


n = 10
d = {i: i**2 for i in range(1,n)}

d = {}
for i in range(1, n):
    d[i] = i**2


d = {}
url = 'http://localhost/user/{id}'
for i in range(n):
    response = request.get(url.format(id=i))
    user_json = response.json()
    user_age = int(user_json['age'])
    if user_age >= 18:
        user_name = user_json['fullName'].strip()
        user_ssn = user_json['ssn']
        d[user_ssn] = user_name


d = dict.fromkeys(['a', (0, 0), 100], 'N/A')
    # {'a' : 'N/A', (0,0) : 'N/A', 100 : 'N/A'}
d = dict.fromkeys((x ** 2 for x in range(1, 5)), False)