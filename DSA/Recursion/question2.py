#What's the runtime of the code below?

def printPairs(array):
    for i in array:
        for j in array:
            print(str(i) + "," + str(j))


#Ans: BigO(N^2)