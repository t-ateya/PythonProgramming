"""
    s1 = {'a', 'b', 'c', 'd,}
    s2 = {'b', 'c', 'd'}
    s1 | s2 -> {'a', 'b', 'c', 'd'}
    s1 & s2 -> {'b', 'c'}
    s1 - s2 -> {'a'}
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s = s1 | s2
a = s1 & s2
b = s1 - s2
print(s)
print(a)
print(b)

d1 = {'a': 1, 'b':2, 'c':3}
d2 = dict(zip('cde', [30, 4, 5]))
#print(d1, d2)

a = d1.keys() & d2.keys()
u = d1.items() | d2.items()
k = d1.keys() | d2.keys()
print(a)
print(u)
print(k)


d3 = {'a': [1, 2], 'b': [3, 4]}
d4 = {'a': [30, 40], 'b': [5, 6]}
#print(hash(('a', [1, 2]))) not hashable. Hence, can't union
print(hash(('a', 1)))

#u = d3.items() | d4.items()  #Can't have a union since there's a list present thereby making the func non-hashable


d1 = {'a':1, 'b' : 2, 'c' : 3}
d2 = {'b' : 2, 'c': 30, 'd':4}

k1 = d1.keys()
k2 = d2.keys()
n = k1 & k2
print(n)

new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = d1[key], d2[key]

print(new_dict)

new_dict = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}
print(new_dict)



d1 = {'a':1, 'b' : 2, 'c' : 3}
d2 = {'b' : 2, 'c': 30, 'd':4}

d1 = {'a':1, 'b' : 2, 'c' : 3, 'd':4}
d2 = {'a' : 10, 'b': 20, 'c':30, 'e':5}


new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = d2[key]

union = d1.keys() | d2.keys()
intersection = d1.keys() & d2.keys()
diff_keys = union - intersection

print(diff_keys)
intersec = d1.keys() ^ d2.keys()
print(intersec)

results = {}
for key in diff_keys:
    results[key] = d1.get(key) or d2.get(key)

print(results)


results = {key: d1.get(key) or d2.get(key) for key in d1.keys()^d2.keys()}
print(results)