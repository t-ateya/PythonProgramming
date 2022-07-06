items = [
    ("Product1", 11),
    ("Product2", 1),
    ("Product3", 14),
    ("Product4", 10)

]


def sort_item(item):
    return item[1]


# lambda is an anonymous func
# lambda func format is: key=lambda parameters:expression
# items.sort(key=sort_item)
items.sort(key=lambda item: item[1])
print(items)


# Map Function
prices = []
products = []
for item in items:
    prices.append(item[1])
    products.append(item[0])

print("prices: ", prices)
print("products: ", products)


# better method
pricez = map(lambda item: item[1], items)
prods = map(lambda item: item[0], items)

for p in pricez:
    print("pricez: ", p)

for pr in prods:
    print("prods: ", pr)

# Best approach
new_prices = list(map(lambda item: item[1], items))
print("new_prices: ", new_prices)

new_prods = list(map(lambda item: item[0], items))
print("new_prods: ", new_prods)

# 3. Filter Items
