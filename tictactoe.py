from game import Game
from pieces import O, X
from player import Computer, Player
from sys import argv

WIDTH = 3
EXPONENT = 2

try:
  WIDTH = int(argv[1])
  EXPONENT = float(argv[2])
except IndexError: ...

game = Game(
  p1=Player(X),
  p2=Computer(O),
  width=WIDTH,
  limit=round(pow(WIDTH, EXPONENT)),
  prune=True)

print("\nTic-Tac-Toe\n")
winner = game.play()
print("Tie" if not winner else f"Winner {winner}")
