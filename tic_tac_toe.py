def create_board():
    """
    :return: empty board
    """
    board = [1,2,3,4,5,6,7,8,9]

    return board


def print_board(board):
    """
    :param board: board
    :return: print board
    """
    for y in range(0,9,3):
       print(f" {board[y]} | {board[y+1]} | {board[y+2]} ")
       if y<6:
          print("___+___+___")


def get_move(player, board):
    """
    Asking the player to choose a spot. Must handle: Not a number · Number not between 1–9 · Occupied spot
    :param player:
    :param board:
    :return: position
    """
    while True:
          position=input(f" {player} Choose a spot from 1-9 or 'r' to reset:")

          if position.lower()=="r":
              return "reset"
          if not position.isdigit():
            print("Please enter a number from 1-9")
            continue

          position=int(position)
          if position not in range(1,10):
              print("Please enter a number from 1-9")
              continue

          if board[position-1] in ["X", "0"]:
              print("This position is already taken")
              continue

          return position

def make_move(board, position, symbol):

    """
    Updates the board at the chosen position with the player's symbol
    :param board: board
    :param position: position
    :param symbol: symbol
    :return: updated board
    """

    board[position-1] = symbol
    return board

def check_winner(board, symbol):
    """
    :param board: board
    :param symbol: symbol
    :return:Returns True if the symbol has 3 in a row (row, column, or diagonal)
    """
    #check win in row
    if board[0]==board[1]==board[2]==symbol or\
            board[3]==board[4]==board[5] ==symbol or\
            board[6]==board[7]==board[8]==symbol:
        return True

    #check win in column
    elif board[0]==board[3]==board[6]==symbol or\
            board[1]==board[4]==board[7]==symbol or\
            board[2]==board[5]==board[8]==symbol:
        return True
    #check win in triangle
    elif board[0]==board[4]==board[8]==symbol or\
            board[2]==board[4]==board[6]==symbol:
        return True
    else:
        return False



def is_tie(board):
    """
    :param board: board
    :return: True if no moves are left and there is no winner

    """
    for num in range(1,10):
        if num  in board:
            return False

    return True


def switch_player(current):
    """
    Switches the current player between X and O
    :param current: current player
    :return:

    """
    if current == "X":
        return "0"
    else:
        return "X"


def updat_score(board,symbol,scores):

    check_winner(board, symbol)
    scores[symbol] += 1
    return scores



def play_game():
    """

    :return:
    """
    board = create_board()
    current_symbol = "X"

    while True:
        print_board(board)
        print(f"--- {current_symbol}'s Turn ---")

        position = get_move(current_symbol, board)
        if position == "reset":
            print("\n NEW GAME STARTED ")
            return play_game()
        make_move(board, position, current_symbol)

        if check_winner(board, current_symbol):
            print_board(board)

            print(f"Player {current_symbol} wins!")
            print(updat_score(board,current_symbol,scores))
            break

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_symbol = switch_player(current_symbol)

    user_choice = input("Game Over! Up for another round?\n 1.YES \n 2.NO\n")
    if user_choice == "1":
        print(" \n NEW GAME STARTED ")
        play_game()

scores = {"X": 0, "0": 0}
play_game()