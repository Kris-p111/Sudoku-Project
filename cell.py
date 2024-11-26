import pygame
from constants import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self, screen):
        # Calculate the width and height of the Sudoku board
        BOARD_WIDTH = 9 * CELL_SIZE
        BOARD_HEIGHT = 9 * CELL_SIZE

        # Calculate the starting position to center the board
        board_start_x = (WIDTH - BOARD_WIDTH) // 2
        board_start_y = (HEIGHT - BOARD_HEIGHT) // 2 - 70  # move board up ~ 70 px

        # Draw the cell rectangle
        cell_rect = pygame.Rect(board_start_x + self.col * CELL_SIZE, board_start_y + self.row * CELL_SIZE, CELL_SIZE,
                                CELL_SIZE)
        pygame.draw.rect(screen, BLACK, cell_rect, CELL_LINE_WIDTH)

        # Draw a thicker border for the cell if selected
        if self.selected:
            pygame.draw.rect(screen, BLUE, cell_rect, 6)

        # Draw the cell value (if not zero)
        if self.value != 0 and self.sketched_value == 0:
            cell_font = pygame.font.Font(None, 55)
            cell_surf = cell_font.render(str(self.value), True, BLACK)
            cell_rect = cell_surf.get_rect(
                center=(board_start_x + self.col * CELL_SIZE + CELL_SIZE // 2,
                        board_start_y + self.row * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(cell_surf, cell_rect)

        # Draw the value using user input
        if self.sketched_value != 0:
            cell_font = pygame.font.Font(None, 50)
            cell_surf = cell_font.render(str(self.sketched_value), True, USER_NUMBER_COLOR)
            # draw the value in the upper left corner (not center)
            cell_rect = cell_surf.get_rect(
                center=((board_start_x + self.col * CELL_SIZE + CELL_SIZE // 2) - 12,
                        (board_start_y + self.row * CELL_SIZE + CELL_SIZE // 2) - 12))
            screen.blit(cell_surf, cell_rect)