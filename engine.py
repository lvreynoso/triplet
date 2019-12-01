#!python
from copy import deepcopy

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

def minimax(player, players, scores, depth, board):
    victory, winner = status(board)
    if victory:
        return scores[winner]
    if player == players.COMPUTER:
        possible_moves = possibilities(board)
        value = -99
        for move in possible_moves:
            child_board = deepcopy(board)
            child_board[move[0]][move[1]] = players.COMPUTER.value
            possible_moves[move] = minimax(players.HUMAN, players, scores, depth + 1, child_board)
        return max(list(possible_moves.values()) + [value])
    if player == players.HUMAN:
        possible_moves = possibilities(board)
        value = 99
        for move in possible_moves:
            child_board = deepcopy(board)
            child_board[move[0]][move[1]] = players.HUMAN.value
            possible_moves[move] = minimax(players.COMPUTER, players, scores, depth + 1, child_board)
        return min(list(possible_moves.values()) + [value])
    return 0

def possibilities(board):
    possible_moves = {}
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col is None:
                possible_moves[(row_index, col_index)] = None
    return possible_moves

def think(players, board):
    scores = {
        players.COMPUTER.value: 99,
        None: 0,
        players.HUMAN.value: -99
    }
    # get possible valid moves
    possible_moves = possibilities(board)
    for move in possible_moves:
        child_board = deepcopy(board)
        child_board[move[0]][move[1]] = players.COMPUTER.value
        possible_moves[move] = minimax(players.COMPUTER, players, scores, 0, child_board)
    # print(possible_moves)
    decision = max(possible_moves, key=possible_moves.get)
    # print(decision)
    return decision

