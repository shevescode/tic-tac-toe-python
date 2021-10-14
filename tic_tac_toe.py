import sys
import random

# Returns the coordinates of a valid move for player on board

def get_move(board):

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
            print('Already occupied cell!')
            continue

# Returns the coordinates of the best move for AI on board

def scan_for_best_move(board, player_sign, enemy_sign):  

    empty_field_index = None

    vertical_check = [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]]]

    diagonal_check = [
        [board[0][0], board[1][1], board[2][2]],   
        [board[2][0], board[1][1], board[0][2]]]

    # Horizontal check.

    for row in (board):
        count = 0
        for i in range(len(row)):
            field = row[i]
            if field == player_sign:
                count += 1
            elif field == enemy_sign:
                count -= 1
            else:
                empty_field_index = i
        if count == 2 or count == -2:
            return board.index(row), empty_field_index

    # Vertical check.

    for col in (vertical_check):
        count = 0  
        for i in range(len(col)):
            field = col[i]
            if field == player_sign:
                count += 1
            elif field == enemy_sign:
                count -= 1
            else:
                empty_field_index = i
        if count == 2 or count == -2:
            return empty_field_index, vertical_check.index(col)

    # Diagonal check.

    for dia in (diagonal_check):
        count = 0
        for i in range(len(dia)):     
            field = dia[i]
            if field == player_sign:
                count += 1
            elif field == enemy_sign:
                count -= 1
            else:
                empty_field_index = i
        if count == 2 or count == -2:
            if diagonal_check.index(dia) == 0 and empty_field_index == 0:
                return 0, 0
            elif diagonal_check.index(dia) == 0 and empty_field_index == 1:
                return 1, 1
            elif diagonal_check.index(dia) == 0 and empty_field_index == 2:
                return 2, 2
            elif diagonal_check.index(dia) == 1 and empty_field_index == 0:
                return 2, 0
            elif diagonal_check.index(dia) == 1 and empty_field_index == 1:
                return 1, 1
            elif diagonal_check.index(dia) == 1 and empty_field_index == 2:
                return 0, 2

    row, col = 0, 0
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ".":
            return row, col
        else:
            continue

# Returns best possible move for AI.

def get_ai_move(board):

    player_sign = "X"
    enemy_sign = "O"
    if board[1][1] == ".":
        row, col = 1, 1
        return row, col
    else:
        return scan_for_best_move(board, player_sign, enemy_sign)

# Marks the element at row & col on the board for player.

def mark(board, player, row, col):
    
    if board[row][col] == ".":
        board[row][col] = player
    return board

# Returns True if player has won the game.

def has_won(board, player):
    
    vertical_check = [
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]]]

    diagonal_check = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]]

    # Horizontal check.

    for row in board:
        has_row_won = True
        for field in row:
            if field != player:
                has_row_won = False
                break
        if has_row_won:
            return True

    # Vertical check.

    for col in vertical_check:
        has_col_won = True
        for field in col:
            if field != player:
                has_col_won = False
                break
        if has_col_won:
            return True

    # Diagonal check.
    
    for dia in diagonal_check:
        has_dia_won = True
        for field in dia:
            if field != player:
                has_dia_won = False
                break
        if has_dia_won:
            return True

# Returns True if board is full.

def is_full(board):
   
    if not '.' in board[0] and not '.' in board[1] and not '.' in board[2]:
        return True
    else:
        return False

# Prints a 3-by-3 board on the screen with borders.

def print_board(board):
    print("\n    1   2   3")
    print("A   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("B   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("C   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")

# Congratulates winner.

def print_result(winner):
    print(f'Congratulations! Player {winner} has won!')

# Runs 2-player game.

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

# Runs 1-player game against AI.

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