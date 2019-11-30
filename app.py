#!python

from enum import Enum, unique, auto

tt_board = [[None, None, None] for i in range(3)]
cols = ['a', 'b', 'c']
rows = ['0', '1', '2']

class Player(Enum):
    """Player enum"""
    HUMAN = 'X'
    COMPUTER = 'O'

def think(board):
    """Examine the board and evaluate and return the best move"""
    pass

def prompt():
    """Prompt the player for a move"""
    valid_move = False
    while not valid_move:
        command = input("Move : ").strip().lower()
        if command in ['exit', 'quit']:
            exit()
        if command[0] in cols and command[1] in rows:
            valid_move = (command[0], command[1])
            break
        else:
            print("Invalid move.")
    return valid_move


def draw(player, move, board):
    """Return an updated tic tac toe board after drawing a move"""
    row = int(move[1])
    col = 'abc'.find(move[0])
    board[row][col] = player.value
    return board

def view(board):
    """Return a string based representation of the current board"""
    blanked_board = map(lambda x: [' ' if sq is None else sq for sq in x], board)
    print(f'   | {cols[0]} | {cols[1]} | {cols[2]} |')
    print('{:-^16}'.format(''))
    for index, row_state in enumerate(blanked_board):
        print(f' {rows[index]} | {row_state[0]} | {row_state[1]} | {row_state[2]} |')
    return

def status(board):
    """Return the win/loss/indeterminate status of the board"""
    pass

if __name__ == '__main__':
    view(tt_board)
    while True:
        human_move = prompt()
        print(human_move)
        tt_board = draw(Player.HUMAN, human_move, tt_board)
        view(tt_board)
        # computer_move = think(tt_board)
        computer_move = prompt()
        tt_board = draw(Player.COMPUTER, computer_move, tt_board)
        view(tt_board)
