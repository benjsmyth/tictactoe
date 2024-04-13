# Tic-Tac-Toe
Intelligent Tic-Tac-Toe, using the [minimax search algorithm](https://en.wikipedia.org/wiki/Minimax).

## How to play
1. Install the latest version of [Python](https://www.python.org/downloads/).
2. Download, unzip, and `cd` into `tictactoe`.
3. Enter `python<version> tictactoe.py <options>` to begin the game.
4. When prompted, enter row-column coordinates: `11`, `23`, etc.
  
## Options
### Quantifiers
- `-w<width>` defines the square board size, where `width` must be an integer.
  - For example, `-w3` defines a board with `3*3 = 9` positions.
- `-d<depth>` defines the exponent to the `width`, where `depth` must be a float.
  - For example, `-w3 -d2` limits the maximum search depth to `3^2 = 9`.
  - Fractions are rounded: `-d1.5` limits the search depth to `3^1.5 ≈ 5`.
### Qualifiers
- `-p` enables [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) for a faster search process.
- `-t` enables the timing and introspection of the AI's search process.
  
## Limitations
- A higher `width` or `depth` will lead to a slower search time.
