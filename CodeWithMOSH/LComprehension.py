items = [
    ("Product1", 11),
    ("Product2", 1),
    ("Product3", 14),
    ("Product4", 10)

]


"""
  List Comprehension format:
  [expression for item in items]
"""
new_prices = list(map(lambda item: item[1], items))
# line 14Same as line 16. Only python supports this format
new_prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
