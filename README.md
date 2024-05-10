# Tic-Tac-Toe
Intelligent Tic-Tac-Toe, built on the [minimax search algorithm](https://en.wikipedia.org/wiki/Minimax) and optimized with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

## How to play
1. [Install the latest version of Python.](https://www.python.org/downloads/)
2. Download and unzip this repository. From your command line, `cd` into `tictactoe`.
3. Execute Python with `tictactoe.py <width>` to begin the game.
4. When prompted, enter zero-indexed row-column coordinates: `00`, `12`, etc. (The origin refers to the top-left of the board.)

## Optional width
`<width>` is an integer that sets the square board size.
  - The default is `3`, which creates a board with `3*3 = 9` positions.
  - The only other option is `4` and this option may degrade performance.
