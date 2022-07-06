
from hashlib import new


myDict = {'name':"ateya", 'age':27, 'address':"London", "school": "uco", "education": "master"}

#print('ateya' in myDict.values())
#print('name' in myDict.keys())

#any()
newDict = {}
#print(any(myDict))
#print(any(newDict))

#len()
#print(len(myDict))

#sorted()
dictionary = {'o':1, 'u':2, "i":3, "a":4, "e":5}
new_dict = {"eaooo2":1, "ass":2, "udd":3, "sseo":4, 'werwi':5}
print(sorted(dictionary, reverse=True))

print(sorted(new_dict, key = len))