# Tic-Tac-Toe
Intelligent Tic-Tac-Toe, using the [minimax search algorithm](https://en.wikipedia.org/wiki/Minimax) with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

## How to play
1. Install the latest version of [Python](https://www.python.org/downloads/).
2. Download, unzip, and `cd` into `tictactoe`.
3. Enter `python<version> tictactoe.py <options>` to begin the game.
4. When prompted, enter row-column coordinates: `11`, `23`, etc.
  
## Options
`<options>` must follow the sequence `<width> <depth>`.
- `<width>` is an integer that sets the square board size.
  - `3` yields a board with `3*3 = 9` positions.
- `<depth>` is a float `<= 2` and `>= 1` that raises the `width` to set a limited search depth.
  - `3 2` yields a limited search depth of `3^2 = 9`.
  - `3 1.5` yields `3^1.5 ≈ 5`.
  
## Limitations
- A higher `width` or `depth` leads to a slower search time.
