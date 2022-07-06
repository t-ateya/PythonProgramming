
items_cost ={
    "Apple": 6,
    "Bananas": 5,
    "Avogadro": 10
}

strings_dic = {}
#print(items_cost.get("Appl"))
word ="love"
for ch in word:
    key = strings_dic.get(ch)
    if not key:
        strings_dic.update({ch:key})


#print(strings_dic)

#print(len(strings_dic))

words = ["Apple", "Orange", "Avogadro"]
for w in words:
    value = items_cost.get(w)
    if value:
        print(w)
        items_cost.pop(w)
        
print(items_cost)
