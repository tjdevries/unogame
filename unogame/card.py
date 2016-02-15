from enum import Enum


class Card():
    def __init__(self, color, rank):
        self._color = color
        self._rank = rank

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value in UnoColor:
            self._color = value
        else:
            raise ValueError('Not a valid UnoColor')

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value


class UnoColor(Enum):
    BLUE = 0
    GREEN = 1
    YELLOW = 2
    RED = 3
    NEUTRAL = 4
