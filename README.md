# Tic-Tac-Toe
Intelligent Tic-Tac-Toe

## How to play
1. Download, unzip, and `cd` into `tictactoe`.
2. Enter `python3 tictactoe.py <width=3> <power=2>` to begin the game.
   - `width` defines the board size.
     - For example, `3` creates a board with `3*3 = 9` cells.
   - `power` defines the search depth.
     - For example, `2` for a width of `3` will limit the AI to a search depth of `3^2 = 9`.
4. When prompted, enter row-column coordinates. For example, `11`, `23`, etc.
   - The origin `(1, 1)` is at the top-left.
  
## Notes
- A higher `width` will lead to a slower search time.
- A higher `power` will lead to a slower search time.
