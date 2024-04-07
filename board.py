class Board:
    def __init__(self, width):
        self.width = width
        self.board = [  # Internal data structure
            [None for _ in range(width)] for _ in range(width)]
        self.cells = [  # Flattened array of coordinates
            (i, j) for i in range(width) for j in range(width)]

    def __str__(self):
        output = "\n"
        for row in self.board:
            for piece in row:
                output += " . " if piece is None else str(piece)
            output += "\n"
        output += "\n"
        return output

    def get(self, cell):
        i, j = map(int, cell)
        piece = self.board[i][j]
        return piece

    def legal_move(self, cell, output=False):
        cell = tuple(map(int, cell))
        if cell not in self.cells:  # Off-board
            if output: print(f"{cell} is not on the board.")
            return False
        elif self.get(cell) is not None:  # Occupied cell
            if output: print(f"{cell} is already occupied.")
            return False
        return True

    def set(self, piece, cell):
        i, j = map(int, cell)
        self.board[i][j] = piece
