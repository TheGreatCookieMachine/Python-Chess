class InputProcessor():
    def __init__(self, inputToProcess, chessNotation="simplified"):
        self.inputToProcess = inputToProcess
        self.chessNotation = chessNotation
        self.pieceAbbreviations = ("p", "r", "n", "b", "k", "q")
    
    def processInput(self, board):
        # Heavily simplified chess notation, simply includes the beginning and ending spots of the move. Castles are still 0-0 or O-O
        if self.chessNotation == "simplified":
            # Castling not implemented yet
            if self.inputToProcess == "0-0" or self.inputToProcess == "O-O":
                pass
            elif self.inputToProcess == "0-0-0" or self.inputToProcess == "O-O-O":
                pass
            elif len(self.inputToProcess) == 4 or len(self.inputToProcess) == 5:
                try:
                    location = [int(self.inputToProcess[1]) - 1, ord(self.inputToProcess[0].lower()) - 97, 
                                int(self.inputToProcess[3]) - 1, ord(self.inputToProcess[2].lower()) - 97]
                    if len(self.inputToProcess) == 5:
                        location.append(self.inputToProcess[4].lower())
                    
                    if (board[location[0]][location[1]] == board[location[2]][location[3]] or
                        (board[location[2]][location[3]] != " " and
                         board[location[0]][location[1]].side == board[location[2]][location[3]].side) or
                        not location[2:] in board[location[0]][location[1]].availableMoves(location[0], location[1], board)):
                        return [False, -1, -1, -1, -1]
                except:
                    return [False, -1, -1, -1, -1]
                else:
                    return [True] + location
        return [False, -1, -1, -1, -1]
