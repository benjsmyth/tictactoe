from math import inf
from time import process_time


class Player:
    def __init__(self, team):
        self.team = team

    def __str__(self):
        return str(self.team.__name__)


class Computer(Player):
    def __init__(self, team):
        self.start = 0
        super().__init__(team)

    def ab_search(self, game, start):
        self.nodes = 0
        self.start = start
        _, move = self.max_value(game, game.state, alpha=-inf, beta=inf)
        return move, self.nodes

    def minimax_search(self, game, start):
        self.nodes = 0
        self.start = start
        _, move = self.max_value(game, game.state)
        return move, self.nodes

    def max_value(self, game, state, alpha=None, beta=None):
        self.nodes += 1
        if game.is_cutoff(state) or game.is_terminal(state) or process_time()-self.start > 60:
            return game.utility(state), None
        utility = -inf
        for action in game.actions(state):
            new_state = game.result(state, action)
            utility2, _ = self.min_value(game, new_state, alpha, beta)
            if utility2 > utility:
                utility, move = utility2, action
                if alpha: alpha = max(alpha, utility)
            if beta and utility >= beta:
                return utility, move
        return utility, move

    def min_value(self, game, state, alpha=None, beta=None):
        self.nodes += 1
        if game.is_cutoff(state) or game.is_terminal(state) or process_time()-self.start > 60:
            return game.utility(state), None
        utility = inf
        for action in game.actions(state):
            new_state = game.result(state, action)
            utility2, _ = self.max_value(game, new_state, alpha, beta)
            if utility2 < utility:
                utility, move = utility2, action
                if beta: beta = min(beta, utility)
            if alpha and utility <= alpha:
                return utility, move
        return utility, move
