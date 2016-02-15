from enum import Enum


class Card():
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if value in UnoSuit:
            self._suit = value
        else:
            raise ValueError('Not a valid UnoColor')

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    def __repr__(self):
        return 'Suit: {}, Rank{}'.format(self.suit, self.rank)

    def __str__(self):
        return 'Suit: {}, Rank{}'.format(self.suit, self.rank)


class UnoSuit(Enum):
    BLUE = 'BLUE'
    GREEN = 'GREEN'
    YELLOW = 'YELLOW'
    RED = 'RED'
    NEUTRAL = 'NEUTRAL'
