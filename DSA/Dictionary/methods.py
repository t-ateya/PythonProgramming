myDict = {'name':"ateya", 'age':27, 'address':"London", "school": "uco", "education": "master"}

#clear() method

#myDict.clear()
#print(myDict)

#copy()
newDic = myDict.copy()
#print(myDict, newDic)

#fromkeys()
newDict = {}.fromkeys([1, "name", 'year'], [0, "ateya", 1994])
#print(newDict)

#get() method

#print(myDict.get('name', "arrey"))

#print(myDict.items())

#keys() method
#print(myDict.keys())

#print(myDict.popitem())


"""
print(myDict.setdefault('name', 'added'))
print(myDict)
print(myDict.setdefault('name1', 'added'))
print(myDict)
"""


#print(myDict.pop('name2', 'does not exist'))

#print(myDict.keys())


dict2 = {'a':1, 'b':2, 'c':3}
myDict.update(dict2)

print(myDict)
