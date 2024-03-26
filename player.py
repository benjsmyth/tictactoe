class Player:
    def __init__(self, team):
        self.team = team

    def __str__(self):
        return str(self.team.__name__)
