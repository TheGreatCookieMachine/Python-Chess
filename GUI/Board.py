import tkinter
import Game.Game as Game

class Board():
    def __init__(self):
        self.moves = tkinter.StringVar()
        self.error = tkinter.StringVar()
        self.pieces = []
        self.numberSwap = (7, 6, 5, 4, 3, 2, 1, 0) # Used in printScreen to ensure the board is printed the right way
        
        self.boardCanvas = tkinter.Canvas(height=400, width=400, borderwidth=1, relief="solid")
        self.boardImage = tkinter.PhotoImage(file="GUI\\Assests\\ChessBoard.gif")
        self.boardCanvas.create_image(3, 3, image=self.boardImage, anchor="nw")
        
        self.moveLogLabelFrame = tkinter.LabelFrame(height=325, width=175, borderwidth=1, relief="solid")
        self.moveLogLabel = tkinter.Label(self.moveLogLabelFrame, textvariable=self.moves, font=("Calbri", 11), anchor="nw", justify="left", wraplength=175)

        self.inputLabelFrame = tkinter.LabelFrame(height=25, width=175, borderwidth=1, relief="solid")
        self.inputLabel = tkinter.Entry(self.inputLabelFrame, font=("Calbri", 12), width=18)
        self.inputLabel.bind("<Return>", self.takeInput)

        self.errorLogLabelFrame = tkinter.LabelFrame(height=25, width=175, borderwidth=1, relief="solid")
        self.errorLogLabel = tkinter.Label(self.errorLogLabelFrame, textvariable=self.error, font=("Calbri", 11), anchor="nw")

        self.session = Game.Game()
    
    def printScreen(self):
        self.boardCanvas.place(x=24, y=24)

        self.moveLogLabelFrame.place(x=450, y=24)
        self.moveLogLabel.place(x=0, y=0)

        self.inputLabelFrame.place(x=450, y=375)
        self.inputLabel.place(x=0, y=0)

        self.errorLogLabelFrame.place(x=450, y=400)
        self.errorLogLabel.place(x=0, y=0)

        self.updateBoard()

    def updateBoard(self):
        self.pieces = []
        for column in range(len(self.session.board)):
            for row in range(len(self.session.board[column])):
                if self.session.board[column][row] != " ":
                    piece = self.session.board[column][row]
                    image = tkinter.PhotoImage(file="GUI\\Assests\\" + str(piece.side.capitalize()) + str(piece.title) + ".gif")
                    self.pieces.append(image)
                    self.boardCanvas.create_image(row * 50 + 3, self.numberSwap[column] * 50 + 3, image=self.pieces[-1], anchor="nw")
    
    def takeInput(self, event):
        userInput = self.inputLabel.get()
        if len(userInput) > 0:
            self.inputLabel.delete(0, "end")
            # Temporary turn rotation fix until AI is added
            if self.session.turn == self.session.player:
                validMove = self.session.playerTurn(userInput)
                if validMove:
                    self.session.turn = self.session.computer
            else:
                validMove = self.session.computerTurn(userInput)
                if validMove:
                    self.session.turn = self.session.player
            
            if validMove:
                self.moves.set(self.moves.get() + userInput + "\n")
                self.error.set("")
                self.updateBoard()
            else:
                self.error.set("Error: Invalid Move")
