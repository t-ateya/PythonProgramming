from sys import getsizeof

values = (x*2 for x in range(100))
print(values)  # values is a generator object

print("gen: ", getsizeof(values))
for x in values:
    print(x)
