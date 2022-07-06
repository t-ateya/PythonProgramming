
newTuple = ('a', 'b','c','d','e')
tuple1 = ('a',)
tuple2 = tuple('b')
tuple3 = tuple("ateya")


"""
print(newTuple)
print(tuple1)
print(tuple2)
print(tuple3)
print(newTuple[-1])
print(newTuple[0])
print(newTuple[1:3])
print(newTuple[0:3])
"""


#[print(x) for x in newTuple if x =="a"]


"""
for item in newTuple:
    print(item)

for index in range(len(newTuple)):
    print(newTuple[index])
"""

[print(newTuple[index]) for index in range(len(newTuple)) if newTuple[index].upper() == "B"]