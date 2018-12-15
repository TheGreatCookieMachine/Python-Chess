class InputProcessor():
    def __init__(self, inputToProcess, chessNotation="algebraic"):
        self.inputToProcess = inputToProcess
        self.chessNotation = chessNotation
        self.tokens = []
        self.check = False
        self.checkMate = False
    
    def tokenizer(self):
        if self.chessNotation == "algebraic":
            # Special case checks
            if self.inputToProcess[len(self.inputToProcess) - 1] == "+":
                self.check = True
            elif self.inputToProcess[len(self.inputToProcess) - 1] == "#":
                self.checkMate = True
            elif self.inputToProcess == "0-0" or "O-O":
                self.tokens.extend(["0-0"])
                return
            elif self.inputToProcess == "0-0-0" or "O-O-O":
                self.tokens.extend(["0-0-0"])
                return
