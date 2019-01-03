import random
import copy
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
    
    def isCheck(self, board):
        for i in range(len(board)):
            for n in range(len(board[i])):
                if type(board[i][n]) == Pieces.King:
                    kingPosition = [i, n]
        for i in range(len(board)):
            for n in range(len(board[i])):
                if board[i][n] != " " and type(board[i][n]) != Pieces.King:
                    moves = board[i][n].availableMoves(i, n, board)
                    if kingPosition in moves:
                        return True
        return False
    
    def playerTurn(self):
        while True:
            userInput = InputProcessor.InputProcessor(input("Please enter your turn: "))
            move = userInput.processInput(self.board)
            if move[0] == True:
                boardCopy = copy.deepcopy(self.board)
                boardCopy[move[3]][move[4]] = boardCopy[move[1]][move[2]] # Replacing the end of move with the starting piece
                boardCopy[move[1]][move[2]] = " " # Clears the starting position
                if self.isCheck(boardCopy):
                    print("Check")
                self.board[move[3]][move[4]] = self.board[move[1]][move[2]] # Replacing the end of move with the starting piece
                self.board[move[3]][move[4]].hasMoved = True
                self.board[move[1]][move[2]] = " " # Clears the starting position
                break
            else:
                print("Error: Invalid Move")
