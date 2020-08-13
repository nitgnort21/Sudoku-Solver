import unittest
from sudoku import sudoku

class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        my_sudoku = sudoku()
        self.assertEqual(my_sudoku.get_sudoku(), [[0] * 9] * 9)

    # http://elmo.sbs.arizona.edu/sandiway/sudoku/examples.html
    def test_1(self):
        init_board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                      [6, 8, 0, 0, 7, 0, 0, 9, 0],
                      [1, 9, 0, 0, 0, 4, 5, 0, 0],
                      [8, 2, 0, 1, 0, 0, 0, 4, 0],
                      [0, 0, 4, 6, 0, 2, 9, 0, 0],
                      [0, 5, 0, 0, 0, 3, 0, 2, 8],
                      [0, 0, 9, 3, 0, 0, 0, 7, 4],
                      [0, 4, 0, 0, 5, 0, 0, 3, 6],
                      [7, 0, 3, 0, 1, 8, 0, 0, 0]]
        solved_board = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
                        [6, 8, 2, 5, 7, 1, 4, 9, 3],
                        [1, 9, 7, 8, 3, 4, 5, 6, 2],
                        [8, 2, 6, 1, 9, 5, 3, 4, 7],
                        [3, 7, 4, 6, 8, 2, 9, 1, 5],
                        [9, 5, 1, 7, 4, 3, 6, 2, 8],
                        [5, 1, 9, 3, 2, 6, 8, 7, 4],
                        [2, 4, 8, 9, 5, 7, 1, 3, 6],
                        [7, 6, 3, 4, 1, 8, 2, 5, 9]]
        my_sudoku = sudoku()
        my_sudoku.set_sudoku(init_board)
        my_sudoku.solve()
        self.assertEqual(my_sudoku.get_sudoku(), solved_board)

    def test_2(self):
        init_board = [[1, 0, 0, 4, 8, 9, 0, 0, 6],
                      [7, 3, 0, 0, 0, 0, 0, 4, 0],
                      [0, 0, 0, 0, 0, 1, 2, 9, 5],
                      [0, 0, 7, 1, 2, 0, 6, 0, 0],
                      [5, 0, 0, 7, 0, 3, 0, 0, 8],
                      [0, 0, 6, 0, 9, 5, 7, 0, 0],
                      [9, 1, 4, 6, 0, 0, 0, 0, 0],
                      [0, 2, 0, 0, 0, 0, 0, 3, 7],
                      [8, 0, 0, 5, 1, 2, 0, 0, 4]]
        solved_board = [[1, 5, 2, 4, 8, 9, 3, 7, 6],
                        [7, 3, 9, 2, 5, 6, 8, 4, 1],
                        [4, 6, 8, 3, 7, 1, 2, 9, 5],
                        [3, 8, 7, 1, 2, 4, 6, 5, 9],
                        [5, 9, 1, 7, 6, 3, 4, 2, 8],
                        [2, 4, 6, 8, 9, 5, 7, 1, 3],
                        [9, 1, 4, 6, 3, 7, 5, 8, 2],
                        [6, 2, 5, 9, 4, 8, 1, 3, 7],
                        [8, 7, 3, 5, 1, 2, 9, 6, 4]]
        my_sudoku = sudoku()
        my_sudoku.set_sudoku(init_board)
        my_sudoku.solve()
        self.assertEqual(my_sudoku.get_sudoku(), solved_board)

    def test_3(self):
        init_board = [[0, 2, 0, 6, 0, 8, 0, 0, 0],
                      [5, 8, 0, 0, 0, 9, 7, 0, 0],
                      [0, 0, 0, 0, 4, 0, 0, 0, 0],
                      [3, 7, 0, 0, 0, 0, 5, 0, 0],
                      [6, 0, 0, 0, 0, 0, 0, 0, 4],
                      [0, 0, 8, 0, 0, 0, 0, 1, 3],
                      [0, 0, 0, 0, 2, 0, 0, 0, 0],
                      [0, 0, 9, 8, 0, 0, 0, 3, 6],
                      [0, 0, 0, 3, 0, 6, 0, 9, 0]]
        solved_board = [[1, 2, 3, 6, 7, 8, 9, 4, 5],
                        [5, 8, 4, 2, 3, 9, 7, 6, 1],
                        [9, 6, 7, 1, 4, 5, 3, 2, 8],
                        [3, 7, 2, 4, 6, 1, 5, 8, 9],
                        [6, 9, 1, 5, 8, 3, 2, 7, 4],
                        [4, 5, 8, 7, 9, 2, 6, 1, 3],
                        [8, 3, 6, 9, 2, 4, 1, 5, 7],
                        [2, 1, 9, 8, 5, 7, 4, 3, 6],
                        [7, 4, 5, 3, 1, 6, 8, 9, 2]]
        my_sudoku = sudoku()
        my_sudoku.set_sudoku(init_board)
        my_sudoku.solve()
        self.assertEqual(my_sudoku.get_sudoku(), solved_board)

    def testPossible(self):
        init_board = [[0, 2, 0, 6, 0, 8, 0, 0, 0],
                      [5, 8, 0, 0, 0, 9, 7, 0, 0],
                      [0, 0, 0, 0, 4, 0, 0, 0, 0],
                      [3, 7, 0, 0, 0, 0, 5, 0, 0],
                      [6, 0, 0, 0, 0, 0, 0, 0, 4],
                      [0, 0, 8, 0, 0, 0, 0, 1, 3],
                      [0, 0, 0, 0, 2, 0, 0, 0, 0],
                      [0, 0, 9, 8, 0, 0, 0, 3, 6],
                      [0, 0, 0, 3, 0, 6, 0, 9, 0]]
        my_sudoku = sudoku()
        my_sudoku.set_sudoku(init_board)
        self.assertTrue(my_sudoku.possible(1, 3, 3))
        self.assertFalse(my_sudoku.possible(1, 3, 4))


if __name__ == '__main__':
    unittest.main()