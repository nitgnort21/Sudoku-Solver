import numpy

class sudoku():
    def __init__(self):
        """
        Initiates the sudoku board
        """

        self.board = [[0] * 9] * 9


    def get_sudoku(self):
        """
        Returns a recieved sudoku board which is solved or unsolved
        """
        
        return self.board


    def set_sudoku(self, sudokuBoard):
        self.board = sudokuBoard

    
    def possible(self, y, x, number):
        """
        Return if number given is possible to be placed in the sudoku
        board in the given cordinates
        """

        # Checks in the columns
        for i in range(1, 9): 
            if self.board[i][y] == number:
                return False

        # Checks in the rows
        for i in range(1, 9):
            if self.board[x][i] == number:
                return False

        # Checks in the squares

        y0 = y // 3 * 3 # Make sense of this later Trongtin, or else you will hate yourself
        x0 = x // 3 * 3

        for i in range(3):
            for j in range(3):
                if self.board[y0 + i][x0  + j] == number:
                    return False

        return True

        # The version of the small brain

        # if 1 <= y <= 3:
        #     if 1 <= x <= 3:
        #         i, j = 1, 1
        #     elif 4 <= x <= 6:
        #         i, j = 1, 4
        #     elif 7 <= x <= 9:
        #         i, j = 1, 7
        # elif 4 <= y <= 6:
        #     if 1 <= x <= 3:
        #         i, j = 4, 1
        #     elif 4 <= x <= 6:
        #         i, j = 4, 4
        #     elif 7 <= x <= 9:
        #         i, j = 4, 7
        # elif 7 <= y <= 9:
        #     if 1 <= x <= 3:
        #         i, j = 7, 1
        #     elif 4 <= x <= 6:
        #         i, j = 7, 4
        #     elif 7 <= x <= 9:
        #         i, j = 7, 7

        # for _ in range(2):
        #     for _ in range(2):
        #         if self.board[i][j] == number:
        #             return False
                
        #         j += 1
        #     i += 1

    def findEmpty(self):
        for column in range(9):
            for row in range(9):
                if self.board[column][row] == 0:
                    return column, row
        return None

    def solve(self):
        """
        Solves the unsolved sudoku board with the backtracking algorithm
        and with some cunfusing recursion which I still do not get
        """

        # column, row = self.findEmpty()
        #
        # for number in range(1, 10):
        #     if self.possible(column, row, number):
        #         self.board[column][row] = number
        #         self.solve()
        #         self.board[column][row] = 0
        # return
        if self.findEmpty() is None:
            return True  # soduku is solved
        row, col = self.findEmpty()

        for i in range(1, 10):
            # YOUR CODE HERE

        return False  # soduku is unsolvable


    def display(self):
        """
        Displays the sudoku board with 9 tiles like a real sudoku board
        """
        pass
