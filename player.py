import random
import deck
import utils.stack

class Player:

    __version__ = '0.3.1'
    
    def __init__(self, Deck, name='Default'):
        self.hand = {}
        self.name = name
        self.hand = Deck.populatePlayerHand()
        self.Deck = Deck


        

    def __populateHand(self, Deck):
        self.hand = Deck.populatePlayerHand()


    def validCards(self):
        valid_cards = self.getValidCards()
        if len(valid_cards) < 1:
            return False
        else:
            return True

        
    def getValidCards(self):
        valid_cards = {}
        flag_suit = self.Deck.table['suit']
        flag_number = self.Deck.table['number']
    
        if flag_suit in self.hand:
            #We have the suit, now lets fetch the numbers from the suit
            if flag_suit not in valid_cards:
                valid_cards[flag_suit] = []
            for value in self.hand[flag_suit]:
                valid_cards[flag_suit].append(value)
    
        #Lets search for the valid numbers now
        for suit in self.hand:
            if suit is not flag_suit: #Already trapped
                if flag_number in self.hand[suit]:
                    #Found a matching number. Add it to the valid stack
                    if suit not in valid_cards:
                        valid_cards[suit] = []
                    valid_cards[suit].append(flag_number)
        return valid_cards

    def play(self):
        #print self.Deck.available
        print '{0} playing.'.format(self.name)
        while not self.validCards():
            self.buyCard()

        valid_cards = self.getValidCards()
        
        if len(valid_cards) > 1:
            #More than one suit
            chosen_card = utils.stack.chooseOne(valid_cards)
            suit = chosen_card[0]
            value = chosen_card[1][0]
            chosen_card = {suit:value}
        else:
            #Choose the suit here
            if utils.stack.valuesAmmount(valid_cards) > 1:
                #One suit, more than a value
                chosen_card = utils.stack.chooseOne(valid_cards)
                suit = chosen_card[0]
                value = chosen_card[1][0]
                chosen_card = {suit:value}
            else:
                #Only one suit and one value, thats the card we want.
                chosen_card = valid_cards
                for k,v in chosen_card.iteritems():
                    suit = k
                    value = v[0]


                    
                chosen_card = {suit:value}
        self.playCard(chosen_card)


    def buyCard(self):
        bought = self.Deck.buyCard()
        print 'Bought card: ',bought
        suit = bought.keys()[0]
        number = bought[suit]
        if suit not in self.hand:
            self.hand[suit] = []
        self.hand[suit].append(number)

    def refreshHand(self):
        pass
        
    def playCard(self, card):
        for k,v in card.items():
            suit = k
            value = v
        self.hand[suit].remove(value)

        #Refresh hand if needed
        if len(self.hand[suit]) == 0:
            del self.hand[suit]
        self.Deck.playCard(card)
        

    def sayUno(self):
        if random.randint(0,20) == 2:
            return True
        else:
            return False


class HumanPlayer(Player):

    def play(self):
        print 'Human playing'

        while not self.validCards():
            raw_input("Buying a card...<enter>")
            self.buyCard()
        print '\nValid cards: {0}'.format(self.getValidCards())
        suit = number = ''
        while suit not in self.getValidCards():
            suit = raw_input("Choose the suit > ")
        while number not in self.getValidCards()[suit]:
            number = raw_input("Choose the number > ")

        card = {suit:number}

        self.playCard(card)

        
if __name__ == '__main__':
    Deck = deck.Deck()
    heya = Player(Deck, 'Pancho')
    heya.play()
