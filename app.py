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
    # transform move to refer to the right index in our list of lists
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

def main(players, game_board):
    """Main game loop"""
    current_player = players('X')
    while True:
        current_move = None
        if current_player == players.COMPUTER:
            print("Computer turn")
            current_move = think(players, game_board)
        else:
            print("Human turn")
            current_move = prompt(current_player, game_board)
        game_board = draw(current_player, current_move, game_board)
        view(game_board)
        victory, winner = status(game_board)
        if victory:
            if winner:
                print(f'\n{winner} ({players(winner).name}) wins!')
            else:
                print(f'\nDraw!')
            break
        current_player = players.COMPUTER if current_player == players.HUMAN else players.HUMAN

if __name__ == '__main__':
    new_board = deepcopy(blank_board)
    Player = player_select()
    view(new_board)
    main(Player, new_board)
    
