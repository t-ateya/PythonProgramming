
items = []


new_item = {
    "name":"apple",
    "price" : 12.99
}

new_item1 = {
    "name":"orange",
    "price" : 16.99
}

items.append(new_item)
items.append(new_item1)
#print(items)

def get_item(name:str):
    for index in range(len(items)):
        if items[index]["name"] == name:
            return items[index]
    return {'Error Message': f'{name} not found in the list of items'}

print(get_item("appl"))