l = [2, 3, 4]
def sq(x):
    return x**2

num_list = list(map(sq, l))
print(num_list)

l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]

def add(x, y):
    return x + y 

"""
print(list(map(add, l1, l2)))
print(list(map(lambda x, y : x + y, l1, l2)))
"""

l = [0, 1, 2, 3, 4]
print(list(filter(None, l)))

def is_even(n):
    return n%2 == 0

even = list(filter(is_even, l))
print(even)

print(list(filter(lambda n : n % 2 == 0, l)))


