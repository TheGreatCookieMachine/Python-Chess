import random
import Pieces

class Game():
    def __init__(self):
        self.player = "white" if random.randint(0, 1) == 1 else "black" # Temporary way of choosing side until player choice is given
        self.computer = "white" if self.player == "black" else "black"
        # This section breaks PEP 8, however I feel breaking lines in two would be weird, I will fix if I think of a solution
        self.board = [[Pieces.Rook("white"), Pieces.Knight("white"), Pieces.Bishop("white"), Pieces.King("white"), Pieces.Queen("white"), Pieces.Bishop("white"), Pieces.Knight("white"), Pieces.Rook("white")],
                      [Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white")],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black")],
                      [Pieces.Rook("black"), Pieces.Knight("black"), Pieces.Bishop("black"), Pieces.King("black"), Pieces.Queen("black"), Pieces.Bishop("black"), Pieces.Knight("black"), Pieces.Rook("black")]]
    
    def drawBoard(self):
        # This section probably killed PEP 8, however as with before splitting lines in two seems odd, I will fix if I think of a solution. Then again it kills my eyes to look at so I may change it sooner
        print("---------------------------------")
        print("| " + str(self.board[7][0]) + " | " + str(self.board[7][1]) + " | " + str(self.board[7][2]) + " | " + str(self.board[7][3]) + " | " + str(self.board[7][4]) + " | " + str(self.board[7][5]) + " | " + str(self.board[7][6]) + " | " + str(self.board[7][7]) + " |")
        print("---------------------------------")
        print("| " + str(self.board[6][0]) + " | " + str(self.board[6][1]) + " | " + str(self.board[6][2]) + " | " + str(self.board[6][3]) + " | " + str(self.board[6][4]) + " | " + str(self.board[6][5]) + " | " + str(self.board[6][6]) + " | " + str(self.board[6][7]) + " |")
        print("---------------------------------")
        print("| " + str(self.board[5][0]) + " | " + str(self.board[5][1]) + " | " + str(self.board[5][2]) + " | " + str(self.board[5][3]) + " | " + str(self.board[5][4]) + " | " + str(self.board[5][5]) + " | " + str(self.board[5][6]) + " | " + str(self.board[5][7]) + " |")
        print("---------------------------------")
        print("| " + str(self.board[4][0]) + " | " + str(self.board[4][1]) + " | " + str(self.board[4][2]) + " | " + str(self.board[4][3]) + " | " + str(self.board[4][4]) + " | " + str(self.board[4][5]) + " | " + str(self.board[4][6]) + " | " + str(self.board[4][7]) + " |")
        print("---------------------------------")
        print("| " + str(self.board[3][0]) + " | " + str(self.board[3][1]) + " | " + str(self.board[3][2]) + " | " + str(self.board[3][3]) + " | " + str(self.board[3][4]) + " | " + str(self.board[3][5]) + " | " + str(self.board[3][6]) + " | " + str(self.board[3][7]) + " |")
        print("---------------------------------")
        print("| " + str(self.board[2][0]) + " | " + str(self.board[2][1]) + " | " + str(self.board[2][2]) + " | " + str(self.board[2][3]) + " | " + str(self.board[2][4]) + " | " + str(self.board[2][5]) + " | " + str(self.board[2][6]) + " | " + str(self.board[2][7]) + " |")
        print("---------------------------------")
        print("| " + str(self.board[1][0]) + " | " + str(self.board[1][1]) + " | " + str(self.board[1][2]) + " | " + str(self.board[1][3]) + " | " + str(self.board[1][4]) + " | " + str(self.board[1][5]) + " | " + str(self.board[1][6]) + " | " + str(self.board[1][7]) + " |")
        print("---------------------------------")
        print("| " + str(self.board[0][0]) + " | " + str(self.board[0][1]) + " | " + str(self.board[0][2]) + " | " + str(self.board[0][3]) + " | " + str(self.board[0][4]) + " | " + str(self.board[0][5]) + " | " + str(self.board[0][6]) + " | " + str(self.board[0][7]) + " |")
        print("---------------------------------")
