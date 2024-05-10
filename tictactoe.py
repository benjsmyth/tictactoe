from game import Game
from pieces import O, X
from player import Computer, Player
from sys import argv

try: (WIDTH := int(argv[1]))
except IndexError: WIDTH = 3

game = Game(
  p1=Player(X),
  p2=Computer(O),
  width=WIDTH,
  limit=round(pow(WIDTH, 1 if WIDTH == 4 else 2)),
  prune=True)

print("\nTic-Tac-Toe\n")
winner = game.play()
print(f"{winner} wins" if winner else "Tie")
