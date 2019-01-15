import tkinter

class Board():
    def __init__(self):
        self.moves = tkinter.StringVar()
        
        self.boardImage = tkinter.PhotoImage(file="ChessBoard.gif")
        self.boardLabel = tkinter.Label(image=self.boardImage, borderwidth=1, relief="solid")

        self.moveLogLabelFrame = tkinter.LabelFrame(height=325, width=175, borderwidth=1, relief="solid")
        self.moveLogLabel = tkinter.Label(self.moveLogLabelFrame, textvariable=self.moves, font=("Calbri", 11), anchor="nw", justify="left", wraplength=175)

        self.inputLabelFrame = tkinter.LabelFrame(height=25, width=175, borderwidth=1, relief="solid")
        self.inputLabel = tkinter.Entry(self.inputLabelFrame, font=("Calbri", 12), width=18)
        self.inputLabel.bind("<Return>", self.takeInput)

        self.errorLogLabelFrame = tkinter.LabelFrame(height=25, width=175, borderwidth=1, relief="solid")
        self.errorLogLabel = tkinter.Label(self.errorLogLabelFrame, text="Error: Error Example", font=("Calbri", 11), anchor="nw")
    
    def printScreen(self):
        self.boardLabel.place(x=24, y=24)

        self.moveLogLabelFrame.place(x=450, y=24)
        self.moveLogLabel.place(x=0, y=0)

        self.inputLabelFrame.place(x=450, y=375)
        self.inputLabel.place(x=0, y=0)

        self.errorLogLabelFrame.place(x=450, y=400)
        self.errorLogLabel.place(x=0, y=0)
    
    def takeInput(self, event):
        userInput = self.inputLabel.get()
        self.inputLabel.delete(0, "end")
        self.moves.set(self.moves.get() + userInput + "\n")
