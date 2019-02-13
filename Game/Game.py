import random
import copy
import Game.Pieces as Pieces
import InputOutput.InputProcessor as InputProcessor

class Game():
    def __init__(self):
        self.turn = "white"
        self.player = "white"
        self.computer = "black"
        # self.player = "white" if random.randint(0, 1) == 1 else "black" # Temporary way of choosing side until player choice is given
        # self.computer = "white" if self.player == "black" else "black"
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
    
    def executeMove(self, board, move, side):
        if not move[1] == "kingside" and not move[1] == "queenside":
            board[move[3]][move[4]] = board[move[1]][move[2]] # Replacing the end of move with the starting piece
            board[move[3]][move[4]].hasMoved = True
            board[move[1]][move[2]] = " " # Clears the starting position
            if len(move) == 6:
                board[move[3]][move[4]] = self.pieces[move[5]](board[move[3]][move[4]].side)
                board[move[3]][move[4]].hasMoved = True
        else:
            kingRow = 0 if side == "white" else 7
            if move[1] == "kingside":
                board[kingRow][6] = board[kingRow][4]
                board[kingRow][6].hasMoved = True
                board[kingRow][4] = " "
                board[kingRow][5] = board[kingRow][7]
                board[kingRow][5].hasMoved = True
                board[kingRow][7] = " "
            else:
                board[kingRow][2] = board[kingRow][4]
                board[kingRow][2].hasMoved = True
                board[kingRow][4] = " "
                board[kingRow][3] = board[kingRow][0]
                board[kingRow][3].hasMoved = True
                board[kingRow][0] = " "
    
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
        move = userInput.processInput(self.board, self.player)
        if move[0] == True:
            boardCopy = copy.deepcopy(self.board)
            self.executeMove(boardCopy, move, self.player)
            if self.isCheck(boardCopy, self.player):
                return False
            else:
                self.executeMove(self.board, move, self.player)
                computerKingPosition = self.getPiecePosition(self.board, Pieces.King, self.computer)[0]
                if self.isCheck(boardCopy, self.computer):
                    print("Computer is in check")
                    self.board[computerKingPosition[0]][computerKingPosition[1]].check = True
                else:
                    self.board[computerKingPosition[0]][computerKingPosition[1]].check = False
                return True
        else:
            return False
    
    # Temporary computer turn
    def computerTurn(self, userInput):
        userInput = InputProcessor.InputProcessor(userInput)
        move = userInput.processInput(self.board, self.computer)
        if move[0] == True:
            boardCopy = copy.deepcopy(self.board)
            self.executeMove(boardCopy, move, self.computer)
            if self.isCheck(boardCopy, self.computer):
                return False
            else:
                self.executeMove(self.board, move, self.computer)
                playerKingPosition = self.getPiecePosition(self.board, Pieces.King, self.player)[0]
                if self.isCheck(boardCopy, self.player):
                    print("Player is in check")
                    self.board[playerKingPosition[0]][playerKingPosition[1]].check = True
                else:
                    self.board[playerKingPosition[0]][playerKingPosition[1]].check = False
                return True
        else:
            return False
