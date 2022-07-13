from numpy import NaN


for i in range(3, 4):
    #print("Hello")
    pass 

def trial(arr, target):
    return [0,0] if len(arr)==1 and arr[0] == target else "Not Found"

#print(trial([4], 0))

def isBadVersion(n):
    return n>=3

#print(isBadVersion(10))

history = """
            Best programmer
            Over best devOps engineer 
            Great Machine Learning Engineer
"""
#print(history)

age = 18
isOldeEnough = age>=15
if (isOldeEnough):
    #print("You can take the test")
    pass 

money  = NaN
if (money):
    print("You can buy an item")

