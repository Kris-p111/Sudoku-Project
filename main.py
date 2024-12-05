# from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board
import pygame
from constants import *
import math, random


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    select_mode_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 45)


    # Color background
    screen.fill(SCREEN_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, BLACK)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 250))
    screen.blit(title_surface, title_rectangle)

    # Initialize and draw game mode
    title_surface = select_mode_font.render("Select Game Mode:", 0, BLACK)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("EASY", 0, WHITE)
    medium_text = button_font.render("MEDIUM", 0, WHITE)
    hard_text = button_font.render("HARD", 0, WHITE)

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(DARK_BLUE)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(DARK_BLUE)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(DARK_BLUE)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 50))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    hard_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 50))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    # Checks if user chooses easy mode
                    easy = 30
                    return easy
                    # return  # If the mouse is on the start button, we can return to main
                elif medium_rectangle.collidepoint(event.pos):
                    # Checks if user chooses medium mode
                    medium = 40
                    return medium
                elif hard_rectangle.collidepoint(event.pos):
                    # Checks if user chooses hard mode
                    hard = 50
                    return hard
        pygame.display.update()


def draw_other_buttons(screen):
    # Initialize title font
    buttons_font = pygame.font.Font(None, 50)

    # Initialize buttons
    # Initialize text first
    reset_text = buttons_font.render("RESET", 0, WHITE)
    restart_text = buttons_font.render("RESTART", 0, WHITE)
    exit_text = buttons_font.render("EXIT", 0, WHITE)

    # Initialize button background color and text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(DARK_BLUE)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(DARK_BLUE)
    restart_surface.blit(restart_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(DARK_BLUE)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 375))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 375))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 375))

    # Draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    buttons = [reset_rectangle, restart_rectangle, exit_rectangle]

    return buttons


# Handle user input errors
def error_message(error, screen):
    message_font = pygame.font.Font(None, 30)
    user_error_message = message_font.render(error, 0, DODGER_BLUE)

    # Initialize button background color and text
    error_message_surface = pygame.Surface(
        (user_error_message.get_size()[0] + 15, user_error_message.get_size()[1] + 15))
    error_message_surface.fill(BG_COLOR)
    error_message_surface.blit(user_error_message, (10, 10))
    error_message_rectangle = error_message_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 325))

    # Write message on the screen
    screen.blit(error_message_surface, error_message_rectangle)

    pygame.display.flip()  # Update the display

    pygame.time.delay(800)  # Display the message for 0.8 sec

    # Clear the error message from the screen
    screen.fill(BG_COLOR)
    pygame.display.flip()


