"""
    Medium #79
    Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells.
    "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    def solution(self, board, word, x, y, curr):
        if (x < 0 or x >= len(board) or y < 0 or y>= len(board) or board[x][y] == ''):
            return False
        curr += board[x][y]
        if (len(curr)>len(word)):
            return False
        if (curr[len(curr)-1] != word[len(curr)-1]):
            return False
        if (curr == word):
            return True 
        temp = board[x][y]
        board[x][y] = ' '

        #loop of size 4(number of neighboring chars)
        for i in range(4):
            if (self.solution(board, word, x + self.dx[i], y+self.dy[i], curr)):
                return True 

        board[x][y] = temp
        return False


    def exist(self, board: list[list[str]], word: str)->bool:
        if (len(word) == 0):
            return True 
        n = len(board)
        for i in range(n):
            m = len(board[i])
            for j in range(m):
                if (word[0] == board[i][j] and self.solution(board, word, i, j, "")):
                    return True 
        return False