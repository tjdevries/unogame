from enum import Enum


class Card(object):
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

    @property
    def effect(self):
        if self.rank < 10:
            return None

    def is_playable_card(self, card):
        """
        Returns true if a card is playable

        TODO:
            Logic
        """
        if card.suit == self.suit:
            return True

        if card.rank == self.rank:
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
        return UnoRanks(self.value).ranks

    @classmethod
    def colors(cls):
        return [cls.BLUE.value, cls.GREEN.value, cls.YELLOW.value, cls.RED.value]

    def __str__(self):
        return self.value[0]


class UnoRanks(object):
    def __init__(self, suit):
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if value in UnoSuit:
            self._suit = value
        else:
            raise ValueError('Not a valid UnoSuit')

    @property
    def ranks(self):
        rank_list = []
        if self.suit in UnoSuit.colors():
            rank_list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
            # TODO: Add skip, reverse

        if self.suit in [UnoSuit.NEUTRAL]:
            rank_list.extend(['wild', 'wild4'])

        return rank_list
