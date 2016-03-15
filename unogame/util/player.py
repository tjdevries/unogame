# !/usr/bin/env python3
#  -*- coding: utf-8 -*-


import logging


my_logger = logging.getLogger('uno.player')


class Player:
    def __init__(self, deck, name='Default'):
        self.name = name
        self.deck = deck
        self.hand = deck.populate_player_hand()

    def get_valid_cards(self):
        valid_cards = []
        table_card = self.deck.table_card

        for card in self.hand:
            if table_card.is_playable_card(card):
                valid_cards.append(card)

        my_logger.debug('Table: {}, {}\'s Valid Cards: {}'.format(
            table_card,
            self.name,
            valid_cards)
        )
        return valid_cards

    def play(self):
        print('{0} playing.'.format(self.name))

        valid_cards = self.get_valid_cards()
        while not valid_cards:
            self.draw_card()
            valid_cards = self.get_valid_cards()

        chosen_card = valid_cards[0]

        return self.play_card(chosen_card)

    def draw_card(self):
        drawn = self.deck.draw_card()
        print('Drew card: ', drawn)
        self.hand.add_card(drawn)

    def refresh_hand(self):
        pass

    def play_card(self, card):
        self.hand.remove_card(card)
        self.deck.play_card(card)
        return card.effect

    def say_uno(self):
        return True

    def draw_cards(self, num):
        for _ in range(num):
            self.draw_card()


class HumanPlayer(Player):

    def play(self):
        print('Human playing')
        my_logger.debug('Current Hand: {}'.format(self.hand))

        while not self.get_valid_cards():
            input("Drawing a card...<enter>")
            self.draw_card()

        print('\nValid cards: {0}'.format(self.get_valid_cards()))

        chosen = ''
        while(not isinstance(chosen, int)):
            try:
                chosen = int(input("Insert something"))
            except Exception:
                continue

            try:
                card = self.get_valid_cards()[chosen]
            except IndexError:
                chosen = ''
                print('Please input a valid card')

        return self.play_card(card)
