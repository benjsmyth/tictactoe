# Tic-Tac-Toe
Intelligent Tic-Tac-Toe, built on the [minimax search algorithm](https://en.wikipedia.org/wiki/Minimax) and optimized with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

## How to play
1. Install the latest version of [Python](https://www.python.org/downloads/).
2. Download, unzip, and `cd` into `tictactoe`.
3. Enter `python<version> tictactoe.py <options>` to begin the game.
4. When prompted, enter zero-indexed row-column coordinates: `00`, `12`, etc. (The origin refers to the top-left of the board.)
  
## Options
`<options>` must follow the sequence `<width> <depth>`.
- `<width>` is an integer that sets the square board size. (The default is `3`.)
  - For example, `3` creates a board with `3*3 = 9` positions.
- `<depth>` is a float `<= 2` and `>= 1` that raises the `width` to set a limited search depth. (The default is `2`.)
  - For example, `3 2` creates a limited search depth of `3^2 = 9`.
  - For a fractional depth, the power is rounded to the nearest integer.
