"""
Number of paths to reach the last cell
    Problem Statement
    - 2D Matrix is given
    - Each cell has a cost associated with it for accessing
    - We need to start from (0,0) cell an go till (n-1, n-1) cell
    - We can go only to right or down cell from current cell
    - We are given total cost to reach the last cell
    - Find the number of ways to reach end of matrix with given "total cost"

    Subproblem:
        Option1 = y + 2 = 22 => f(row3, col4, 22)
                                                    =>Sum(Option1, Option2)
        Option2 = z + 6 = 22 => f(row4, col3, 22)
"""

def number_of_paths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return number_of_paths(twoDArray, 0, col-1, cost-twoDArray[row][col])
    elif col == 0:
        return number_of_paths(twoDArray, row-1, 0, cost-twoDArray[row][col])
    else:
        opt1 = number_of_paths(twoDArray, row-1, col, cost-twoDArray[row][col])
        opt2 = number_of_paths(twoDArray, row, col-1, cost-twoDArray[row][col])
        return opt1 + opt2

twoDArray =[
            [4, 7, 1, 6],
            [5, 7, 3, 9],
            [3, 2, 1, 2],
            [7, 1, 6, 3],
]

print(number_of_paths(twoDArray, 3, 3, 45))