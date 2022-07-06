from numpy import average


nums = [10, 20, 30, 40, 50, 80, 90]
print(sum(nums)/len(nums))

myList = list()
keep_adding_element = True
while keep_adding_element:
    num = input("Enter a number: ")
    if num == "done": break
    value = float(num)
    myList.append(value)
    average = sum(myList)/len(myList)
print("Average: ", average)