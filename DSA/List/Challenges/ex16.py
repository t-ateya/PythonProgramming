#Given 2D list calculate the sum of diagonal elements

myList2D = [  [1,2,3], [4, 5, 6], [7, 8, 9]  ]

def sumDiagonal(a):
    sum = 0
    for row in range(len(a)):
        for col in range(len(a[0])):
            if row == col:
                sum += a[row][col]
    return (sum)


def sum2Diagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    return sum

print(sumDiagonal(myList2D))
print(sum2Diagonal(myList2D))
