#This is a practice project to test converting higher or lower from https://github.com/IrvKalb/Object-Oriented-Python-Code/blob/master/Chapter_1/HigherOrLowerProcedural.py
#into object oriented style before progressing further into the book


#BSD 2-Clause License

#Copyright (c) 2020, Irv Kalb
#All rights reserved.


import random

class Deck():
    # Card constants
    SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
    RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self):
        self.deck = self.__generateDeck()
        self.shuffledDeck = self.shuffle()

    #private method only invoced during init
    def __generateDeck(self):
        startingDeckList = []
        for suit in self.SUIT_TUPLE:
            for thisValue, rank in enumerate(self.RANK_TUPLE):
                cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
                startingDeckList.append(cardDict)
        return startingDeckList

    def shuffle(self):
        deckListOut = self.deck.copy()  # make a copy of the starting deck
        random.shuffle(deckListOut)
        self.shuffledDeck = deckListOut

    def getCard(self):
        thisCard = self.shuffledDeck.pop() # pops one off the top of the deck and returns it
        return thisCard
        
#  Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

score = 50
NCARDS = 8

deck = Deck()

while True:  # play multiple games
    print()
    deck.shuffle()
    currentCardDict = deck.getCard()
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']    
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):   # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' + 
                               currentCardRank + ' of ' + 
                               currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()  # force lower case
        nextCardDict = deck.getCard()
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15          

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')


    
    



         

    
