'''
author: Hekmat Hamidi
purpose: OOP practice / Data abstraction
State: Compeleted
'''
import random


class Cards:

    def __init__(self):
        self.ranks = {1: 'Ace', 2: 2, 3: 3, 4: 4,
                    5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
                    10: 10, 11: 'Jack', 12: 'Queen', 13: 'King'}

        self.types = {0: 'Hearts', 1: 'Clubs', 2: 'Clover', 3: 'Spades'}


    def getRank(self):
        return self.ranks

    def getTypes(self):
        return self.types


class Deck(Cards):

    def __init__(self):
        Cards.__init__(self)
        self.cardDeck = []
        self.generateDeck()

    def generateDeck(self):
        for rank in self.ranks:
            for type in self.types:
                self.cardDeck.append([rank,type]) # vector stores type and rank
        return self.cardDeck


    def getCard(self):
        running = True
        while running:
            try:
                random_card = self.cardDeck[random.randrange(0,51)] # workd on removing the card after it gets chosen
                self.cardDeck.remove(random_card)
                running = False
            except:
                if len(self.cardDeck) == 0:
                    return 'Deck of card is empty.'
                running = True
        return self.ranks[random_card[0]], self.types[random_card[1]]







card = Deck()
for i in range(1,54):
    print(card.getCard())
    print(card.cardDeck)
