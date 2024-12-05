import pygame
from constants import *
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = 750
        self.height = 900
        self.screen = pygame.display.set_mode((width, height))
        self.difficulty = difficulty
        self.board_rows = 9
        self.board_cols = 9
        self.board_line_width = 5
        self.cell_size = 82
        self.cells = [[Cell(self.board[row][col], row, col, self.screen)
                       for col in range(self.board_cols)]
                      for row in range(self.board_rows)]
        difficulty_levels = {"easy": 30, "medium": 40, "hard": 50}
        if self.difficulty in difficulty_levels:
            self.empty_cells = difficulty_levels[self.difficulty]
        else:
            raise ValueError("Invalid difficulty level")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.original = [row[:] for row in self.board]

    def draw(self):
        # Calculate the width and height of the board
        BOARD_WIDTH = 9 * CELL_SIZE
        BOARD_HEIGHT = 9 * CELL_SIZE

        # Calculate the starting position
        board_start_x = (WIDTH - BOARD_WIDTH) // 2
        board_start_y = (HEIGHT - BOARD_HEIGHT) // 2 - 70  # move board up ~ 70 px

        # Draw the cells
        for row in self.cells:
            for cell in row:
                cell_rect = pygame.Rect(board_start_x + cell.col * CELL_SIZE, board_start_y + cell.row * CELL_SIZE,
                                        CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, SCREEN_COLOR, cell_rect)
                cell.draw(self.screen)

        # Draw the squares for the board
        for i in range(0, 4):
            pygame.draw.line(self.screen, BLACK,
                             (board_start_x, board_start_y + (3 * i) * CELL_SIZE),
                             (board_start_x + BOARD_WIDTH, board_start_y + (3 * i) * CELL_SIZE),
                             BOARD_LINE_WIDTH)

        for i in range(0, 4):
            pygame.draw.line(self.screen, BLACK,
                             (board_start_x + (3 * i) * CELL_SIZE, board_start_y),
                             (board_start_x + (3 * i) * CELL_SIZE, board_start_y + BOARD_HEIGHT),
                             BOARD_LINE_WIDTH)

    # Marks the cell at (row, col) in the board as the current selected cell
    def select(self, row, col):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                if i == row and j == col:
                    self.cells[i][j].selected = True
                else:
                    self.cells[i][j].selected = False

    # returns a tuple of the (row, col) of the cell which was clicked
    def click(self, x, y):
        # Calculate the width and height of the board
        BOARD_WIDTH = 9 * CELL_SIZE
        BOARD_HEIGHT = 9 * CELL_SIZE

        # Calculate the starting position
        board_start_x = (WIDTH - BOARD_WIDTH) // 2
        board_start_y = (HEIGHT - BOARD_HEIGHT) // 2 - 70  # move board up ~ 70 px

        # if coordinates inside the board (which calculated by adding board's width and height to the starting points)
        if board_start_x <= x < board_start_x + BOARD_WIDTH and board_start_y <= y < board_start_y + BOARD_HEIGHT:
            clicked_row = (y - board_start_y) // CELL_SIZE
            clicked_col = (x - board_start_x) // CELL_SIZE
            return clicked_row, clicked_col

        return None

    # allows user to remove the cell values and sketched value that are filled by themselves
    def clear(self):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                if self.cells[i][j].selected:
                    # check if it's an empty cell in the original board
                    if self.board[i][j] == 0:
                        self.cells[i][j].sketched_value = 0
                        self.cells[i][j].value = 0

    def sketch(self, value):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].selected:
                    if self.board[col][row] == 0:
                        self.cells[col][row].set_sketched_value(value)
        # sketched_val = str(value)
        # font = pygame.font.SysFont('Times New Roman', 100)
        # number_print = font.render(sketched_val, True, 'Grey')
        # self.screen.blit(number_print, (selected_cell[0], selected_cell[1]))
        # pygame.display.update()

    def place_number(self, value):
        self.value = value
        sketched_val = str(self.value)
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.cells[col][row].selected:
                    if self.board[col][row] == 0:
                        self.cells[col][row].set_sketched_value(0)
                        self.cells[col][row].set_cell_value(value)
        # x = selected_cell[0] * 82
        # y = selected_cell[1] * 82
        # font = pygame.font.SysFont('Times New Roman', 50)
        # number_print = font.render(sketched_val, True, 'Black')
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RETURN:
        #             self.screen.blit(number_print, (x, y))

    def reset_to_original(self):
        super().__init__()
        self.board = self.original

    def is_full(self):
        for row in self.board:
            for square in row:
                if square == '':
                    return False
        return True

    def update_board(self):
        for row in self.board:
            for col in self.board:
                font = pygame.font.SysFont('Times New Roman', 50)
                number_print = font.render(str(self.value), True, 'Black')
                x = col * 82
                y = row * 82
                self.screen.blit(number_print, (x, y))
        pygame.display.update()

    def find_empty(self):
        # loop through cells and find empty, then return row and col as tuple
        for row in self.board:
            for col in self.board:
                if self.board[row][col] == '0':
                    tup = (row, col)
                    return tup

    def check_board(self):
        def valid(row, column, box):
            return sorted(row, column, box) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for row in self.board_rows:
            if not valid(row):
                return False
        for col in self.board_cols:
            if not valid(col):
                return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = [self.board[row][col]
                       for row in range(box_row, box_row + 3)
                       for col in range(box_col, box_col + 3)]
                if not valid(box):
                    return False
        return True