from logic import *

def test_has_won_diagonal():
    board = [
        [PLAYERX, PLAYERO, PLAYERX],
        [EMPTY, PLAYERX, PLAYERO],
        [EMPTY, EMPTY, PLAYERX]
    ]
    assert has_won(board, PLAYERX)
    assert not has_won(board, PLAYERO)

def test_has_won_vertical():
    board = [
        [PLAYERO, PLAYERX, PLAYERX],
        [PLAYERO, PLAYERX, PLAYERO],
        [PLAYERO, EMPTY, PLAYERX]
    ]
    assert not has_won(board, PLAYERX)
    assert has_won(board,PLAYERO)


def test_make_move():
    board = [row.copy() for row in INITIAL_BOARD]
    board = make_move(board, (0,0), PLAYERX)
    new_board = [
        [PLAYERX, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert board == new_board
    