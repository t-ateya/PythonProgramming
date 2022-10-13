"""
    Generator Expressions use the same comprehension syntax but instead of using [], we use ()
    Ex. (i ** 2 for i in range(5)). A generator is returned and the evaluation is lazy.

    -list comprehension [i ** 2 for i in range(5)] is an iterable while 
    - Generator expression (i ** 2 for i in range(5)) is an iterator.

                Resource Utilization
    List Comprehension                                              Generator Expression
    1. All objects are created right away(eager)                    object creation is delayed(lazy evaluation) until requested by next()
         -takes longer to create/return the list                        - generator is created/returned immediately
         -iteration is faster(object already created)                    - iteration is slower(objects need to be created)
               
               if you iterate via all the elements, time performance is about the same
               if you do not iterate through all the elements, generator is more efficient
    2. Entire collection is loaded into memory                       Only a single item is loaded at a time

    In general, generators tend to have less memory overhead
"""

l = [x**2 for x in range(5)]
g = (x**2 for x in range(5))



"""

print("======= List Expression ==========")
for item in l:
    print(item)

print("==== Generator Expression =========")
for item in g:
    print(item)


print("======List Expression =============")

for item in l:
    print(item)


print("========Generator Expression========")
for item in g:
    print(item)

print(list(g))

"""

from math import factorial

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10
pascal = [[combo(n,k) for k in range(n+1)] for n in range(size + 1)]
print(pascal)

#Using generator expression
pascal = ([combo(n,k) for k in range(n+1)] for n in range(size + 1))
#print(pascal)

print([list(row) for row in pascal])