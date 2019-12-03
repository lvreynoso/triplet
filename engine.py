#!python

from enum import Enum, auto

State = Enum('State', [('VICTORY', auto()), ('DRAW', auto()), ('ONGOING', auto())])

def status(board):
    """Return the win/draw/indeterminate status of the board"""
    for player in ['X', 'O']:
        row_win = True in map(lambda x: x[0] == x[1] == x[2] == player, board)
        col_win = True in (board[0][i] == board[1][i] == board[2][i] == player for i in range(3))
        diag_win_one = board[0][0] == board[1][1] == board[2][2] == player
        diag_win_two = board[0][2] == board[1][1] == board[2][0] == player
        if True in (row_win, col_win, diag_win_one, diag_win_two):
            return (State.VICTORY, player)
    draw = True
    for row in board:
        draw = False if None in row else draw
    if draw:
        return (State.DRAW, None)
    return (State.ONGOING, None)

def minimax(player, players, scores, depth, board):
    """minimax algorithm to navigate the game decision tree"""
    gamestate, winner = status(board)
    if gamestate is State.VICTORY:
        # scores adjusted for depth to value earlier wins
        # and avoid earlier losses
        if winner == players.COMPUTER.value:
            return scores[winner] - depth
        if winner == players.HUMAN.value:
            return scores[winner] + depth
    elif gamestate is State.DRAW:
        return scores[None] # winner is None, value is 0
    possible_moves = possibilities(board)
    default = 99 if player == players.HUMAN else -99
    next_player = players.COMPUTER if player == players.HUMAN else players.HUMAN
    for move in possible_moves:
        board[move[0]][move[1]] = player.value
        possible_moves[move] = minimax(next_player, players, scores, depth + 1, board)
        board[move[0]][move[1]] = None
    possible_moves['default'] = default

    score = min(possible_moves.values()) if player == players.HUMAN else max(possible_moves.values())
    return score

def possibilities(board):
    possible_moves = {}
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col is None:
                possible_moves[(row_index, col_index)] = None
    return possible_moves

def think(players, board):
    # weights for victory, draw, and loss
    # used in minimax function
    scores = {
        players.COMPUTER.value: 99,
        None: 0,
        players.HUMAN.value: -99
    }
    # get possible valid moves
    possible_moves = possibilities(board)
    for move in possible_moves:
        board[move[0]][move[1]] = players.COMPUTER.value
        possible_moves[move] = minimax(players.HUMAN, players, scores, 1, board)
        board[move[0]][move[1]] = None
    decision = max(possible_moves, key=possible_moves.get)
    return decision

