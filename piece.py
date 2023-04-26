class Piece:
    def __init__(self, team, type, sym):
        self.team = team
        self.type = type
        self.sym = sym

    def toString(self):
        return self.sym