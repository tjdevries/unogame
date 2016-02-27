#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random
import logging
from unogame.util.hand import Hand
from unogame.util.card import Card, UnoSuit

my_logger = logging.getLogger('uno.deck')


class Deck(object):
    def __init__(self):
        self.available = []
        self.table = []
        self.__trash = []
        self.__unavailable = []

        # Populate the Deck
        self._populate()
        self._put_card_on_table(random.choice(self.available))

        print('On the table: ', self.table[-1])
        # self.scaffold()

    @property
    def table_card(self):
        return self.table[-1]

    def _populate(self):
        for suit in list(UnoSuit):
            my_logger.debug('Available Ranks for Suit <{}>: {}'.format(
                suit,
                suit.possible_ranks)
            )

            for i in suit.possible_ranks:
                self.available.append(Card(suit, i))

    def _put_card_on_table(self, card):
        # Neutrals compliant as of Oct.27, 21: 55
        '''Appends the new card to the table'''
        self._set_as_unavailable(card)
        self.table.append(card)

    def _set_as_unavailable(self, card):
        # Remove the card from its stack
        try:
            self.available.remove(card)
        except ValueError:
            my_logger.debug('Could not remove: `{}`'.format(card))
        self.__unavailable.append(card)

    def play_card(self, card):
        self._put_card_on_table(card)
        print('Card played.\n\nOn the table: ', self.table[-1], '\n')

    def populate_player_hand(self):
        hand = Hand()
        for _ in range(5):
            card = self.random_card()

            hand.add_card(card)

            self._set_as_unavailable(card)

        return hand

    def _reshuffle(self):
        pass

    def random_card(self):
        return random.choice(self.available)

    def draw_card(self):
        if len(self.available) == 0:
            self.discard_pile_reshuffle()

        drawn = self.random_card()
        self._set_as_unavailable(drawn)

        return drawn

    def discard_pile_reshuffle(self):
        reshuffle_cards = self.table[0:-1]
        self.table = [self.table[-1]]
        self.available.extend(reshuffle_cards)


if __name__ == '__main__':
    deck = Deck()
    print('-----\nAvailable: \n %s \n-----' % deck.available)
