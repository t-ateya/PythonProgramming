from re import X


point = (1, 3) + (5, 6)
point2 = (3, 7)*3
point3 = tuple("Hello World")
print(point)
print(point2)
print(point3)
print(type(point3))

if 3 in point:
    print("exists")


# Swap 2 variables
x = 10
y = 20
x, y = y, x

print("x: ", x)
print("y: ", y)
