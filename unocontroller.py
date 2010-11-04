

#UNO Main Controller
import player
import deck
import utils


__version__ = '0.3.0'


winner = None

def doTurn():
    print "\nHuman has {0} cards.\nAI has {1} cards\n".format(
        utils.stack.count(Player1.hand),utils.stack.count(AIPlayer.hand))
                                                                            
    raw_input('\nNew turn')

    playing_now = 0

    player_stack[playing_now].play()
    playing_now += 1
    
    if check_for_special():
        player_stack.reverse()
    elif check_for_neutral():
        print 'FOUND NEUTRAL, DO WHAT?'

    player_stack[playing_now].play()

def check_for_special():
    suit =  Deck.table['suit']
    value = Deck.table['number']
    if value in Deck.specials:
        return True
    return False

def check_for_neutral():
    print 'CHECKING NEUTRAL'

def hasWinner():
    if utils.stack.count(Player1.hand) == 0 or utils.stack.count(AIPlayer.hand) == 0:
        print 'THE WINNER IS: ', getWinner()
        return True
    return False

def getWinner():
    if utils.stack.count(Player1.hand) == 0:
        return Player1.name
    elif utils.stack.count(AIPlayer.hand) == 0:
        return AIPlayer.name

def checkForWinner():
    if utils.stack.count(Player1.hand) == 0 or utils.stack.count(AIPlayer.hand) == 0:
        return True
    return False


Deck = deck.Deck()
Player1 = player.HumanPlayer(Deck,'Humano')
AIPlayer = player.Player(Deck, 'PC')
player_stack = [Player1,AIPlayer]

while not hasWinner():
    doTurn()


