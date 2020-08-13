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


    def find_empty_slot(self, sudokuBoard):
        for column in range(9):
            for row in range(9):
                if sudokuBoard[column][row] == 0:
                    return True
        return False

    
    def possible(self, y, x, number):
        self.board

        for i in range(1, 9):
            if self.board[i][y] == number:
                return False
        for i in range(1, 9):
            if self.board[x][i] == number:
                return False

        return True


    def solve(self):
        """
        Solves the unsolved sudoku board with the backtracking algorithm
        and with some cunfusing recursion which I still do not get
        """

        grid = self.board
        self.find_empty_slot(grid)


        

    def display(self):
        """
        Displays the sudoku board with 9 tiles like a real sudoku board
        """
        pass
