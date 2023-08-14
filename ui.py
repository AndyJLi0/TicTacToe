from logic import *

global_board = [row.copy() for row in INITIAL_BOARD]

# displays the global_board
def display_board(global_board):
    print("\n ")
    print(global_board[0][0] + '|' + global_board[0][1] + '|' +  global_board[0][2])
    print('-----')
    print(global_board[1][0] + '|' + global_board[1][1] + '|' + global_board[1][2])
    print('-----')
    print(global_board[2][0] + '|' + global_board[2][1] + '|' + global_board[2][2])
    print("\n ")

# gets the players input for the move
def get_player_input(global_board):
    while True:
        move = input("Enter your move (row col): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter row and column separated by space.")
            continue
        i, j = int(move[0]), int(move[1])
        if 0 <= i < 3 and 0 <= j < 3 and global_board[i][j] == EMPTY:
            return (i, j)
        else:
            print("Invalid move. Try again.")

# determines if the game is a draw or not (all spaces are filled)
def is_draw(global_board):
    return all(cell != EMPTY for row in global_board for cell in row)


def main():
    global global_board
    current_player = PLAYERO 
    
    while not game_over(global_board) and not is_draw(global_board):
        display_board(global_board)
        if current_player == PLAYERO:
            move = get_player_input(global_board)
            global_board = make_move(global_board, move, PLAYERO)
            current_player = PLAYERX
        else:
            move = make_ai_move(global_board)
            global_board = make_move(global_board, move, PLAYERX)
            current_player = PLAYERO
            
    # after a turn is made
    display_board(global_board)
    if has_won(global_board, PLAYERO):
        print("Player O wins!")
    elif has_won(global_board, PLAYERX):
        print("Player X (AI) wins!")
    else:
        print("you suck you fucking loser")


if __name__ == "__main__":
    main()
