"""
    A function which does not have a name and is only used to return values.
    lambda is a short function usually used with map and has no name
"""

add = lambda x, y : x+y
#print((lambda x, y : x+y)(5,7))
#print(add(5,7))

#Great use of lambda
def double(x):
    return x*2

sequence = [1, 3, 5, 9]
doubled1 = [x*2 for x in sequence]
doubled2 = [double(x) for x in sequence]

doubled3 =list(map(double, sequence))#map goes through each sequence and calls the double function on it

doubled4 = [(lambda x: x*2)(x) for x in sequence]

doubled5 = list(map(lambda x: x*2, sequence))

print(doubled1)
print(doubled2)
print(doubled3)
print(doubled4)
print(doubled5)
