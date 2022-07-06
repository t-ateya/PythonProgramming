#Accessing/Traversing the List

shoppingList = ["Milk", "Cheese", "Butter"]

#print(shoppingList)
print([x for x in shoppingList])
print([shoppingList[i] for i in range(len(shoppingList))])

for i in range(len(shoppingList)):
    print(shoppingList[i])