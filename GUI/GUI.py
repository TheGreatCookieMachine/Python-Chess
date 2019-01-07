import tkinter
import Board

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

if __name__ == "__main__":
    gui = GUI()
    gui.printScreen()
    gui.root.mainloop()
