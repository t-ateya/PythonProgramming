"""
    Python provides many functions that return iterables or iterators.

    Additionally, the iterators perform lazy evaluation

    You must always be aware of whether you are dealing with an iterable or an iterator.

        If an object is an iterable (but not an iterator), you can iterate over it many times
        If an object is an iterator you can iterate over it once

        An iterator just returns itself and so, it becomes exhaustive.

    Examples
    1. range(10) -> iterable since you can iterate over it more than once
    2. zip(l1, l2)  ->iterator since you cannot iterator over it more than once. It gets exhausted
    3. enumerate(l1) ->iterator
    4. open('cars.csv) ->iterator
    5. dictionary .keys() -> iterable
    6. dictionary .values() -> iterable
    7. dictionary .items() -> iterable
    
"""


"""

r = range(10)
print(type(r))
print('__iter__' in dir(r))
print('__next__' in dir(r))

print(iter(r))
print([num for num in r])

z = zip([1,2,3], 'abc')
print('__iter__' in dir(z))
print('__next__' in dir(z))

print(z)
print(list(z)) #iterator over and it gets exhausted
print(list(z)) #empty. 


f = open("cars.csv")
print(next(f))
print(f.__next__())
print(f.readline())
f.close()
"""

with open('cars.csv') as f:
    print(type(f))
    print('__iter__' in dir(f))
    print('__next__' in dir(f))

#print("=====Test if a with open method is an iterator ===")
with open("cars.csv") as f:
    #print(iter(f) is f)
    pass


#Testing for iterator
l = [1, 2, 3]
#print(iter(l) is l)

r = range(1,10)
#print(iter(r) is r)

with open('cars.csv') as f:
    l = f.readlines()
#print(l)

origins = set()
with open('cars.csv') as f:
    rows = f.readlines() #reads the entire file and stores in rows in memory
for row in rows[2:]:
    origin = row.strip("\n").split(";")[-1] 
    origins.add(origin)

#print(origins)

#Better approach

origins = set()
with open("cars.csv") as f:
    next(f)
    next(f) #skip first two lines in the file
    for row in f:
        origin = row.strip("\n").split(";")[-1] 
        origins.add(origin)

#print(origins)

e = enumerate('Python Books')
print(iter(e) is e)
print('__next__' in dir(e))
print(list(e))
print(list(e))

d = {"a":1, "b":3}
keys = d.keys()
print(iter(keys) is keys)

print("__iter__" in dir(keys))
print("__next__" in dir(keys))







