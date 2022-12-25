"""
    unpacking dictionary
    works similar to unpacking a dictionary into keyword arguments in function calls

    def func(**kwargs):
        print(kwargs)

    d = {'a' : 1, 'b' : 2}
    func(**d)

    d1 = {'a' : 1, 'b' : 2}
    d2 = {'a' : 10, (0, 0) : 'origin'}
    d3 = {'b' : 20, 'c' : 30, 'a' : 100}

    d = {'a' : 100, 'b' : 20, (0, 0) : 'origin', 'c': 30}


    ========== Copying dict =========
    1. shallow copies
        -container object is a new object
        -copied container element keys/values are shared references with original object

    d_copy = d.copy()
    d_copy = {**d}
    d_copy = dict(d)
    d_copy = {k: v for k, v in d.items()} 

    2. Deep copy
        simpler to use: copy.deepcopy

"""

d1 = {'a' : 1, 'b': 2}
d2 = {'c' : 3, 'd': 4}
d1.update(d2)

print(d1)

d1 = {'a' : 1, 'b': 2}
d1.update(b=20, x = 40, c = 30)
print(d1)

d1 = {'a' : 1, 'b': 2}
d1.update([('c', 2), ['d', 3]]) #passing in an iterable
print(d1)

d1 = {'a' : 1, 'b': 2}

s = "pythonAa"
for c in s:
    print(ord(c))

d1.update((k, ord(k)) for k in "python") #updating dictionary using generator object
print(d1)

l1 = [1, 2, 3]
l2 = 'abc'
l = [*l1, *l2]
ll = (*l1, *l2)
print(l)
print(ll)

d1 = {'a' : 1, 'b': 2}
d2 = {'c' : 3, 'd': 4}
d = {**d1, **d2}

print(d)


conf_default = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
print(conf_default)

conf_global = {'port': 5432, 'database':'deepdive'}

conf_dev = {
    'host': 'localhost',
    'user':'test',
    'pwd': 'test'
}

conf_prod = {
    'host': 'prodpg.deepdive.com',
    'user': '$prod_user',
    'pwd' : '$prod_pwd',
    'database':'deepdive_prod'
}

#conf_default->global->dev/prod
print("=====================================================================")
conf = {**conf_default, **conf_global, **conf_dev}
print(conf)

conf = {**conf_default, **conf_global, **conf_prod}
print(conf)

def my_func(*, kw1, kw2, kw3):
    print(kw1, kw2, kw3)

d = {'kw2': 20, 'kw1': 10, 'kw3': 30}

my_func(**d)

d = {'a':[1, 2], 'b': [3,4]}
#Shallow copy
d1 = d.copy()
print(d1)
print(id(d), id(d1))

print(d is d1)

print(d['a'] is d1['a'])
print(id(d['a']), id(d1['a']))

#Effect of shallow copy
d['a'].append(100)
print(d)
print(d1)


##########  Deep Copy ###########
from copy import deepcopy
d = {
    'id': 123445,
    'person': {
        'name': 'John',
        'age': 70
                },
    'posts': [ 100, 105, 200]
}

d1 = deepcopy(d)
print(id(d), id(d1))

d1 = {'a':[1, 2], 'b':[3,4]}
d2 = {k : v for k, v in d1.items()} #shallow copy


#Finding out which is the best way of making a copy of a dictionary
from random import randint
big_d = {k: randint(1, 100) for k in range(1_000_000)}
#print(len(big_d))

def copy_unpacking(d):
    d1 = {**d}

def copy_copy(d):
    d1 = d.copy()

def copy_create(d):
    d1 = dict(d)

def copy_comprehension(d):
    d1 = {k:v for k, v in d.items()}

def copy_deepcopy(d):
    d1 = deepcopy(d)

from timeit import timeit
print(timeit('copy_unpacking(big_d)', globals=globals(), number=100))
print(timeit('copy_copy(big_d)', globals=globals(), number=100))
print(timeit('copy_create(big_d)', globals=globals(), number=100))
print(timeit('copy_comprehension(big_d)', globals=globals(), number=100))
print(timeit('copy_deepcopy(big_d)', globals=globals(), number=100))