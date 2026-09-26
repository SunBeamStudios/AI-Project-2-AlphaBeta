import math

def min_value(game, state, player, alpha=None, beta=None):
    pruning = alpha != None and beta != None
    if game.is_terminal(state):
        return game.utility(state, player), None
    value = math.inf
    move = None
    for action in game.actions(state):
        if pruning:
            value_max, action_max = max_value(game, game.result(state, action), player, alpha, beta)
        else:
            value_max, action_max = max_value(game, game.result(state, action), player)
        if value_max < value:
            value = value_max
            move = action
            if pruning:
                beta = min(beta, value)
        if pruning and value <= alpha:
            return value, move
    return value, move

def max_value(game, state, player, alpha=None, beta=None):
    pruning = alpha != None and beta != None
    if game.is_terminal(state):
        return game.utility(state, player), None
    value = -math.inf
    move = None
    for action in game.actions(state):
        if pruning:
            value_min, action_min = min_value(game, game.result(state, action), player, alpha, beta)
        else:
            value_min, action_min = min_value(game, game.result(state, action), player)
        if value_min > value:
            value = value_min
            move = action
            if pruning:
                alpha = max(alpha, value)
        if pruning and value >= beta:
            return value, move
    return value, move

def minimax_search(game, state):
    move = alpha_beta_search(game, state, False)
    return move

def alpha_beta_search(game, state, use_pruning=True):
    player = game.to_move(state)
    if use_pruning:
        value, move = max_value(game, state, player, -math.inf, math.inf)
    else:
        value, move = max_value(game, state, player)
    return move
