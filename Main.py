import Game

class Main():
    def __init__(self):
        self.running = True
    
    def startUp(self):
        return
    
    def mainLoop(self):
        return

# Here for testing purposes, will be changed and moved into Main() later
session = Game.Game()
session.drawBoard()
while True:
    print(session.getLocation(input()))
