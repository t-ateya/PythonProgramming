myDict = {'name':"ateya", 'age':27, 'address':"London"}

def searchElement(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The value does not exist"

    

print(searchElement(myDict, 27))