from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board
import pygame
from constants import *
import math, random

def rand_position():
    x = random.randrange(0, 750)
    y = random.randrange(0, 750)
    rand_pos = (x, y)
    return rand_pos

def rand_num():
    number = random.randrange(1, 9)
    return number

def main():
    try:
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                board = Board(width, height, screen, "easy")
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for r in range(0, 750, 82):
                        for c in range(0, 750, 82):
                            position = (r, c)
                            #if position.collidepoint(event.pos):
                #elif they click easy
                    for n in range(51):
                        pos = rand_position()
                        num = rand_num()
                        def valid(row, column, box):
                            return sorted(row, column, box) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        for box_row in range(0, 9, 3):
                            for box_col in range(0, 9, 3):
                                box = [board[row][col]
                                    for row in range(box_row, box_row + 3)
                                    for col in range(box_col, box_col + 3)]
                                font = pygame.font.SysFont('Times New Roman', 50)
                                number_print = font.render(str(num), True, 'Black')
                                Board.screen.blit(number_print, pos)
                                if not valid(box):
                                    break

                #elif they click medium:
                    for n in range(41):
                        pos = rand_position()
                        num = rand_num()
                        def valid(row, column, box):
                            return sorted(row, column, box) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        for box_row in range(0, 9, 3):
                            for box_col in range(0, 9, 3):
                                box = [board[row][col]
                                       for row in range(box_row, box_row + 3)
                                       for col in range(box_col, box_col + 3)]
                                font = pygame.font.SysFont('Times New Roman', 50)
                                number_print = font.render(str(num), True, 'Black')
                                Board.screen.blit(number_print, pos)
                                if not valid(box):
                                    break

                #elif they click hard:
                    for n in range(31):
                        pos = rand_position()
                        num = rand_num()
                        def valid(row, column, box):
                            return sorted(row, column, box) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

                        for box_row in range(0, 9, 3):
                            for box_col in range(0, 9, 3):
                                box = [board[row][col]
                                       for row in range(box_row, box_row + 3)
                                       for col in range(box_col, box_col + 3)]
                                font = pygame.font.SysFont('Times New Roman', 50)
                                number_print = font.render(str(num), True, 'Black')
                                Board.screen.blit(number_print, pos)
                                if not valid(box):
                                    break

#Buttons, calling functions, screen problem,