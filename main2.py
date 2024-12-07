from cell import Cell
from board import Board
import pygame
from constants import *
import random

def is_valid_move(board, row, col, num):
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def draw_game_start(screen):
    # Initialize fonts
    title_font = pygame.font.Font(None, 100)
    mode_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 45)

    # Clear screen
    screen.fill(SCREEN_COLOR)

    # Draw title
    title_text = title_font.render("Welcome to Sudoku", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 250))
    screen.blit(title_text, title_rect)

    # Draw mode selection text
    mode_text = mode_font.render("Select Game Mode:", True, BLACK)
    mode_rect = mode_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(mode_text, mode_rect)

    # Draw buttons
    button_positions = [(-200, "EASY", 30), (0, "MEDIUM", 40), (200, "HARD", 50)]
    buttons = {}
    for offset, label, value in button_positions:
        button_text = button_font.render(label, True, WHITE)
        button_surface = pygame.Surface((button_text.get_width() + 20, button_text.get_height() + 20))
        button_surface.fill(DARK_BLUE)
        button_surface.blit(button_text, (10, 10))
        button_rect = button_surface.get_rect(center=(WIDTH // 2 + offset, HEIGHT // 2 + 50))
        screen.blit(button_surface, button_rect)
        buttons[label] = (button_rect, value)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for label, (rect, value) in buttons.items():
                    if rect.collidepoint(event.pos):
                        return value

def generate_initial_board(num_cells):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    initial_board = Board(WIDTH, HEIGHT, screen, difficulty=0)
    filled_cells = 0
    while filled_cells < num_cells:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if initial_board.board[row][col] == 0:
            num = random.randint(1, 9)
            if is_valid_move(initial_board.board, row, col, num):
                initial_board.select(row, col)
                initial_board.place_number(num)
                filled_cells += 1
    initial_board.draw()  # Ensure the board is drawn completely
    pygame.display.update()  # Refresh the screen after the loop
    return initial_board
#print(board.place_number(board.cells[row][col].sketched_value))
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

    restart_surf = game_over_font.render('RESTART', 0, DARK_BLUE)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)

    menu_surf = game_over_font.render(
        'Press m to return to the main menu...', 0, DARK_BLUE)
    menu_rect = menu_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                return  # Exit this function to restart the main loop


def handle_board_events(board, screen):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            clicked_cell = board.click(*pos)
            if clicked_cell:
                board.select(*clicked_cell)
        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                board.sketch(event.key - pygame.K_0)
            elif event.key == pygame.K_RETURN:
                board.place_number()
    board.draw()
    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    # Select difficulty and generate the board
    difficulty = draw_game_start(screen)
    board = Board(WIDTH, HEIGHT, screen, difficulty)
    generate_initial_board(51)
    #board.board = initial_board

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                clicked_cell = board.click(*pos)
                row, col = clicked_cell
                if clicked_cell:
                    board.select(row, col)
            elif event.type == pygame.KEYDOWN:
                selected_row, selected_col = 0, 0
                if pygame.K_1 <= event.key <= pygame.K_9:
                    board.sketch(event.key - pygame.K_0)
                elif event.key == pygame.K_RETURN:
                    for row in range(board.board_rows):
                        for col in range(board.board_cols):
                            if board.cells[row][col].selected:
                                if board.cells[row][col].sketched_value != 0:
                                    board.place_number(board.cells[row][col].sketched_value)

                elif event.key == pygame.K_LEFT:
                    new_col = selected_col - 1
                    if new_col < 0:
                        new_col = 8
                    board.select(selected_row, new_col)
                    selected_col = new_col
                elif event.key == pygame.K_RIGHT:
                    new_col = selected_col + 1
                    if new_col > 8:
                        new_col = 0
                    board.select(selected_row, new_col)
                    selected_col = new_col
                elif event.key == pygame.K_UP:
                    new_row = selected_row - 1
                    if new_row < 0:
                        new_row = 8
                    board.select(new_row, selected_col)
                    selected_row = new_row
                elif event.key == pygame.K_DOWN:
                    new_row = selected_row + 1
                    if new_row > 8:
                        new_row = 0
                    board.select(new_row, selected_col)
                    selected_row = new_row
        board.draw()
        pygame.display.flip()
        #elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     board.sketch(1)
        #     board.draw()
        #     if event.type == pygame.K_RETURN:
        #         board.place_number(1)
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
        #     board.sketch(2)
        #     board.draw()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
        #     board.sketch(3)
        #     board.draw()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
        #     board.sketch(4)
        #     board.draw()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
        #     board.sketch(5)
        #     board.draw()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
        #     board.sketch(6)
        #     board.draw()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_7:
        #     board.sketch(7)
        #     board.draw()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
        #     board.sketch(8)
        #     board.draw()
        # elif event.type == pygame.KEYDOWN and event.key == pygame.K_9:
        #     board.sketch(9)
        #     board.draw()
        #
        # else:
        #     error_message('Invalid input', screen)
        if board.is_full():
            draw_game_over(screen, board.check_board())
            running = False

    pygame.quit()

if __name__ == '__main__':
    main()