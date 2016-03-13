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
        self._current_player_id = 0

        # Special Cases
        self.direction = 1

    def game_over(self):
        return any(player.hand.count == 0 for player in self.players)

    @property
    def current_player_id(self):
        return self._current_player_id

    @current_player_id.setter
    def current_player_id(self, value):
        value = value % len(self.players)
        self._current_player_id = value

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_id]

    @current_player.setter
    def current_player(self, value):
        value = value % len(self.players)
        self.current_player_id = value

    @property
    def next_player(self) -> Player:
        next_player = self._current_player % len(self.players)
        return self.players[next_player]

    def increment_player(self):
        self.current_player_id = self.current_player_id + self.direction

    def reverse(self):
        self.direction = -1 * self.direction

    def skip(self):
        self.increment_player()
