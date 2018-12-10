import random
import Pieces

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
    
    def isValidInput(self, userInput):
        if ord(userInput[0].lower()) > 96 and ord(userInput[0].lower()) < 105:
            try:
                location = self.getLocation(userInput[2:4])
                if self.board[location[0]][location[1]] != " ":
                    return False
                location += self.getLocation(userInput[0:2])
                if not self.board[location[2]][location[3]].title == "Pawn":
                    return False
            except:
                return False
            else:
                if not -1 in location:
                    return True
        elif userInput[0].lower() == "x":
            try:
                location = self.getLocation(userInput[3:5])
                if self.board[location[0]][location[1]] == " ":
                    return False
                location += self.getLocation(userInput[1:3])
                if not self.board[location[2]][location[3]].title == "Pawn":
                    return False
            except:
                return False
            else:
                if not -1 in location:
                    return True
        elif userInput[0].lower() in self.pieces:
            if userInput[1].lower() == "x":
                try:
                    location = self.getLocation(userInput[4:6])
                    if self.board[location[0]][location[1]] == " ":
                        return False
                    location += self.getLocation(userInput[2:4])
                    if not self.board[location[2]][location[3]].title == self.pieces[userInput[0].lower()]:
                        return False
                except:
                    return False
                else:
                    if not -1 in location:
                        return True
            else:
                try:
                    location = self.getLocation(userInput[3:5])
                    if self.board[location[0]][location[1]] != " ":
                        return False
                    location += self.getLocation(userInput[1:3])
                    if not self.board[location[2]][location[3]].title == self.pieces[userInput[0].lower()]:
                        return False
                except:
                    return False
                else:
                    if not -1 in location:
                        return True
        return False
    
    def playerTurn(self):
        while True:
            move = input("Please enter your turn: ")
            try:
                start = self.getLocation(move[:2])
                end = self.getLocation(move[2:4])
                # If the user had an invalid input, which does not otherwise cause an error, raise an error
                if start[0] == -1 or end[0] == -1 or start == end:
                    raise BaseException
                # Otherwise, begin modifications to the board itself (Due to the first line checking both the start and end, errors will occur before destructive changes to the board are made)
                self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
                self.board[start[0]][start[1]] = " "
                break
            except:
                print("Error: Invalid Move")
