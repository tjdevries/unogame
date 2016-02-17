

class Hand():
    def __init__(self):
        self._cards = []
        self.__index = 0

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value

    @property
    def count(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def is_empty(self):
        if self.cards == []:
            return True
        return False

    # Iterator functionality
    #   You can now just loop over whats in your hand
    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.cards[self.__index]
        except IndexError:
            self.__index = 0
            raise StopIteration

        self.__index += 1
        return result

    def __str__(self):
        s = '<'
        for card in self.cards:
            s += ' ' + str(card)
        s += '>'
        return s
