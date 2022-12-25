d = {(1, 2, 3) : "this is a tuple"}
print(d[(1, 2, 3)])


#N.B Only immutables are hashable e.g tuples and can be used as keys for dictionary. Mutables such as list are not hashable
t1 = (1, 2, 3)
t2  = (1, 2, 3)
t3 = [1, 2, 3] #Not hashable and cannot be used as key in dict
print(t1==t2)

print(hash(t1))
print(hash(t2))
print(hash(t2)==hash(t1))
print(t1 is t2)

#print(hash(t3)) #error. List not hashable

#functions are hashable
def my_func(a, b, c):
    print(a, b, c)

#print(hash(my_func))

d = {my_func: [10, 20, 30]}

def fn_add(a, b):
    return a + b

def fn_inv(a):
    return 1 / a

def fn_mult(a, b):
    return a * b


funcs = {fn_add : (10, 20), fn_inv : (2,), fn_mult : (2, 8)}
print(funcs)

for f in funcs:
    print(f)

for f in funcs:
    value = f(*funcs[f])
    print(value)

for f, args in funcs.items():
    print(f, args)

for f, args in funcs.items():
    print(f(*args))

d = dict([('a', 100), ['x', 200]])
print(d)

d = {'a':100, 'b' : 200}
#Copy of dictionary
d1 = dict(d)
print(d1)


keys = ['a', 'b', 'c']
values = [1, 2, 3]

d = {}
for k, v in zip(keys, values):
    d[k] = v

print(d)

d = {k : v for k, v in zip(keys, values)}
print(d)

keys = 'abcd'
values = range(1, 5)

d = {k: v for k, v in zip(keys, values) if v % 2 == 0}
print(d)

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)

grid = [(x, y) 
        for x in x_coords
        for y in y_coords]

#print(grid)

import math 
grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]
#print(grid_extended)

counter = dict.fromkeys(['a', 'b', 'c'])
print(counter)

d = dict.fromkeys('python')

for k in d:
    print(k)


