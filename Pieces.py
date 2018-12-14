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
    
    def availableMoves(self, row, column, board):
        moves = []
        # Checks if an oppenent is in front of the pawn, if not it can move there
        if board[row + 1][column] == " ":
            moves.append([row + 1, column])
        # Checks if an oppenent is diagonal to the pawn, if so it can move there
        if board[row + 1][column - 1] != " " and board[row + 1][ column - 1].side != board[row][column].side:
            moves.append([row + 1, column - 1])
        if board[row + 1][column + 1] != " " and board[row + 1][ column + 1].side != board[row][column].side:
            moves.append([row + 1, column + 1])
        return moves

class Rook(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Rook"

    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        # Checks if an oppenent is in front of the pawn, if not it can move there
        if board[row + 1][column] == " ":
            moves.append([row + 1, column])
        # Checks if an oppenent is diagonal to the pawn, if so it can move there
        if board[row + 1][column - 1] != " " and board[row + 1][ column - 1].side != board[row][column].side:
            moves.append([row + 1, column - 1])
        if board[row + 1][column + 1] != " " and board[row + 1][ column + 1].side != board[row][column].side:
            moves.append([row + 1, column + 1])
        return moves

class Knight(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Knight"
    
    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        # Checks if an oppenent is in front of the pawn, if not it can move there
        if board[row + 1][column] == " ":
            moves.append([row + 1, column])
        # Checks if an oppenent is diagonal to the pawn, if so it can move there
        if board[row + 1][column - 1] != " " and board[row + 1][ column - 1].side != board[row][column].side:
            moves.append([row + 1, column - 1])
        if board[row + 1][column + 1] != " " and board[row + 1][ column + 1].side != board[row][column].side:
            moves.append([row + 1, column + 1])
        return moves

class Bishop(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Bishop"
    
    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        # Checks if an oppenent is in front of the pawn, if not it can move there
        if board[row + 1][column] == " ":
            moves.append([row + 1, column])
        # Checks if an oppenent is diagonal to the pawn, if so it can move there
        if board[row + 1][column - 1] != " " and board[row + 1][ column - 1].side != board[row][column].side:
            moves.append([row + 1, column - 1])
        if board[row + 1][column + 1] != " " and board[row + 1][ column + 1].side != board[row][column].side:
            moves.append([row + 1, column + 1])
        return moves

class King(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "King"
    
    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        # Checks if an oppenent is in front of the pawn, if not it can move there
        if board[row + 1][column] == " ":
            moves.append([row + 1, column])
        # Checks if an oppenent is diagonal to the pawn, if so it can move there
        if board[row + 1][column - 1] != " " and board[row + 1][ column - 1].side != board[row][column].side:
            moves.append([row + 1, column - 1])
        if board[row + 1][column + 1] != " " and board[row + 1][ column + 1].side != board[row][column].side:
            moves.append([row + 1, column + 1])
        return moves

class Queen(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Queen"
    
    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        # Checks if an oppenent is in front of the pawn, if not it can move there
        if board[row + 1][column] == " ":
            moves.append([row + 1, column])
        # Checks if an oppenent is diagonal to the pawn, if so it can move there
        if board[row + 1][column - 1] != " " and board[row + 1][ column - 1].side != board[row][column].side:
            moves.append([row + 1, column - 1])
        if board[row + 1][column + 1] != " " and board[row + 1][ column + 1].side != board[row][column].side:
            moves.append([row + 1, column + 1])
        return moves
