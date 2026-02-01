from random import shuffle

SUIT_SYMBOLS = {
    "Hearts": "♥",
    "Diamonds": "♦",
    "Clubs": "♣",
    "Spades": "♠",
}


SUITS = ["Diamonds",
         "Hearts",
         "Spades",
         "Clubs"]

RANKS = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.point : int = self._get_point()

    def _get_point(self):
        if self.rank in["1","2","3","4","5","6","7","8","9","10"]:
            self.point = int(self.rank)
        elif self.rank == "Jack":
            self.point = 11
        elif self.rank == "Queen":
            self.point = 12
        elif self.rank == "King":
            self.point = 13
        else:
            raise ValueError("invalid rank for this card")

        return self.point


    def __str__(self):
        symbol = SUIT_SYMBOLS[self.suit]
        return f"{symbol} {self.rank}"

def get_cards():
    cards = []

    for suit in SUITS:
        for rank in RANKS:
            cards.append(Card(suit,rank))

    shuffle(cards)
    return cards