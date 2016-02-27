#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Unogame imports
from unogame.util.deck import Deck
from unogame.util.player import Player


class Model():
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [Player(self.deck) for player in range(num_players)]
