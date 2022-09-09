
"""
    Comprehensions are basically functions.
    generate a list by transforming, and optionally filtering another iterable
"""

other_list = ["this", 'is', 'a', 'parrot']
new_list = []

for item in other_list:
    if len(item) > 2:
        new_list.append(item[::-1])

lc = [item[::-1] for item in other_list if len(item) > 2]

#print(other_list)
#print(new_list)
#print(lc)

"""
    E.g create a list of squares of all the integers between 1 and 100 that are not divisible by 2,3 or 5
"""
sq = [n**2 
        for n in range(1, 101) 
        if n%2 and n%3 and n%5]

#print(sq)

#lc = [ [i*j for j in range(5)] for i in range(5) ]
#print(lc)

"""
    l = []
    for i in range(5):
        for j in range(5):
            for k in range(5):
                l.append((i, j, k))
"""

l = [(i, j, k) for i in range(5) for j in range(5) for k in range(5)]

l = [(i, j) for i in range(5) for j in range(5) if i ==j]
#print(l)

"""
    l = []
    for i in range(1, 6):
        for j in range(1,6):
            if i%2 == 0:
                if j%3 == 0:
                    l.append((i, j))

[(i, j)
    for i in range(1, 6)
    for j in range(1, 6)
    if i%2 == 0
    if j%3 == 0]

[(i, j)
    for i in range(1, 6)
    for j in range(1, 6)
    if i%2 == 0 and j%3 == 0]

"""


