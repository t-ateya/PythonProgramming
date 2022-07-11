items = [5, 6, 8, 9,23]
new_items = [items[i] for i in range (2)]
#print(new_items)
#print(sum(items))

#print(items)
#items.pop(1)
#items.append()
#print(items)

j = 0
for num in items:
    if (num != 0):
        items[j] = 0
        j += 1

print(items)