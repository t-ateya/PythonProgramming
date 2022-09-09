
from math import factorial
from re import L


squares = [x**2 for x in range(1,101)]
squares = [x**2 
            for x in range(1,101) 
            if x%2 == 0]

#print(squares[0:10])

#multiplication table
table = []

for i in range(1, 11):
    row = []
    for j in range(1,11):
        row.append(i*j)
    table.append(row)

#print(table)

table2 = [ [i*j for j in range(1,11)] #inner loop
            for i in range(1,11)]    #outer loop
            #N.B: j is the inner loop and it comes first

#print(table2)

"""
    Pascal's triangle
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1

    C(n, k) = n! / (k! * (n-k)!) #combination of Pascal's triangle

    C(0, 0)
    C(1, 0) C(1,1)
    C(2, 0) C(2,1) C(2,2)
    C(3, 0) C(3,1) C(3,2) C(3,3)

"""

#Nesting comprehensions: Nested Comprehension
def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10

pascal = [ 
            [ combination(n, k) for k in range(n + 1)] #inner loop
            for n in range(size + 1)] #outer loop

#print(pascal)

#Nested Loops for comprehensions
"""
    Example:
    suppose:
    l1 = ['a', 'b', 'c']
    l2 = ['x', 'y', 'z']

    Let's write code to get: 'ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz'
"""

l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

lc = [i+j 
        for i in l1
        for j in l2]
#print(lc)

result = []
for s1 in l1:
    for s2 in l2:
        result.append(s1 + s2)

#print(result)

l1 = ["a", "b", "c"]
l2 = ["b", "c", "d"]

result = [s1 + s2 for s1 in l1 for s2 in l2 if s1 != s2]
#print(result)

l1 = [1,2,3,4,5,6,7,8,9]
l2 = ['a', 'b', 'c', 'd']
result = list(zip(l1, l2))
#print(result)

# ########## Let's create zip function using both list comprehension and traditional for loop
#NB. enumerate(iterable) returns and item and its index

result = []
for index_1, item_1 in enumerate(l1):
    for index_2, item_2 in enumerate(l2):
        if index_1 == index_2:
            result.append((item_1, item_2))

#print(result)

result_lc = [   (item_1, item_2) 
                for index_1, item_1 in enumerate(l1)
                for index_2, item_2 in enumerate(l2)
                if index_1 == index_2
            ]

#print(result_lc)

"""
    dot product of two vectors
        Suppose
    v1 = (c1, c2, c3, ..., cn)
    v2 = (d1, d2, d3, ..., dn)

    v1.v2 = c1*d1  + c2*d2 + c3*d3 + ... + cn*dn
"""

v1 = (1, 2, 3, 4, 5, 6)
v2 = (10, 20, 30, 40, 50, 60)

dot = 0
for i in range(len(v1)):
    dot += v1[i] * v2[i]
#print(dot)

dot_prod = sum([i*j for i, j in zip(v1, v2)])
dot_prod2 = sum(i*j for i, j in zip(v1, v2))
#print(dot_prod)
#print(dot_prod2)


"""
fn_0 = lambda x: x**0
fn_1 = lambda x: x**2
fn_2 = lambda x: x**3
fn_3 = lambda x: x**4
"""

funcs = [lambda x: x**0, lambda x: x**1, lambda x: x**2, lambda x: x**3]

for i in range(4):
    print(funcs[i](10))


funcs = [lambda x, p=i: x**p for i in range(5)]