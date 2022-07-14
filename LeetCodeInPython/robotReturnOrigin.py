"""
#657
    Imagine a robbot standing at position (0,0) in a 2D grid, given a string consisting of its moves, judge if this robot ends up at (0,0) after it completes
    its moves

"""

class Solution:
    def judgeCircle(self, moves: str)->bool:
        x = 0;
        y= 0;
        for move in moves:
            if (move == "U"):
                y +=1
            elif (move == "R"):
                x +=1
            elif (move == 'D'):
                y -=1
            elif (move == 'L'):
                x -=1

        return x == 0 and y ==0

sol = Solution()
Input = "LL"
print(sol.judgeCircle(Input))
