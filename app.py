#!python

from enum import Enum, unique, auto

tt_board = [[None, None, None] for i in range(3)]
cols = ['a', 'b', 'c']
rows = ['0', '1', '2']

Player = Enum('Player', [('HUMAN', 'X'), ('COMPUTER', 'O')])

def think(board):
    """Examine the board and evaluate and return the best move"""
    pass

def prompt(player, board):
    """Prompt the player for a move"""
    valid_move = False
    while not valid_move:
        command = input(f"Move ({player.value}): ").strip().lower()
        if command in ['exit', 'quit']:
            exit()
        move = validate_move(command, board)
        if move[0] is True: # is valid, explicit for readibility
            valid_move = move[1]
            break
        else:
            print("Invalid move.")
    return valid_move

def validate_move(move, board):
    """Check if a move is valid"""
    if move[0] not in cols and move[1] not in rows:
        return (False, None)
    row = int(move[1])
    col = 'abc'.find(move[0])
    if board[row][col] is not None:
        return (False, None)
    return (True, (col, row))


def draw(player, move, board):
    """Return an updated tic tac toe board after drawing a move"""
    # row = int(move[1])
    # col = 'abc'.find(move[0])
    board[move[1]][move[0]] = player.value
    return board

def view(board):
    """Return a string based representation of the current board"""
    blanked_board = map(lambda x: [' ' if sq is None else sq for sq in x], board)
    print(f'\n   | {cols[0]} | {cols[1]} | {cols[2]} |')
    print('{:-^16}'.format(''))
    for index, row_state in enumerate(blanked_board):
        print(f' {rows[index]} | {row_state[0]} | {row_state[1]} | {row_state[2]} |')
    return

def status(board):
    """Return the win/draw/indeterminate status of the board"""
    for player in ['X', 'O']:
        row_win = True in map(lambda x: x[0] == x[1] == x[2] == player, board)
        col_win = True in (board[0][i] == board[1][i] == board[2][i] == player for i in range(3))
        diag_win_one = board[0][0] == board[1][1] == board[2][2] == player
        diag_win_two = board[0][2] == board[1][1] == board[2][0] == player
        if True in (row_win, col_win, diag_win_one, diag_win_two):
            return (True, player)
    draw = True
    for row in board:
        draw = False if None in row else draw
    if draw:
        return (True, None)
    return (False, None)

if __name__ == '__main__':
    view(tt_board)
    current_player = Player.HUMAN
    while True:
        current_move = prompt(current_player, tt_board)
        tt_board = draw(current_player, current_move, tt_board)
        view(tt_board)
        victory, winner = status(tt_board)
        if victory:
            if winner:
                print(f'\n{winner} wins!')
            else:
                print(f'\nDraw!')
            break
        current_player = Player.COMPUTER if current_player == Player.HUMAN else Player.HUMAN
