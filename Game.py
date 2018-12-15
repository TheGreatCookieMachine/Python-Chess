import random
import Pieces
import InputProcessor

class Game():
    def __init__(self):
        self.player = "white" if random.randint(0, 1) == 1 else "black" # Temporary way of choosing side until player choice is given
        self.computer = "white" if self.player == "black" else "black"
        self.board = [[Pieces.Rook("white"), Pieces.Knight("white"), Pieces.Bishop("white"), Pieces.King("white"),
                      Pieces.Queen("white"), Pieces.Bishop("white"), Pieces.Knight("white"), Pieces.Rook("white")],
                      [Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"),
                      Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white")],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"),
                      Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black")],
                      [Pieces.Rook("black"), Pieces.Knight("black"), Pieces.Bishop("black"), Pieces.King("black"),
                      Pieces.Queen("black"), Pieces.Bishop("black"), Pieces.Knight("black"), Pieces.Rook("black")]]
        self.pieces = {"r": "Rook", "n": "Knight", "b": "Bishop", "q": "Queen", "k": "King"}
    
    def drawBoard(self):
        print("---------------------------------")
        # Technically breaks PEP 8, however only by a little, and this is with splitting the line in two
        for i in range(7, -1, -1):
            print("| " + str(self.board[i][0]) + " | " + str(self.board[i][1]) + " | " + str(self.board[i][2]) + " | " + str(self.board[i][3]) +
                  " | " + str(self.board[i][4]) + " | " + str(self.board[i][5]) + " | " + str(self.board[i][6]) + " | " + str(self.board[i][7]) + " |")
            print("---------------------------------")
    
    # Takes input such as e5 or a1 and turns it into a list which is usable for finding locations on the board
    def getLocation(self, baseLocation):
        if ord(baseLocation[0].lower()) > 96 and ord(baseLocation[0].lower()) < 105:
            try:
                return [int(baseLocation[1]) - 1, ord(baseLocation[0].lower()) - 97]
            except:
                pass
        return [-1, -1] # [-1, -1] is used as a way to tell the rest of the code that there was an invalid input, since [-1, -1] is not achievable through a valid input
    
    # Multi-purpose function, returns if the input is valid, and if so it returns the starting and ending location of the input
    # This entire thing will be redone eventually since I am a moron and didnt realize how chess notation was supposed to work
    def processInput(self, userInput):
        def mainCode(midNum, targetPiece, isSpace): # Number at the middle, the piece that should be at the start, if there should be a space at the end
            try:
                location = self.getLocation(userInput[midNum:midNum + 2])
                if isSpace and self.board[location[0]][location[1]] != " ":
                    return [False, -1, -1, -1, -1]
                elif not isSpace and self.board[location[0]][location[1]] == " ":
                    return [False, -1, -1, -1, -1]
                location += self.getLocation(userInput[midNum - 2:midNum]) # Adds the start onto the end, meaning the list is end then beginning of move
                if (not self.board[location[2]][location[3]].title == targetPiece or
                    self.board[location[0]][location[1]] == self.board[location[2]][location[3]]):
                    return [False, -1, -1, -1, -1]
            except:
                return [False, -1, -1, -1, -1]
            else:
                if (not -1 in location and  # Checks to make sure the valid input has a valid location assosiated with it
                    location[0:2] in self.board[location[2]][location[3]].availableMoves(location[2], location[3], self.board)): # Checks if the end spot is a valid place for the piece to move
                    return [True] + location # True, ending coordinate 1, ending coordinate 2, starting coordinate 1, starting coordinate 2
                return [False, -1, -1, -1, -1] 
        
        if ord(userInput[0].lower()) > 96 and ord(userInput[0].lower()) < 105:
            return mainCode(2, "Pawn", True)
        elif userInput[0].lower() == "x":
            return mainCode(3, "Pawn", False)
        elif userInput[0].lower() in self.pieces:
            if userInput[1].lower() == "x":
                return mainCode(4, self.pieces[userInput[0].lower()], False)
            else:
                return mainCode(3, self.pieces[userInput[0].lower()], True)
        return [False, -1, -1, -1, -1]
    
    def playerTurn(self):
        while True:
            userInput = InputProcessor.InputProcessor(input("Please enter your turn: "))
            move = userInput.ProcessInput(self.board)
            if move[0] == True:
                self.board[move[3]][move[4]] = self.board[move[1]][move[2]] # Replacing the end of move with the starting piece
                self.board[move[1]][move[2]] = " " # Clears the starting position
                break
            else:
                print("Error: Invalid Move")
