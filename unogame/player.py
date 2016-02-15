# !/usr/bin/env python3
#  -*- coding: utf-8 -*-


import random
from unogame import deck
from unogame.utils import stack


class Player:
    __version__ = '0.3.1'

    def __init__(self, deck, name='Default'):
        self.hand = {}
        self.name = name
        self.hand = deck.populatePlayerHand()
        self.Deck = deck

    def __populate_hand(self, deck):
        self.hand = deck.populatePlayerHand()

    def valid_cards(self):
        valid_cards = self.get_valid_cards()
        if len(valid_cards) < 1:
            return False
        else:
            return True

    def get_valid_cards(self):
        valid_cards = {}
        flag_suit = self.Deck.table['suit']
        flag_number = self.Deck.table['number']

        if flag_suit in self.hand:
            # We have the suit, now lets fetch the numbers from the suit
            if flag_suit not in valid_cards:
                valid_cards[flag_suit] = []
            for value in self.hand[flag_suit]:
                valid_cards[flag_suit].append(value)

        # Lets search for the valid numbers now
        for suit in self.hand:
            # Already trapped
            if suit is not flag_suit:
                if flag_number in self.hand[suit]:
                    # Found a matching number. Add it to the valid stack
                    if suit not in valid_cards:
                        valid_cards[suit] = []
                    valid_cards[suit].append(flag_number)
        return valid_cards

    def play(self):
        # print self.Deck.available
        print('{0} playing.'.format(self.name))
        while not self.valid_cards():
            self.buy_card()

        valid_cards = self.get_valid_cards()

        if len(valid_cards) > 1:
            # More than one suit
            chosen_card = stack.chooseOne(valid_cards)
            suit = chosen_card[0]
            value = chosen_card[1][0]
            chosen_card = {suit: value}
        else:
            # Choose the suit here
            if stack.valuesAmmount(valid_cards) > 1:
                # One suit, more than a value
                chosen_card = stack.chooseOne(valid_cards)
                suit = chosen_card[0]
                value = chosen_card[1][0]
                chosen_card = {suit: value}
            else:
                # Only one suit and one value, thats the card we want.
                chosen_card = valid_cards
                for k, v in chosen_card.iteritems():
                    suit = k
                    value = v[0]

                chosen_card = {suit: value}
        self.play_card(chosen_card)

    def buy_card(self):
        bought = self.Deck.buy_card()
        print('Bought card: ', bought)
        suit = bought.keys()[0]
        number = bought[suit]
        if suit not in self.hand:
            self.hand[suit] = []
        self.hand[suit].append(number)

    def refresh_hand(self):
        pass

    def play_card(self, card):
        for k, v in card.items():
            suit = k
            value = v
        self.hand[suit].remove(value)

        # Refresh hand if needed
        if len(self.hand[suit]) == 0:
            del self.hand[suit]
        self.Deck.play_card(card)

    def say_uno(self):
        if random.randint(0, 20) == 2:
            return True
        else:
            return False


class HumanPlayer(Player):

    def play(self):
        print('Human playing')

        while not self.valid_cards():
            input("Buying a card...<enter>")
            self.buy_card()
        print('\nValid cards: {0}'.format(self.get_valid_cards()))
        suit = number = ''
        while suit not in self.get_valid_cards():
            suit = input("Choose the suit > ")
        while number not in self.get_valid_cards()[suit]:
            number = input("Choose the number > ")

        card = {suit: number}

        self.play_card(card)


if __name__ == '__main__':
    Deck = deck.Deck()
    heya = Player(Deck, 'Pancho')
    heya.play()
