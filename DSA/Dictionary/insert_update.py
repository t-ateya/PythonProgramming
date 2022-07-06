myDict = {"name":"ateya", 'age':27}

myDict["age"]= 28

myDict["address"] = 'London'

def traverseDict(dict):
    for key in myDict:
        print(key, dict[key])


traverseDict(myDict)
#print(myDict)
