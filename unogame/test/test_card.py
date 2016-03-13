#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard Imports
import unittest

# Module Imports
from unogame.util.card import Card, UnoSuit


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        c = Card("BLUE", 5)

        self.assertEqual(c.suit, UnoSuit.BLUE)
        self.assertEqual(c.rank, 5)
        self.assertEqual(c.effect, None)

    def test_special_card_creation(self):
        c = Card("BLUE", 11)

        self.assertEqual(c.rank, 11)
