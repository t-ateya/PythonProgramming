"""
    Aggregators
    - Functions that iterate through an iterable and return a single value that (usually) takes into 
        account every element of the iterable.

    Example:
        - min(iterable)
        - max(iterable)
        - sum (iterable)

"""

def square(n):
    for i in range(n):
        yield i**2


class Person:
    def __bool__(self):
        return True 
    
    def __len__(self):
        return 0 

class MySeq:
    def __init__(self, n):
        self.n = n 

    def __len__(self):
        return self.n

    def __getitem__(self):
        pass 

#any is an OR function 

#print(any([0, '', None]))
#print(any([0, '', None, (10,20)]))


"""
p = Person()
print(bool(p))


print(list(square(5)))
"""

#all is an AND function

"""
all(10, 'hello', None)
all(10, 'hello')
"""

from numbers import Number

#print(isinstance(10, Number))

from decimal import Decimal
isinstance(Decimal('10.5'), Number)


l = [10, 20, 30, 40]

is_all_numbers = True 
for item in l:
    if not isinstance(item, Number):
        is_all_numbers = False
        break 

def is_numeric(v):
    return isinstance(v, Number)


pred_l = map(is_numeric, l)
predicate_l = (is_numeric(item) for item in l)

predic_l = map(lambda x : isinstance(x, Number), l)

"""
print(list(predicate_l))
print(list(pred_l))
print(list(predic_l))

print(all(predic_l))
"""

l = [10, 20, 30,0, 'hello']

#print(all( map(lambda x: isinstance(x, Number), l)))

with open("car-brands.txt") as f:
    for row in f:
        #print(len(row), row, end="")
        pass 

with open("car-brands.txt") as f:
    result = all(map(lambda row: len(row) >= 4, f))


with open("car-brands.txt") as f:
    result = any(map(lambda row: len(row) >= 10, f))


with open("car-brands.txt") as f:
    result = all(len(row) >= 4 for row in f)



print(result)