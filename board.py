from io import StringIO

class Board:
    def __init__(self, width):
        self.width = width
        self.board = [[None for _ in range(width)] for _ in range(width)]
        self.cells = [(i, j) for i in range(width) for j in range(width)]

    def __str__(self):
        NEWLINE = '\n'
        output = StringIO(NEWLINE)
        for row in self.board:
            for piece in row: output.write(
                "{:^3}".format(str(piece) if piece else '.'))
            output.write(NEWLINE)
        output.write(NEWLINE)
        value = output.getvalue()
        return value

    def get(self, cell):
        """Get the piece at a given position."""
        i, j = map(int, cell)
        piece = self.board[i][j]
        return piece

    def legal_move(self, cell, output=False):
        """Check if a given position is valid."""
        cell = tuple(map(int, cell))
        if cell not in self.cells:
            # Off-board
            if output: print(f"{cell} is not on the board.")
            return False
        elif self.get(cell) is not None:
            # Occupied cell
            if output: print(f"{cell} is already occupied.")
            return False
        return True

    def set(self, piece, cell):
        """Set a given piece at a given position."""
        i, j = map(int, cell)
        self.board[i][j] = piece
