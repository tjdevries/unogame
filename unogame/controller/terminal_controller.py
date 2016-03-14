#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple terminal controller to play Uno.
Make a terminal object, and then just run its main function!
"""
# Standard Imports
# from typing import String

# UNO Terminal Controller
from unogame import my_logger
from unogame.util.card import Card
from unogame.util.player import Player
from unogame.model.model import Model

winner = None


class TerminalController(object):
    def __init__(self):
        """Create our terminal controller object"""
        self.model = Model(3)
        self.winner = None

    def main(self):
        """Play the game"""
        while(not self.winner):
            self.play_turn()

        print('========================================')
        print('Winner is {}'.format(self.winner.name))
        print('========================================')

    def display_card(self, card: Card):
        card = [
            '┌─────────┐',
            '│{:2}       │'.format(card.rank),
            '│         │',
            '│         │',
            '│    {:3}  │'.format(card.suit),
            '│         │',
            '│         │',
            '│      {:2} │'.format(card.rank),
            '└─────────┘',
        ]

        return card

    def display_hand(self, player: Player):
        """Displays the hand in a nice string."""
        # TODO: Kind of ugly hack. Just made with empty strings and a new line at the end
        to_display = ['', '', '', '', '', '', '', '', '', '']
        for card in player.hand:
            card_str = self.display_card(card)
            for row in range(len(card_str)):
                to_display[row] += card_str[row] + '\t'

        return '\n'.join(to_display)

    def play_turn(self):
        """Perform one turn in the game"""
        player_status = '========================================\n'
        for player in self.model.players:
            player_status += '{} has {} cards\n'.format(
                    player.name, player.hand.count)

        player = self.model.current_player

        player_status += 'Player {0} Hand: {1}\n'.format(player.name, player.hand)

        player_status += self.display_hand(player)

        player_status += '========================================\n'
        print(player_status)

        # Have the player make his/her move and then
        #   Handle the result once it is completed
        effect = player.play()

        if effect:
            if 'skip' in effect.keys():
                my_logger.debug('Player {0} played a `{1}`'.format(player.name, 'SKIP'))
                self.model.skip()

            if 'reverse' in effect.keys():
                my_logger.debug('Player {0} played a `{1}`'.format(player.name, 'REVERSE'))
                self.model.reverse()

            if 'draw' in effect.keys():
                my_logger.debug('Player {0} played a `{1}`'.format(player.name, 'DRAW'))
                for _ in range(effect['draw']):
                    self.model.next_player.draw_card()

            if 'wild' in effect.keys():
                # TODO
                pass

        # Move the current player -> next player
        self.model.increment_player()

        if self.model.game_over():
            self.winner = player


if __name__ == '__main__':
    t = TerminalController()
    t.main()
