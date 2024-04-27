# Tic-Tac-Toe
Intelligent Tic-Tac-Toe, built on the [minimax search algorithm](https://en.wikipedia.org/wiki/Minimax) and optimized with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

## How to play
1. Install [the latest version of Python](https://www.python.org/downloads/).
2. Download and unzip this repository, and from your command line `cd` into `tictactoe`.
3. Execute Python with `tictactoe.py <options>` to begin the game.
4. When prompted, enter zero-indexed row-column coordinates: `00`, `12`, etc. (The origin refers to the top-left of the board.)
  
## Options
`<options>` must follow the sequence `<width> <exponent>`.
- `<width>` is an integer that sets the square board size. (The default is `3`.)
  - For example, `3` creates a board with `3*3 = 9` positions.
- `<exponent>` is a float `<= 2` and `>= 1` that exponentiates the `width` to set a limited search depth. (The default is `2`.) The exponent can be used as a parameter that controls the breadth of the search tree; lower it when using a larger `width`.
  - For example, `3 2` creates a limited search depth of `3^2 = 9`.
  - For a fractional exponent, the resulting power is rounded to the nearest integer.

## Bugs
- `game.Game` does not recognize certain Tie conditions.
