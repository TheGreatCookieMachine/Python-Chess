import random
import copy
import Game.Pieces as Pieces
import InputOutput.InputProcessor as InputProcessor

class Game():
    def __init__(self):
        self.turn = "white"
        self.player = "white" if random.randint(0, 1) == 1 else "black" # Temporary way of choosing side until player choice is given
        self.computer = "white" if self.player == "black" else "black"
        self.board = [[Pieces.Rook("white"), Pieces.Knight("white"), Pieces.Bishop("white"), Pieces.Queen("white"),
                      Pieces.King("white"), Pieces.Bishop("white"), Pieces.Knight("white"), Pieces.Rook("white")],
                      [Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"),
                      Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white"), Pieces.Pawn("white")],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " ", " "],
                      [Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"),
                      Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black"), Pieces.Pawn("black")],
                      [Pieces.Rook("black"), Pieces.Knight("black"), Pieces.Bishop("black"), Pieces.Queen("black"),
                      Pieces.King("black"), Pieces.Bishop("black"), Pieces.Knight("black"), Pieces.Rook("black")]]
        self.pieces = {"r": Pieces.Rook, "n": Pieces.Knight, "b": Pieces.Bishop, "q": Pieces.Queen, "k": Pieces.King}
    
    def drawBoard(self):
        print("---------------------------------")
        # Technically breaks PEP 8, however only by a little, and this is with splitting the line in two
        for i in range(7, -1, -1):
            print("| " + str(self.board[i][0]) + " | " + str(self.board[i][1]) + " | " + str(self.board[i][2]) + " | " + str(self.board[i][3]) +
                  " | " + str(self.board[i][4]) + " | " + str(self.board[i][5]) + " | " + str(self.board[i][6]) + " | " + str(self.board[i][7]) + " |")
            print("---------------------------------")
    
    def getPiecePosition(self, board, piece, side=None):
        piecePosition = []
        for i in range(len(board)):
            for n in range(len(board[i])):
                if type(board[i][n]) == piece and side != None and board[i][n].side == side:
                    piecePosition.append([i, n])
        return piecePosition

    def isCheck(self, board, side):
        kingPosition = self.getPiecePosition(board, Pieces.King, side)[0] # Only one king per side is possible, as such we can simply take the first item of the list
        for i in range(len(board)):
            for n in range(len(board[i])):
                if board[i][n] != " " and type(board[i][n]) != Pieces.King:
                    moves = board[i][n].availableMoves(i, n, board)
                    if kingPosition in moves:
                        return True
        return False
    
    def playerTurn(self, userInput):
        userInput = InputProcessor.InputProcessor(userInput)
        move = userInput.processInput(self.board)
        if move[0] == True:
            boardCopy = copy.deepcopy(self.board)
            boardCopy[move[3]][move[4]] = boardCopy[move[1]][move[2]] # Replacing the end of move with the starting piece
            boardCopy[move[1]][move[2]] = " " # Clears the starting position
            if len(move) == 6:
                boardCopy[move[3]][move[4]] = self.pieces[move[5]](boardCopy[move[3]][move[4]].side)
                boardCopy[move[3]][move[4]].hasMoved = True
            if self.isCheck(boardCopy, self.player):
                return False
            else:
                if self.isCheck(boardCopy, self.computer):
                    print("Computer is in check")
                self.board[move[3]][move[4]] = self.board[move[1]][move[2]] # Replacing the end of move with the starting piece
                self.board[move[3]][move[4]].hasMoved = True
                self.board[move[1]][move[2]] = " " # Clears the starting position
                if len(move) == 6:
                    self.board[move[3]][move[4]] = self.pieces[move[5]](self.board[move[3]][move[4]].side)
                    self.board[move[3]][move[4]].hasMoved = True
                return True
        else:
            return False
