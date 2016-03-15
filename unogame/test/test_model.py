#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard Imports
import unittest

# Unogame imports
from unogame.model import Model


class TestModel(unittest.TestCase):
    def test_model_init(self):
        num_players = 2
        m = Model(num_players)
        self.assertEqual(len(m.players), num_players)
