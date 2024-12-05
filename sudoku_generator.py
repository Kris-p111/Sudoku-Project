import math, random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell)
            if cell != 0 else "0" for cell in row))

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False

        for i in range(9):
            if self.board[i][col] == num:
                return False

        box_start_row = row - row % 3
        box_start_col = col - col % 3
        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def fill_box(self, row_start, col_start):
        from random import shuffle
        nums = list(range(1, 10))
        shuffle(nums)
        idx = 0
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                self.board[i][j] = nums[idx]
                idx += 1


    def fill_diagonal(self):
        for i in range(0, 9, 3):
            self.fill_box(i, i)


    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        from random import randint

        num_to_remove = 30
        count = 0
        while count < num_to_remove:
            row = randint(0, 8)
            col = randint(0, 8)
            if self.board[row][col] != 0:  # Only remove if the cell is not already empty
                self.board[row][col] = 0
                count += 1

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
