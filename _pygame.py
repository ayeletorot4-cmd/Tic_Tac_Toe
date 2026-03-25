import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 300
CELL = WIDTH // 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

font = pygame.font.SysFont(None, 60)


# ---------- YOUR FUNCTIONS ----------

def create_board():
    board = [1,2,3,4,5,6,7,8,9]
    return board


def make_move(board, position, symbol):
    board[position-1] = symbol
    return board


def check_winner(board, symbol):

    if board[0]==board[1]==board[2]==symbol or\
       board[3]==board[4]==board[5]==symbol or\
       board[6]==board[7]==board[8]==symbol:
        return True

    elif board[0]==board[3]==board[6]==symbol or\
         board[1]==board[4]==board[7]==symbol or\
         board[2]==board[5]==board[8]==symbol:
        return True

    elif board[0]==board[4]==board[8]==symbol or\
         board[2]==board[4]==board[6]==symbol:
        return True

    return False


def is_tie(board):
    for num in range(1,10):
        if num in board:
            return False
    return True


def switch_player(current):
    if current == "X":
        return "0"
    else:
        return "X"


# ---------- PYGAME DRAW ----------

def draw_board(board):

    screen.fill((255,255,255))

    # grid
    for i in range(1,3):
        pygame.draw.line(screen,(0,0,0),(0,i*CELL),(WIDTH,i*CELL),3)
        pygame.draw.line(screen,(0,0,0),(i*CELL,0),(i*CELL,HEIGHT),3)

    # symbols
    for i in range(9):

        x = (i % 3) * CELL + CELL//3
        y = (i // 3) * CELL + CELL//4

        if board[i] == "X":
            text = font.render("X", True, (0,0,0))
            screen.blit(text,(x,y))

        if board[i] == "0":
            text = font.render("O", True, (0,0,0))
            screen.blit(text,(x,y))


# ---------- MAIN GAME ----------

def play_game():

    board = create_board()
    current_symbol = "X"
    game_over = False

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                x, y = pygame.mouse.get_pos()

                col = x // CELL
                row = y // CELL

                position = row * 3 + col + 1

                if board[position-1] not in ["X","0"]:

                    make_move(board, position, current_symbol)

                    if check_winner(board, current_symbol):
                        print(f"{current_symbol} wins!")
                        game_over = True

                    elif is_tie(board):
                        print("Tie!")
                        game_over = True

                    else:
                        current_symbol = switch_player(current_symbol)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return play_game()


        draw_board(board)
        pygame.display.update()


play_game()