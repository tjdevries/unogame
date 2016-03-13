from enum import Enum


class Card(object):
    def __init__(self, suit, rank):
        """Create a card object"""
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        """Getter for suit"""
        return UnoSuit(self._suit)

    @suit.setter
    def suit(self, value):
        """Correctly sets the suit"""
        if value in UnoSuit:
            self._suit = value
        # TODO(Q): Check if already an UnoSuit object
        else:
            raise ValueError('Not a valid UnoColor')

    @property
    def rank(self):
        """Getter for rank"""
        return self._rank

    @rank.setter
    def rank(self, value):
        """Correctly sets the rank"""
        self._rank = value

    @property
    def effect(self):
        """
        Numbers work as follows:
            1 - 9   : No effect
            10      : Skip
            11      : Reverse
            12      : Draw 2
            13      : Wild
            14      : Draw 4 + Wild
        """
        if self.rank < 10:
            return None
        # Skip
        elif self.rank == 10:
            return {'skip': 1}
        # Reverse
        elif self.rank == 11:
            return {'reverse': 1}
        # Draw 2
        elif self.rank == 12:
            return {'draw': 2}
        # Basic wild
        elif self.rank == 13:
            return {'wild': 'TODO'}
        # Draw 4, Wild
        elif self.rank == 14:
            return {'wild': 'TODO', 'draw': 4}

    def is_playable_card(self, card):
        """
        Returns true if a card is playable

        TODO:
            Logic
        """
        # Playing cards of the same color
        if card.suit == self.suit:
            return True

        # Playing cards of the same type
        if card.rank == self.rank:
            return True

        # You can always play neutral cards
        if self.suit == UnoSuit.NEUTRAL:
            return True

        return False

    def __repr__(self):
        return 'Suit: {}, Rank: {}'.format(self.suit, self.rank)

    def __str__(self):
        return 'S:{}, R:{}'.format(self.suit, self.rank)


# class CardEffects:
#     def __init__(self, rank):
#         self.rank = rank

#     @property


class UnoSuit(Enum):
    BLUE = 'BLUE'
    GREEN = 'GREEN'
    YELLOW = 'YELLOW'
    RED = 'RED'
    NEUTRAL = 'NEUTRAL'

    @property
    def possible_ranks(self):
        return UnoRanks(self).ranks

    @classmethod
    def colors(cls):
        return [cls.BLUE.value, cls.GREEN.value, cls.YELLOW.value, cls.RED.value]

    def __str__(self):
        return self.value[0]


class UnoRanks(object):
    def __init__(self, suit):
        """UnoRanks are objects that make sure we have correct ranks per each suit"""
        self._suit = suit

    @property
    def suit(self):
        return UnoSuit(self._suit)

    @suit.setter
    def suit(self, value):
        if value in UnoSuit:
            self._suit = value
        else:
            raise ValueError('Not a valid UnoSuit')

    @property
    def ranks(self):
        rank_list = []
        if self.suit in list(UnoSuit):
            rank_list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
            # TODO: Add skip, reverse

        # if self.suit in [UnoSuit.NEUTRAL]:
        #     rank_list.extend(['wild', 'wild4'])

        return rank_list
