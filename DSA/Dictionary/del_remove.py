myDict = {'name':"ateya", 'age':27, 'address':"London", "school": "uco"}

#myDict.pop('name')
print(myDict.popitem()) #removes last item and key
print(myDict)

del myDict['name']
print(myDict)