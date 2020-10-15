import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + " of " + self.suit


class Deck:
    def __init__(self):
        suits = ["spades","diamonds","clubs","hearts"]
        self.cards = [Card(value, suit) for suit in suits for value in range(1, 14)]

    def __str__(self):
        for card in self.cards:
            print(card)


    def draw(self):
        print(self.cards[0])
        self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
print(len(deck.cards))
