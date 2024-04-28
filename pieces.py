class Piece():
    def __init__(self, team, cell):
        self.team = team
        self.cell = cell

    def __str__(self):
        return f"{self.team}"

    def set(self, cell):
        self.cell = cell


class O(Piece):
    def __init__(self, cell=None):
        super().__init__('O', cell)

class X(Piece):
    def __init__(self, cell=None):
        super().__init__('X', cell)
