import Game.Game as Game

class Main():
    def __init__(self):
        self.running = True
    
    def startUp(self):
        self.session = Game.Game()
        self.mainLoop()

    def mainLoop(self):
        while True:
            if self.session.turn == self.session.player:
                self.session.drawBoard()
                print("Player's turn")
                self.session.playerTurn()
                self.session.turn = self.session.computer
            # Temporarily does player turn until AI is added
            if self.session.turn == self.session.computer:
                self.session.drawBoard()
                print("Computer's turn")
                self.session.playerTurn()
                self.session.turn = self.session.player

main = Main()
main.startUp()
