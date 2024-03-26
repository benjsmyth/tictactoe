from modules.computer import Computer
from modules.game import Game
from modules.pieces import O, X
from modules.player import Player

print("\nTic-Tac-Toe\n")
p1 = Player(X)
p2 = Computer(O)
game = Game(p1, p2, width=3, limit=9, prune=True, order=False, utype=1)
winner = game.play()
print("Tie" if not winner else f"Winner {winner}")
