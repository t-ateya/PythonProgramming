
from ntpath import join


name = "ateya"
list_name = list(name)
#print(list_name)
#print(name[0])


#Convert string to list using split() method
user = "Joyce/A./Ateya"
delimeter = "y"
b=user.split(delimeter)
#print(b)

#Convert list to string using join() method

letters = ["a", "t", "e", "y", "a"]
delimeter= ""
print(delimeter.join(letters))

fami = ["f","a","m","i","l","y"]
print("//".join(fami))