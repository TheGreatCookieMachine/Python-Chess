import tkinter
import GUI.Board as Board

class GUI():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Chess")
        self.root.geometry("650x450")
        # self.root.resizable(False, False)

        self.frames = [Board.Board()]
        self.currentFrame = 0
    
    def printScreen(self):
        self.frames[self.currentFrame].printScreen()
