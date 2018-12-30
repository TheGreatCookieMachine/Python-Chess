import random
import Game.Pieces as Pieces
import InputOutput.InputProcessor as InputProcessor

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
    
    def playerTurn(self):
        while True:
            userInput = InputProcessor.InputProcessor(input("Please enter your turn: "))
            move = userInput.processInput(self.board)
            if move[0] == True:
                self.board[move[3]][move[4]] = self.board[move[1]][move[2]] # Replacing the end of move with the starting piece
                self.board[move[3]][move[4]].hasMoved = True
                self.board[move[1]][move[2]] = " " # Clears the starting position
                break
            else:
                print("Error: Invalid Move")
