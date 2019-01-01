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
    
    # Used for pieces with normative move sets, for example a rook or bishop
    def normativeAvailableMoves(self, row, column, board, isDiagonal, isUpDown, moveAmount):
        moveAmount += 1 # Without this, the moveAmount would need to be inputed with a value one too high, which would be confusing
        moves = []
        if isUpDown:
            for i in range(-1, 2, 2):
                tempRow = row
                for n in range(1, moveAmount):
                    tempRow = tempRow + i
                    try:
                        if board[tempRow][column] != " ":
                            if board[tempRow][column].side != board[row][column].side:
                                moves.append([tempRow, column])
                            break
                    except:
                        break
                    moves.append([tempRow, column])
            for i in range(-1, 2, 2):
                tempColumn = column
                for n in range(1, moveAmount):
                    tempColumn = tempColumn + i
                    try:
                        if board[row][tempColumn] != " ":
                            if board[row][tempColumn].side != board[row][column].side:
                                moves.append([row, tempColumn])
                            break
                    except:
                        break
                    moves.append([row, tempColumn])
        if isDiagonal:
            for i in range(-1, 2, 2):
                tempRow = row
                tempColumn = column
                for n in range(1, moveAmount):
                    tempRow = tempRow + i
                    tempColumn = tempColumn + i
                    try:
                        if board[tempRow][tempColumn] != " ":
                            if board[tempRow][tempColumn].side != board[row][column].side:
                                moves.append([tempRow, tempColumn])
                            break
                    except:
                        break
                    moves.append([tempRow, tempColumn])
            for i in range(-1, 2, 2):
                tempRow = row
                tempColumn = column
                for n in range(1, moveAmount):
                    tempRow = tempRow - i
                    tempColumn = tempColumn + i
                    try:
                        if board[tempRow][tempColumn] != " ":
                            if board[tempRow][tempColumn].side != board[row][column].side:
                                moves.append([tempRow, tempColumn])
                            break
                    except:
                        break
                    moves.append([tempRow, tempColumn])
        return moves

class Pawn(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Pawn"
    
    def availableMoves(self, row, column, board):
        moves = []
        rowMovement = 1 if self.side == "white" else -1
        # Checks if an oppenent is in front of the pawn, if not it can move there
        if board[row + rowMovement][column] == " ":
            moves.append([row + rowMovement, column])
        if not self.hasMoved and board[row + (rowMovement + rowMovement)][column] == " ":
            moves.append([row + (rowMovement + rowMovement), column])
        # Checks if an oppenent is diagonal to the pawn, if so it can move there
        try:
            if board[row + rowMovement][column - 1] != " " and board[row + rowMovement][column - 1].side != board[row][column].side:
                moves.append([row + rowMovement, column - 1])
        except:
            pass
        try:
            if board[row + rowMovement][column + 1] != " " and board[row + rowMovement][column + 1].side != board[row][column].side:
                moves.append([row + rowMovement, column + 1])
        except:
            pass
        return moves

class Rook(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Rook"

    def availableMoves(self, row, column, board):
        moves = []
        moves = self.normativeAvailableMoves(row, column, board, False, True, 7)
        return moves

class Knight(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Knight"
    
    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        for vertical in range(-2, 3, 4):
            for horizontal in range(-1, 2, 2):
                tempColumn = column + vertical
                tempRow = row + horizontal
                try:
                    if board[tempRow][tempColumn] == " " or board[tempRow][tempColumn].side != self.side:
                        moves.append([tempRow, tempColumn])
                except:
                    pass
        for vertical in range(-1, 2, 2):
            for horizontal in range(-2, 3, 4):
                tempColumn = column + vertical
                tempRow = row + horizontal
                try:
                    if board[tempRow][tempColumn] == " " or board[tempRow][tempColumn].side != self.side:
                        moves.append([tempRow, tempColumn])
                except:
                    pass
        return moves

class Bishop(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Bishop"
    
    def availableMoves(self, row, column, board):
        moves = []
        moves = self.normativeAvailableMoves(row, column, board, True, False, 7)
        return moves

class King(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "King"
    
    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        moves = self.normativeAvailableMoves(row, column, board, True, True, 1)
        return moves

class Queen(Piece):
    def __init__(self, side):
        super().__init__(side)
        self.title = "Queen"
    
    # Temporary pawn movement
    def availableMoves(self, row, column, board):
        moves = []
        moves = self.normativeAvailableMoves(row, column, board, True, True, 7)
        return moves
