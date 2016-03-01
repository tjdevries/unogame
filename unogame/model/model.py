#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unogame imports
from unogame.util.deck import Deck
from unogame.util.player import Player


class Model(object):
    def __init__(self, num_players):
        ''' Creates a model object that will be used to control one particular game '''
        self.deck = Deck()
        self.players = [Player(self.deck, 'Player {}'.format(num)) for num in range(num_players)]

    def game_over(self):
        return any(player.hand.count == 0 for player in self.players)
