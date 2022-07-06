point = {"x": 1, "y": 2}
point = dict(x=1, y=3)
print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])

print(point.get("a", 0))
del point["x"]
print(point)

for key in point:
    print(key)

for item in point.items():
    print(item)

for key, value in point.items():
    print(key, value)

print(type(item))


# Dict comprehension
values = {}
for x in range(5):
    values[x] = x*2

#values = {expression for item in items}
values = {x: x*2 for x in range(5)}
print(values)
