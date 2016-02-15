#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# UNO Main Controller
from unogame import player
from unogame import deck
from unogame import utils

__version__ = '0.4.0'


winner = None


def do_turn():
    print("\nHuman has {0} cards.\nAI has {1} cards\n".format(
        utils.stack.count(Player1.hand),
        utils.stack.count(AIPlayer.hand)
        )
    )

    input('\nNew turn')

    playing_now = 0

    player_stack[playing_now].play()
    playing_now += 1

    if check_for_special():
        player_stack.reverse()
    elif check_for_neutral():
        print('FOUND NEUTRAL, DO WHAT?')

    player_stack[playing_now].play()


def check_for_special():
    # suit = Deck.table['suit']
    value = Deck.table['number']
    if value in Deck.specials:
        return True
    return False


def check_for_neutral():
    print('CHECKING NEUTRAL')


def has_winner():
    if utils.stack.count(Player1.hand) == 0 or utils.stack.count(AIPlayer.hand) == 0:
        print('THE WINNER IS: ', get_winner())
        return True
    return False


def get_winner():
    if utils.stack.count(Player1.hand) == 0:
        return Player1.name
    elif utils.stack.count(AIPlayer.hand) == 0:
        return AIPlayer.name


def check_for_winner():
    if utils.stack.count(Player1.hand) == 0 or utils.stack.count(AIPlayer.hand) == 0:
        return True
    return False


Deck = deck.Deck()
Player1 = player.HumanPlayer(Deck, 'Humano')
AIPlayer = player.Player(Deck, 'PC')
player_stack = [Player1, AIPlayer]

while not has_winner():
    do_turn()
