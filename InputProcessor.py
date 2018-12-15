class InputProcessor():
    def __init__(self, inputToProcess, chessNotation="simplified"):
        self.inputToProcess = inputToProcess
        self.chessNotation = chessNotation
        self.tokens = []
        self.check = False
        self.checkMate = False
        self.capture = False
    
    def ProcessInput(self, board):
        #if self.chessNotation == "algebraic":
        #    # Special case checks
        #    if self.inputToProcess[len(self.inputToProcess) - 1] == "+":
        #        self.check = True
        #    elif self.inputToProcess[len(self.inputToProcess) - 1] == "#":
        #        self.checkMate = True
        #    elif self.inputToProcess == "0-0" or self.inputToProcess == "O-O":
        #        self.tokens.extend(["0-0"])
        #        return
        #    elif self.inputToProcess == "0-0-0" or self.inputToProcess == "O-O-O":
        #        self.tokens.extend(["0-0-0"])
        #        return

        # Heavily simplified chess notation, simply includes the beginning and ending spots of the move. Castles are still 0-0 or O-O
        if self.chessNotation == "simplified":
            # Castling not implemented yet
            if self.inputToProcess == "0-0" or self.inputToProcess == "O-O":
                pass
            elif self.inputToProcess == "0-0-0" or self.inputToProcess == "O-O-O":
                pass
            else:
                try:
                    location = [int(self.inputToProcess[1]) - 1, ord(self.inputToProcess[0].lower()) - 97, 
                                int(self.inputToProcess[3]) - 1, ord(self.inputToProcess[2].lower()) - 97]
                    if (board[location[0]][location[1]] == board[location[2]][location[3]] or
                        (board[location[2]][location[3]] != " " and
                         board[location[0]][location[1]].side == board[location[2]][location[3]].side) or
                        not location[2:] in board[location[0]][location[1]].availableMoves(location[0], location[1], board)):
                        return [False, -1, -1, -1, -1]
                except:
                    return [False, -1, -1, -1, -1]
                else:
                    return [True] + location
