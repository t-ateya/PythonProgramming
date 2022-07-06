#What's the runtime of the below code?

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(array[i] + "," + array[j])

#Ans: BigO(N^2)