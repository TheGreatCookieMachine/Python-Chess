import GUI.GUI as GUI

class Main():
    def __init__(self):
        self.gui = GUI.GUI()
        self.gui.printScreen()

if __name__ == "__main__":
    main = Main()
    main.gui.root.mainloop()
