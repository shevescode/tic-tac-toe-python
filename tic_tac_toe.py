import sys
import random

def get_move(board):
    # ask for user input and returs as 2 integers
    """Returns the coordinates of a valid move for player on board."""
    while True:
        print('What is your next move?')
        user_move = input()
        row = user_move[0]
        col = user_move[1]
        rows = ["A","B","C"]
        cols = ["1","2","3"]
        if user_move == 'quit':
            exit()
        if row in rows and col in cols:
            row = rows.index(row)
            col = cols.index(col)
        else:
            print('Please provide valid coordinates!')
            continue
        if board[row][col] == ".":
            return row, col
        else:
            print('Please provide valid coordinates!')
            continue


def get_ai_move(board):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    if board[1][1] == ".":
        row, col = 1, 1
        return row, col
    else:
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == ".":
                return row, col
            else:
                continue



def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if board[row][col] == ".":
        board[row][col] = player
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    
    vertical_check = [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][0], board[1][0], board[2][0]]]

    diagonal_check = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]]

    # horizontal check

    for row in board:
        has_row_won = True
        for field in row:
            if field != player:
                has_row_won = False
                break
        if has_row_won:
            return True

    # vertical check

    for col in vertical_check:
        has_col_won = True
        for field in col:
            if field != player:
                has_col_won = False
                break
        if has_col_won:
            return True

    # diagonal check
    
    for dia in diagonal_check:
        has_dia_won = True
        for field in dia:
            if field != player:
                has_dia_won = False
                break
        if has_dia_won:
            return True


def is_full(board):
    """Returns True if board is full."""
    if not '.' in board[0] and not '.' in board[1] and not '.' in board[2]:
        return True
    else:
        return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    print("\n    1   2   3")
    print("A   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("B   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("C   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    print(f'Congratulations! Player {winner} has won!')


def tictactoe_game_human():
    board = [ 
        [ '.','.','.' ],
        [ '.','.','.' ],
        [ '.','.','.' ] ]
    print_board(board)
    player = "X"
    while True:
        row, col = get_move(board)
        mark(board, player, row, col)
        print_board(board)
        winner = player
        if has_won(board, player):
            return print_result(winner)
        if is_full(board):
            return print("No winner! It is a tie!")
        if player == "X":
            player = "O"
        else:
            player = "X"

def tictactoe_game_ai():
    board = [ 
        [ '.','.','.' ],
        [ '.','.','.' ],
        [ '.','.','.' ] ]
    player = "X"
    while True:
        if player == "X":
            row, col = get_ai_move(board)
            mark(board, player, row, col)
            print_board(board)
            winner = player
        if has_won(board, player):
            return print_result(winner)
        if is_full(board):
            return print("No winner! It is a tie!")
        player = "O"


        if player == "O":
            row, col = get_move(board)
            mark(board, player, row, col)
            print_board(board)
            winner = player
        if has_won(board, player):
            return print_result(winner)
        if is_full(board):
            return print("No winner! It is a tie!")
        player = "X"



def main_menu():
    if len(sys.argv) > 1 and sys.argv[1] == "HUMAN-AI":
        print("\n########################################")
        print(" Welcome to 3x3 Tic Tac Toe HUMAN-AI! ")
        print("########################################")
        tictactoe_game_ai()
    else:
        print("\n########################################")
        print(" Welcome to 3x3 Tic Tac Toe HUMAN-HUMAN! ")
        print("########################################")
        tictactoe_game_human()

if __name__ == '__main__':
    main_menu()