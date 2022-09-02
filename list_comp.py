l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]
l3 = 'python'

"""
print(list(map(lambda x, y : x + y, l1, l2)))
print([x + y for x, y in zip(l1, l2)])


print([x**2 for x in range(10) if x**2< 25 ])
"""

def fact(n):
    return 1 if n < 1 else n * fact(n-1)

results = list(map(fact, range(6)))
#print(results)

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = 10, 200, 300, 400

results = list(map(lambda x, y, z,: x + y + z, l1,l2,l3))
#print(results)

results = list(filter(lambda x: x % 3 ==0, range(25)))
#print(results)

results = list(filter(None, [1, 0, 4, 'a', '', None, True, False]))

#print(results)


l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'
results = list(zip(l1, l2, l3))

#[print(x) for x in results]

results = [fact(n) for n in range(10)]
#print(results)

results = (fact(n) for n in range(10))

for x in results:
    #print(x)
    pass 

print(list(filter(lambda x: x%2==0, map(lambda x,y: x + y. l1, l2))))
results = (x + y for x, y in zip(l1, l2) if ( x+ y) % 2 ==0)
print(results)