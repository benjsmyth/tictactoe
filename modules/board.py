from io import StringIO

class Board:
    EMPTY = '.'.center(3, ' ')
    
    def __init__(self, width):
        # Initialize the game board.
        self.width = width
        self.board = [[None for _ in range(width)] for _ in range(width)]
        self.cells = [(i, j) for i in range(width) for j in range(width)]

    def __str__(self):
        # Visualize the game board.
        output = StringIO('\n')
        for row in self.board:
            for piece in row:
                output.write(Board.EMPTY if piece is None else str(piece))
        output.write()  # Newline
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
