
import random
import customdict

class Deck:
    __version__ = '0.3.1'
    
    def __init__(self):
        self.available = customdict.CustomDict()
        self.table = {}
        self.__trash = {}
        self.__unavailable = {}
        self.specials = ['stop','reverse']

        #Populate the Deck
        self._populate()
        self._putCardOnTable(self.available.randomPair(method='simple'))
        
        print 'On the table: ',self.table
        #self.scaffold()

    def scaffold(self):
        print 'Playing with the neutrals stuff'
        rc = self._getStack({'neutral':'changecolor'})
        print 'RC: ',rc


    def _populate(self):
        #Neutrals compliant as of Oct.27,21:52
        card_limit = 10
        suits = ['blue','green','yellow','red','neutral']
        neutrals = ['buy2','buy2','buy4','buy4','changecolor','changecolor']

        for suit in suits:
            if suit not in self.available:
                self.available[suit] = []
            if suit == 'neutral':
                for action in neutrals:
                    self.available[suit].append(action)
            else:
                for i in xrange(card_limit):
                    self.available[suit].append(str(i))
                for special in self.specials:
                    self.available[suit].append(special)
        '''self.available['neutral'] = []
        for value in neutrals:
            self.available['neutral'].append(value)'''


    def _setAsTrash(self, card):
        '''Sends the card to the trash stack'''

        stack = self._getStack(card)
        card = self._dissectCard(card)
        suit = card[0]
        number = card[1]

        stack[suit].remove(number)
        
        if suit not in self.__trash:
            self.__trash[suit] = []
        self.__trash[suit].append(number)
        

    def _setAsTable(self, card):
        #Neutrals compliant as of Oct.27,21:55
        '''Appends the card to the table stack
            @card: {'suit':'number'}
        '''

        for k,v in card.items():
            suit = k
            number = v

        if type(number) is not str:
            number = number[0]
            
        stack = self._getStack(card)
        stack[suit].remove(number)

        #Append to the table stack
        self.table['suit'] = suit
        self.table['number'] = number


        
    def _putCardOnTable(self, card):
        #Neutrals compliant as of Oct.27,21:55
        '''Appends the new card to the table'''
        if self.table:
            suit = self.table['suit']
            number = self.table['number']
            if suit not in self.__trash:
                self.__trash[suit]= []
            self.__trash[suit].append(number) 
        self._setAsTable(card)  

        
    def _setAsUnavailable(self, card):
        stack = self._getStack(card)
        card = self._dissectCard(card)
        suit = card[0]
        number = card[1]
        
        #Remove the card from its stack
        stack[suit].remove(number)

        #Append the card to the unavailable stack
        if suit not in self.__unavailable:
            self.__unavailable[suit] = []
        self.__unavailable[suit].append(number)


    def playCard(self, card):
        self._putCardOnTable(card)
        print 'Card played.\n\nOn the table: ',self.table,'\n'

        #Probably not useful
        '''if self.check_special(card):
            print 'SPECIAL CARD COMING THROUGH, MOVE, MOVE!'
            for k,v in card.items():
                suit = k
                value = v
            if value == 'stop':
                print 'dispatch_stop()'
            elif value == 'reverse':
                print 'dispatch_reverse()'
            else:
                print 'Unrecognized special type'''
        # End probably not useful

    def getRandomCard(self, stack):
        '''Randomly choose a card from the given stack'''
        suits = []
        for suit in stack:
            suits.append(suit)

        random_suit = random.sample(suits,1)[0]
        random_number = random.sample(self.available[random_suit],1)[0]

        random_card = {random_suit:random_number}
        return random_card

    def populatePlayerHand(self):
        hand = {}
        for x in xrange(5):
            pair = self.available.randomPair()
            suit = pair['key']
            number = pair['value']
            
            if suit not in hand:
                hand[suit] = []
            hand[suit].append(number)

            card = {suit:number}
            self._setAsUnavailable(card)

        return hand

    
    def _reshuffle(self):
        pass


    def isTrash(self,card):
        if self._hasCard(card, self.__trash):
            return True
        else:
            return False


    def isTable(self, card):
        card = self._dissectCard(card)
        suit = card[0]
        number = card[1]
        if self.table:
            if self.table['suit'] == suit:
                if self.table['number'] == number:
                    return True
            else:
                return False
        else:
            return False

        
    def isAvailable(self, card):
        if self._hasCard(card, self.available):
            return True
        else:
            return False
                

    def isUnavailable(self, card):
        if self._hasCard(card, self.__unavailable):
           return True
        else:
            return False


        
    def _getStack(self, card):
        if self.isTrash(card):
            return self.__trash
        elif self.isTable(card):
            return self.table
        elif self.isAvailable(card):
            return self.available
        elif self.isUnavailable(card):
            return self.__unavailable
        else:
            return 'unknown'

    def _hasCard(self, card, stack):
        suit = card.keys()[0]
        number = card[suit]

        if suit in stack:
            if number in stack[suit]:
                return True
            else:
                return False
        else:
            return False
        
    def _dissectCard(self, card, request=None):
        if 'suit' in card:
            suit = card['suit']
            number = card['number']
            return [suit,number]
        else:
            for k,v in card.items():
                suit = k
                number = v
            if request == 'suit':
                return suit
            elif request == 'number':
                return number
            else:
                return [suit,number]
            

    def buyCard(self):
        if self.available.needs_reshuffling():
           self.available.reshuffle(self.__trash)
           self.emptyTrash()
        bought = self.available.randomPair(method='simple')
        self._setAsUnavailable(bought)
        self.available.refresh()
       
        return bought


    def emptyTrash(self):
        self.__trash = {}

    def check_special(self, card):
        for k,v in card.items():
            suit = k
            value = v
        if value in  self.specials:
            return True
        return False
    def check_neutral(self,card):
        print 'CHECKING NEUTRAL '*5
        for k,v in card.items():
            suit = k
            value = v
        

if __name__ == '__main__':
    deck = Deck()
    print '-----\nAvailable:\n %s \n-----' % deck.available
