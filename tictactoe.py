from defaults import POWER, WIDTH
from game import Game
from pieces import O, X
from player import Computer, Player
from sys import argv

try:
  WIDTH = int(argv[1])
  POWER = int(argv[2])
except IndexError: ...

game = Game(
  p1=Player(X),
  p2=Computer(O),
  width=WIDTH,
  limit=pow(WIDTH, POWER),
  prune=True,
  order=False,
  utype=1)

print("\nTic-Tac-Toe\n")
winner = game.play()
print("Tie" if not winner else f"Winner {winner}")
