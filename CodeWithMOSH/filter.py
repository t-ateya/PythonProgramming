items = [
    ("Product1", 11),
    ("Product2", 1),
    ("Product3", 14),
    ("Product4", 10)

]

filtered = list(filter(lambda item: item[1] >= 10, items))
print("filtered: ", filtered)
