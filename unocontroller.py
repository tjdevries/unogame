#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# UNO Main Controller
from unogame import player
from unogame import deck

__version__ = '0.4.0'


winner = None


def do_turn():
    print("\nHuman has {0} cards.\nAI has {1} cards\n".format(
        Player1.hand.count,
        AIPlayer.hand.count
        )
    )

    input('\nNew turn')

    playing_now = 0

    player_stack[playing_now].play()
    playing_now += 1

    player_stack[playing_now].play()


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


Deck = deck.Deck()
Player1 = player.Player(Deck, 'Human')
AIPlayer = player.Player(Deck, 'PC')
player_stack = [Player1, AIPlayer]

while not has_winner():
    do_turn()
