from math import inf
from player import Player
from time import process_time


class Computer(Player):
    def __init__(self, team):
        self.nodes = 0
        self.start = 0
        super().__init__(team)

    def max_value(self, game, state, alpha=None, beta=None):
        self.nodes += 1
        if game.is_cutoff(state) or game.is_terminal(state) or process_time()-self.start > 60:
            return game.utility(state) if game.utype == 1 \
                else game.utility2(state), None
        utility = -inf
        if game.order: fringe = []
        for action in game.actions(state):
            new_state = game.result(state, action)
            if game.order: fringe.append(new_state)
            else:
                utility2, _ = self.min_value(game, new_state, alpha, beta)
                if utility2 > utility:
                    utility, move = utility2, action
                    if alpha: alpha = max(alpha, utility)
                if beta and utility >= beta:
                    return utility, move
        if game.order:
            fringe.sort(key=game.blockline)
            for new_state in fringe:
                utility2, _ = self.min_value(game, new_state, alpha, beta)
                if utility2 > utility:
                    utility, move = utility2, action
                    if alpha: alpha = max(alpha, utility)
                if beta and utility >= beta:
                    return utility, move
        return utility, move

    def min_value(self, game, state, alpha=None, beta=None):
        self.nodes += 1
        if game.is_cutoff(state) or game.is_terminal(state):
            return game.utility(state) if game.utype == 1 \
                else game.utility2(state), None
        utility = inf
        if game.order: fringe = []
        for action in game.actions(state):
            new_state = game.result(state, action)
            if game.order: fringe.append(new_state)
            else:
                utility2, _ = self.max_value(game, new_state, alpha, beta)
                if utility2 < utility:
                    utility, move = utility2, action
                    if beta: beta = min(beta, utility)
                if alpha and utility <= alpha:
                    return utility, move
        if game.order:
            fringe.sort(key=game.blockline)
            for new_state in fringe:
                utility2, _ = self.max_value(game, new_state, alpha, beta)
                if utility2 < utility:
                    utility, move = utility2, action
                    if beta: beta = min(beta, utility)
                if alpha and utility <= alpha:
                    return utility, move
        return utility, move

    def minimax_search(self, game, start):
        self.nodes = 0
        self.start = start
        _, move = self.max_value(game, game.state)
        return move, self.nodes

    def ab_search(self, game, start):
        self.nodes = 0
        self.start = start
        _, move = self.max_value(game, game.state, alpha=-inf, beta=inf)
        return move, self.nodes