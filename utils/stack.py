from random import sample
def chooseOne(stack):
    '''Choose a random card from a dict-list compound'''
    card_options = []
    if len(stack) == 1:
        #Choose from the only suit available
        for suit in stack:
            chosen_suit = suit
            for value in stack[suit]:
                card_options.append(value)
        chosen_value = sample(card_options,1)
    else:
        #Choose a suit
        chosen_suit = sample(stack,1)[0]
        card_options = []
        for value in stack[chosen_suit]:
            card_options.append(value)
        chosen_value = sample(card_options,1)

    chosen_card = chosen_suit, chosen_value
    return chosen_card

def valuesAmmount(stack):
    '''Gets the ammount of values in a dictionary'''
    ammount = 0
    for k,v in stack.iteritems():
        for value in v:
            ammount = ammount+1
    return ammount


def count(stack):
    #stack = {'green':['0']}
    ammount = 0
    for k,v in stack.iteritems():
        for item in v:
            ammount = ammount+1
    return ammount
        


            
    
    
