
suites = ['Spades', "Hearts", "Diamons", "Clubs"]
alias = suites
#print(id(alias))
#print(id(suites))

l = [1, 2, 3, 4, 5]
print(l)
l[0:2] = ('a', 'b', 'c', 'd')
print(l)

l.extend([9, "e"])
l.extend({11, 13, "A", "Z"})
print(l)
del l[1]
l.insert(2, "u")
l.reverse()
print(l)
l2 = l[:]
l3 = l2.copy()

print(l2)
print(l3)