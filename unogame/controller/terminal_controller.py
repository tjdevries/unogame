#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# UNO Terminal Controller
from unogame.model.model import Model

winner = None


class TerminalController(object):
    def __init__(self):
        ''' Create our terminal controller object '''
        self.model = Model(2)
        self.winner = None

    def main(self):
        ''' Play the game '''
        while(not self.winner):
            self.play_turn()

        print('========================================')
        print('Winner is {}'.format(self.winner.name))
        print('========================================')

    def play_turn(self):
        ''' Perform one turn in the game '''
        player_status = '========================================\n'
        for player in self.model.players:
            player_status += '{} has {} cards\n'.format(
                    player.name, player.hand.count)

        player_status += '========================================\n'
        print(player_status)

        for player in self.model.players:
            player.play()

            if self.model.game_over():
                self.winner = player

        choice = input()

        if choice == 'e':
            self.winner = True


'''
def check_for_neutral():
    print('CHECKING NEUTRAL')


def has_winner():
    if Player1.hand.is_empty() or AIPlayer.hand.is_empty():
        print('THE WINNER IS: ', get_winner())
        return True
    return False


def get_winner():
    if Player1.hand.is_empty():
        return Player1.name
    elif AIPlayer.hand.is_empty():
        return AIPlayer.name


def check_for_winner():
    if Player1.hand.is_empty()or AIPlayer.hand.is_empty():
        return True
    return False
'''

if __name__ == '__main__':
    t = TerminalController()
    t.main()