def draw_game_over(screen, winner):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)

    if winner != 0:
        text = 'Game Won!'
    else:
        text = "Game Over :("

    game_over_surf = game_over_font.render(text, 0, DARK_BLUE)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    restart_surf = game_over_font.render(
        'RESTART', 0, DARK_BLUE)
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)

    #  Added key to return to main menu
    menu_surf = game_over_font.render(
        'Press m to return to the main menu...', 0, DARK_BLUE)
    menu_rect = menu_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)

    pygame.display.update()


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
        game_over = False
        winner = 0
        screen = pygame.display.set_mode((750, 900))
        pygame.init()
        running = True
        while running:
            dif = draw_game_start(screen)
            draw_other_buttons(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif dif == 30:
                    board = Board(750, 750, screen, dif)
                    for n in range(51):
                        pos = rand_position()
                        num = rand_num()
                        for r in range(0, 750, 82):
                            for c in range(0, 750, 82):
                                position = (r, c)
                                # if position.collidepoint(event.pos):
                                    # draw initial numbers
                                board.draw()
                        if not board.is_full():
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                # we need the coordinates of the click
                                x, y = board.click
                                board.select(x,y)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                                    board.sketch(1)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                                    board.sketch(2)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                                    board.sketch(3)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                                    board.sketch(4)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                                    board.sketch(5)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                                    board.sketch(6)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                                    board.sketch(7)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                                    board.sketch(8)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                                    board.sketch(9)
                                    board.draw()
                                else:
                                    error_message('Invalid input', screen)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                    #board.place_number()
                                    #parameter should be the selected cell's sketched value
                                    #board.draw()
                        else:
                            draw_game_over(screen, board.check_board())


                        def valid(row, column, box):
                            return sorted(row, column, box) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        for box_row in range(0, 9, 3):
                            for box_col in range(0, 9, 3):
                                box = [board[row][col]
                                    for row in range(box_row, box_row + 3)
                                    for col in range(box_col, box_col + 3)]
                                font = pygame.font.SysFont('Times New Roman', 50)
                                number_print = font.render(str(num), True, 'Black')
                                screen.blit(number_print, pos)
                                if not valid(box):
                                    break

                elif dif == 40:
                    board = Board(750, 750, screen, dif)
                    for n in range(41):
                        pos = rand_position()
                        num = rand_num()
                        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for r in range(0, 750, 82):
                            for c in range(0, 750, 82):
                                position = (r, c)
                                # if position.collidepoint(event.pos):
                                    # draw initial numbers
                                board.draw()
                        if not board.is_full():
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                # we need the coordinates of the click
                                x, y = board.click
                                board.select(x, y)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                                    board.sketch(1)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                                    board.sketch(2)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                                    board.sketch(3)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                                    board.sketch(4)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                                    board.sketch(5)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                                    board.sketch(6)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                                    board.sketch(7)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                                    board.sketch(8)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                                    board.sketch(9)
                                    board.draw()
                                else:
                                    error_message('Invalid input', screen)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            # board.place_number()
                            # parameter should be the selected cell's sketched value
                            # board.draw()
                        else:
                            draw_game_over(screen, board.check_board())

                    def valid(row, column, box):
                            return sorted(row, column, box) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        for box_row in range(0, 9, 3):
                            for box_col in range(0, 9, 3):
                                box = [board[row][col]
                                       for row in range(box_row, box_row + 3)
                                       for col in range(box_col, box_col + 3)]
                                font = pygame.font.SysFont('Times New Roman', 50)
                                number_print = font.render(str(num), True, 'Black')
                                screen.blit(number_print, pos)
                                if not valid(box):
                                    break

                elif dif == 50:
                    board = Board(750, 750, screen, dif)
                    for n in range(31):
                        pos = rand_position()
                        num = rand_num()
                        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        for r in range(0, 750, 82):
                            for c in range(0, 750, 82):
                                position = (r, c)
                                # if position.collidepoint(event.pos):
                                    # draw initial numbers
                                board.draw()
                        if not board.is_full():
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                # we need the coordinates of the click
                                x, y = board.click
                                board.select(x, y)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                                    board.sketch(1)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                                    board.sketch(2)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                                    board.sketch(3)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                                    board.sketch(4)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                                    board.sketch(5)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                                    board.sketch(6)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                                    board.sketch(7)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                                    board.sketch(8)
                                    board.draw()
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                                    board.sketch(9)
                                    board.draw()
                                else:
                                    error_message('Invalid input', screen)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            # board.place_number()
                            # parameter should be the selected cell's sketched value
                            # board.draw()
                        else:
                            draw_game_over(screen, board.check_board())

                        def valid(row, column, box):
                            return sorted(row, column, box) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

                        for box_row in range(0, 9, 3):
                            for box_col in range(0, 9, 3):
                                box = [board[row][col]
                                       for row in range(box_row, box_row + 3)
                                       for col in range(box_col, box_col + 3)]
                                font = pygame.font.SysFont('Times New Roman', 50)
                                number_print = font.render(str(num), True, 'Black')
                                screen.blit(number_print, pos)
                                if not valid(box):
                                    break
    finally:
        pygame.quit()


if __name__ == "__main__":
     main()
#Buttons, calling functions, screen problem,problem,