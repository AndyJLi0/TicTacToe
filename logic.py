import math


# Define the player symbols
PLAYERX = 'x'
PLAYERO = 'o'
EMPTY = ' '

INITIAL_BOARD = [
    [EMPTY, EMPTY , EMPTY],
    [EMPTY, EMPTY , EMPTY],
    [EMPTY, EMPTY , EMPTY],
]

# minimax algorithm for the game. X is maximizing; O is minimizing
def minimax(board, depth, isPlayerX):
    if game_over(board) or depth == 0:
        return evaluate(board)
    
    # player x is ai
    if isPlayerX:
        max_eval = float('-inf')
        for move in get_possible_moves(board):
            new_board = make_move(board, move, PLAYERX)
            eval = minimax(new_board, depth -1, isPlayerX = False)
            max_eval = max(max_eval, eval)
        return max_eval
    else :
        min_eval = float('inf')
        for move in get_possible_moves(board):
            new_board = make_move(board, move, PLAYERO)
            eval = minimax(new_board, depth -1, isPlayerX = True)
            min_eval = min(min_eval, eval)
        return min_eval


# returns 1 if x has won, -1 if y has won, and 0 if else
def evaluate(board):
    if has_won(board, PLAYERX):
        return 1
    elif has_won(board, PLAYERO):
        return -1
    else:
        return 0

# returns true if player has won, false otherwise
def has_won(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): 
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False
        

# returns true if either players have won
def game_over(board):
    return has_won(board, PLAYERX) or has_won(board, PLAYERO)

# returns an array of possible moves. first number is row, second is column
def get_possible_moves(board):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.append((i, j))
    return possible_moves

# makes a move 
def make_move(board, move, player):
    new_board = [row.copy() for row in board]
    i, j = move
    new_board[i][j] = player
    return new_board

# ai makes move
def make_ai_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_possible_moves(board):
        new_board = make_move(board, move, PLAYERX)
        score = minimax(new_board, depth = 0, isPlayerX = False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

