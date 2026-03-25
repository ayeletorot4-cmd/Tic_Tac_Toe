import pygame
import sys


# --- ORIGINAL LOGIC FUNCTIONS ---

def create_board():
    """Returns a list representing the 3x3 board positions 1-9."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_winner(board, symbol):
    """Checks all winning combinations (rows, columns, diagonals)."""
    # Check rows
    if (board[0] == board[1] == board[2] == symbol or
            board[3] == board[4] == board[5] == symbol or
            board[6] == board[7] == board[8] == symbol):
        return True
    # Check columns
    elif (board[0] == board[3] == board[6] == symbol or
          board[1] == board[4] == board[7] == symbol or
          board[2] == board[5] == board[8] == symbol):
        return True
    # Check diagonals
    elif (board[0] == board[4] == board[8] == symbol or
          board[2] == board[4] == board[6] == symbol):
        return True
    return False


def is_tie(board):
    """Returns True if no numbers are left in the board list (all spots filled)."""
    return all(isinstance(x, str) for x in board)


# --- PYGAME CONFIGURATION ---

pygame.init()
WIDTH, HEIGHT = 300, 400  # Extra 100px height for the UI/Button area
SQUARE_SIZE = 100
LINE_WIDTH = 5

# Colors (RGB)
BG_COLOR = (28, 170, 156)  # Teal background
LINE_COLOR = (23, 145, 135)  # Darker teal for grid lines
X_COLOR = (84, 84, 84)  # Dark grey for X
O_COLOR = (239, 231, 200)  # Off-white for O
BUTTON_COLOR = (255, 255, 255)  # White for reset button
TEXT_COLOR = (0, 0, 0)  # Black for button text

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.SysFont("Arial", 24, bold=True)


# --- DRAWING HELPERS ---

def draw_lines():
    """Draws the 3x3 grid lines."""
    screen.fill(BG_COLOR)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)


def draw_figures(board):
    """Iterates through the board list and draws X or O on the screen."""
    for idx, spot in enumerate(board):
        row, col = idx // 3, idx % 3
        # Calculate center of the square for drawing
        center = (col * 100 + 50, row * 100 + 50)

        if spot == 'X':
            # Draw two diagonal lines for X
            pygame.draw.line(screen, X_COLOR, (col * 100 + 25, row * 100 + 75), (col * 100 + 75, row * 100 + 25), 10)
            pygame.draw.line(screen, X_COLOR, (col * 100 + 25, row * 100 + 25), (col * 100 + 75, row * 100 + 75), 10)
        elif spot == 'O':
            # Draw a circle for O
            pygame.draw.circle(screen, O_COLOR, center, 30, 8)


def draw_button(text):
    """Draws a clickable 'Play Again' button."""
    button_rect = pygame.Rect(50, 330, 200, 45)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)
    text_surf = font.render(text, True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)
    return button_rect


# --- MAIN GAME LOOP ---

def main():
    board = create_board()
    player = "X"
    game_over = False
    status_message = f"Turn: {player}"

    while True:
        draw_lines()
        draw_figures(board)

        # Display either the current turn or the final result + Play Again button
        if not game_over:
            msg_surf = font.render(status_message, True, (255, 255, 255))
            screen.blit(msg_surf, (WIDTH // 2 - msg_surf.get_width() // 2, 335))
            button_rect = None
        else:
            # Game ended: show result and the reset button
            res_surf = font.render(status_message, True, (255, 255, 255))
            screen.blit(res_surf, (WIDTH // 2 - res_surf.get_width() // 2, 305))
            button_rect = draw_button("Play Again")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos  # Get (x, y) of the mouse click

                # Logic for clicking 'Play Again'
                if game_over and button_rect and button_rect.collidepoint(pos):
                    board = create_board()
                    player = "X"
                    game_over = False
                    status_message = f"Turn: {player}"

                # Logic for clicking a square on the board
                elif not game_over and pos[1] < 300:
                    clicked_row = pos[1] // 100
                    clicked_col = pos[0] // 100
                    idx = clicked_row * 3 + clicked_col

                    # If the spot is still a number (not 'X' or 'O')
                    if isinstance(board[idx], int):
                        board[idx] = player

                        if check_winner(board, player):
                            status_message = f"Player {player} Wins!"
                            game_over = True
                        elif is_tie(board):
                            status_message = "It's a Tie!"
                            game_over = True
                        else:
                            # Switch player and update message
                            player = "O" if player == "X" else "X"
                            status_message = f"Turn: {player}"

        pygame.display.update()


if __name__ == "__main__":
    main()