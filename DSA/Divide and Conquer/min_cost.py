"""
    Minimum cost to reach the last cell

    Problem Statement:
    - 2D Matrix is given
    - Each cell has a cost associated with if for accessing
    - We need to start from (0,0) cell and go till (n-1, n-1) cell
    - We can go only to right or down cell from current cell
    - Find the way in which the cost is minimum

    Subproblems
     Option1 = y + 9 + 3   f(4,3)
                                    =>Min(Option1, Option2)
     Option2 = z + 7 + 3   f(3,4)
"""

def find_min_cost(two_DArray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return two_DArray[0][0]
    else:
        option1 = find_min_cost(two_DArray, row-1, col)
        option2 = find_min_cost(two_DArray, row, col-1) 
        return two_DArray[row][col] + min(option1, option2)

twoDList = [
            [4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3],
]

print(find_min_cost(twoDList, 4,4))

