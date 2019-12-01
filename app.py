#!python

from enum import Enum
from copy import deepcopy

from engine import think, status

blank_board = [[None, None, None] for i in range(3)]
cols = ['a', 'b', 'c']
rows = ['0', '1', '2']

def prompt(player, board):
    """Prompt the player for a move"""
    valid_move = False
    while not valid_move:
        command = input(f"Move ({player.value}): ").strip().lower()
        if command in ['exit', 'quit']:
            exit()
        move = validate_move(command, board)
        if move[0] is True: # move is valid, explicit for readibility
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
    return (True, (row, col))


def draw(player, move, board):
    """Return an updated tic tac toe board after drawing a move"""
    board[move[0]][move[1]] = player.value
    return board

def view(board):
    """Return a string based representation of the current board"""
    blanked_board = map(lambda x: [' ' if sq is None else sq for sq in x], board)
    print(f'\n   | {cols[0]} | {cols[1]} | {cols[2]} |')
    print('{:-^16}'.format(''))
    for index, row_state in enumerate(blanked_board):
        print(f' {rows[index]} | {row_state[0]} | {row_state[1]} | {row_state[2]} |')
    return

def player_select():
    """Prompt the player for their choice of X or O"""
    valid_choice = False
    while not valid_choice:
        command = input(f"Would you like to play as X or O? ").strip().lower()
        if command in ['exit', 'quit']:
            exit()
        if command in ['x', 'o']:
            valid_choice = command
            break
        else:
            print("Invalid choice.")
    computer = 'O' if valid_choice == 'x' else 'X'
    positions = Enum('Player', [('HUMAN', valid_choice.upper()), ('COMPUTER', computer)])
    return positions

if __name__ == '__main__':
    game_board = deepcopy(blank_board)
    Player = player_select()
    view(game_board)
    current_player = Player('X')
    while True:
        current_move = None
        if current_player == Player.COMPUTER:
            print("Computer turn")
            current_move = think(Player, game_board)
        else:
            print("Human turn")
            current_move = prompt(current_player, game_board)
        print(current_player, current_move)
        game_board = draw(current_player, current_move, game_board)
        view(game_board)
        victory, winner = status(game_board)
        if victory:
            if winner:
                print(f'\n{winner} wins!')
            else:
                print(f'\nDraw!')
            break
        current_player = Player.COMPUTER if current_player == Player.HUMAN else Player.HUMAN
