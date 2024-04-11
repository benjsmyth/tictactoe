from game import Game
from pieces import O, X
from player import Computer, Player

game = Game(
  p1=Player(X),
  p2=Computer(O),
  width=3,
  limit=9,
  prune=True,
  order=False,
  utype=1)

print("\nTic-Tac-Toe\n")
winner = game.play()
print("Tie" if not winner else f"Winner {winner}")
