import math

def min_value(game, state, alpha=None, beta=None):
    return NotImplementedError

def max_value(game, state, alpha=None, beta=None);
    return NotImplementedError

def minimax_search(game, state):
    move = alpha_beta_search(game, state, False)
    return move

def alpha_beta_search(game, state, use_pruning=True):
    player = game.to_move(state)
    if use_pruning:
        value, move = max_value(game, state, -math.inf, math.inf)
    else:
        value, move = max_value(game, state)
    return move
