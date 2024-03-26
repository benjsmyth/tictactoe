from copy import deepcopy
from itertools import combinations
from math import inf
from modules.board import Board
from modules.pieces import O, X
from time import process_time


class Game:
    def __init__(self, p1, p2, width=3, limit=9, prune=True, order=False, utype=1):
        self.player = p1
        self.computer = p2
        self.width = width
        self.limit = limit
        self.prune = prune
        self.order = order
        self.utype = utype
        self.state = {  # Game state
            'p1': p1,
            'p2': p2,
            'board': Board(width),
            'depth': 0,
            'winner': None}

    def __str__(self):
        return f"{self.state['board']} depth={self.state['depth']}\n"

    def actions(self, state):
        for cell in state['board'].cells:
            if state['board'].legal_move(cell):
                yield cell

    def play(self):
        winner = None
        while True:  # Game loop
            print(self.state['p1'], self.state['depth'], sep='|')
            print(self.state['board'])
            if self.state['p1'].team is self.player.team:
                while True:
                    action = _, _ = input("Move: ")
                    if self.state['board'].legal_move(action, output=True):
                        self.state['board'].set(X(), action)
                        self.state['depth'] += 1
                        break
                if self.is_terminal(self.state) is self.player:
                    winner = self.player  # Player wins
                    break  # Game over
                self.state['p1'], self.state['p2'] = \
                    self.computer, self.player
            else:  # Computer turn
                print("Searching ...")
                start = process_time()
                action, nodes = self.state['p1'].minimax_search(self, start) if not self.prune \
                    else self.state['p1'].ab_search(self, start)
                end = process_time()
                print(f"Found {action}")
                if action is None:
                    print(); return None  # Tie
                else: print(nodes, "nodes at depth", self.state['depth'])
                print(end - start, "seconds")
                self.state = self.result(self.state, action)
                if self.is_terminal(self.state) is self.computer:
                    winner = self.computer  # Computer wins
                    break
                self.state['p1'], self.state['p2'] = \
                    self.player, self.computer
            print()  # Newline
        print(self.state['board'])
        return winner

    def has_column(self, state, team):
        for column in zip(*state['board'].board):
            piece_count = sum(1 for piece in column if piece is not None \
                and isinstance(piece, team))
            if piece_count == self.width:
                return True
        return False

    def has_column_part(self, state, team):
        for column in zip(*state['board'].board):
            piece_count = sum(1 for piece in column if piece is not None \
                and isinstance(piece, team))
            if piece_count > 1 and piece_count < self.width:
                return True
        return False

    def has_diagonal(self, state, team):
        diagonals = (
            [(+i, +j) for i in range(0, self.width + 0) for j in range(self.width) if i == j + 0],
            [(-i, +j) for i in range(1, self.width + 1) for j in range(self.width) if i == j + 1])
        for diagonal in diagonals:
            piece_count = sum(1 for cell in diagonal if state['board'].get(cell) is not None \
                and isinstance(state['board'].get(cell), team))
            if piece_count == self.width:
                return True
        return False

    def has_plus(self, state, team):
        i, j = 1, 1
        while i < self.width - 1:
            while j < self.width - 1:
                plus = (i, j), (i-1, j), (i, j+1), (i+1, j), (i, j-1)
                piece_count = sum(1 for cell in plus \
                    if isinstance(state['board'].get(cell), team))
                if piece_count == 5:
                    return True
                j += 1
            i += 1
            j += 1
        return False

    def has_row(self, state, team):
        for row in state['board'].board:
            piece_count = sum(1 for piece in row if piece is not None \
                and isinstance(piece, team))
            if piece_count == self.width:
                return True
        return False

    def has_row_part(self, state, team):
        for row in state['board'].board:
            piece_count = sum(1 for piece in row if piece is not None \
                and isinstance(piece, team))
            if piece_count > 1 and piece_count < self.width:
                return True
        return False

    def has_square(self, state, team):
        i, j = 0, 0
        while i < self.width - 1:
            while j < self.width - 1:
                square = (i, j), (i, j+1), (i+1, j), (i+1, j+1)
                piece_count = sum(1 for cell in square \
                    if isinstance(state['board'].get(cell), team))
                if piece_count == 4:
                    return True
                j += 1
            i += 1
        return False

    def is_cutoff(self, state):
        return state['depth'] % self.limit == 0

    def is_terminal(self, state):
        if (self.has_column(state, X)
            or self.has_diagonal(state, X)
            or self.has_row(state, X)):
            return self.player
        elif (self.has_column(state, O)
            or self.has_diagonal(state, O)
            or self.has_row(state, O)):
            return self.computer
        if self.width > 3:  # Complex wins
            if (self.has_plus(state, X)
                or self.has_square(state, X)):
                return self.player
            elif (self.has_plus(state, O)
                or self.has_square(state, O)):
                return self.computer
        return False

    def report(self):
        print(f"Team {self.winner.team.name} wins.\n")

    def result(self, state, action):
        next_state = deepcopy(state)
        next_state['board'].set(state['p1'].team(), action)
        next_state['p1'], next_state['p2'] = \
            next_state['p2'], next_state['p1']
        next_state['depth'] += 1
        return next_state

    def utility(self, state):
        utility = 0
        if self.is_terminal(state) is self.computer:
            utility += 1  # Win
        elif self.is_terminal(state) is self.player:
            utility -= 1  # Lose
        return utility

    def utility2(self, state):
        if state['p1'] is self.computer:
            return self.block(state)
        else: return -self.blockline(state)

    def blockline(self, state):
        for cell1, cell2 in combinations(state['board'].cells, 2):
            c1 = state['board'].get(cell1)
            c2 = state['board'].get(cell2)
            if c1 is not None and c2 is not None:
                c1i, c1j = cell1
                c2i, c2j = cell2
                if c1.__class__ is not c2.__class__:
                    if c1i == c2i or c1j == c2j:
                        return True
        return False
