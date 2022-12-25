
#Views: Keys, Values and Items

d= {'a':1, "b":2}
keys= d.keys()
values = d.values()
items = d.items()

d = dict(zip('abc', range(1,4)))

d = {'a':1, 'b':2, 'c':3}
while len(d) > 0:
    key, value = d.popitem()
    print(key, value ** 2)

while True:
    try:
        key, value = d.popitem()
    except KeyError:
        break
    else:
        print(key, value ** 2)