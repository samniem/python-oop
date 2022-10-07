import random

class Coin():
    def __init__(self):
        self.state = "head"

    def checkState(self):
        print("The coin is showing", self.state)
    
    def flip(self):
        self.state = random.choice(['head','tails'])
        self.checkState()

coin1 = Coin()
coin1.checkState()
coin1.flip()

coin2 = Coin()
coin2.checkState()
coin2.flip()