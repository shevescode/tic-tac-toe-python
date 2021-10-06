def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [ 
        [ '.','.','.' ],
        [ '.','.','.' ],
        [ '.','.','.' ] ]
    return board

def get_move(board, player):
    # ask for user input and returs as 2 integers
    """Returns the coordinates of a valid move for player on board."""
    board = init_board()
    while True:
        print('What is your next move?')
        user_move = list(input())
        row = user_move[0]
        col = user_move[1]
        if row == "A":
            row = 0
        elif row == "B":
            row = 1
        elif row == "C":
            row = 2
        else:
            print('Please provide valid coordinates!')
            continue
        if col == "1":
            col = 0
        elif col == "2":
            col = 1
        elif col == "3":
            col = 2
        else:
            print('Please provide valid coordinates!')
            continue
        print(row)
        print(col)
        return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print("\n    1   2   3 \n")
    print("A   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("B   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("C   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
