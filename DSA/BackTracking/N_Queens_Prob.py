"""
    Place N queens on an NxN chess board, in such a manner that no two queens can attack each other.

    Bounding Condition
    -Not Same Column
    -Not Same Row
    -Not Diagonal
"""

class NQueen:
    def __init__(self, n):
        self.board_size= n
        self.chess_table = [[0 for row in range(n)] for col in range(n)]

    def print_queens(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.chess_table[row][col] == 1:
                    print(" Q ", end = '')
                else:
                    print(" - ", end = '')
            print("\n")

    def is_place_safe(self, row_index, col_index):
        """Returns True if the loc is safe to place a queen"""
        #Check horizontally
        for col in range(self.board_size):
            if self.chess_table[row_index][col] == 1:
                return False

        #check diagonal from current positon to top left
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break 
            if self.chess_table[i][j] == 1:
                return False

            j = j - 1

        #check diagonal from current position to bottom left
        j = col_index
        for i in range(row_index,  self.board_size):
            if i < 0:
                break 
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1

        return True 

    def solve(self, col_index):
        if col_index == self.board_size:
            return True 

        for row_index in range(self.board_size):
            if self.is_place_safe(row_index, col_index):
                self.chess_table[row_index][col_index] = 1
                if self.solve(col_index+1):
                    return True 
                # Perform back Tracking
                self.chess_table[row_index][col_index] = 0
        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("There is no solution for this problem")





queens = NQueen(4)
queens.solve_NQueens()
