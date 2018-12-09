class Piece():
    def __init__(self, side):
        self.side = side
        self.hasMoved = False
        self.title = ""
    
    def __str__(self):
        if not self.title == "Knight":
            if self.side == "white":
                return self.title[0]
            else:
                return self.title[0].lower()
        else:
            if self.side == "white":
                return "N"
            else:
                return "n"

class Pawn(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Pawn"

class Rook(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Rook"

class Knight(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Knight"

class Bishop(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Bishop"

class King(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "King"

class Queen(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Queen"
