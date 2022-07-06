#Write a function to find the duplicate numbers on a given array/list

def removeDuplicates(myList):
    temp = []
    for item in myList:
        if item in temp:continue #pass the item and go to the next
        else:
            temp.append(item)
    return temp

def removeDuplicatesMethod2(myList):
    new_list=[]
 
    for i in myList:
 
        if i not in new_list:
 
            new_list.append(i)
 
    return new_list
print(removeDuplicates([1,1,2,2,3,4,5,6,6]))